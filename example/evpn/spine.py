import json
import subprocess
import pydantic_srlinux.models.interfaces as srl_if
import pydantic_srlinux.models.network_instance as srl_ni
import pydantic_srlinux.models.routing_policy as srl_rp
import pydantic_srlinux.models.tunnel_interfaces as srl_ti
from example.client import Action, SRLClient
from example.log import setup_logging

setup_logging()


def get_container_ip(container_name: str) -> str:
    """Get the first available IP address of a Docker container."""
    try:
        inspect_output = subprocess.check_output(
            ["docker", "inspect", container_name],
            text=True,
        )
        container_data = json.loads(inspect_output)[0]
        networks = container_data.get("NetworkSettings", {}).get("Networks", {})

        if not networks:
            raise ValueError(f"No networks found for container '{container_name}'")

        for network_data in networks.values():
            ip = network_data.get("IPAddress", "").strip()
            if ip:
                return ip

        available = ", ".join(sorted(networks.keys())) or "none"
        raise ValueError(
            f"No IP address found for container '{container_name}'. "
            f"Available networks: {available}"
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to inspect container '{container_name}': {e}") from e

# --8<-- [start:physical-interfaces]
e1_1 = srl_if.InterfaceListEntry(
    name="ethernet-1/1",
    admin_state=srl_if.EnumerationEnum.enable,
    subinterface=[
        srl_if.SubinterfaceListEntry(
            index=1,
            ipv6=srl_if.Ipv6Container(
                admin_state=srl_if.EnumerationEnum.enable,
                router_advertisement=srl_if.RouterAdvertisementContainer(
                    router_role=srl_if.RouterRoleContainer(
                        admin_state=srl_if.EnumerationEnum.enable
                        )
                    )
            )
        )
    ],
)

e1_2 = srl_if.InterfaceListEntry(
    name="ethernet-1/2",
    admin_state=srl_if.EnumerationEnum.enable,
    subinterface=[
        srl_if.SubinterfaceListEntry(
            index=1,
            ipv6=srl_if.Ipv6Container(
                admin_state=srl_if.EnumerationEnum.enable,
                router_advertisement=srl_if.RouterAdvertisementContainer(
                    router_role=srl_if.RouterRoleContainer(
                        admin_state=srl_if.EnumerationEnum.enable
                        )
                    )
            )
        )
    ],
)

# --8<-- [end:physical-interfaces]

# --8<-- [start:loopback-interfaces]
e0_0 = srl_if.InterfaceListEntry(
    name="system0",
    admin_state=srl_if.EnumerationEnum.enable,
    subinterface=[
        srl_if.SubinterfaceListEntry(
            index=0,
            ipv4=srl_if.Ipv4Container(
                admin_state=srl_if.EnumerationEnum.enable,
                address=[
                    srl_if.AddressListEntry(
                        ip_prefix="10.10.10.10/32",
                    )
                ],
            )
        )
    ],
)
# --8<-- [end:loopback-interfaces]


# --8<-- [start:ebgp-underlay]
rp = srl_rp.RoutingPolicyContainer(
    prefix_set=[
        srl_rp.PrefixSetListEntry(
            name="system-loopbacks",
            prefix=[
                srl_rp.PrefixListEntry(
                    ip_prefix=srl_rp.Ipv4PrefixType(root="10.0.0.0/8"),
                    mask_length_range="32..32"
                )
            ],
        )
    ],
    policy=[
        srl_rp.PolicyListEntry(
            name="system-loopbacks-policy",
            statement=[
                srl_rp.StatementListEntry(
                    name="1",
                    match=srl_rp.MatchContainer(
                        prefix=srl_rp.PrefixContainer(
                            prefix_set="system-loopbacks"
                        )
                    ),
                    action=srl_rp.ActionContainer(
                        policy_result=srl_rp.EnumerationEnum23.accept
                    )
                )
            ]
        )
    ]
)
# --8<-- [end:ebgp-underlay]

# --8<-- [start:ibgp-overlay]



ni_default = srl_ni.NetworkInstanceListEntry(
    name="default",
    interface=[
        srl_ni.InterfaceListEntry(
            name="ethernet-1/1.1",
        ),
        srl_ni.InterfaceListEntry(
            name="ethernet-1/2.1",
        ),
        srl_ni.InterfaceListEntry(
            name="system0.0",
        )
    ],
    protocols=srl_ni.ProtocolsContainer(
        bgp=srl_ni.BgpContainer(
            autonomous_system=4200000010, 
            router_id=srl_ni.Ipv4AddressType(root="10.10.10.10"),
            afi_safi=[srl_ni.AfiSafiListEntry(
                afi_safi_name="ipv4-unicast",
                admin_state=srl_ni.EnumerationEnum.enable,
            )],
            dynamic_neighbors=srl_ni.DynamicNeighborsContainer(
                interface=[
                    srl_ni.InterfaceListEntry2(
                    interface_name="ethernet-1/1.1",
                    peer_group="underlay",
                    allowed_peer_as=[srl_ni.AllowedPeerAsLeafList2(root="4200000001..4200000010")],),
                    srl_ni.InterfaceListEntry2(
                    interface_name="ethernet-1/2.1",
                    peer_group="underlay",
                    allowed_peer_as=[srl_ni.AllowedPeerAsLeafList2(root="4200000001..4200000010")],),
                    ],
                accept=srl_ni.AcceptContainer(
                    match=[srl_ni.MatchListEntry(
                        prefix=srl_ni.Ipv4PrefixType(root="0.0.0.0/0"),
                        peer_group="overlay",)]
                )
            ),
            group=[
                srl_ni.GroupListEntry(
                    group_name="underlay", 
                    export_policy=[srl_ni.ExportPolicyLeafList3(root="system-loopbacks-policy")],
                    import_policy=[srl_ni.ImportPolicyLeafList3(root="system-loopbacks-policy")],),
                srl_ni.GroupListEntry(
                    group_name="overlay", 
                    peer_as=65535,
                    local_as=srl_ni.LocalAsContainer(
                        as_number=65535,),
                    afi_safi=[
                        srl_ni.AfiSafiListEntry2(
                            afi_safi_name="ipv4-unicast",
                            admin_state=srl_ni.EnumerationEnum.disable,
                        ),
                        srl_ni.AfiSafiListEntry2(
                            afi_safi_name="evpn",
                            admin_state=srl_ni.EnumerationEnum.enable)],
                    route_reflector=srl_ni.RouteReflectorContainer2(client=True)
                )
                ],
            neighbor=[srl_ni.NeighborListEntry(
                peer_address=srl_ni.Ipv4AddressWithZoneType(root="10.10.10.10"),
                peer_group="overlay",
                admin_state=srl_ni.EnumerationEnum.enable,
            )]
        ),),
    ip_forwarding=srl_ni.IpForwardingContainer(receive_ipv4_check=False)
)

is_by_alias = False
cmd_list = [
    e0_0.model_dump_json(indent=2, exclude_none=True, exclude_unset=True, by_alias=is_by_alias, exclude_defaults=True),
    rp.model_dump_json(indent=2, exclude_none=True, exclude_unset=True, by_alias=is_by_alias, exclude_defaults=True),
    e1_1.model_dump_json(indent=2, exclude_none=True, exclude_unset=True, by_alias=is_by_alias, exclude_defaults=True),
    e1_2.model_dump_json(indent=2, exclude_none=True, exclude_unset=True, by_alias=is_by_alias, exclude_defaults=True),
    ni_default.model_dump_json(indent=2, exclude_none=True, exclude_unset=True, by_alias=is_by_alias, exclude_defaults=True),
]
## Print 
for cmd in cmd_list:
    # print("\n---\n")
    print(cmd)
    print("\n")
import sys
sys.exit(0)

# SRL_VERSION=25.10.1 SRL_TYPE=ixr-d2l clab deploy -c -t srlinux.dev/clab-srl
# SRL_VERSION=25.10.1 SRL_TYPE=ixr-d2l clab destroy -c -t srlinux.dev/clab-srl
# slr_name = "leaf1"
# slr_name = "srl"
slr_name = "l3evpn-spine"
slr_ip = get_container_ip(slr_name)
print(slr_ip)

with SRLClient(host=slr_ip) as client:

    client.add_set_command(
        action=Action.UPDATE,
        path="/interface[name=system0]",
        value=e0_0,
    )
    client.add_set_command(
        action=Action.UPDATE,
        path="/routing-policy",
        value=rp,
    )
    client.add_set_command(
        action=Action.UPDATE,
        path="/interface[name=ethernet-1/1]",
        value=e1_1,
    )
    client.add_set_command(
        action=Action.UPDATE,
        path="/interface[name=ethernet-1/2]",
        value=e1_2,
    )
    client.add_set_command(
        action=Action.UPDATE,
        path="/network-instance[name=default]",
        value=ni_default,
    )
    
    # Send all commands in a single request
    response = client.send_set_request()
    print(f"Response: {response.status_code} - {response.text}")