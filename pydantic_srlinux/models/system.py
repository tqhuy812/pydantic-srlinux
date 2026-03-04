from __future__ import annotations

from enum import Enum
from typing import Annotated, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel


class AsicLoopbackContainer(BaseModel):
    """
    ASIC loopback

    Use the ASIC loopback mode
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class BpduGuardRecoveryTimeExpiresLeaf1(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=0, le=4294967295)]
    """
    The remaining time until the bpdu-guard-down-time expires and the error is cleared on the interface
    """


class DomainNameType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$'
        ),
    ]
    """
    The domain-name type represents a DNS domain name.  The
    name SHOULD be fully qualified whenever possible.

    Internet domain names are only loosely specified.  Section
    3.5 of RFC 1034 recommends a syntax (modified in Section
    2.1 of RFC 1123).  The pattern above is intended to allow
    for current practice in domain name use, and some possible
    future expansion.  It is designed to hold various types of
    domain names, including names used for A or AAAA records
    (host names) and other records, such as SRV records.  Note
    that Internet host names have a stricter syntax (described
    in RFC 952) than the DNS recommendations in RFCs 1034 and
    1123, and that systems that want to store host names in
    schema nodes using the domain-name type are recommended to
    adhere to this stricter standard to ensure interoperability.

    The encoding of DNS names in the DNS protocol is limited
    to 255 characters.  Since the encoding consists of labels
    prefixed by a length bytes and there is a trailing NULL
    byte, only 253 characters can appear in the textual dotted
    notation.

    The description clause of schema nodes using the domain-name
    type MUST describe when and how these names are resolved to
    IP addresses.  Note that the resolution of a domain-name value
    may require to query multiple DNS records (e.g., A for IPv4
    and AAAA for IPv6).  The order of the resolution process and
    which DNS record takes precedence can either be defined
    explicitly or may depend on the configuration of the
    resolver.

    Domain-name values use the US-ASCII encoding.  Their canonical
    format uses lowercase US-ASCII characters.  Internationalized
    domain names MUST be A-labels as per RFC 5890.
    """


class DomainSearchListLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$'
        ),
    ]
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames - option 119
    """


class DomainSearchListLeafList2(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$'
        ),
    ]
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames - option 119
    """


class DomainSearchListLeafList3(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$'
        ),
    ]
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames - option 119
    """


class DomainSearchListLeafList4(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$'
        ),
    ]
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames
    """


class DomainSearchListLeafList5(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$'
        ),
    ]
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames
    """


class DscpValueType(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=0, le=63)]
    """
    A DiffServ Code Point represented numerically.
    """


class FilterLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str, Field(pattern='^(?=^([0-9a-zA-Z\\-_.@!%^*()\\[\\]{}|\\\\/<>,;])+$).*$')
    ]
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class FilterLeafList2(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str, Field(pattern='^(?=^([0-9a-zA-Z\\-_.@!%^*()\\[\\]{}|\\\\/<>,;])+$).*$')
    ]
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class FilterLeafList3(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str, Field(pattern='^(?=^([0-9a-zA-Z\\-_.@!%^*()\\[\\]{}|\\\\/<>,;])+$).*$')
    ]
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class FilterLeafList4(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str, Field(pattern='^(?=^([0-9a-zA-Z\\-_.@!%^*()\\[\\]{}|\\\\/<>,;])+$).*$')
    ]
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class GnssContainer(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class HealthCheckLeaf1(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=6, le=1500)]
    """
    RADIUS and TACACS+ health check interval
    """


class HoldDownTimerLeaf1(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=1, le=500)]
    """
    Specifies a hold-down timer value when seamless-bfd is enabled

    The timer is started when the number of S-BFD sessions that are up drops below the threshold. The TE-policy path is not considered to be up again until the hold-down timer has expired and the number of S-BFD sessions that are up equals or exceeds the threshold.
    A grace preiod after session down such that sBFD session flaps does not impact active path.

    The default is 4 seconds.
    """


class IndexLeaf4(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=0, le=255)]
    """
    Each key in a keychain requires a unique identifier, the index value specifies this identifier
    """


class InterfaceStandbySignalingOnNonDfContainer(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class Ipv4AddressWithZoneType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    The ipv4-address-with-zone type represents an IPv4 address in dotted quad notation (added only for symmetry)
    """


class Ipv4Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]


class Ipv6AddressWithZoneType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%.+)?$)(?=^(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?$)(?=^([^%]+)(%(mgmt0\\.0|system0\\.0|lo(0|1[0-9][0-9]|2([0-4][0-9]|5[0-5])|[1-9][0-9]|[1-9])\\.(0|[1-9](\\d){0,3})|lif-.*\\.(0|[1-9](\\d){0,3})|vhn-.*\\.(0|[1-9](\\d){0,3})|enp(0|1[0-9][0-9]|2([0-4][0-9]|5[0-5])|[1-9][0-9]|[1-9])s(0|[1-9]|[1-2][0-9]|3[0-1])f[0-7]\\.(0|[1-9](\\d){0,3})|ethernet-([1-9](\\d){0,1}(/m[1-6])?(/[1-9](\\d){0,1})?/(([1-9](\\d){0,1})|(1[0-1]\\d)|(12[0-8])))\\.([0]|[1-9](\\d){0,3})|irb(0|1[0-9][0-9]|2([0-4][0-9]|5[0-5])|[1-9][0-9]|[1-9])\\.(0|[1-9](\\d){0,3})|lag(([1-9](\\d){0,2})|(1000))\\.(0|[1-9](\\d){0,3})))?$).*$'
        ),
    ]
    """
    The ipv6-address-with-zone type represents an IPv6 address in full, mixed, shortened, and
    shortened-mixed notation.  The IPv6 address may include a zone index, separated by
    a % sign. The zone index is used to disambiguate identical address values.  For link-local
    addresses, the zone index is expected to be the name of a subinterface. An example of
    a link-local address is:

    fe80::1234%ethernet-1/1.1
    """


class Ipv6Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$'
        ),
    ]


class MtuContainer(BaseModel):
    """
    Top-level container for configuration and state data related to the system MTU
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    default_port_mtu: Annotated[
        Optional[int], Field(alias='srl_nokia-mtu:default-port-mtu', ge=1500, le=9500)
    ] = 9232
    """
    System default port MTU in bytes including ethernet overhead but excluding 4-bytes FCS

    The 7220 IXR systems support a maximum port MTU of 9412 bytes.

    The 7730 SXR systems support a maximum port MTU of 9408 bytes.
    """
    default_l2_mtu: Annotated[
        Optional[int], Field(alias='srl_nokia-mtu:default-l2-mtu', ge=1500, le=9500)
    ] = 9232
    """
    System default Layer-2 MTU in bytes for bridged subinterfaces

    It includes the ethernet overhead and VLAN tags but excludes 4-bytes FCS. The default-l2-mtu
    is also used as the oper-mac-vrf-mtu and oper-vpws-mtu value if the network-instance does
    not have subinterfaces.

    The 7220 IXR systems support a maximum L2 MTU of 9412 bytes.

    The 7730 SXR systems support a maximum L2 MTU of 9408 bytes.
    """
    default_ip_mtu: Annotated[
        Optional[int], Field(alias='srl_nokia-mtu:default-ip-mtu', ge=1280, le=9486)
    ] = 1500
    """
    System default IP MTU in bytes including the IP header but excluding Ethernet overhead

    The 7220 IXR systems support a maximum IP MTU of 9398 bytes.

    The 7730 SXR systems support a maximum IP MTU of 9394 bytes.
    """
    default_mpls_mtu: Annotated[
        Optional[int], Field(alias='srl_nokia-mtu:default-mpls-mtu', ge=1284, le=9496)
    ] = 1508
    """
    System default MPLS MTU in bytes including the size of the transmitted label stack.

    The 7730 SXR systems support a maximum MPLS MTU of 9404 bytes.
    """
    min_path_mtu: Annotated[
        Optional[int], Field(alias='srl_nokia-mtu:min-path-mtu', ge=552, le=9232)
    ] = 552
    """
    Sets the minimum path MTU to use when receiving an ICMP fragmentation needed message

    The 7730 SXR systems support a maximum min path MTU of 9176 bytes.

    This is controlled via the kernel min_pmtu option. In the event an ICMP fragmentation needed message is received by the kernel, the system will drop the session to this MTU to allow packets to traverse the entire path.
    """


class MulticastContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    leave_sync_propagation: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-multicast:leave-sync-propagation',
            ge=0,
            le=300,
        ),
    ] = 5
    """
    This value is the delta time applied by a node sending the leave synch route before removing the multicast state

    When EVPN multi-homing is used along with igmp/mld snooping, a node receiving a leave message from a receiver will
    advertise an EVPN Multicast Leave Sync route to synchronize the leave state across all nodes attached to the
    Ethernet Segment. This route encodes the maximum response time that the receiving node needs to apply for a given
    (S,G) or (*,G) state before removing it. The leave-sync-propagation time accounts for the BGP propagation
    time so that the local node minimizes the potential churn of removing the multicast state before the route made it
    to the node receiving a join for the multicast group to be removed. The value must be adjusted to the estimated
    BGP propagation time between the Ethernet Segment peers.
    """


class PathsLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?\\-{}*\\\\\\\\"\\[\\]]+$).*$'
        ),
    ]
    """
    List of valid YANG paths in CLI notation to monitor for changes

    If any events are received on any of the provided paths, the configured script will be executed.

    This path may include keys, wildcards, ranges, and other management server supported constructs.

    E.g.
        "interface * oper-state"
        "acl ipv4-filter foo* description"
    """


class PtpContainer2(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class RateLimitPerHostContainer(BaseModel):
    """
    Context for controller rate limiting behavior per host
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    peak_rate: Annotated[
        Optional[int], Field(alias='srl_nokia-system-datapath:peak-rate', ge=1, le=20)
    ] = 10
    """
    The peak rate for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv4 senders that generated traffic requiring ICMP messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by the max-burst parameter and a fill/drain rate controlled by this peak-rate parameter
    """
    max_burst: Annotated[
        Optional[int], Field(alias='srl_nokia-system-datapath:max-burst', ge=1, le=50)
    ] = 10
    """
    The maximum burst size for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv4 senders that generated traffic requiring ICMP messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by this max-burst parameter and a fill/drain rate controlled by the peak-rate parameter
    """


class RateLimitPerHostContainer2(BaseModel):
    """
    Context for controller rate limiting behavior per host
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    peak_rate: Annotated[
        Optional[int], Field(alias='srl_nokia-system-datapath:peak-rate', ge=1, le=20)
    ] = 10
    """
    The peak rate for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv6 senders that generated traffic requiring ICMPv6 messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by the max-burst parameter and a fill/drain rate controlled by this peak-rate parameter
    """
    max_burst: Annotated[
        Optional[int], Field(alias='srl_nokia-system-datapath:max-burst', ge=1, le=50)
    ] = 10
    """
    The maximum burst size for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv6 senders that generated traffic requiring ICMPv6 messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by this max-burst parameter and a fill/drain rate controlled by the peak-rate parameter
    """


class RevertTimerLeaf1(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=0, le=4320)]
    """
    Revert timer for the segment-list.

    Timer till a revert to primary/best path after it is recovered from a failure. In case of uncolored te-policy, applies to primary segment-list and in case of colored te-policy applies to best candidate path.

    The default is 0 seconds.
    """


class RouteDistinguisherType0Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9]):(429496729[0-5]|42949672[0-8][0-9]|4294967[0-1][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[0-1][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9])$).*$'
        ),
    ]


class RouteDistinguisherType1Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$).*$'
        ),
    ]


class RouteDistinguisherType2Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(429496729[0-5]|42949672[0-8][0-9]|4294967[0-1][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[0-1][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9]):(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$).*$'
        ),
    ]


class RouteDistinguisherType2bType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])\\.(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9]):(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$).*$'
        ),
    ]


class SampleCountBasedContainer(BaseModel):
    """
    Systematic count-based packet Sampling.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    packet_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:packet-interval', ge=1, le=1)
    ] = None
    """
    The number of packets that are consecutively
    sampled between gaps of length packetSpace.
    This parameter corresponds to the Information Element
    samplingPacketInterval and to psampSampCountBasedInterval
    in the PSAMP MIB module.
    """
    packet_space: Annotated[
        int, Field(alias='srl_nokia-ipfix:packet-space', ge=0, le=4294967295)
    ]
    """
    The number of unsampled packets between two
    Sampling intervals.
    This parameter corresponds to the Information Element
    samplingPacketSpace and to psampSampCountBasedSpace
    in the PSAMP MIB module.
    """


class Server6PreferenceContainer(BaseModel):
    """
    Specifies value to be verified with the received DHCPv6 server preference option

    Verifies that DHCPv6 server preference option value is in the range between min and max.
    If DHCPv6 server preference option is not received then the preference value is set to zero.
    If not specified then the verification is skipped.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    min: Annotated[
        Optional[int], Field(alias='srl_nokia-dhcp-server-guard:min', ge=0, le=255)
    ] = None
    """
    Specifies the minimum value expected in DHCPv6 server preference option
    """
    max: Annotated[
        Optional[int], Field(alias='srl_nokia-dhcp-server-guard:max', ge=0, le=255)
    ] = None
    """
    Specifies the maximum value expected in DHCPv6 server preference option
    """


class ServiceRequestContainer(BaseModel):
    """
    Tacacs VSA config to be retrieved from server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    nokia_srl_authorization_role: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:nokia-srl-authorization-role')
    ] = False
    """
    Request nokia-srl-authorization-role service VSAs
    """
    nokia_srl_authorization_role_cli: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:nokia-srl-authorization-role-cli')
    ] = False
    """
    Request nokia-srl-authorization-role-cli service VSAs
    """
    nokia_srl_authorization_role_netconf: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-aaa:nokia-srl-authorization-role-netconf'),
    ] = False
    """
    Request nokia-srl-authorization-role-netconf service VSAs
    """
    nokia_srl_configuration_role: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:nokia-srl-configuration-role')
    ] = False
    """
    Request nokia-srl-configuration-role service VSAs
    """


class SpiffeIdsLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[str, Field(pattern='^(?=^spiffe://.*$).*$')]
    """
    The SPIFFE ID list for the user, including the spiffe:// URI

    This list of IDs is evaluated by TLS-consuming servers (e.g. gNMI, JSON-RPC) that use a TLS server-profile with authenticate-client set to true.

    If a match is found in any incoming offered client certificates, the provider of the certificate is associated with this local user, and given resulting permissions.
    """


class StaticFunctionContainer(BaseModel):
    """
    Enter the static-function context
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    max_entries: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:max-entries', ge=1, le=1048575)
    ] = 1
    """
    Maximum number of static micro-segment functions
    """


class StaticFunctionContainer2(BaseModel):
    """
    Enter the static-function context
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    max_entries: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:max-entries', ge=1, le=1048575)
    ] = 1
    """
    Maximum number of static SID functions
    """


class StringOrBinaryType1(RootModel[bytes]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[bytes, Field(max_length=18446744073709551615)]
    """
    Type definition for string or binary represenation
    """


class Sync0Container(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class SystemContainer(BaseModel):
    """
    Properties of the LI system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lawful-intercept:name',
            pattern='^(?=^([a-zA-Z0-9]+[\\-\\.])*[a-zA-Z0-9]+$).*$',
        ),
    ] = None
    """
    Hostname of the LI management system
    """


class TacacsContainer(BaseModel):
    """
    Top-level container for configuration relating to TACACS+ interworking with roles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    priv_lvl: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:priv-lvl', ge=0, le=15)
    ] = None
    """
    The TACACS+ priv-lvl to map to this role

    All roles matching each specific priv-lvl, and their lessers are merged together to create the final ruleset applied to the user.
    """


class TacacsContainer2(BaseModel):
    """
    Top-level container for TACACS servergroup data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    service_request: Annotated[
        Optional[ServiceRequestContainer], Field(alias='srl_nokia-aaa:service-request')
    ] = None


class TacacsContainer3(BaseModel):
    """
    Top-level container for TACACS+ server data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:port', ge=0, le=65535)
    ] = 49
    """
    The port number on which to contact the TACACS+ server
    """
    secret_key: Annotated[Optional[str], Field(alias='srl_nokia-aaa:secret-key')] = None
    """
    The unencrypted shared key used between the system and server, up to 128 characters cleartext
    """


class TimersContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    activation_timer: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:activation-timer',
            ge=0,
            le=100,
        ),
    ] = None
    """
    Remaining activation timer per Ethernet segment
    """


class TlsCase(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class UnicastMsgRateContainer(BaseModel):
    """
    Aggregate unicast message rates for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages transmitted
    """
    anno_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages received
    """
    sync_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages transmitted
    """
    sync_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages received
    """
    del_req_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages transmitted
    """
    del_req_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages received
    """
    del_resp_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages transmitted
    """
    del_resp_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages received
    """
    follow_up_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages transmitted
    """
    follow_up_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages received
    """
    signaling_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages transmitted
    """
    signaling_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages received
    """
    other_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:other-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of other messages received
    """


class UserListEntry2(BaseModel):
    """
    The list of protocols that are using this label block. If the block is not shared there will only be 1 user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    index: Annotated[
        int, Field(alias='srl_nokia-mpls-label-management:index', ge=0, le=255)
    ]
    """
    Index number used to enumerate the clients
    """
    owner: Annotated[
        Optional[str], Field(alias='srl_nokia-mpls-label-management:owner')
    ] = None
    """
    The protocol or service associated with the client
    """


class UserListEntry3(BaseModel):
    """
    The list of protocols that are using this label block. If the block is not shared there will only be 1 user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    index: Annotated[
        int, Field(alias='srl_nokia-mpls-label-management:index', ge=0, le=255)
    ]
    """
    Index number used to enumerate the clients
    """
    owner: Annotated[
        Optional[str], Field(alias='srl_nokia-mpls-label-management:owner')
    ] = None
    """
    The protocol or service associated with the client
    """


class VlanIdLeaf1(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=0, le=4094)]
    """
    VLAN tagging requirements for the application type, VLAN-ID (range 0..4094) or untagged
    """


class YangContainer(BaseModel):
    """
    Top-level container for application state related to YANG
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    modules: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-app-mgmt:modules')
    ] = []
    """
    YANG module names used by this application instance
    """
    source_directories: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-app-mgmt:source-directories')
    ] = []
    """
    Source directories searched for YANG modules to load

    These directories are used to load modules indicated in the modules leaf, and any modules imported/included within them
    """


class EnumerationEnum(Enum):
    request = 'request'
    response = 'response'
    common = 'common'


class EnumerationEnum10(Enum):
    cli = 'cli'
    gnmi = 'gnmi'
    gnoi = 'gnoi'
    gnpsi = 'gnpsi'
    gnsi = 'gnsi'
    gribi = 'gribi'
    netconf = 'netconf'
    p4rt = 'p4rt'
    json_rpc = 'json-rpc'
    ftp = 'ftp'
    grpc_reflection = 'grpc-reflection'


class EnumerationEnum100(Enum):
    admin_disabled = 'admin-disabled'
    failed_to_compile = 'failed-to-compile'
    exception = 'exception'
    timeout = 'timeout'
    subscription_failed = 'subscription-failed'
    script_unavailable = 'script-unavailable'
    script_error = 'script-error'
    missing_function = 'missing-function'
    system_error = 'system-error'
    ephemeral_action_failed = 'ephemeral-action-failed'
    cfg_action_failed = 'cfg-action-failed'
    tools_action_failed = 'tools-action-failed'
    state_action_failed = 'state-action-failed'
    script_action_failed = 'script-action-failed'


class EnumerationEnum101(Enum):
    request = 'request'
    response = 'response'
    common = 'common'


class EnumerationEnum102(Enum):
    accept = 'accept'
    discard = 'discard'


class EnumerationEnum103(Enum):
    input = 'input'
    output = 'output'
    both = 'both'


class EnumerationEnum104(Enum):
    unused = 'unused'
    prs = 'prs'
    stu = 'stu'
    st2 = 'st2'
    tnc = 'tnc'
    st3e = 'st3e'
    st3 = 'st3'
    prc = 'prc'
    ssua = 'ssua'
    ssub = 'ssub'
    sec = 'sec'
    eec1 = 'eec1'
    eec2 = 'eec2'


class EnumerationEnum105(Enum):
    unknown = 'unknown'
    prs = 'prs'
    stu = 'stu'
    st2 = 'st2'
    tnc = 'tnc'
    st3e = 'st3e'
    st3 = 'st3'
    smc = 'smc'
    st4 = 'st4'
    dus = 'dus'
    prc = 'prc'
    ssua = 'ssua'
    ssub = 'ssub'
    sec = 'sec'
    dnu = 'dnu'
    inv = 'inv'
    pno = 'pno'
    eec1 = 'eec1'
    eec2 = 'eec2'
    failed = 'failed'


class EnumerationEnum106(Enum):
    qualified = 'qualified'
    not_qualified = 'not-qualified'


class EnumerationEnum107(Enum):
    not_applicable = 'not-applicable'
    los = 'los'
    ssm_quality = 'ssm-quality'
    out_of_range = 'out-of-range'
    wtr = 'wtr'
    admin_disabled = 'admin-disabled'


class EnumerationEnum108(Enum):
    sdh = 'sdh'
    sonet = 'sonet'


class EnumerationEnum109(Enum):
    field_1 = '1'
    field_2 = '2'
    field_3 = '3'
    field_4 = '4'
    field_5 = '5'
    internal = 'internal'


class EnumerationEnum11(Enum):
    action = 'action'
    cancel_commit = 'cancel-commit'
    close_session = 'close-session'
    commit = 'commit'
    copy_config = 'copy-config'
    delete_config = 'delete-config'
    discard_changes = 'discard-changes'
    edit_config = 'edit-config'
    edit_data = 'edit-data'
    get = 'get'
    get_config = 'get-config'
    get_data = 'get-data'
    get_schema = 'get-schema'
    kill_session = 'kill-session'
    lock = 'lock'
    unlock = 'unlock'
    validate = 'validate'


class EnumerationEnum110(Enum):
    not_present = 'not-present'
    master_free_run = 'master-free-run'
    master_holdover = 'master-holdover'
    master_locked = 'master-locked'
    slave = 'slave'
    acquiring = 'acquiring'


class EnumerationEnum111(Enum):
    itug8275dot1 = 'itug8275dot1'
    itug8275dot2 = 'itug8275dot2'


class EnumerationEnum112(Enum):
    bc = 'bc'


class EnumerationEnum113(Enum):
    backup = 'backup'
    time_source = 'time-source'


class EnumerationEnum114(Enum):
    sync0_a = 'sync0-a'
    sync0_b = 'sync0-b'


class EnumerationEnum115(Enum):
    not_applicable = 'not-applicable'
    initial = 'initial'
    acquiring = 'acquiring'
    holdover = 'holdover'
    locked = 'locked'


class EnumerationEnum116(Enum):
    not_applicable = 'not-applicable'
    initial = 'initial'
    acquiring = 'acquiring'
    phase_tracking = 'phase-tracking'
    holdover = 'holdover'
    locked = 'locked'


class EnumerationEnum117(Enum):
    atomic_clock = 'atomic-clock'
    gps = 'gps'
    terrestrial_radio = 'terrestrial-radio'
    ptp = 'ptp'
    ntp = 'ntp'
    hand_set = 'hand-set'
    other = 'other'
    internal_oscillator = 'internal-oscillator'
    reserved = 'reserved'


class EnumerationEnum118(Enum):
    initializing = 'initializing'
    faulty = 'faulty'
    disabled = 'disabled'
    listening = 'listening'
    pre_master = 'pre-master'
    master = 'master'
    passive = 'passive'
    uncalibrated = 'uncalibrated'
    slave = 'slave'


class EnumerationEnum119(Enum):
    forwardable = 'forwardable'
    non_forwardable = 'non-forwardable'


class EnumerationEnum12(Enum):
    none = 'none'


class EnumerationEnum120(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum121(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum122(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum123(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum124(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum125(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum126(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum127(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum128(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum129(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum13(Enum):
    request = 'request'
    response = 'response'
    stream = 'stream'
    common = 'common'
    grpc = 'grpc'


class EnumerationEnum130(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum131(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum132(Enum):
    forwardable = 'forwardable'
    non_forwardable = 'non-forwardable'


class EnumerationEnum133(Enum):
    gnss_a = 'gnss-a'
    gnss_b = 'gnss-b'


class EnumerationEnum134(Enum):
    gnss_a = 'gnss-a'
    gnss_b = 'gnss-b'


class EnumerationEnum135(Enum):
    unknown = 'unknown'
    locked = 'locked'
    not_locked = 'not-locked'


class EnumerationEnum136(Enum):
    unknown = 'unknown'
    unsupported = 'unsupported'
    ok = 'ok'
    over_current = 'over-current'
    under_current = 'under-current'
    no_bias_voltage = 'no-bias-voltage'


class EnumerationEnum14(Enum):
    native = 'native'
    openconfig = 'openconfig'


class EnumerationEnum15(Enum):
    gnmi = 'gnmi'
    acctz = 'acctz'
    gribi = 'gribi'
    p4rt = 'p4rt'


class EnumerationEnum16(Enum):
    on_change = 'ON_CHANGE'
    sample = 'SAMPLE'
    target_defined = 'TARGET_DEFINED'
    poll = 'POLL'
    once = 'ONCE'


class EnumerationEnum17(Enum):
    preserve = 'preserve'
    delete = 'delete'


class EnumerationEnum18(Enum):
    static = 'static'
    duplicate = 'duplicate'
    learnt = 'learnt'
    irb_interface = 'irb-interface'
    evpn = 'evpn'
    evpn_static = 'evpn-static'
    irb_interface_anycast = 'irb-interface-anycast'
    proxy_anti_spoof = 'proxy-anti-spoof'
    reserved = 'reserved'
    eth_cfm = 'eth-cfm'
    irb_interface_vrrp = 'irb-interface-vrrp'


class EnumerationEnum19(Enum):
    static = 'static'
    dynamic = 'dynamic'
    evpn = 'evpn'
    duplicate = 'duplicate'


class EnumerationEnum2(Enum):
    idevid = 'idevid'
    oidevid = 'oidevid'


class EnumerationEnum20(Enum):
    both = 'both'
    input = 'input'
    output = 'output'


class EnumerationEnum21(Enum):
    action = 'action'
    cancel_commit = 'cancel-commit'
    close_session = 'close-session'
    commit = 'commit'
    copy_config = 'copy-config'
    delete_config = 'delete-config'
    discard_changes = 'discard-changes'
    edit_config = 'edit-config'
    edit_data = 'edit-data'
    get_config = 'get-config'
    get_data = 'get-data'
    get_schema = 'get-schema'
    get = 'get'
    hello = 'hello'
    kill_session = 'kill-session'
    lock = 'lock'
    unknown = 'unknown'
    unlock = 'unlock'
    validate = 'validate'


class EnumerationEnum22(Enum):
    rsyslog_file_format = 'RSYSLOG_FileFormat'
    rsyslog_traditional_file_format = 'RSYSLOG_TraditionalFileFormat'
    rsyslog_debug_format = 'RSYSLOG_DebugFormat'


class EnumerationEnum23(Enum):
    all = 'all'
    audit = 'audit'
    auth = 'auth'
    authpriv = 'authpriv'
    console = 'console'
    cron = 'cron'
    daemon = 'daemon'
    ftp = 'ftp'
    kern = 'kern'
    lpr = 'lpr'
    mail = 'mail'
    news = 'news'
    ntp = 'ntp'
    syslog = 'syslog'
    user = 'user'
    uucp = 'uucp'
    local0 = 'local0'
    local1 = 'local1'
    local2 = 'local2'
    local3 = 'local3'
    local4 = 'local4'
    local5 = 'local5'
    local6 = 'local6'
    local7 = 'local7'


class EnumerationEnum24(Enum):
    emergency = 'emergency'
    alert = 'alert'
    critical = 'critical'
    error = 'error'
    warning = 'warning'
    notice = 'notice'
    informational = 'informational'
    debug = 'debug'


class EnumerationEnum25(Enum):
    udp = 'udp'
    tcp = 'tcp'
    tls = 'tls'


class EnumerationEnum26(Enum):
    rsyslog_forward_format = 'RSYSLOG_ForwardFormat'
    rsyslog_syslog_protocol23_format = 'RSYSLOG_SyslogProtocol23Format'
    rsyslog_traditional_forward_format = 'RSYSLOG_TraditionalForwardFormat'


class EnumerationEnum27(Enum):
    store_and_forward = 'store-and-forward'
    cut_through = 'cut-through'


class EnumerationEnum28(Enum):
    active = 'active'
    inactive = 'inactive'


class EnumerationEnum29(Enum):
    mirror_inst_admin_down = 'mirror-inst-admin-down'
    no_mirror_source = 'no-mirror-source'
    local_mirror_subif_down = 'local-mirror-subif-down'
    remote_mirror_dst_unreachable = 'remote-mirror-dst-unreachable'


class EnumerationEnum3(Enum):
    enable = 'enable'
    disable = 'disable'


class EnumerationEnum30(Enum):
    ingress_only = 'ingress-only'
    egress_only = 'egress-only'
    ingress_egress = 'ingress-egress'


class EnumerationEnum31(Enum):
    mirror_source_ingress_table_full = 'mirror-source-ingress-table-full'
    mirror_source_egress_table_full = 'mirror-source-egress-table-full'
    not_applicable = 'not-applicable'


class EnumerationEnum32(Enum):
    ipv4 = 'ipv4'
    ipv6 = 'ipv6'
    mac = 'mac'


class EnumerationEnum33(Enum):
    l2ogre = 'l2ogre'
    l3ogre = 'l3ogre'
    mpls = 'mpls'


class EnumerationEnum34(Enum):
    destination_nexthop_not_resolved = 'destination-nexthop-not-resolved'
    destination_tunnel_nexthop_resolve_failed = (
        'destination-tunnel-nexthop-resolve-failed'
    )
    destination_nexthop_group_id_failed = 'destination-nexthop-group-id-failed'
    not_applicable = 'not-applicable'


class EnumerationEnum35(Enum):
    messages = 'messages'


class EnumerationEnum36(Enum):
    messages = 'messages'


class EnumerationEnum37(Enum):
    inline = 'inline'
    popup = 'popup'


class EnumerationEnum38(Enum):
    fuzzy = 'fuzzy'
    prefix = 'prefix'
    smart = 'smart'
    substring = 'substring'


class EnumerationEnum39(Enum):
    basic = 'basic'
    advanced = 'advanced'


class EnumerationEnum4(Enum):
    up = 'up'
    down = 'down'
    empty = 'empty'
    downloading = 'downloading'
    booting = 'booting'
    starting = 'starting'
    failed = 'failed'
    synchronizing = 'synchronizing'
    upgrading = 'upgrading'
    low_power = 'low-power'
    degraded = 'degraded'
    warm_reboot = 'warm-reboot'
    waiting = 'waiting'


class EnumerationEnum40(Enum):
    json = 'json'
    table = 'table'
    text = 'text'
    xml = 'xml'
    yaml = 'yaml'


class EnumerationEnum41(Enum):
    off = 'off'
    on = 'on'


class EnumerationEnum42(Enum):
    oc = 'oc'
    srl = 'srl'


class EnumerationEnum43(Enum):
    mac_vrf = 'mac-vrf'
    vxlan_interface = 'vxlan-interface'
    l2_proxy_arp_nd = 'l2-proxy-arp-nd'
    mfib = 'mfib'
    mac_vrf_bgp_evpn = 'mac-vrf-bgp-evpn'
    mldp = 'mldp'


class EnumerationEnum44(Enum):
    ready = 'ready'
    not_ready = 'not-ready'
    delete_pending = 'delete-pending'
    updating = 'updating'


class EnumerationEnum45(Enum):
    ready = 'ready'
    not_ready = 'not-ready'
    delete_pending = 'delete-pending'
    updating = 'updating'


class EnumerationEnum46(Enum):
    tcp_md5 = 'tcp-md5'
    isis = 'isis'
    ospf = 'ospf'
    tcp_ao = 'tcp-ao'
    vrrp = 'vrrp'
    macsec = 'macsec'
    macsec_fallback = 'macsec-fallback'


class EnumerationEnum47(Enum):
    none = 'none'


class EnumerationEnum48(Enum):
    cleartext = 'cleartext'
    md5 = 'md5'
    hmac_md5 = 'hmac-md5'
    hmac_sha_1 = 'hmac-sha-1'
    hmac_sha_256 = 'hmac-sha-256'
    aes_128_cmac = 'aes-128-cmac'
    aes_256_cmac = 'aes-256-cmac'


class EnumerationEnum49(Enum):
    forever = 'forever'


class EnumerationEnum5(Enum):
    password = 'password'
    publickey = 'publickey'
    keyboard_interactive = 'keyboard-interactive'


class EnumerationEnum50(Enum):
    shared = 'shared'
    private = 'private'


class EnumerationEnum51(Enum):
    validating = 'validating'
    publishing = 'publishing'
    unconfirmed = 'unconfirmed'
    checkpoint = 'checkpoint'
    save = 'save'
    complete = 'complete'
    reverting = 'reverting'
    failed = 'failed'


class EnumerationEnum52(Enum):
    active = 'ACTIVE'
    sandbox = 'SANDBOX'


class EnumerationEnum53(Enum):
    read = 'read'
    write = 'write'
    deny = 'deny'


class EnumerationEnum54(Enum):
    disable = 'disable'


class EnumerationEnum55(Enum):
    disable = 'disable'


class EnumerationEnum56(Enum):
    monitored = 'monitored'
    ecmp_protected = 'ecmp-protected'
    linear = 'linear'


class EnumerationEnum57(Enum):
    psp = 'psp'
    usp = 'usp'
    psp_usd = 'psp-usd'
    usp_usd = 'usp-usd'
    psp_usp_usd = 'psp-usp-usd'


class EnumerationEnum58(Enum):
    accept = 'accept'
    discard = 'discard'


class EnumerationEnum59(Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'


class EnumerationEnum6(Enum):
    hiba_chk = 'hiba-chk'


class EnumerationEnum60(Enum):
    none = 'none'
    virtual = 'virtual'


class EnumerationEnum61(Enum):
    all_active = 'all-active'
    single_active = 'single-active'


class EnumerationEnum62(Enum):
    default = 'default'
    preference = 'preference'
    manual = 'manual'


class EnumerationEnum63(Enum):
    include = 'include'
    exclude = 'exclude'


class EnumerationEnum64(Enum):
    use_system_ipv4_address = 'use-system-ipv4-address'
    use_system_ipv6_address = 'use-system-ipv6-address'


class EnumerationEnum65(Enum):
    mpls_label = 'mpls-label'
    vni = 'vni'
    transposed_srv6_function = 'transposed-srv6-function'


class EnumerationEnum66(Enum):
    admin_disabled = 'admin-disabled'
    no_nexthop_address = 'no-nexthop-address'
    no_originating_address = 'no-originating-address'
    no_associated_interface = 'no-associated-interface'
    associated_interface_oper_down = 'associated-interface-oper-down'
    no_esi = 'no-esi'
    no_esi_label = 'no-esi-label'
    tag_set_not_resolved = 'tag-set-not-resolved'


class EnumerationEnum67(Enum):
    auto_derived_from_system_ip_0 = 'auto-derived-from-system-ip:0'
    none = 'none'


class EnumerationEnum68(Enum):
    auto_derived_from_esi_bytes_1_6 = 'auto-derived-from-esi-bytes-1-6'
    none = 'none'


class EnumerationEnum69(Enum):
    auto_derived_from_esi_bytes_1_6 = 'auto-derived-from-esi-bytes-1-6'
    none = 'none'


class EnumerationEnum7(Enum):
    ssh_rsa_3076 = 'ssh-rsa-3076'
    ecdsa_sha2_nistp256 = 'ecdsa-sha2-nistp256'
    ecdsa_sha2_nistp521 = 'ecdsa-sha2-nistp521'
    ssh_ed25519 = 'ssh-ed25519'
    ssh_rsa_2048 = 'ssh-rsa-2048'
    ssh_rsa_4096 = 'ssh-rsa-4096'


class EnumerationEnum70(Enum):
    no_loopback_address = 'no-loopback-address'
    no_esi = 'no-esi'
    none = 'none'
    network_instance_oper_down = 'network-instance-oper-down'
    bad_rd_format = 'bad-rd-format'


class EnumerationEnum71(Enum):
    rstp = 'rstp'
    mstp = 'mstp'


class EnumerationEnum72(Enum):
    all = 'all'
    bpdu = 'bpdu'
    connectivity = 'connectivity'
    exception = 'exception'
    fsm_state = 'fsm-state'
    fsm_timers = 'fsm-timers'
    port_role = 'port-role'
    port_state = 'port-state'


class EnumerationEnum73(Enum):
    root = 'ROOT'
    none = 'NONE'


class EnumerationEnum74(Enum):
    stp = 'stp'
    rstp = 'rstp'
    mstp = 'mstp'


class EnumerationEnum75(Enum):
    dot1d = 'dot1d'
    pvst = 'pvst'


class EnumerationEnum76(Enum):
    dhcp = 'dhcp'
    dhcp_pd = 'dhcp-pd'
    nd = 'nd'
    static = 'static'


class EnumerationEnum77(Enum):
    endpoint = 'endpoint'
    switch = 'switch'


class EnumerationEnum78(Enum):
    init = 'init'
    in_progress = 'in-progress'
    complete = 'complete'


class EnumerationEnum79(Enum):
    dhcp_discover = 'dhcp_discover'
    dhcp_offer = 'dhcp_offer'
    dhcp_request = 'dhcp_request'
    dhcp_decline = 'dhcp_decline'
    dhcp_ack = 'dhcp_ack'
    dhcp_nak = 'dhcp_nak'
    dhcp_release = 'dhcp_release'
    dhcp_inform = 'dhcp_inform'


class EnumerationEnum8(Enum):
    remote = 'remote'
    console = 'console'


class EnumerationEnum80(Enum):
    dhcp6_solicit = 'dhcp6_solicit'
    dhcp6_advertise = 'dhcp6_advertise'
    dhcp6_request = 'dhcp6_request'
    dhcp6_confirm = 'dhcp6_confirm'
    dhcp6_renew = 'dhcp6_renew'
    dhcp6_rebind = 'dhcp6_rebind'
    dhcp6_reply = 'dhcp6_reply'
    dhcp6_release = 'dhcp6_release'
    dhcp6_decline = 'dhcp6_decline'
    dhcp6_reconfigure = 'dhcp6_reconfigure'
    dhcp6_info_request = 'dhcp6_info_request'
    dhcp6_relay_forward = 'dhcp6_relay_forward'
    dhcp6_relay_reply = 'dhcp6_relay_reply'


class EnumerationEnum81(Enum):
    running = 'running'
    waiting_for_config = 'waiting-for-config'
    error = 'error'
    starting = 'starting'
    stopped = 'stopped'


class EnumerationEnum82(Enum):
    synchronized = 'synchronized'
    not_synchronized = 'not-synchronized'
    not_applicable = 'not-applicable'


class EnumerationEnum83(Enum):
    hot = 'hot'
    warm = 'warm'
    cold = 'cold'


class EnumerationEnum84(Enum):
    restart = 'restart'
    stop = 'stop'
    start = 'start'
    reload = 'reload'
    quit = 'quit'
    kill = 'kill'


class EnumerationEnum85(Enum):
    ingress_only = 'ingress-only'
    egress_only = 'egress-only'
    ingress_egress = 'ingress-egress'


class EnumerationEnum86(Enum):
    received = 'received'
    transmitted = 'transmitted'
    common = 'common'


class EnumerationEnum87(Enum):
    chassis_component = 'CHASSIS_COMPONENT'
    interface_alias = 'INTERFACE_ALIAS'
    port_component = 'PORT_COMPONENT'
    mac_address = 'MAC_ADDRESS'
    network_address = 'NETWORK_ADDRESS'
    interface_name = 'INTERFACE_NAME'
    local = 'LOCAL'


class EnumerationEnum88(Enum):
    i_pv4 = 'IPv4'
    i_pv6 = 'IPv6'


class EnumerationEnum89(Enum):
    untagged = 'untagged'


class EnumerationEnum9(Enum):
    ar2 = 'ar2'
    sha2 = 'sha2'
    yescrypt = 'yescrypt'


class EnumerationEnum90(Enum):
    cs0 = 'CS0'
    le = 'LE'
    cs1 = 'CS1'
    af11 = 'AF11'
    af12 = 'AF12'
    af13 = 'AF13'
    cs2 = 'CS2'
    af21 = 'AF21'
    af22 = 'AF22'
    af23 = 'AF23'
    cs3 = 'CS3'
    af31 = 'AF31'
    af32 = 'AF32'
    af33 = 'AF33'
    cs4 = 'CS4'
    af41 = 'AF41'
    af42 = 'AF42'
    af43 = 'AF43'
    cs5 = 'CS5'
    ef = 'EF'
    cs6 = 'CS6'
    cs7 = 'CS7'


class EnumerationEnum91(Enum):
    unknown = 'unknown'
    true = 'true'
    false = 'false'
    tlv_not_enabled = 'tlv-not-enabled'


class EnumerationEnum92(Enum):
    unknown = 'unknown'
    true = 'true'
    false = 'false'
    tlv_not_enabled = 'tlv-not-enabled'


class EnumerationEnum93(Enum):
    other = 'other'
    field_10base_t = '10baseT'
    field_10base_tfd = '10baseTFD'
    field_100base_t4 = '100baseT4'
    field_100base_tx = '100baseTX'
    field_100base_txfd = '100baseTXFD'
    field_100base_t2 = '100baseT2'
    field_100base_t2_fd = '100baseT2FD'
    fdx_pause = 'FdxPause'
    fdx_a_pause = 'FdxAPause'
    fdx_s_pause = 'FdxSPause'
    fdx_b_pause = 'FdxBPause'
    field_1000base_x = '1000baseX'
    field_1000base_xfd = '1000baseXFD'
    field_1000base_t = '1000baseT'
    field_1000base_tfd = '1000baseTFD'


class EnumerationEnum94(Enum):
    other = 'Other'
    aui = 'AUI'
    field_10base5 = '10base5'
    foirl = 'Foirl'
    field_10base2 = '10base2'
    field_10base_t = '10baseT'
    field_10base_fp = '10baseFP'
    field_10base_fb = '10baseFB'
    field_10base_fl = '10baseFL'
    field_10broad36 = '10broad36'
    field_10base_thd = '10baseTHD'
    field_10base_tfd = '10baseTFD'
    field_10base_flhd = '10baseFLHD'
    field_10base_flfd = '10baseFLFD'
    field_100base_t4 = '100baseT4'
    field_100base_txhd = '100baseTXHD'
    field_100base_txfd = '100baseTXFD'
    field_100base_fxhd = '100baseFXHD'
    field_100base_fxfd = '100baseFXFD'
    field_100base_t2_hd = '100baseT2HD'
    field_100base_t2_fd = '100baseT2FD'
    field_1000base_xhd = '1000baseXHD'
    field_1000base_xfd = '1000baseXFD'
    field_1000base_lxhd = '1000baseLXHD'
    field_1000base_lxfd = '1000baseLXFD'
    field_1000base_sxhd = '1000baseSXHD'
    field_1000base_sxfd = '1000baseSXFD'
    field_1000base_cxhd = '1000baseCXHD'
    field_1000base_cxfd = '1000baseCXFD'
    field_1000base_thd = '1000baseTHD'
    field_1000base_tfd = '1000baseTFD'
    field_10_gbase_x = '10GbaseX'
    field_10_gbase_lx4 = '10GbaseLX4'
    field_10_gbase_r = '10GbaseR'
    field_10_gbase_er = '10GbaseER'
    field_10_gbase_lr = '10GbaseLR'
    field_10_gbase_sr = '10GbaseSR'
    field_10_gbase_w = '10GbaseW'
    field_10_gbase_ew = '10GbaseEW'
    field_10_gbase_lw = '10GbaseLW'
    field_10_gbase_sw = '10GbaseSW'
    field_10_gbase_cx4 = '10GbaseCX4'
    field_2_base_tl = '2BaseTL'
    field_10_pass_ts = '10PassTS'
    field_100_base_bx10_d = '100BaseBX10D'
    field_100_base_bx10_u = '100BaseBX10U'
    field_100_base_lx10 = '100BaseLX10'
    field_1000_base_bx10_d = '1000BaseBX10D'
    field_1000_base_bx10_u = '1000BaseBX10U'
    field_1000_base_lx10 = '1000BaseLX10'
    field_1000_base_px10_d = '1000BasePX10D'
    field_1000_base_px10_u = '1000BasePX10U'
    field_1000_base_px20_d = '1000BasePX20D'
    field_1000_base_px20_u = '1000BasePX20U'
    field_10_gbase_t = '10GbaseT'
    field_10_gbase_lrm = '10GbaseLRM'
    field_1000base_kx = '1000baseKX'
    field_10_gbase_kx4 = '10GbaseKX4'
    field_10_gbase_kr = '10GbaseKR'
    field_10_g1_gbase_prxd1 = '10G1GbasePRXD1'
    field_10_g1_gbase_prxd2 = '10G1GbasePRXD2'
    field_10_g1_gbase_prxd3 = '10G1GbasePRXD3'
    field_10_g1_gbase_prxu1 = '10G1GbasePRXU1'
    field_10_g1_gbase_prxu2 = '10G1GbasePRXU2'
    field_10_g1_gbase_prxu3 = '10G1GbasePRXU3'
    field_10_gbase_prd1 = '10GbasePRD1'
    field_10_gbase_prd2 = '10GbasePRD2'
    field_10_gbase_prd3 = '10GbasePRD3'
    field_10_gbase_pru1 = '10GbasePRU1'
    field_10_gbase_pru3 = '10GbasePRU3'
    field_40_gbase_kr4 = '40GbaseKR4'
    field_40_gbase_cr4 = '40GbaseCR4'
    field_40_gbase_sr4 = '40GbaseSR4'
    field_40_gbase_fr = '40GbaseFR'
    field_40_gbase_lr4 = '40GbaseLR4'
    field_100_gbase_cr10 = '100GbaseCR10'
    field_100_gbase_sr10 = '100GbaseSR10'
    field_100_gbase_lr4 = '100GbaseLR4'
    field_100_gbase_er4 = '100GbaseER4'
    field_1000base_t1 = '1000baseT1'
    field_1000base_px30_d = '1000basePX30D'
    field_1000base_px30_u = '1000basePX30U'
    field_1000base_px40_d = '1000basePX40D'
    field_1000base_px40_u = '1000basePX40U'
    field_10_g1_gbase_prxd4 = '10G1GbasePRXD4'
    field_10_g1_gbase_prxu4 = '10G1GbasePRXU4'
    field_10_gbase_prd4 = '10GbasePRD4'
    field_10_gbase_pru4 = '10GbasePRU4'
    field_25_gbase_cr = '25GbaseCR'
    field_25_gbase_crs = '25GbaseCRS'
    field_25_gbase_kr = '25GbaseKR'
    field_25_gbase_krs = '25GbaseKRS'
    field_25_gbase_r = '25GbaseR'
    field_25_gbase_sr = '25GbaseSR'
    field_25_gbase_t = '25GbaseT'
    field_40_gbase_er4 = '40GbaseER4'
    field_40_gbase_r = '40GbaseR'
    field_40_gbase_t = '40GbaseT'
    field_100_gbase_cr4 = '100GbaseCR4'
    field_100_gbase_kr4 = '100GbaseKR4'
    field_100_gbase_kp4 = '100GbaseKP4'
    field_100_gbase_r = '100GbaseR'
    field_100_gbase_sr4 = '100GbaseSR4'
    field_2p5_gbase_t = '2p5GbaseT'
    field_5_gbase_t = '5GbaseT'
    field_100base_t1 = '100baseT1'
    field_1000base_rha = '1000baseRHA'
    field_1000base_rhb = '1000baseRHB'
    field_1000base_rhc = '1000baseRHC'
    field_2p5_gbase_kx = '2p5GbaseKX'
    field_2p5_gbase_x = '2p5GbaseX'
    field_5_gbase_kr = '5GbaseKR'
    field_5_gbase_r = '5GbaseR'
    field_10_gpass_xr = '10GpassXR'
    field_25_gbase_lr = '25GbaseLR'
    field_25_gbase_er = '25GbaseER'
    field_50_gbase_r = '50GbaseR'
    field_50_gbase_cr = '50GbaseCR'
    field_50_gbase_kr = '50GbaseKR'
    field_50_gbase_sr = '50GbaseSR'
    field_50_gbase_fr = '50GbaseFR'
    field_50_gbase_lr = '50GbaseLR'
    field_50_gbase_er = '50GbaseER'
    field_100_gbase_cr2 = '100GbaseCR2'
    field_100_gbase_kr2 = '100GbaseKR2'
    field_100_gbase_sr2 = '100GbaseSR2'
    field_100_gbase_dr = '100GbaseDR'
    field_200_gbase_r = '200GbaseR'
    field_200_gbase_dr4 = '200GbaseDR4'
    field_200_gbase_fr4 = '200GbaseFR4'
    field_200_gbase_lr4 = '200GbaseLR4'
    field_200_gbase_cr4 = '200GbaseCR4'
    field_200_gbase_kr4 = '200GbaseKR4'
    field_200_gbase_sr4 = '200GbaseSR4'
    field_200_gbase_er4 = '200GbaseER4'
    field_400_gbase_r = '400GbaseR'
    field_400_gbase_sr16 = '400GbaseSR16'
    field_400_gbase_dr4 = '400GbaseDR4'
    field_400_gbase_fr8 = '400GbaseFR8'
    field_400_gbase_lr8 = '400GbaseLR8'
    field_400_gbase_er8 = '400GbaseER8'
    field_10base_t1_l = '10baseT1L'
    field_10base_t1_shd = '10baseT1SHD'
    field_10base_t1_smd = '10baseT1SMD'
    field_10base_t1_sfd = '10baseT1SFD'
    field_100_gbase_fr1 = '100GbaseFR1'
    field_100_gbase_lr1 = '100GbaseLR1'
    field_400_gbase_fr4 = '400GbaseFR4'
    field_400_gbase_lr46 = '400GbaseLR46'
    field_400_gbase_sr8 = '400GbaseSR8'
    field_400_gbase_sr4p2 = '400GbaseSR4p2'
    field_2p5_gbase_t1 = '2p5GbaseT1'
    field_5_gbase_t1 = '5GbaseT1'
    field_10_gbase_t1 = '10GbaseT1'
    field_25_g10_gbase_pqgd2 = '25G10GbasePQGD2'
    field_25_g10_gbase_pqgd3 = '25G10GbasePQGD3'
    field_25_g10_gbase_pqgu2 = '25G10GbasePQGU2'
    field_25_g10_gbase_pqgu3 = '25G10GbasePQGU3'
    field_25_g10_gbase_pqxd2 = '25G10GbasePQXD2'
    field_25_g10_gbase_pqxd3 = '25G10GbasePQXD3'
    field_25_g10_gbase_pqxu2 = '25G10GbasePQXU2'
    field_25_g10_gbase_pqxu3 = '25G10GbasePQXU3'
    field_25_gbase_pqgd2 = '25GbasePQGD2'
    field_25_gbase_pqgd3 = '25GbasePQGD3'
    field_25_gbase_pqgu2 = '25GbasePQGU2'
    field_25_gbase_pqgu3 = '25GbasePQGU3'
    field_25_gbase_pqxd2 = '25GbasePQXD2'
    field_25_gbase_pqxd3 = '25GbasePQXD3'
    field_25_gbase_pqxu2 = '25GbasePQXU2'
    field_25_gbase_pqxu3 = '25GbasePQXU3'
    field_50_g10_gbase_pqgd2 = '50G10GbasePQGD2'
    field_50_g10_gbase_pqgd3 = '50G10GbasePQGD3'
    field_50_g10_gbase_pqgu2 = '50G10GbasePQGU2'
    field_50_g10_gbase_pqgu3 = '50G10GbasePQGU3'
    field_50_g10_gbase_pqxd2 = '50G10GbasePQXD2'
    field_50_g10_gbase_pqxd3 = '50G10GbasePQXD3'
    field_50_g10_gbase_pqxu2 = '50G10GbasePQXU2'
    field_50_g10_gbase_pqxu3 = '50G10GbasePQXU3'
    field_50_g25_gbase_pqgd2 = '50G25GbasePQGD2'
    field_50_g25_gbase_pqgd3 = '50G25GbasePQGD3'
    field_50_g25_gbase_pqgu2 = '50G25GbasePQGU2'
    field_50_g25_gbase_pqgu3 = '50G25GbasePQGU3'
    field_50_g25_gbase_pqxd2 = '50G25GbasePQXD2'
    field_50_g25_gbase_pqxd3 = '50G25GbasePQXD3'
    field_50_g25_gbase_pqxu2 = '50G25GbasePQXU2'
    field_50_g25_gbase_pqxu3 = '50G25GbasePQXU3'
    field_50_gbase_pqgd2 = '50GbasePQGD2'
    field_50_gbase_pqgd3 = '50GbasePQGD3'
    field_50_gbase_pqgu2 = '50GbasePQGU2'
    field_50_gbase_pqgu3 = '50GbasePQGU3'
    field_50_gbase_pqxd2 = '50GbasePQXD2'
    field_50_gbase_pqxd3 = '50GbasePQXD3'
    field_50_gbase_pqxu2 = '50GbasePQXU2'
    field_50_gbase_pqxu3 = '50GbasePQXU3'
    field_100_gbase_zr = '100GbaseZR'
    field_10_gbase_br10_d = '10GbaseBR10D'
    field_10_gbase_br10_u = '10GbaseBR10U'
    field_10_gbase_br20_d = '10GbaseBR20D'
    field_10_gbase_br20_u = '10GbaseBR20U'
    field_10_gbase_br40_d = '10GbaseBR40D'
    field_10_gbase_br40_u = '10GbaseBR40U'
    field_25_gbase_br10_d = '25GbaseBR10D'
    field_25_gbase_br10_u = '25GbaseBR10U'
    field_25_gbase_br20_d = '25GbaseBR20D'
    field_25_gbase_br20_u = '25GbaseBR20U'
    field_25_gbase_br40_d = '25GbaseBR40D'
    field_25_gbase_br40_u = '25GbaseBR40U'
    field_50_gbase_br10_d = '50GbaseBR10D'
    field_50_gbase_br10_u = '50GbaseBR10U'
    field_50_gbase_br20_d = '50GbaseBR20D'
    field_50_gbase_br20_u = '50GbaseBR20U'
    field_50_gbase_br40_d = '50GbaseBR40D'
    field_50_gbase_br40_u = '50GbaseBR40U'
    field_2p5_gbase_au = '2p5GbaseAU'
    field_5_gbase_au = '5GbaseAU'
    field_10_gbase_au = '10GbaseAU'
    field_25_gbase_au = '25GbaseAU'
    field_50_gbase_au = '50GbaseAU'
    field_25_gbase_t1 = '25GbaseT1'
    field_400_gbase_dr42 = '400GbaseDR42'
    field_800_gbase_cr8 = '800GbaseCR8'
    field_800_gbase_dr8 = '800GbaseDR8'
    field_800_gbase_dr82 = '800GbaseDR82'
    field_800_gbase_kr8 = '800GbaseKR8'
    field_800_gbase_r = '800GbaseR'
    field_800_gbase_sr8 = '800GbaseSR8'
    field_800_gbase_vr8 = '800GbaseVR8'


class EnumerationEnum95(Enum):
    interface_alias = 'INTERFACE_ALIAS'
    port_component = 'PORT_COMPONENT'
    mac_address = 'MAC_ADDRESS'
    network_address = 'NETWORK_ADDRESS'
    interface_name = 'INTERFACE_NAME'
    agent_circuit_id = 'AGENT_CIRCUIT_ID'
    local = 'LOCAL'


class EnumerationEnum96(Enum):
    unknown = 'unknown'
    known = 'known'


class EnumerationEnum97(Enum):
    unknown = 'unknown'


class EnumerationEnum98(Enum):
    serial = 'serial'


class EnumerationEnum99(Enum):
    ztp = 'ztp'
    secure = 'secure'
    inband = 'inband'
    ooband = 'ooband'


class AliasListEntry(BaseModel):
    """
    Create or overwrite an alias

    Aliases can be entered at the start of the input line, and must represent a complete command.

    The alias name can contain the following:
       - One or more fixed keywords, for example 'display stuff' and 'my-alias' are valid names.
       - One or more required arguments, entered between '{' and '}'.
         These arguments will then be substituted in the alias value before executing.

    For example, if you create this alias:
        environment alias 'display interface {name}' 'info / interface {name} | as table'

    Then entering 'display interface ethernet-1/1' will execute 'info / interface ethernet-1/1 | as table'.

    The alias value can contain the following keywords:
        - '{}' will add an optional unnamed parameter.
            It defaults to '*' if it is not entered.
        - '{<name>}' will add an optional named parameter with name '<name>'.
            It defaults to '*' if it is not entered.

    For example, if you create this alias:
        environment alias 'display interface' 'info / interface {} subinterface {subinterface} | as table'

    Then entering the following are all equivalent:
        display interface
        display interface *
        display interface * subinterface *
    But you can of course also use other values
        display interface my_interface subinterface 1
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-system-cli:name',
            pattern='^(?=^[^|\\[\\]>\\t\\n"]*$)(?=^[^\']*$)(?=^[^\\s{}].*$)(?=^.*[^\\s]$)(?=^([^{}]*(\\{([^{}\\s]*)\\})?)*[^{}]*$).*$',
        ),
    ]
    """
    Name of the alias
    """
    command: Annotated[
        str,
        Field(
            alias='srl_nokia-system-cli:command',
            pattern='^(?=^[^\\s].*$)(?=^.*[^\\s]$).*$',
        ),
    ]
    """
    Aliased command
    """


class AsicLoopbackCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    asic_loopback: Annotated[
        Optional[AsicLoopbackContainer],
        Field(alias='srl_nokia-packet-link-qual:asic-loopback'),
    ] = None


class BannerContainer(BaseModel):
    """
    Contains configuration and state related to system banners
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    login_banner: Annotated[
        Optional[str], Field(alias='srl_nokia-system-banner:login-banner')
    ] = None
    """
    Banner to display before a user has authenticated
    """
    motd_banner: Annotated[
        Optional[str], Field(alias='srl_nokia-system-banner:motd-banner')
    ] = None
    """
    Banner to display after a user has authenticated
    """


class BgpAutoDiscoveryContainer3(BaseModel):
    """
    Enclosing container for BGP auto discovery
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp_peer_addresses: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-lldp:bgp-peer-addresses')
    ] = []
    """
    List of IP address learned from neighbor for BGP auto discovery
    """
    group_id: Annotated[
        Optional[int], Field(alias='srl_nokia-lldp:group-id', ge=0, le=4294967295)
    ] = None
    """
    A four byte integer to send on outgoing LLDPDUs, this value can be used on the remote
    end to do peer group association. This sub-TLV is not sent by default
    """


class CapabilitiesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ac_df: Annotated[
        Optional[EnumerationEnum63],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ac-df'
        ),
    ] = 'include'
    """
    Attachment Circuit influenced DF Election.
    """
    non_revertive: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:non-revertive'
        ),
    ] = False
    """
    Non Revertive mode. If set to true, the 'Don't Preempt Me' capability is advertised in the ES route.
    """


class CapabilitiesListEntry(BaseModel):
    """
    List name
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-lldp:name')]
    """
    Neighbor supported capabilities
    """


class CapabilityListEntry(BaseModel):
    """
    List of LLDP system capabilities advertised by the neighbor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-lldp:name')]
    """
    Name of the system capability advertised by the neighbor

    Capabilities are represented in a bitmap that defines the
    primary functions of the system. The capabilities are
    defined in IEEE 802.1AB.
    """
    enabled: Annotated[Optional[bool], Field(alias='srl_nokia-lldp:enabled')] = None
    """
    Indicates whether the corresponding system capability is enabled on the neighbor
    """


class CliContainer(BaseModel):
    """
    Top-level container for cli plugin configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    load_global_plugins: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:load-global-plugins')
    ] = True
    """
    Specifies whether cli should load plugins from global plugin directory (from /etc/opt/srlinux/cli/plugins/).
    """
    load_user_plugins: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:load-user-plugins')
    ] = True
    """
    Specifies whether cli should load plugins from user home directory (from ~/cli/plugins/).
    """
    deny_command_list: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:deny-command-list')
    ] = []
    """
    List of cli commands that are denied for this role

    Python style regular expressions are supported. Every item is left anchored (it matches from the beginning
    of line). Empty deny-command-list means anything that is not in allow-command-list is denied. If both lists
    are empty then everything is allowed.
    """
    allow_command_list: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:allow-command-list')
    ] = []
    """
    List of cli commands that are allowed for this role

    Python style regular expressions are supported. Every item is left anchored (it matches from the beginning
    of line). Empty allow-command-list means anything that is not in deny-command-list is allowed. If both
    lists are empty then everything is allowed.
    """


class ClockQualityContainer(BaseModel):
    """
    The clockQuality of the local clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_class: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:clock-class', ge=0, le=255)
    ] = None
    """
    The clockClass denotes the traceability of the time or frequency distributed by the clock
    """
    clock_accuracy: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:clock-accuracy', ge=0, le=255)
    ] = None
    """
    The clockAccuracy indicates the expected accuracy of the clock
    """
    offset_scaled_log_variance: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:offset-scaled-log-variance', ge=0, le=65535),
    ] = None
    """
    The offsetScaledLogVariance provides an estimate of the variations of the clock
    """


class ComplexityRulesContainer(BaseModel):
    """
    Top-level container for password complexity rules
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    minimum_length: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:minimum-length', ge=1, le=12)
    ] = 1
    """
    The minimum length of the password for local users, including admin and linuxadmin
    """
    maximum_length: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:maximum-length', ge=1, le=1023)
    ] = 1023
    """
    The maximum length of the password for local users, including admin and linuxadmin
    """
    minimum_lowercase: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:minimum-lowercase', ge=0, le=10)
    ] = 0
    """
    The minimum lowercase characters from (a-z) that the user password must include

    A value of 0 results in no minimum-lowercase being enforced.
    """
    minimum_uppercase: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:minimum-uppercase', ge=0, le=10)
    ] = 0
    """
    The minimum uppercase characters from (A-Z) that the user password must include

    A value of 0 results in no minimum-uppercase being enforced.
    """
    minimum_numeric: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:minimum-numeric', ge=0, le=10)
    ] = 0
    """
    The minimum numeric digits that the user password must include

    A value of 0 results in no minimum-numeric being enforced.
    """
    minimum_special_character: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:minimum-special-character', ge=0, le=10),
    ] = 0
    """
    The minimum special characters that the user password must include

    A value of 0 results in no minimum-special-character being enforced.
    """
    allow_username: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:allow-username')
    ] = True
    """
    Enable or disable using username as part of the user password
    """
    disallow_sequence_keys: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:disallow-sequence-keys', ge=0, le=8)
    ] = 0
    """
    The minimum length of disallowed sequential characters
    to appear (letters or numbers) from left to right,
    right to left, down to up-right/left, or up to down-right/left.
    """


class ConstellationContainer(BaseModel):
    """
    Selects which constellations to be used for GNSS
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    gps: Annotated[Optional[bool], Field(alias='srl_nokia-sync:gps')] = True
    galileo: Annotated[Optional[bool], Field(alias='srl_nokia-sync:galileo')] = False


class CoordinatesContainer(BaseModel):
    """
    Contains configuration and state related to system coordinates
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    latitude: Annotated[
        Optional[float],
        Field(alias='srl_nokia-system-coordinates:latitude', ge=-90.0, le=90.0),
    ] = None
    """
    Decimal latitude between -90 and 90 to a maximum of 6 decimal places
    """
    longitude: Annotated[
        Optional[float],
        Field(alias='srl_nokia-system-coordinates:longitude', ge=-180.0, le=180.0),
    ] = None
    """
    Decimal longitude between -180 and 180 to a maximum of 6 decimal places
    """
    height: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-coordinates:height', ge=0, le=65535),
    ] = None
    """
    Height in meters
    """


class CustomTlvListEntry(BaseModel):
    """
    List of custom LLDP TLVs from a neighbor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        int, Field(alias='srl_nokia-lldp:type', ge=-2147483648, le=2147483647)
    ]
    """
    The integer value identifying the type of information
    contained in the value field.
    """
    oui: Annotated[str, Field(alias='srl_nokia-lldp:oui')]
    """
    The organizationally unique identifier field from the custom TLV

    This field shall contain the organization's OUI as defined in
    Clause 9 of IEEE Std 802. The high-order octet is 0 and the
    low-order 3 octets are the SMI Network Management Private Enterprise
    Code of the Vendor in network byte order, as defined in the
    'Assigned Numbers' RFC [RFC3232].
    """
    oui_subtype: Annotated[str, Field(alias='srl_nokia-lldp:oui-subtype')]
    """
    The subtype value defined by the OUI for this custom TLV

    The organizationally defined subtype field shall contain a
    unique subtype value assigned by the defining organization.
    """
    value: Annotated[
        Optional[bytes],
        Field(alias='srl_nokia-lldp:value', max_length=18446744073709551615),
    ] = None
    """
    A variable-length octet-string containing the value for this TLV
    """


class CustomListEntry(BaseModel):
    """
    List of custom DHCP options
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    code: Annotated[int, Field(alias='srl_nokia-dhcp-server:code', ge=1, le=254)]
    """
    The code of the DHCP option
    """
    value: Annotated[
        str, Field(alias='srl_nokia-dhcp-server:value', max_length=255, min_length=1)
    ]
    """
    The value of the DHCP option
    """
    always_send: Annotated[
        Optional[bool], Field(alias='srl_nokia-dhcp-server:always-send')
    ] = False
    """
    If true, the option will always be sent to the client, even if it is not configured in the client request
    """
    encoding: Annotated[
        Optional[str], Field(alias='srl_nokia-dhcp-server:encoding')
    ] = 'string'
    """
    The encoding of the value of the DHCP option
    """


class CustomListEntry2(BaseModel):
    """
    List of custom DHCP options
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    code: Annotated[int, Field(alias='srl_nokia-dhcp-server:code', ge=1, le=254)]
    """
    The code of the DHCP option
    """
    value: Annotated[
        str, Field(alias='srl_nokia-dhcp-server:value', max_length=255, min_length=1)
    ]
    """
    The value of the DHCP option
    """
    always_send: Annotated[
        Optional[bool], Field(alias='srl_nokia-dhcp-server:always-send')
    ] = False
    """
    If true, the option will always be sent to the client, even if it is not configured in the client request
    """
    encoding: Annotated[
        Optional[str], Field(alias='srl_nokia-dhcp-server:encoding')
    ] = 'string'
    """
    The encoding of the value of the DHCP option
    """


class CustomListEntry3(BaseModel):
    """
    List of custom DHCP options
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    code: Annotated[int, Field(alias='srl_nokia-dhcp-server:code', ge=1, le=254)]
    """
    The code of the DHCP option
    """
    value: Annotated[
        str, Field(alias='srl_nokia-dhcp-server:value', max_length=255, min_length=1)
    ]
    """
    The value of the DHCP option
    """
    always_send: Annotated[
        Optional[bool], Field(alias='srl_nokia-dhcp-server:always-send')
    ] = False
    """
    If true, the option will always be sent to the client, even if it is not configured in the client request
    """
    encoding: Annotated[
        Optional[str], Field(alias='srl_nokia-dhcp-server:encoding')
    ] = 'string'
    """
    The encoding of the value of the DHCP option
    """


class DateAndTimeDeltaType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$'
        ),
    ]
    """
    When this type is used to store a date and time, show routines should display it as a delta
    with respect to the current date and time in the format 'dddd:hh:mm:ss ago' (for a past
    event) or 'in dddd:hh:mm:ss' (future event), where dddd is the number of days, hh is the
    number of  hours, mm is the number of  minutes and ss is the number of seconds.
    """


class DiscardsContainer(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:bad-domain', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:alternate-master', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:out-of-sequence', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:peer-disabled', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class DiscardsContainer2(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:bad-domain', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:alternate-master', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:out-of-sequence', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:peer-disabled', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class DiscardsContainer3(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:bad-domain', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:alternate-master', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:out-of-sequence', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:peer-disabled', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class DiscardsContainer4(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:bad-domain', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:alternate-master', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:out-of-sequence', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:peer-disabled', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class DiscardsContainer5(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:bad-domain', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:alternate-master', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:out-of-sequence', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:peer-disabled', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class EventListEntry(BaseModel):
    """
    List of events subject to accounting
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    event_type: Annotated[str, Field(alias='srl_nokia-aaa:event-type')]
    """
    The type of activity to record at the accounting server
    """
    record: Annotated[Optional[str], Field(alias='srl_nokia-aaa:record')] = None
    """
    Type of record to send to the accounting server for this activity type
    """


class EviListEntry(BaseModel):
    """
    evi range for this ethernet-segment association
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start: Annotated[
        int,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:start',
            ge=1,
            le=65535,
        ),
    ]
    """
    start of the evi-range for this ethernet-segment
    """


class FieldListEntry(BaseModel):
    """
    This list contains the (Options) Template
    fields of which the (Options) Template is defined.
    The order of the list corresponds to the order of the fields
    in the (Option) Template Record.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    element_id: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:element-id', ge=1, le=32767)
    ] = None
    """
    This parameter indicates the Information
    Element identifier of the field.
    Note that this parameter corresponds to
    ipfixTemplateDefinitionIeId in the IPFIX MIB module.
    """
    element_length: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:element-length', ge=0, le=65535)
    ] = None
    """
    This parameter indicates the length of the
    Information Element of the field.
    Note that this parameter corresponds to
    ipfixTemplateDefinitionIeLength in the IPFIX MIB
    module.
    """
    ie_enterprise_number: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:ie-enterprise-number', ge=0, le=4294967295),
    ] = None
    """
    This parameter indicates the IANA enterprise
    number of the authority defining the Information Element
    identifier.
    If the Information Element is not enterprise-specific,
    this state parameter is zero.
    Note that this parameter corresponds to
    ipfixTemplateDefinitionIeEnterpriseNumber in the IPFIX
    MIB module.
    """
    is_flow_key: Annotated[
        Optional[List[None]],
        Field(alias='srl_nokia-ipfix:is-flowKey', max_length=1, min_length=1),
    ] = None
    """
    If present, this is a Flow Key field.

    Note that this corresponds to flowKey(1) being set in
    ipfixTemplateDefinitionFlags.
    """
    is_scope: Annotated[
        Optional[List[None]],
        Field(alias='srl_nokia-ipfix:is-scope', max_length=1, min_length=1),
    ] = None
    """
    If present, this is a scope field.

    Note that this corresponds to scope(0) being set in
    ipfixTemplateDefinitionFlags.
    """


class ForwardingComplexContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[Optional[str], Field(alias='srl_nokia-grpc:id')] = None
    """
    The normalized ID for this forwarding-complex

    This is the slot number and complex number seperated by a '/', 0 indexed. For example '1/0', or '1/1' representing two forwarding complexes on slot 1.
    """
    device: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:device', ge=0, le=18446744073709551615),
    ] = None
    """
    The P4Runtime ID of the forwarding complex for which this client has established itself

    This is the value configured at /platform/linecard/forwarding-complex/p4rt/id, or a system derived default.
    """
    slot: Annotated[Optional[int], Field(alias='srl_nokia-grpc:slot', ge=0, le=255)] = (
        None
    )
    """
    The linecard slot for which this forwarding complex resides on
    """


class GnmiContainer(BaseModel):
    """
    Container for gnmi configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    commit_confirmed_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:commit-confirmed-timeout', ge=0, le=86400),
    ] = 0
    """
    Number of seconds to wait for confirmation

    A value of 0 means commit confirmed is not used
    """
    commit_save: Annotated[
        Optional[bool], Field(alias='srl_nokia-grpc:commit-save')
    ] = False
    """
    Specifies whether to save startup configuration after every successful commit
    """
    include_defaults_in_config_only_responses: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-grpc:include-defaults-in-config-only-responses'),
    ] = False
    """
    Specifies whether to include field default values in get/subscribe responses when
    using configuration only datastore (for example running/intended datastore)
    """


class GnssCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    gnss: Annotated[Optional[GnssContainer], Field(alias='srl_nokia-sync:gnss')] = None


class GrandmasterClockQualityContainer(BaseModel):
    """
    The clockQuality of the grandmaster clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_class: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:clock-class', ge=0, le=255)
    ] = None
    """
    The clockClass denotes the traceability of the time or frequency distributed by the clock
    """
    clock_accuracy: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:clock-accuracy', ge=0, le=255)
    ] = None
    """
    The clockAccuracy indicates the expected accuracy of the clock
    """
    offset_scaled_log_variance: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:offset-scaled-log-variance', ge=0, le=65535),
    ] = None
    """
    The offsetScaledLogVariance provides an estimate of the variations of the clock
    """


class GrandmasterClockQualityContainer2(BaseModel):
    """
    The clock quality of the grandmaster clock in the last Announce message received from this peer
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_class: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:clock-class', ge=0, le=255)
    ] = None
    """
    The clockClass denotes the traceability of the time or frequency distributed by the clock
    """
    clock_accuracy: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:clock-accuracy', ge=0, le=255)
    ] = None
    """
    The clockAccuracy indicates the expected accuracy of the clock
    """
    offset_scaled_log_variance: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:offset-scaled-log-variance', ge=0, le=65535),
    ] = None
    """
    The offsetScaledLogVariance provides an estimate of the variations of the clock
    """


class Icmp6Container(BaseModel):
    """
    Context for system-wide control of ICMPv6 message generation
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rate_limit_per_host: Annotated[
        Optional[RateLimitPerHostContainer2],
        Field(alias='srl_nokia-system-datapath:rate-limit-per-host'),
    ] = None


class IcmpContainer(BaseModel):
    """
    Context for system-wide control of ICMP message generation
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rate_limit_per_host: Annotated[
        Optional[RateLimitPerHostContainer],
        Field(alias='srl_nokia-system-datapath:rate-limit-per-host'),
    ] = None


class ImageLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[str, Field(pattern='^(?=^[0-9A-Za-z_\\-\\.]*$).*$')]
    """
    Ordered list of local images used to boot the system

    This directly translates into boot configuration in grub, where the images are tried in the order specified by the user. Images are sourced via the internal SD card, and the value passed is the folder that contains the initramfs, kernel, and squashfs image. The search path for these directories is /mnt/nokiaos/<folder>
    """


class InstanceListEntry4(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_number: Annotated[
        int, Field(alias='srl_nokia-sync:instance-number', ge=0, le=255)
    ]
    """
    Information regarding each SV (Space Vehicle)
    """
    constellation: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:constellation')
    ] = None
    """
    Constellation of the SV (Space Vehicle)
    """
    prn: Annotated[Optional[int], Field(alias='srl_nokia-sync:prn', ge=0, le=255)] = (
        None
    )
    """
    Pseudo Random Number (PRN) of the Space Vehicle

    This represents the satellite's unique pseudorandom noise code
    """
    band: Annotated[Optional[str], Field(alias='srl_nokia-sync:band')] = None
    """
    SV's band
    """
    signal_strength: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:signal-strength', ge=0, le=255)
    ] = None
    """
    Carrier to noise ratio in dB-Hz
    """


class InventoryContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    hardware_revision: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:hardware-revision', max_length=32, min_length=0),
    ] = None
    firmware_revision: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:firmware-revision', max_length=32, min_length=0),
    ] = None
    software_revision: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:software-revision', max_length=32, min_length=0),
    ] = None
    serial_number: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:serial-number', max_length=32, min_length=0),
    ] = None
    manufacturer_number: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:manufacturer-number', max_length=32, min_length=0),
    ] = None
    model_name: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:model-name', max_length=32, min_length=0),
    ] = None
    asset_id: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:asset-id', max_length=32, min_length=0),
    ] = None


class Ipv4AddressType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    An IPv4 address in dotted quad notation.
    """


class Ipv6AddressType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$'
        ),
    ]
    """
    An IPv6 address represented as either a full address, shortened or mixed-shortened formats
    """


class LacpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    system_priority: Annotated[
        Optional[int], Field(alias='srl_nokia-lacp:system-priority', ge=0, le=65535)
    ] = None
    """
    System priority used by the node on this LAG interface.
    Lower value is higher priority for determining which node
    is the controlling system.
    """
    system_id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lacp:system-id',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ] = None
    """
    The MAC address portion of the node's System ID. This is
    combined with the system priority to construct the 8-octet
    system-id
    """


class LldpContainer2(BaseModel):
    """
    Container for LLDP.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Link Layer Discovery Protocol tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled LLDP frames. LLDP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and EtherType value
    of 0x88cc.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Link Layer Discovery Protocol frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu LLDP frames. LLDP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and EtherType value
    of 0x88cc.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the LACP counters were cleared.
    """


class LocalLinuxUsersContainer(BaseModel):
    """
    Enclosing container for local linux users
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    disable_login: Annotated[
        Optional[List[EnumerationEnum8]], Field(alias='srl_nokia-aaa:disable-login')
    ] = []
    """
    disable the loging for all local linux users via remote login or console
    """
    allow_fallback: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:allow-fallback')
    ] = False
    """
    enable linux users login in case aaa_mgr is not working
    """


class LocationContainer(BaseModel):
    """
    Selection of location information to transmit when the endpoint supports location capability
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    system_coordinates: Annotated[
        Optional[bool], Field(alias='srl_nokia-lldp:system-coordinates')
    ] = False
    """
    Transmit the configured system coordinate values

    All values will be included in the LLDPDU location TLV.  If no /system/location/coordinates are configured
    the location TLV will not include coordinate information
    """
    elin: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:elin', max_length=25, min_length=10)
    ] = None
    """
    Emergency Location Identification Number

    Included in the location TLV using civic-address encoded as CA-type 128.  The ../system-civic-address does
    not have to be configured or enabled to send this value.
    """


class LockoutPolicyContainer(BaseModel):
    """
    Top-level container for lockout policy
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    attempts: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:attempts', ge=0, le=64)
    ] = 0
    """
    The number of failed login attempts that will lock the account

    A value of 0 means unlimited number of failed login attempts is allowed
    """
    time: Annotated[Optional[int], Field(alias='srl_nokia-aaa:time', ge=0, le=1440)] = 1
    """
    The time period in minutes within which the failed login attempts occur
    """
    lockout: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:lockout', ge=0, le=1440)
    ] = 15
    """
    The time duration in minutes the user account will be locked out

    A value of 0 means that the user account will be locked out/disabled indefinitely
    """


class MacLearningContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac_relearn_only: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-bridge-table:mac-relearn-only')
    ] = None
    """
    The value of this leaf indicates that the system will not
    learn any new mac addresses, but will relearn any that are already
    programmed
    """


class MacLimitContainer(BaseModel):
    """
    Bridge Table size and thresholds.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    maximum_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:maximum-entries',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    Maximum number of mac addresses allowed in the system bridge-table.
    """
    warning_threshold_pct: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:warning-threshold-pct',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    Percentage of the configured max-number-macs over which a warning is triggered.
    The warning message is cleared when the percentage drops below the configured
    percentage minus 5%
    """


class MstInstanceListEntry(BaseModel):
    """
    List of the mstp instances
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mst_id: Annotated[
        int, Field(alias='srl_nokia-system-protocols-mgmt-stp:mst-id', ge=1, le=15)
    ]
    """
    In an MSTP Bridge, an MSTID, is used to identify a multiple-spanning-tree-instance.
    """
    mst_priority: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:mst-priority')
    ] = None
    """
    Priority component of the Bridge Identifier
    """
    vlan_range: Annotated[
        Optional[List[str]],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:vlan-range'),
    ] = []
    """
    List of vlans mapped to the MST instance
    """
    regional_root: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:regional-root')
    ] = None
    """
    The bridge identifier of the regional root determined by the Mst Instance STP
    """
    internal_root_cost: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:internal-root-cost',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The cost of the path to the regional root bridge as seen from this bridge
    """
    remaining_hop_count: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:remaining-hop-count',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The value specifies the remaining number of hops.
    """
    root_port: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:root-port',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The port number of port which offers the lowest cost path from this bridge to the regional root bridge.
    """


class MulticastMsgRateContainer(BaseModel):
    """
    Aggregate multicast message rates for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages transmitted
    """
    anno_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages received
    """
    sync_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages transmitted
    """
    sync_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages received
    """
    del_req_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages transmitted
    """
    del_req_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages received
    """
    del_resp_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages transmitted
    """
    del_resp_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages received
    """
    follow_up_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages transmitted
    """
    follow_up_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages received
    """
    signaling_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages transmitted
    """
    signaling_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages received
    """
    other_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:other-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    Specifies the rate of messages of other messages received
    """


class NameContainer(BaseModel):
    """
    Contains configuration and state related to system naming
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    domain_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-name:domain-name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
        ),
    ] = None
    """
    The system domain name
    """
    host_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-name:host-name',
            pattern='^(?=^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])$).*$',
        ),
    ] = None
    """
    The system host name
    """


class NeighborListListEntry(BaseModel):
    """
    List of MAC address of all the neighbors of this port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_identity: Annotated[
        str, Field(alias='srl_nokia-sync:clock-identity', max_length=8, min_length=8)
    ]
    """
    The clockIdentity of this neighbor clock
    """
    port_number: Annotated[
        int, Field(alias='srl_nokia-sync:port-number', ge=0, le=65535)
    ]
    """
    The port number of this neighbor clock
    """
    mac_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:mac-address',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ] = None
    """
    Specifies the MAC address of this neighbor
    """
    rx_message_rate: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:rx-message-rate',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    The receive message rate from this neighbor clock
    """
    parent_clock: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:parent-clock')
    ] = None
    """
    Indicates if this neighbor is the current parent clock of this PTP clock
    """
    port_timestamping: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:port-timestamping')
    ] = None
    """
    Indicates if this port supports timestamping of PTP event messages

    If this is false, this is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """


class NeighborListListEntry2(BaseModel):
    """
    List of MAC address of all the neighbors of this port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_identity: Annotated[
        str, Field(alias='srl_nokia-sync:clock-identity', max_length=8, min_length=8)
    ]
    """
    The clockIdentity of this neighbor clock
    """
    port_number: Annotated[
        int, Field(alias='srl_nokia-sync:port-number', ge=0, le=65535)
    ]
    """
    The port number of this neighbor clock
    """
    mac_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:mac-address',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ] = None
    """
    Specifies the MAC address of this neighbor
    """
    rx_message_rate: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:rx-message-rate',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
        ),
    ] = None
    """
    The receive message rate from this neighbor clock
    """
    parent_clock: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:parent-clock')
    ] = None
    """
    Indicates if this neighbor is the current parent clock of this PTP clock
    """
    port_timestamping: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:port-timestamping')
    ] = None
    """
    Indicates if this port supports timestamping of PTP event messages

    If this is false, this is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """


class NetconfContainer(BaseModel):
    """
    Top-level container for netconf plugin configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    allowed_operations: Annotated[
        Optional[List[EnumerationEnum11]],
        Field(alias='srl_nokia-aaa:allowed-operations'),
    ] = []
    """
    List of netconf operation, that are allowed for this role. Rest of the operations are denied.
    """


class NetworkInstanceLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$'
        ),
    ]
    """
    List of network instances to enable LLDP BGP auto discovery in

    Default is to run LLDP BGP auto discovery in all network instances
    """


class NetworkInstancesLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$'
        ),
    ]
    """
    List of network instances that should be part of the maintenance group.
    """


class NetworkPolicyLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$'
        ),
    ]
    """
    Name of the network policy for a specific application type

    Multiple network policies can be assigned to a single interface, one per application type.
    """


class NtpServerLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    List of NTP Servers to return to the dhcp client - option 42
    """


class NtpServerLeafList2(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    List of NTP Servers to return to the dhcp client - option 42
    """


class NtpServerLeafList3(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    List of NTP Servers to return to the dhcp client - option 42
    """


class OptionsListEntry(BaseModel):
    """
    List of options reported by the Exporting
    Process.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Key of this list.
    """
    options_type: Annotated[str, Field(alias='srl_nokia-ipfix:options-type')]
    """
    Type of the exported options data.
    """
    options_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:options-timeout', ge=0, le=4294967295),
    ] = None
    """
    Time interval for periodic export of the options
    data.  If set to zero, the export is triggered when the
    options data has changed.
    If not configured by the user, this parameter is set by the
    Monitoring Device.
    """


class OutputModifierAliasListEntry(BaseModel):
    """
    Create or overwrite an output modifier alias

    Output modifier aliases can be entered after '|'.
    They can represent a complete command or part of a target command.

    For example, if you create the following aliases, the output will be the same:
    count = "grep --count"
    match_if = "grep interface"
    count_if = "count interface"
    info | count interface
    info | match_if --count
    info | count_if
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-system-cli:name',
            pattern='^(?=^[^|\\[\\]>\\t\\n" ]*$)(?=^[^\']*$)(?=^[^\\s].*$)(?=^.*[^\\s]$).*$',
        ),
    ]
    """
    Name of the alias
    """
    command: Annotated[
        str,
        Field(
            alias='srl_nokia-system-cli:command',
            pattern='^(?=^[^\\s].*$)(?=^.*[^\\s]$).*$',
        ),
    ]
    """
    Aliased command
    """


class OverloadContainer(BaseModel):
    """
    Container for ISIS overload configurations.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    set_bit: Annotated[
        Optional[bool], Field(alias='srl_nokia-maintenance-mode:set-bit')
    ] = False
    """
    When set to true, the Overload bit is set
    """
    max_metric: Annotated[
        Optional[bool], Field(alias='srl_nokia-maintenance-mode:max-metric')
    ] = False
    """
    When set to true transit links are advertised with a wide metric of 0xffffffe and a narrow metric of 0x3f
    """


class P4rtContainer(BaseModel):
    """
    Container for P4RT related session info
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    primary: Annotated[Optional[bool], Field(alias='srl_nokia-grpc:primary')] = None
    """
    Indicates if this client is the primary for the specified forwarding complex

    Only a single primary per forwarding complex is supported
    """
    forwarding_complex: Annotated[
        Optional[ForwardingComplexContainer],
        Field(alias='srl_nokia-grpc:forwarding-complex'),
    ] = None


class PacketGeneratorContainer(BaseModel):
    """
    Packet generator endpoint
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    packet_rate: Annotated[
        int, Field(alias='srl_nokia-packet-link-qual:packet-rate', ge=1, le=4294967295)
    ]
    """
    Packet rate of the packet generator
    """
    packet_size: Annotated[
        int, Field(alias='srl_nokia-packet-link-qual:packet-size', ge=64, le=8184)
    ]
    """
    Packet size (in bytes) of the packet generator
    """


class ParentPortIdentityContainer(BaseModel):
    """
    The portIdentity of the port on the master
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_identity: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:clock-identity', max_length=8, min_length=8),
    ] = None
    """
    Identity of the parent clock
    """
    port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:port-number', ge=0, le=65535)
    ] = None
    """
    Port number of the parent clock
    """


class PasswordContainer4(BaseModel):
    """
    Top-level container for policies around user passwords
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    complexity_rules: Annotated[
        Optional[ComplexityRulesContainer],
        Field(alias='srl_nokia-aaa:complexity-rules'),
    ] = None
    lockout_policy: Annotated[
        Optional[LockoutPolicyContainer], Field(alias='srl_nokia-aaa:lockout-policy')
    ] = None
    hash_method: Annotated[
        Optional[EnumerationEnum9], Field(alias='srl_nokia-aaa:hash-method')
    ] = None
    """
    The hash algorithm for the passwords entered as plain text

    If no value is configured, then Yescrypt will be used as the hash algorithm unless overriden for specific leafs
    using the srl_nokia-extensions:hash-algorithm yang extension. The Argon2 (ar2) hash algorithm is not supported
    for the linuxadmin user and if selected then the linuxadmin password will be hashed using Yescrypt.
    """
    aging: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:aging', ge=0, le=500)
    ] = 0
    """
    Expire user passwords after this period

    A value of 0 means that the user passwords do not expire
    """
    change_on_first_login: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:change-on-first-login')
    ] = False
    """
    Enable or disable a user being forced to change their password on first time login
    """
    history: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:history', ge=0, le=20)
    ] = 0
    """
    Defines how many previous passwords a new password is matched against, such that a new password can't be one of the previous n passwords
    """


class PathsListEntry(BaseModel):
    """
    List of paths being subscribed to
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[int, Field(alias='srl_nokia-grpc:id', ge=0, le=65535)]
    """
    System generated ID for the subscribed path (within subscription)
    """
    path: Annotated[Optional[str], Field(alias='srl_nokia-grpc:path')] = None
    """
    Path being subscribed to
    """
    mode: Annotated[Optional[EnumerationEnum16], Field(alias='srl_nokia-grpc:mode')] = (
        None
    )
    """
    Subscription mode (on-change, sample, target-defined, poll, once)
    """
    sample_interval: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:sample-interval', ge=0, le=18446744073709551615),
    ] = None
    """
    Time in seconds to provide updates to the remote host, set to 0 for all subscription modes except SAMPLE
    """


class PeerGroupLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    List of BGP peer groups that belong to the network instance and that should be part of the maintenance group

    If this list is empty and so is the neighbor list, then the system interprets the meaning as ALL static and dynamic sessions belonging to the specified network-instance.
    """


class PfcpContainer(BaseModel):
    """
    Configure the PFCP interface between the cMAG-c and the MAG-u
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    shared_secret: Annotated[
        str, Field(alias='srl_nokia-lawful-intercept:shared-secret')
    ]
    """
    Secret shared between the cMAG-c and the MAG-u
    """


class PortDsCfgIpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    index: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:index', ge=1, le=999)
    ] = None
    """
    Peer used as the source of PTP messages into the recovery engine
    """


class PreferenceAlgContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    preference_value: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:preference-value',
            ge=0,
            le=65535,
        ),
    ] = 32767
    """
    Preference that is used to elect the designated forwarder
    """
    oper_preference_value: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-preference-value',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    Operational Preference value
    """
    oper_do_not_prempt: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-do-not-prempt'
        ),
    ] = None
    """
    Operational do-not-preempt value
    """
    capabilities: Annotated[
        Optional[CapabilitiesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:capabilities'
        ),
    ] = None


class PrimaryEviRangeListEntry(BaseModel):
    """
    evi range for this ethernet-segment
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_evi: Annotated[
        int,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:start-evi',
            ge=1,
            le=65535,
        ),
    ]
    """
    start of the evi-range for this ethernet-segment
    """
    end_evi: Annotated[
        int,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:end-evi',
            ge=1,
            le=65535,
        ),
    ]
    """
    end of the evi-range for this ethernet-segment
    """


class PtpCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ptp: Annotated[Optional[PtpContainer2], Field(alias='srl_nokia-sync:ptp')] = None


class PtpContainer(BaseModel):
    """
    Container for Precision Time Protocol Peer-Delay protocol.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Precision Time Protocol Peer-Delay tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled PTP frames. PTP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and Ethertype
    value of 0x88F7.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Precision Time Protocol Peer-Delay frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu PTP frames. PTP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and Ethertype
    value of 0x88F7.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the PTP counters were cleared.
    """


class RadiusContainer(BaseModel):
    """
    Top-level container for RADIUS server data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    auth_port: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:auth-port', ge=0, le=65535)
    ] = 1812
    """
    Port number for authentication requests
    """
    acct_port: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:acct-port', ge=0, le=65535)
    ] = 1813
    """
    Port number for accounting requests
    """
    secret_key: Annotated[Optional[str], Field(alias='srl_nokia-aaa:secret-key')] = None
    """
    The unencrypted shared key used between the system and server, up to 64 characters cleartext
    """
    retransmit_attempts: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:retransmit-attempts', ge=0, le=255)
    ] = 3
    """
    Number of times the system may send a request to the unresponsive server
    """


class ReadsContainer(BaseModel):
    """
    The counter were collected while performing a read operation on the schema path.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-rejects', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module denied access
    to a schema path.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz denied access to
    a schema path.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-accepts', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module allowed access
    to a schema path.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz allowed access to
    a schema path.
    """


class RoleLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    List of roles to assign to this user

    The most specific rule for a particular role takes precedence.
    Rules from all user roles are evaluated together, most permissive privilege taking precedence.
    """


class RoleLeafList2(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    List of roles to assign to this user

    The most specific rule for a particular role takes precedence.
    Rules from all user roles are evaluated together, most permissive privilege taking precedence.
    """


class RouteDistinguisherContainer(BaseModel):
    """
    Route Distinguisher (RD) of the bgp-vpn instance.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rd: Annotated[
        Optional[
            Union[
                RouteDistinguisherType0Type,
                RouteDistinguisherType1Type,
                RouteDistinguisherType2Type,
                RouteDistinguisherType2bType,
            ]
        ],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:rd'),
    ] = None
    """
    Route Distinguisher (RD) of the system bgp-vpn instance. The RD is auto-derived
    as <ip-address>:0 where 'ip-address' is the ipv4 address associated to the subinterface lo0.1.
    """
    route_distinguisher_origin: Annotated[
        Optional[EnumerationEnum67],
        Field(
            alias='srl_nokia-system-network-instance-bgp-vpn:route-distinguisher-origin'
        ),
    ] = None
    """
    Origin of the operational Route Distinguisher (RD) of the bgp-vpn instance.

     'Auto-derived-from-system-ip:0' refers to the RD for the EVPN Ethernet Segment routes that is automatically allocated with the format <ip-address>:0
     where 'ip-address' is the ipv4 address associated to the subinterface lo0.1.
    """


class RouteTargetContainer(BaseModel):
    """
    Route Target (RT) of the system bgp-vpn instance.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    export_route_target_origin: Annotated[
        Optional[EnumerationEnum68],
        Field(
            alias='srl_nokia-system-network-instance-bgp-vpn:export-route-target-origin'
        ),
    ] = None
    """
    Origin of the operational export Route Target (RT) of the bgp-vpn instance.

     'Auto-derived-from-esi-bytes-1-6' refers to the ES-import RT for the EVPN Ethernet Segment routes that is derived from bytes 1 to 6 of the Ethernet Segment
     Identifier of the route.
    """
    import_route_target_origin: Annotated[
        Optional[EnumerationEnum69],
        Field(
            alias='srl_nokia-system-network-instance-bgp-vpn:import-route-target-origin'
        ),
    ] = None
    """
    Origin of the operational import Route Target (RT) of the bgp-vpn instance.

     'Auto-derived-from-esi-bytes-1-6' refers to the ES-import RT for the EVPN Ethernet Segment routes that is derived from bytes 1 to 6 of the Ethernet Segment
     Identifier of the route.
    """


class RpcContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    pre_sync_duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:pre-sync-duration', ge=0, le=4294967295
        ),
    ]
    """
    Duration of the pre-sync phase
    """
    setup_duration: Annotated[
        int,
        Field(alias='srl_nokia-packet-link-qual:setup-duration', ge=20, le=4294967295),
    ]
    """
    Duration of the setup phase
    """
    duration: Annotated[
        int, Field(alias='srl_nokia-packet-link-qual:duration', ge=1, le=4294967295)
    ]
    """
    Duration of the test
    """
    post_sync_duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:post-sync-duration', ge=0, le=4294967295
        ),
    ]
    """
    Duration of the post-sync phase
    """
    teardown_duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:teardown-duration', ge=15, le=4294967295
        ),
    ]
    """
    Duration of the teardown phase
    """


class RpcListEntry(BaseModel):
    """
    A collection of counters collected by the gNSI.authz module
    for a RPC identified by the `name`.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-gnsi-authz:name')]
    """
    The name of the RPC the counters were collected
    for.
    """
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-authz:access-rejects', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of times the gNSI.authz module denied access
    to a RPC.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-authz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz denied access to
    a RPC.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-authz:access-accepts', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of times the gNSI.authz module allowed access
    to a RPC.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-authz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz allowed access to
    a RPC.
    """


class RpcListEntry2(BaseModel):
    """
    A collection of counters collected by the gNSI.authz module
    for a RPC identified by the `name`.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-grpc:name')]
    """
    The name of the RPC the counters were collected
    for.
    """
    access_rejects: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:access-rejects', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of times the gNSI.authz module denied access
    to a RPC.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz denied access to
    a RPC.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:access-accepts', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of times the gNSI.authz module allowed access
    to a RPC.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz allowed access to
    a RPC.
    """


class SampleCountBasedCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    sample_count_based: Annotated[
        Optional[SampleCountBasedContainer],
        Field(alias='srl_nokia-ipfix:sample-count-based'),
    ] = None


class SatellitesInUseContainer(BaseModel):
    """
    The list of satellites currently in use
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    number_of_satellites_in_use: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:number-of-satellites-in-use', ge=0, le=255),
    ] = None
    """
    The number of satellites currently in use
    """
    instance: Annotated[
        Optional[List[InstanceListEntry4]], Field(alias='srl_nokia-sync:instance')
    ] = None


class SelectionProcessLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    Selection Processes in this list process
    packets in parallel.
    """


class SelectorListEntry(BaseModel):
    """
    List of Selectors that define the action of the
    Selection Process on a single packet.  The Selectors are
    serially invoked in the same order as they appear in this
    list.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Key of this list.
    """
    method: Annotated[SampleCountBasedCase, Field(alias='srl_nokia-ipfix:method')]
    packets_observed: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:packets-observed', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of packets observed at the input of
    the Selector.
    """
    packets_dropped: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:packets-dropped', ge=0, le=18446744073709551615),
    ] = 0
    """
    The total number of packets discarded by the
    Selector.
    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    selectorDiscontinuityTime.
    """
    selector_discontinuity_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ipfix:selector-discontinuity-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the most recent occasion at which
    one or more of the Selector counters suffered a
    discontinuity.
    """


class SessionListEntry(BaseModel):
    """
    List of active sessions in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[Optional[str], Field(alias='srl_nokia-aaa:username')] = None
    """
    Username linked to the session
    """
    id: Annotated[int, Field(alias='srl_nokia-aaa:id', ge=0, le=4294967295)]
    """
    System generated session ID
    """
    spiffe_id: Annotated[Optional[str], Field(alias='srl_nokia-aaa:spiffe-id')] = None
    """
    SPIFFE ID linked to the session
    """
    service_name: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:service-name')
    ] = None
    """
    Service name that called login for the session
    """
    authentication_method: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:authentication-method')
    ] = None
    """
    Authentication method that authorized the user (the server-group name or local)
    """
    priv_lvl: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:priv-lvl', ge=0, le=255)
    ] = None
    """
    TACACS+ authorization priv-lvl (if TACACS+ authorization is enabled)
    """
    tty_name: Annotated[Optional[str], Field(alias='srl_nokia-aaa:tty-name')] = None
    """
    Terminal type
    """
    pid: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:pid', ge=-2147483648, le=2147483647)
    ] = None
    """
    Process identifier
    """
    remote_host: Annotated[Optional[str], Field(alias='srl_nokia-aaa:remote-host')] = (
        None
    )
    """
    Remote host of the session
    """
    login_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:login-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time the user logged in
    """
    role: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:role')] = []
    """
    List of roles assigned to this user
    """


class SetTagSetLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    Reference to a tag-set defined under routing-policy
    """


class SignalingUniNegTlvContainer(BaseModel):
    """
    Counts of different unicast negotiation TLVs
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    request_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for announce messages have been received
    """
    grant_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for announce messages have been received
    """
    reject_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been received
    """
    cancel_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been received
    """
    ack_cancel_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been received
    """
    request_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for sync messages have been received
    """
    grant_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for sync messages have been received
    """
    reject_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been received
    """
    cancel_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been received
    """
    ack_cancel_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been received
    """
    request_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been received
    """
    grant_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been received
    """
    reject_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been received
    """
    cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been received
    """
    ack_cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been received
    """
    request_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for announce messages have been transmitted
    """
    grant_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for announce messages have been transmitted
    """
    reject_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been transmitted
    """
    cancel_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been transmitted
    """
    ack_cancel_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been transmitted
    """
    request_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for sync messages have been transmitted
    """
    grant_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for sync messages have been transmitted
    """
    reject_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been transmitted
    """
    cancel_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been transmitted
    """
    ack_cancel_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been transmitted
    """
    request_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been transmitted
    """
    grant_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been transmitted
    """
    reject_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been transmitted
    """
    cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been transmitted
    """
    ack_cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been transmitted
    """
    other_tlv: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:other-tlv', ge=0, le=18446744073709551615),
    ] = 0
    """
    The count of unsupported signaling message TLVs received.
    """


class SignalingUniNegTlvContainer2(BaseModel):
    """
    Counts of different unicast negotiation TLVs
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    request_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for announce messages have been received
    """
    grant_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for announce messages have been received
    """
    reject_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been received
    """
    cancel_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been received
    """
    ack_cancel_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been received
    """
    request_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for sync messages have been received
    """
    grant_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for sync messages have been received
    """
    reject_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been received
    """
    cancel_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been received
    """
    ack_cancel_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been received
    """
    request_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been received
    """
    grant_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been received
    """
    reject_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been received
    """
    cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been received
    """
    ack_cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been received
    """
    request_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for announce messages have been transmitted
    """
    grant_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for announce messages have been transmitted
    """
    reject_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been transmitted
    """
    cancel_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been transmitted
    """
    ack_cancel_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been transmitted
    """
    request_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for sync messages have been transmitted
    """
    grant_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for sync messages have been transmitted
    """
    reject_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been transmitted
    """
    cancel_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been transmitted
    """
    ack_cancel_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been transmitted
    """
    request_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been transmitted
    """
    grant_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been transmitted
    """
    reject_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been transmitted
    """
    cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been transmitted
    """
    ack_cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been transmitted
    """
    other_tlv: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:other-tlv', ge=0, le=18446744073709551615),
    ] = 0
    """
    The count of unsupported signaling message TLVs received.
    """


class SignalingUniNegTlvContainer3(BaseModel):
    """
    Counts of different unicast negotiation TLVs
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    request_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for announce messages have been received
    """
    grant_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for announce messages have been received
    """
    reject_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been received
    """
    cancel_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been received
    """
    ack_cancel_anno_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-anno-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been received
    """
    request_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for sync messages have been received
    """
    grant_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for sync messages have been received
    """
    reject_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been received
    """
    cancel_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been received
    """
    ack_cancel_sync_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-sync-rx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been received
    """
    request_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been received
    """
    grant_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been received
    """
    reject_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been received
    """
    cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-rx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been received
    """
    ack_cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been received
    """
    request_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for announce messages have been transmitted
    """
    grant_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for announce messages have been transmitted
    """
    reject_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been transmitted
    """
    cancel_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been transmitted
    """
    ack_cancel_anno_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-anno-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been transmitted
    """
    request_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:request-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of requests for sync messages have been transmitted
    """
    grant_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:grant-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of grants for sync messages have been transmitted
    """
    reject_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:reject-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been transmitted
    """
    cancel_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:cancel-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been transmitted
    """
    ack_cancel_sync_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:ack-cancel-sync-tx', ge=0, le=18446744073709551615),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been transmitted
    """
    request_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been transmitted
    """
    grant_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been transmitted
    """
    reject_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been transmitted
    """
    cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-tx', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been transmitted
    """
    ack_cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been transmitted
    """
    other_tlv: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:other-tlv', ge=0, le=18446744073709551615),
    ] = 0
    """
    The count of unsupported signaling message TLVs received.
    """


class SshCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ssh_server: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-netconf-server:ssh-server',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    The SSH server instance to bind the NETCONF server to
    """


class StaticRouteListEntry(BaseModel):
    """
    This option can contain one or more static routes, each of which consists of a destination descriptor and the IP address of the router that should be used to reach that destination - option 121
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    destination: Annotated[
        str,
        Field(
            alias='srl_nokia-dhcp-server:destination',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))$).*$',
        ),
    ]
    """
    A destination descriptor
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IP address of the router that should be used to reach that destination
    """


class StaticRouteListEntry2(BaseModel):
    """
    This option can contain one or more static routes, each of which consists of a destination descriptor and the IP address of the router that should be used to reach that destination - option 121
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    destination: Annotated[
        str,
        Field(
            alias='srl_nokia-dhcp-server:destination',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))$).*$',
        ),
    ]
    """
    A destination descriptor
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IP address of the router that should be used to reach that destination
    """


class StaticRouteListEntry3(BaseModel):
    """
    This option can contain one or more static routes, each of which consists of a destination descriptor and the IP address of the router that should be used to reach that destination - option 121
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    destination: Annotated[
        str,
        Field(
            alias='srl_nokia-dhcp-server:destination',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))$).*$',
        ),
    ]
    """
    A destination descriptor
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IP address of the router that should be used to reach that destination
    """


class StatisticsContainer10(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    client_packets_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total received dhcp packets from dhcp client(s)
    """
    client_packets_discarded: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-discarded',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total discarded dhcp packets from dhcp client(s)
    """
    server_packets_sent: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:server-packets-sent',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total dhcp packets sent from DHCP server towards dhcp client(s)
    """


class StatisticsContainer13(BaseModel):
    """
    Top-level container for application statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    restart_count: Annotated[
        Optional[int],
        Field(alias='srl_nokia-app-mgmt:restart-count', ge=0, le=4294967295),
    ] = 0
    """
    The number of times this application instance has restarted
    """


class StatisticsContainer17(BaseModel):
    """
    Top-level container for event handler statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    upython_duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:upython-duration',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    Total time taken for all executions of this script to return output
    """
    execution_count: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-count',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total number of executions of this script
    """
    execution_successes: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-successes',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total number of successful executions of this script
    """
    execution_timeouts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-timeouts',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total number of timeouts in executions of this script
    """
    execution_errors: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-errors',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total number of errors in executions of this script
    """


class StatisticsContainer2(BaseModel):
    """
    Statistics related to the gRPC server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:access-rejects', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of times the gRPC server denied access to the server
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gRPC server denied access to the server
    """
    access_accepts: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:access-accepts', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of times the gPRC allowed access to the server
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gRPC allowed access to the server
    """
    rpc: Annotated[Optional[List[RpcListEntry2]], Field(alias='srl_nokia-grpc:rpc')] = (
        None
    )


class StatisticsContainer21(BaseModel):
    """
    Total messages for a specific PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer2], Field(alias='srl_nokia-sync:discards')
    ] = None


class StatisticsContainer22(BaseModel):
    """
    Total messages for a specific PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer3], Field(alias='srl_nokia-sync:discards')
    ] = None
    signaling_uni_neg_tlv: Annotated[
        Optional[SignalingUniNegTlvContainer2],
        Field(alias='srl_nokia-sync:signaling-uni-neg-tlv'),
    ] = None


class StatisticsContainer23(BaseModel):
    """
    Total messages for a specific PTP port

    This container is not used with PTP special ports (gnss).
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer4], Field(alias='srl_nokia-sync:discards')
    ] = None
    signaling_uni_neg_tlv: Annotated[
        Optional[SignalingUniNegTlvContainer3],
        Field(alias='srl_nokia-sync:signaling-uni-neg-tlv'),
    ] = None


class StatisticsContainer24(BaseModel):
    """
    Total messages for a specific PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer5], Field(alias='srl_nokia-sync:discards')
    ] = None


class StatisticsContainer25(BaseModel):
    """
    Enclosing container for system dot1x tunneling statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dot1x-tunneling:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System or interface level incoming 802.1x tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled 802.1x frames.
    802.1x frames are identified by a destination MAC value of 01:80:c2:00:00:03 and EtherType value of 0x888e.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dot1x-tunneling:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System or interface level incoming 802.1x frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu 802.1x frames.
    802.1x frames are identified by a destination MAC value of 01:80:c2:00:00:03 and EtherType value of 0x888e.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dot1x-tunneling:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the 802.1x counters were cleared
    """


class StatisticsContainer8(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ingress_mirrored_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:ingress-mirrored-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of ingress mirrored packets
    """
    egress_mirrored_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:egress-mirrored-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of egress mirrored packets
    """
    ingress_mirrored_octets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:ingress-mirrored-octets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of ingress mirrored octets
    """
    egress_mirrored_octets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:egress-mirrored-octets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of egress mirrored octets
    """


class StatisticsContainer9(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    client_packets_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total received dhcp packets from dhcp client(s)
    """
    client_packets_discarded: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-discarded',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total discarded dhcp packets from dhcp client(s)
    """
    server_packets_sent: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:server-packets-sent',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total dhcp packets sent from DHCP server towards dhcp client(s)
    """


class Sync0Case(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    sync0: Annotated[Optional[Sync0Container], Field(alias='srl_nokia-sync:sync0')] = (
        None
    )


class TemplateListEntry(BaseModel):
    """
    This list contains the Templates and Options
    Templates that are transmitted by the Exporting Process
    or received by the Collecting Process.
    Withdrawn or invalidated (Options) Templates MUST be removed
    from this list.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    observation_domain_id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:observation-domain-id', ge=0, le=4294967295),
    ] = None
    """
    The ID of the Observation Domain for which this
    Template is defined.
    """
    template_id: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:template-id', ge=256, le=65535)
    ] = None
    """
    This number indicates the Template ID in the IPFIX
    message.
    """
    set_id: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:set-id', ge=0, le=65535)
    ] = None
    """
    This number indicates the Set ID of the Template.
    Currently, there are two values defined.  The value 2 is used
    for Sets containing Template definitions.  The value 3 is
    used for Sets containing Options Template definitions.
    """
    access_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ipfix:access-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Used for Exporting Processes, this parameter
    contains the time when this (Options) Template was last
    sent to the Collector(s) or written to the file.
    Used for Collecting Processes, this parameter contains the
    time when this (Options) Template was last received from the
    Exporter.
    """
    template_data_records: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ipfix:template-data-records', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    The number of transmitted or received Data
    Records defined by this (Options) Template.
    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    templateDiscontinuityTime.
    """
    template_discontinuity_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ipfix:template-discontinuity-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the most recent occasion at which
    the counter templateDataRecords suffered a discontinuity.
    Note that this parameter functionally corresponds to
    ipfixTemplateDiscontinuityTime in the IPFIX MIB module.
    In contrast to ipfixTemplateDiscontinuityTime, the time
    is absolute and not relative to sysUpTime.
    """
    field: Annotated[
        Optional[List[FieldListEntry]], Field(alias='srl_nokia-ipfix:field')
    ] = None


class TftpServerAddressLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """


class TftpServerAddressLeafList2(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """


class TftpServerAddressLeafList3(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """


class TimeoutCacheContainer(BaseModel):
    """
    Flow expiration after active and idle
    timeout; generation of Flow Records.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    maximum_flows: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:maximum-flows', ge=0, le=4294967295)
    ] = 250000
    """
    This parameter configures the maximum number of flows in the Cache

    This values is the maximum number of Flows that can be monitored simultaneously.
    The Monitoring Device MUST ensure that sufficient resources
    are available to store the configured maximum number of Flows.
    If the maximum number of Flows is measured, an additional
    Flow can be measured only if an existing entry is removed
    and exported to available collectors.
    """
    active_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:active-timeout', ge=0, le=4294967295),
    ] = 1800
    """
    This parameters specified the active timeout for active flows within the cache

    This parameter configures the time in seconds after which a Flow is expired even though packets matching this Flow are still received by the Cache.
    The parameter value zero indicates infinity, meaning that there is no active timeout.
    """
    idle_timeout: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:idle-timeout', ge=0, le=4294967295)
    ] = 15
    """
    This parameters specified the idle timeout for in-active flows within the cache.

    This parameter configures the time in seconds after which a Flow is expired if no more packets matching this Flow are received by the Cache.
    The parameter value zero indicates infinity, meaning that there is no idle timeout.
    If not configured by the user, the Monitoring Device sets this parameter.
    """
    active_flows: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:active-flows', ge=0, le=4294967295)
    ] = None
    """
    The number of Flows currently active in this Cache.

    Note that this parameter corresponds to ipfixMeteringProcessCacheActiveFlows in the IPFIX MIB module.
    """
    unused_cache_entries: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:unused-cache-entries', ge=0, le=4294967295),
    ] = None
    """
    The number of unused Cache entries in this Cache.
    Note that this parameter corresponds to ipfixMeteringProcessCacheUnusedCacheEntries in the IPFIX MIB module.
    """
    overflow_flush: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:overflow-flush', ge=0, le=255)
    ] = 1
    """
    Set the percentage of the cache that is flushed when an overflow event occurs
    """


class TunnelContainer(BaseModel):
    """
    Enclosing container for system dot1x tunneling
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer25],
        Field(alias='srl_nokia-dot1x-tunneling:statistics'),
    ] = None


class TxAnnounceContainer(BaseModel):
    """
    Statistics for transmit announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum123], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxAnnounceContainer2(BaseModel):
    """
    Statistics for transmit announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum129], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxDelayRespContainer(BaseModel):
    """
    Statistics for transmit delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum125], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxDelayRespContainer2(BaseModel):
    """
    Statistics for transmit delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum131], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxSyncContainer(BaseModel):
    """
    Statistics for transmit sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum124], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxSyncContainer2(BaseModel):
    """
    Statistics for transmit sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum130], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TypeListEntry(BaseModel):
    """
    List of the SSH servers host private-keys and certificates
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[EnumerationEnum7, Field(alias='srl_nokia-ssh:type')]
    """
    Type of generated host key
    """
    private_key: Annotated[Optional[str], Field(alias='srl_nokia-ssh:private-key')] = (
        None
    )
    """
    The value should be the host private key as read from the private key file.

    This sets the HostKey option within each SSH servers configuration file.
    """
    public_key: Annotated[Optional[str], Field(alias='srl_nokia-ssh:public-key')] = None
    """
    The value is be the host public key as read from the public key file.
    """
    certificate: Annotated[Optional[str], Field(alias='srl_nokia-ssh:certificate')] = (
        None
    )
    """
    Each item value should be the host key certificate as read from the *-cert.pub file generated by the CA including the certificate type, e.g. 'ssh-rsa-cert-v01@openssh.com AAAA<...> comment'.

    This certificate is returned to clients during SSH init for the client to verify the host it is communicating with.

    This sets the HostCertificate option within each SSH servers configuration file. The certificate should be generated by first extracting the systems current public key and having this signed by a CA.
    """


class ValueCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    value: Annotated[Optional[str], Field(alias='srl_nokia-event-handler:value')] = None
    """
    Single value to associate with this object
    """


class ValuesCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    values: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-event-handler:values')
    ] = []
    """
    List of values to associate with this object

    These are serialized as a JSON array when provided as input to the script.
    """


class WritesContainer(BaseModel):
    """
    The counter were collected while performing a write operation on the schema path.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-rejects', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module denied access
    to a schema path.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz denied access to
    a schema path.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-accepts', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module allowed access
    to a schema path.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz allowed access to
    a schema path.
    """


class XstpContainer(BaseModel):
    """
    Container for Spanning Tree Protocols.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Spanning Tree tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled Spanning Tree frames.
    xSTP frames are identified by a destination MAC value of 01:80:c2:00:00:00 and LLC value
    0x42.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Spanning Tree Protocol frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu Spanning Tree frames.
    Spanning Tree frames are identified by a destination MAC value of 01:80:c2:00:00:00 and
    LLC value 0x42.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the xSTP counters were cleared.
    """


class AccountingMethodLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    Ordered list of server-groups to use for accounting in the system

    If accounting fails with one method, the next defined method is tried -- failure of all methods results in the accounting request failing.
    """


class AccountingContainer(BaseModel):
    """
    Top-level container for accounting
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    accounting_method: Annotated[
        Optional[List[AccountingMethodLeafList]],
        Field(alias='srl_nokia-aaa:accounting-method'),
    ] = []
    """
    Ordered list of server-groups to use for accounting in the system

    If accounting fails with one method, the next defined method is tried -- failure of all methods results in the accounting request failing.
    """
    event: Annotated[
        Optional[List[EventListEntry]], Field(alias='srl_nokia-aaa:event')
    ] = None


class AdmfContainer(BaseModel):
    """
    Configure IP address and port of the administration function (ADMF)
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    address: Annotated[
        str,
        Field(
            alias='srl_nokia-lawful-intercept:address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ]
    """
    IP address of the ADMF server
    """
    port: Annotated[
        Optional[int], Field(alias='srl_nokia-lawful-intercept:port', ge=0, le=65535)
    ] = None
    """
    Port number of the ADMF server
    """


class AuthenticationMethodLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    Ordered list of server-groups to be used during user authentication

    If authentication fails with one method, the next defined method is tried -- failure of all methods results in the user being denied access.
    """


class BgpAutoDiscoveryContainer(BaseModel):
    """
    Top-level container for global LLDP BGP auto discovery
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-lldp:admin-state')
    ] = 'disable'
    """
    Enable or disable LLDP BGP auto discovery at the system level

    Setting this to disable will override any per-interface LLDP
    BGP autodiscovery configuration
    """
    network_instance: Annotated[
        Optional[List[NetworkInstanceLeafList]],
        Field(alias='srl_nokia-lldp:network-instance'),
    ] = []
    """
    List of network instances to enable LLDP BGP auto discovery in

    Default is to run LLDP BGP auto discovery in all network instances
    """
    group_id: Annotated[
        Optional[int], Field(alias='srl_nokia-lldp:group-id', ge=0, le=4294967295)
    ] = None
    """
    A four byte integer to send on outgoing LLDPDUs

    This value can be used on the remote end to do peer group association.
    This sub-TLV is not sent by default
    """


class BgpInstanceListEntry3(BaseModel):
    """
    List of bgp-vpn instances configured in the system network-instance. Only one instance allowed in the current release.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        int, Field(alias='srl_nokia-system-network-instance-bgp-vpn:id', ge=1, le=2)
    ]
    """
    The index of the bgp-vpn instance
    """
    route_distinguisher: Annotated[
        Optional[RouteDistinguisherContainer],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:route-distinguisher'),
    ] = None
    route_target: Annotated[
        Optional[RouteTargetContainer],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:route-target'),
    ] = None
    oper_down_reason: Annotated[
        Optional[EnumerationEnum70],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:oper-down-reason'),
    ] = None
    """
    Reason for the system bgp-instance being down
    """


class BgpVpnContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp_instance: Annotated[
        Optional[List[BgpInstanceListEntry3]],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:bgp-instance'),
    ] = None


class CandidateListEntry(BaseModel):
    """
    List of configuration candidates currently active
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-configuration:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Name of the configuration candidate
    """
    type: Annotated[
        Optional[EnumerationEnum50], Field(alias='srl_nokia-configuration:type')
    ] = None
    """
    Type of configuration candidate
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    User that started the configuration session
    """
    started: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:started',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Start date and time of the configuration session
    """


class CliEngineContainer(BaseModel):
    """
    CLI engine settings
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    completion_ignore_case: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-cli:completion-ignore-case')
    ] = False
    """
    Ignore case when filtering completion results
    """
    completion_display: Annotated[
        Optional[EnumerationEnum37],
        Field(alias='srl_nokia-system-cli:completion-display'),
    ] = 'popup'
    """
    Display style of possible commands

    Note: The basic CLI engine supports only completion display 'inline'.
    """
    completion_type: Annotated[
        Optional[EnumerationEnum38], Field(alias='srl_nokia-system-cli:completion-type')
    ] = 'smart'
    """
    Set completion type used for auto completions and auto suggestions in the CLI

    Note: The basic CLI engine supports only completion type 'prefix'.
    """
    history_filename: Annotated[
        Optional[str], Field(alias='srl_nokia-system-cli:history-filename')
    ] = '~/.srlinux_history'
    """
    Set the filename where history is stored
    """
    max_history_items: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-cli:max-history-items', ge=1, le=1000),
    ] = 1000
    """
    Set the maximum history items to be stored in persistent storage
    """
    refresh_interval: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-cli:refresh-interval', ge=0, le=86400),
    ] = 5
    """
    Set refresh interval in seconds (0 means refresh is disabled)
    """
    type: Annotated[
        Optional[EnumerationEnum39], Field(alias='srl_nokia-system-cli:type')
    ] = 'advanced'
    """
    Set CLI engine type for interactive logins
    """
    vi_editing_mode: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-cli:vi-editing-mode')
    ] = False
    """
    Set vi editing mode
    """


class CommitListEntry(BaseModel):
    """
    List of configuration transactions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[int, Field(alias='srl_nokia-configuration:id', ge=0, le=4294967295)]
    """
    System identifier for the commit
    """
    type: Annotated[
        Optional[EnumerationEnum50], Field(alias='srl_nokia-configuration:type')
    ] = None
    """
    Type of configuration candidate the commit was triggered from
    """
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Name of the configuration candidate the commit was triggered from
    """
    status: Annotated[
        Optional[EnumerationEnum51], Field(alias='srl_nokia-configuration:status')
    ] = None
    """
    Current status of the commit
    """
    comment: Annotated[
        Optional[str], Field(alias='srl_nokia-configuration:comment')
    ] = None
    """
    Operator provided comment associated with this commit
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    User that started the commit
    """
    started: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:started',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Start date and time of the commit
    """
    ended: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:ended',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    End date and time of the commit

    This field is not populated if the commit is in progress
    """
    persist_id: Annotated[
        Optional[str], Field(alias='srl_nokia-configuration:persist-id')
    ] = None
    """
    Persistent confirmed commit identifier
    """


class CountersContainer(BaseModel):
    """
    A collection of counters that were collected by the SSH server during the SSH authentication process.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-credentialz:access-rejects',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    The total number of times the SSH server denied access to the server.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the SSH server denied access to the server.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-credentialz:access-accepts',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    The total number of times the SSH allowed access to the server.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    A timestamp of the last time the SSH allowed access to the server.
    """


class CountersContainer2(BaseModel):
    """
    A collection of counters collected by the gNSI.authz module.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rpc: Annotated[
        Optional[List[RpcListEntry]], Field(alias='srl_nokia-gnsi-authz:rpc')
    ] = None


class CrlContainer(BaseModel):
    """
    State relating to the active certificate revocation list provided via Certz

    The list of certificates provided will not be used to validate mTLS or servers, even if those certificates exist within the trust anchor.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-gnsi-certz:version')] = (
        None
    )
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-certz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CrlContainer2(BaseModel):
    """
    State relating to the active certificate revocation list provided via Certz

    The list of certificates provided will not be used to validate mTLS or servers, even if those certificates exist within the trust anchor.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-grpc:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CurrentDsContainer(BaseModel):
    """
    Provides current data from operation of the protocol
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    steps_removed: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:steps-removed', ge=0, le=65535)
    ] = None
    """
    The number of PTP clock steps in the path between the this PTP instance and the GM
    """
    offset_from_master: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:offset-from-master',
            ge=-9223372036854775808,
            le=9223372036854775807,
        ),
    ] = None
    """
    The time difference between this PTP instance and the master clock
    """
    mean_delay: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:mean-delay',
            ge=-9223372036854775808,
            le=9223372036854775807,
        ),
    ] = None
    """
    The mean propagation time between this PTP instance and the master clock
    """


class CurrentTimeContainer(BaseModel):
    """
    The current time in the current data set
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    time_seconds: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-seconds', ge=0, le=18446744073709551615),
    ] = None
    """
    Seconds of time
    """
    time_nano_seconds: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-nano-seconds', ge=0, le=4294967295),
    ] = None
    """
    Nano-seconds of time
    """
    date_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:date-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    PTP current time converted to UTC and presented as a date-time string
    """


class DhcpServerGuardPolicyListEntry(BaseModel):
    """
    List containing DHCP server Guard Policy and parameters
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-dhcp-server-guard:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    DHCP server guard policy name
    """
    action: Annotated[
        Optional[EnumerationEnum102], Field(alias='srl_nokia-dhcp-server-guard:action')
    ] = 'discard'
    """
    Describes the DHCP server guard policy action for DHCP server Messages matching specified attributes
    DHCP server messages not matching the specified attributes will be handled in the opposite manner.
    """
    source_prefix_set: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server-guard:source-prefix-set',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to a prefix set to match DHCP server source address
    If not specified the verification is skipped.
    """
    server6_preference: Annotated[
        Optional[Server6PreferenceContainer],
        Field(alias='srl_nokia-dhcp-server-guard:server6-preference'),
    ] = None


class DnsServerLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """


class DnsServerLeafList2(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """


class DnsServerLeafList3(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """


class DnsServerLeafList4(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$'
        ),
    ]
    """
    An Ordered List of DNS servers to return to the dhcp client
    """


class DnsServerLeafList5(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$'
        ),
    ]
    """
    An Ordered List of DNS servers to return to the dhcp client
    """


class Dot1xContainer(BaseModel):
    """
    Enclosing container for system dot1x
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    tunnel: Annotated[
        Optional[TunnelContainer], Field(alias='srl_nokia-dot1x-tunneling:tunnel')
    ] = None


class DynamicListEntry(BaseModel):
    """
    List of dynamic label blocks

    When a client application binds its operation to a dynamic label block that client application is expected to just ask for the next available label within the dynamic label block.

    At this time a dynamic label block cannot be shared by multiple different clients/protocols. Each protocol needing dynamic labels must have its own label block.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-mpls-label-management:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    The name of the dynamic label block
    """
    start_label: Annotated[
        int,
        Field(alias='srl_nokia-mpls-label-management:start-label', ge=16, le=1048575),
    ]
    """
    The starting label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    end_label: Annotated[
        int, Field(alias='srl_nokia-mpls-label-management:end-label', ge=16, le=1048575)
    ]
    """
    The ending label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    allocated_labels: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:allocated-labels',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    The number of labels that are currently used in this block
    """
    free_labels: Annotated[
        Optional[int],
        Field(alias='srl_nokia-mpls-label-management:free-labels', ge=0, le=4294967295),
    ] = None
    """
    The number of labels that are currently available and free in this block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    status: Annotated[
        Optional[EnumerationEnum45],
        Field(alias='srl_nokia-mpls-label-management:status'),
    ] = None
    """
    The status of the MPLS label block
    """
    user: Annotated[
        Optional[List[UserListEntry3]],
        Field(alias='srl_nokia-mpls-label-management:user'),
    ] = None


class EfmOamContainer(BaseModel):
    """
    Container for Ethernet in the First Mile OAM frames

    EFM-OAM frames are identified by a Ethertype value 0x8809 and slow protocol subtype 0x03.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming EFM-OAM tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled EFM-OAM frames. 
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming EFM-OAM frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu EFM-OAM frames.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the EFM-OAM counters were cleared.
    """


class ElmiContainer(BaseModel):
    """
    Container for Ethernet local management interface frames

    ELMI frames are identified by MAC DA 01-80-C2-00-00-07 and Ethertype 0x88ee.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming ELMI tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled ELMI frames.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming ELMI frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu ELMI frames.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the ELMI counters were cleared
    """


class EntryListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    sequence_id: Annotated[
        int, Field(alias='srl_nokia-mirroring:sequence-id', ge=0, le=65535)
    ]
    """
    A number to indicate the relative evaluation order of the different entries; lower numbered entries are evaluated before higher numbered entries
    """


class EnvironmentContainer(BaseModel):
    """
    Top-level container for global environment data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    alias: Annotated[
        Optional[List[AliasListEntry]], Field(alias='srl_nokia-system-cli:alias')
    ] = None
    basic_prompt: Annotated[
        Optional[str], Field(alias='srl_nokia-system-cli:basic-prompt')
    ] = '\\n--{{ {banner}{startup_config_state}{modified_flags}{short_yang_models}{mode_and_session} }}--[ {pwc} ]--\\n{short_redundancy}{hw_slot}:{aaa_user}@{host}# '
    """
    Change the prompt for 'basic' cli-engine type displayed before every input line

    The following list of keywords will be replaced automatically:
        aaa_session_id  The session id of the current AAA session.
        aaa_user        The user name from the current AAA session.
        banner          Shows server status banner if there is any (for example
                        [WARM BOOT])
        candidate_name  The current candidate name or empty string if not in
                        candidate mode.
        commit_confirmed
                        Shows [commit confirmed] if there is commit confirmed in
                        progress.
        commit_confirmed_with_remaining_time
                        Shows [commit confirmed] and the remaining time if there is
                        commit confirmed in progress.
        configuration_session_type
                        The current configuration session type (e.g. shared,
                        shared-exclusive or private or private-exclusive).
                        Will output empty string when no configuration session
                        has been established.
        domain          The domain name (as returned by domainname program, same as
                        sysctl kernel.domainname).
        fqdn            Returns FQDN (if the domain name is not defined or unknown,
                        then returns the host name).
        host            The host name.
        hw_slot         Slot letter of the CPM slot ('A' or 'B').
        jspath_pwc      The present working context, formatted as a jspath.
                        Example: .interface{.name=="mgmt0"}.subinterface{.index==0}
        last_executed_command_duration
                        Duration of the last executed command in seconds.
        last_executed_command_status
                        Status of the last executed command ('0' if successful, '1'
                        if the last command failed to parse or execute).
        mode            The current CLI mode (e.g. candidate, running, show, state
                        or tools).
        mode_and_session
                        The current CLI mode and configuration session type and
                        candidate name (e.g. candidate shared default, candidate
                        private-exclusive mycandidate, running, show, state or
                        tools).
        mode_and_session_type
                        The current CLI mode and configuration session type (e.g.
                        candidate shared, candidate shared-exclusive, running, show,
                        state or tools).
        modified        Same as {banner}{startup_config_state}{modified_flags}
        modified_flags  Shows + if the running configuration is different from the
                        saved configuration (unsaved changes).
                        Shows ! if the baseline is out of sync with the running
                        configuration.
                        Shows * if there are any changes in the candidate
                        configuration to commit or discard.
        modified_with_change_count
                        Same as {modified} but shows count of changed objects in
                        addition to '*' if there are any changes in the candidate
                        configuration.
        pwc             The present working context, formatted as a CLI command.
                        Example: interface mgmt0 subinterface 0
        pwd             The present working directory
                        Example: /home/admin
        redundancy      Active/standby CPM redundancy status ('standby ' or ' ').
        short_pwc       The nodes in the present working context, separated by '>'.
                        Note this does not include any key values.
                        Example: interface>subinterface
        short_redundancy
                        Short active/standby CPM redundancy status ('s' or '').
        short_yang_models
                        The currently used yang models ('' or 'oc ')
        startup_config_state
                        Shows [RESCUE], [FACTORY] or [FAILED] if the initial
                        configuration has issues or does not exist.
                        Is empty when the initial configuration exists and was
                        loaded/saved without problems.
                        [RESCUE] means that the initial (startup) configuration
                        failed to load or commit, but rescue configuration was
                        successfully loaded and committed.
                        [FACTORY] means that neither initial (startup) configuration
                        or rescue configuration exists and hard-coded factory
                        configuration was successfully loaded and committed.
                        [FAILED] means that no configuration was successfully loaded
                        and committed. The default candidate may contain initial
                        (startup) or rescue configuration content (it can be empty
                        if it is not possible to load them because they are
                        invalid).
        time_12         Current day of the week and local time (e.g. Fri 1:23PM).
        time_24         Same as {time_12} but using 24h format (e.g. Fri 13:23).
        user            The user name.
        vi_editing_mode
                        The current vi editing mode (if vi-editing-mode is enabled).
                        Shows one of INSERT, REPLACE, REPLACE_SINGLE, NAVIGATION
        xpath_pwc       The present working context, formatted as a xpath path.
                        Example: /interface[name=mgmt0]/subinterface[index=0]
    To enter a keyword, enclose it with '{' and '}', e.g. '{pwc}'.
    To create a multiline prompt, use '
    ' for newlines.
    To print a '{' or '}', use '{{' or '}}', respectively. e.g. '{{pwc}}'.
    In addition | can be used to separate left and right aligned part.
    Use || for literal '|'.
    """
    bottom_toolbar: Annotated[
        Optional[str], Field(alias='srl_nokia-system-cli:bottom-toolbar')
    ] = '{banner}{startup_config_state}{commit_confirmed_with_remaining_time}|{time_24}'
    """
    Change the text displayed in the bottom toolbar

    The following list of keywords will be replaced automatically:
        aaa_session_id  The session id of the current AAA session.
        aaa_user        The user name from the current AAA session.
        banner          Shows server status banner if there is any (for example
                        [WARM BOOT])
        candidate_name  The current candidate name or empty string if not in
                        candidate mode.
        commit_confirmed
                        Shows [commit confirmed] if there is commit confirmed in
                        progress.
        commit_confirmed_with_remaining_time
                        Shows [commit confirmed] and the remaining time if there is
                        commit confirmed in progress.
        configuration_session_type
                        The current configuration session type (e.g. shared,
                        shared-exclusive or private or private-exclusive).
                        Will output empty string when no configuration session
                        has been established.
        domain          The domain name (as returned by domainname program, same as
                        sysctl kernel.domainname).
        fqdn            Returns FQDN (if the domain name is not defined or unknown,
                        then returns the host name).
        host            The host name.
        hw_slot         Slot letter of the CPM slot ('A' or 'B').
        jspath_pwc      The present working context, formatted as a jspath.
                        Example: .interface{.name=="mgmt0"}.subinterface{.index==0}
        last_executed_command_duration
                        Duration of the last executed command in seconds.
        last_executed_command_status
                        Status of the last executed command ('0' if successful, '1'
                        if the last command failed to parse or execute).
        mode            The current CLI mode (e.g. candidate, running, show, state
                        or tools).
        mode_and_session
                        The current CLI mode and configuration session type and
                        candidate name (e.g. candidate shared default, candidate
                        private-exclusive mycandidate, running, show, state or
                        tools).
        mode_and_session_type
                        The current CLI mode and configuration session type (e.g.
                        candidate shared, candidate shared-exclusive, running, show,
                        state or tools).
        modified        Same as {banner}{startup_config_state}{modified_flags}
        modified_flags  Shows + if the running configuration is different from the
                        saved configuration (unsaved changes).
                        Shows ! if the baseline is out of sync with the running
                        configuration.
                        Shows * if there are any changes in the candidate
                        configuration to commit or discard.
        modified_with_change_count
                        Same as {modified} but shows count of changed objects in
                        addition to '*' if there are any changes in the candidate
                        configuration.
        pwc             The present working context, formatted as a CLI command.
                        Example: interface mgmt0 subinterface 0
        pwd             The present working directory
                        Example: /home/admin
        redundancy      Active/standby CPM redundancy status ('standby ' or ' ').
        short_pwc       The nodes in the present working context, separated by '>'.
                        Note this does not include any key values.
                        Example: interface>subinterface
        short_redundancy
                        Short active/standby CPM redundancy status ('s' or '').
        short_yang_models
                        The currently used yang models ('' or 'oc ')
        startup_config_state
                        Shows [RESCUE], [FACTORY] or [FAILED] if the initial
                        configuration has issues or does not exist.
                        Is empty when the initial configuration exists and was
                        loaded/saved without problems.
                        [RESCUE] means that the initial (startup) configuration
                        failed to load or commit, but rescue configuration was
                        successfully loaded and committed.
                        [FACTORY] means that neither initial (startup) configuration
                        or rescue configuration exists and hard-coded factory
                        configuration was successfully loaded and committed.
                        [FAILED] means that no configuration was successfully loaded
                        and committed. The default candidate may contain initial
                        (startup) or rescue configuration content (it can be empty
                        if it is not possible to load them because they are
                        invalid).
        time_12         Current day of the week and local time (e.g. Fri 1:23PM).
        time_24         Same as {time_12} but using 24h format (e.g. Fri 13:23).
        user            The user name.
        vi_editing_mode
                        The current vi editing mode (if vi-editing-mode is enabled).
                        Shows one of INSERT, REPLACE, REPLACE_SINGLE, NAVIGATION
        xpath_pwc       The present working context, formatted as a xpath path.
                        Example: /interface[name=mgmt0]/subinterface[index=0]
    To enter a keyword, enclose it with '{' and '}', e.g. '{pwc}'.
    To create a multiline prompt, use '
    ' for newlines.
    To print a '{' or '}', use '{{' or '}}', respectively. e.g. '{{pwc}}'.
    In addition | can be used to separate left and right aligned part.
    Use || for literal '|'.
    """
    cli_engine: Annotated[
        Optional[CliEngineContainer], Field(alias='srl_nokia-system-cli:cli-engine')
    ] = None
    complete_on_enter: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-cli:complete-on-enter')
    ] = False
    """
    Trigger auto-completion whenever you type an Enter

    Disabled by default.
    """
    complete_on_space: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-cli:complete-on-space')
    ] = False
    """
    Trigger auto-completion whenever you type a Space

    Disabled by default.
    """
    complete_on_tab: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-cli:complete-on-tab')
    ] = True
    """
    Trigger auto-completion whenever you type a Tab

    Enabled by default.
    """
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-cli:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ] = None
    """
    The default network-instance to be used if not specified
    """
    key_completer_limit: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-cli:key-completer-limit', ge=1, le=1000),
    ] = 100
    """
    The limit on number of keys shown in auto-completion
    """
    output_format: Annotated[
        Optional[EnumerationEnum40], Field(alias='srl_nokia-system-cli:output-format')
    ] = 'text'
    """
    The CLI output display format. Set to 'text' by default
    """
    output_modifier_alias: Annotated[
        Optional[List[OutputModifierAliasListEntry]],
        Field(alias='srl_nokia-system-cli:output-modifier-alias'),
    ] = None
    pagination: Annotated[
        Optional[EnumerationEnum41], Field(alias='srl_nokia-system-cli:pagination')
    ] = None
    """
    Pagination override of the CLI output, either 'on' or 'off'

    If turned on, then any CLI command behaves as if '| more' was entered at the
    end of the input command.
    Default value is unset (empty string). Unset value means there is no override.
    """
    prompt: Annotated[Optional[str], Field(alias='srl_nokia-system-cli:prompt')] = (
        '\\n--{{ {modified_flags}{short_yang_models}{mode_and_session} }}--[ {pwc} ]--\\n{short_redundancy}{hw_slot}:{aaa_user}@{host}# '
    )
    """
    Change the prompt for 'advanced' cli-engine type displayed before every input line

    The following list of keywords will be replaced automatically:
        aaa_session_id  The session id of the current AAA session.
        aaa_user        The user name from the current AAA session.
        banner          Shows server status banner if there is any (for example
                        [WARM BOOT])
        candidate_name  The current candidate name or empty string if not in
                        candidate mode.
        commit_confirmed
                        Shows [commit confirmed] if there is commit confirmed in
                        progress.
        commit_confirmed_with_remaining_time
                        Shows [commit confirmed] and the remaining time if there is
                        commit confirmed in progress.
        configuration_session_type
                        The current configuration session type (e.g. shared,
                        shared-exclusive or private or private-exclusive).
                        Will output empty string when no configuration session
                        has been established.
        domain          The domain name (as returned by domainname program, same as
                        sysctl kernel.domainname).
        fqdn            Returns FQDN (if the domain name is not defined or unknown,
                        then returns the host name).
        host            The host name.
        hw_slot         Slot letter of the CPM slot ('A' or 'B').
        jspath_pwc      The present working context, formatted as a jspath.
                        Example: .interface{.name=="mgmt0"}.subinterface{.index==0}
        last_executed_command_duration
                        Duration of the last executed command in seconds.
        last_executed_command_status
                        Status of the last executed command ('0' if successful, '1'
                        if the last command failed to parse or execute).
        mode            The current CLI mode (e.g. candidate, running, show, state
                        or tools).
        mode_and_session
                        The current CLI mode and configuration session type and
                        candidate name (e.g. candidate shared default, candidate
                        private-exclusive mycandidate, running, show, state or
                        tools).
        mode_and_session_type
                        The current CLI mode and configuration session type (e.g.
                        candidate shared, candidate shared-exclusive, running, show,
                        state or tools).
        modified        Same as {banner}{startup_config_state}{modified_flags}
        modified_flags  Shows + if the running configuration is different from the
                        saved configuration (unsaved changes).
                        Shows ! if the baseline is out of sync with the running
                        configuration.
                        Shows * if there are any changes in the candidate
                        configuration to commit or discard.
        modified_with_change_count
                        Same as {modified} but shows count of changed objects in
                        addition to '*' if there are any changes in the candidate
                        configuration.
        pwc             The present working context, formatted as a CLI command.
                        Example: interface mgmt0 subinterface 0
        pwd             The present working directory
                        Example: /home/admin
        redundancy      Active/standby CPM redundancy status ('standby ' or ' ').
        short_pwc       The nodes in the present working context, separated by '>'.
                        Note this does not include any key values.
                        Example: interface>subinterface
        short_redundancy
                        Short active/standby CPM redundancy status ('s' or '').
        short_yang_models
                        The currently used yang models ('' or 'oc ')
        startup_config_state
                        Shows [RESCUE], [FACTORY] or [FAILED] if the initial
                        configuration has issues or does not exist.
                        Is empty when the initial configuration exists and was
                        loaded/saved without problems.
                        [RESCUE] means that the initial (startup) configuration
                        failed to load or commit, but rescue configuration was
                        successfully loaded and committed.
                        [FACTORY] means that neither initial (startup) configuration
                        or rescue configuration exists and hard-coded factory
                        configuration was successfully loaded and committed.
                        [FAILED] means that no configuration was successfully loaded
                        and committed. The default candidate may contain initial
                        (startup) or rescue configuration content (it can be empty
                        if it is not possible to load them because they are
                        invalid).
        time_12         Current day of the week and local time (e.g. Fri 1:23PM).
        time_24         Same as {time_12} but using 24h format (e.g. Fri 13:23).
        user            The user name.
        vi_editing_mode
                        The current vi editing mode (if vi-editing-mode is enabled).
                        Shows one of INSERT, REPLACE, REPLACE_SINGLE, NAVIGATION
        xpath_pwc       The present working context, formatted as a xpath path.
                        Example: /interface[name=mgmt0]/subinterface[index=0]
    To enter a keyword, enclose it with '{' and '}', e.g. '{pwc}'.
    To create a multiline prompt, use '
    ' for newlines.
    To print a '{' or '}', use '{{' or '}}', respectively. e.g. '{{pwc}}'.
    In addition | can be used to separate left and right aligned part.
    Use || for literal '|'.
    """
    session_idle_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-cli:session-idle-timeout', ge=0, le=86400),
    ] = None
    """
    The idle timeout override for the CLI session in seconds

    Can be used to override the value of the idle timer value received from AAA session.
    Value of 0 means idle timeout is disabled.
    Unset value means there is no override.
    """
    yang_models: Annotated[
        Optional[EnumerationEnum42], Field(alias='srl_nokia-system-cli:yang-models')
    ] = 'srl'
    """
    The default yang-models to be used when starting the CLI

    Default is 'srl'.
    """


class EsmcContainer(BaseModel):
    """
    Container for Ethernet Synchronization Messaging Channel protocol

    ESMC frames are identified by a Ethertype 0x8809 and slow protocol subtype 0x0A.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming ESMC tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled ESMC frames. 
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming ESMC frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu ESMC frames.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the ESMC counters were cleared
    """


class EvpnContainer2(BaseModel):
    """
    Container for system wide Services EVPN MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dynamic_label_block: Annotated[
        str,
        Field(
            alias='srl_nokia-mpls-services-evpn-label-management:dynamic-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    The dynamic label block used by EVPN in the system network-instance

    The label block is used by all EVPN services that require MPLS labels in the
    system network-instance. For example, EVPN-MPLS multi-homing (ESI label).
    """


class ExportingProcessLeafList(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$'
        ),
    ]
    """
    Records are exported by all Exporting Processes
    in the list.
    """


class FhsClassidMgmtContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    first_hop_security: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:first-hop-security'),
    ] = 'disable'
    """
    Controls the first hop security feature.
    """
    ra_guard: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:ra-guard'),
    ] = 'enable'
    """
    Controls the ra-guard security feature.
    """
    first_hop_security_ip_source_guard_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:first-hop-security-ip-source-guard-entries',
            ge=0,
            le=1280,
        ),
    ] = 0
    """
    Number of hardware TCAM entries to use for First Hop Security (FHS) IP Source Guard

    The number of hardware TCAM entries to allocate when First Hop Security
    IP source guard is enabled on a subinterface. This number must be set to be
    equal to or more than the number of IP-MAC association entries in the
    First Hop security ip-mac-binding-table. Software will allocate the required
    number of hardware TCAM entries.
    """


class FirstHopSecurityPolicyListEntry(BaseModel):
    """
    List of First Hop Security policies
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    First Hop Security (FHS) policy name
    """
    protocols: Annotated[
        Optional[List[EnumerationEnum76]],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:protocols'),
    ] = ['static', 'dhcp', 'dhcp-pd', 'nd']
    """
    List of protocols to build IP-MAC association

    List of protocols used to build IP-MAC association and can be
     configured by the user. User can specify one or more values.
    """
    limit_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:limit-entries',
            ge=0,
            le=8192,
        ),
    ] = None
    """
    Maximum number of IP-MAC association entries to learn

    Maximum number of IP-MAC association allowed to be associated with an
      entity (e.g. sub-interface, etc.)  where this policy is attached.
    """
    device_role: Annotated[
        Optional[EnumerationEnum77],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:device-role'),
    ] = 'switch'


class GnmiContainer2(BaseModel):
    """
    Container for gNMI related session info
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    paths: Annotated[
        Optional[List[PathsListEntry]], Field(alias='srl_nokia-grpc:paths')
    ] = None


class GribiContainer(BaseModel):
    """
    Container for gRIBI related session info
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    persistence_mode: Annotated[
        Optional[EnumerationEnum17], Field(alias='srl_nokia-grpc:persistence-mode')
    ] = None
    """
    The defined persistence mode as signaled by the client
    """


class HostCertificateContainer(BaseModel):
    """
    State relating to the Host Certificates provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-credentialz:version')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class HostKeyContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        Optional[List[TypeListEntry]], Field(alias='srl_nokia-ssh:type')
    ] = None
    preserve: Annotated[Optional[bool], Field(alias='srl_nokia-ssh:preserve')] = True
    """
    Indicates whether the autogenerated SSH server host keys should be preserved on reboots

    Setting this to true will result in host keys in /etc/sshd not being cleared on a reboot. Alternatively
    setting this to false will result in host keys being removed and regenerated on each reboot of the system.

    This is useful only when the host keys are not statically configured and not dynamically configured using
    gNSI Credentialz service (and therefore are suitable to be potentially regenerated on every reboot).

    Takes effect only if the value is set to false for every configured ssh server instance.
    """


class HostKeyContainer2(BaseModel):
    """
    State relating to the Host Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-credentialz:version')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class InformationContainer(BaseModel):
    """
    Top-level container for system information configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    contact: Annotated[Optional[str], Field(alias='srl_nokia-system-info:contact')] = (
        None
    )
    """
    The system contact

    This field represents contact information for the person or group that maintains the system. This field is exposed via SNMP at the sysContact OID.
    """
    location: Annotated[
        Optional[str], Field(alias='srl_nokia-system-info:location')
    ] = None
    """
    The system location

    This field represents the location of the system, and is commonly used by inventory management systems to group elements together. This field is exposed via SNMP at the sysLocation OID.
    """
    description: Annotated[
        Optional[str], Field(alias='srl_nokia-system-info:description')
    ] = None
    """
    The system description

    This field is system generated, and is a combination of the system host name, software version, kernel version, and build date. The template for this field is: SRLinux-<version> <hostname> <kernel> <build date>. This field is exposed via SNMP at the sysDescr OID.
    """
    current_datetime: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-info:current-datetime',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The current system date and time
    """
    last_booted: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-info:last-booted',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time the system was last booted
    """
    version: Annotated[Optional[str], Field(alias='srl_nokia-system-info:version')] = (
        None
    )
    """
    The system version

    This field represents the version of the management server
    """
    coordinates: Annotated[
        Optional[CoordinatesContainer],
        Field(alias='srl_nokia-system-coordinates:coordinates'),
    ] = None


class InterfaceContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    auto_negotiation_support: Annotated[
        Optional[EnumerationEnum91],
        Field(alias='srl_nokia-lldp:auto-negotiation-support'),
    ] = None
    """
    Support of auto-negotiation
    """
    auto_negotiation_enabled: Annotated[
        Optional[EnumerationEnum92],
        Field(alias='srl_nokia-lldp:auto-negotiation-enabled'),
    ] = None
    """
    Enable state of auto-negotiation
    """
    auto_negotiation_capabilities: Annotated[
        Optional[List[EnumerationEnum93]],
        Field(alias='srl_nokia-lldp:auto-negotiation-capabilities'),
    ] = []
    """
    List of auto-negotiation capabilities advertised
    """


class InterfaceListEntry(BaseModel):
    """
    List of interfaces used as mirror source
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-mirroring:name')]
    """
    Reference type to a specific subinterface of the form <interface-name>
    """
    direction: Annotated[
        Optional[EnumerationEnum30], Field(alias='srl_nokia-mirroring:direction')
    ] = 'egress-only'
    """
    The direction of traffic to be mirrored
    """


class InterfaceListEntry2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ethernet_interface: Annotated[
        str,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-interface'
        ),
    ]
    """
    Interface associated with the ethernet segment.
    """


class InterfaceListEntry5(BaseModel):
    """
    List of interfaces associated with the observation-point
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-ipfix:name')]
    """
     Subinterface to associate with Observation-point and perform sampling
    """
    direction: Annotated[
        Optional[EnumerationEnum103], Field(alias='srl_nokia-ipfix:direction')
    ] = 'input'
    """
    The direction of traffic to be sampled
    """
    ifindex: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:ifindex', ge=0, le=4294967295)
    ] = None
    """
    System-wide persistent unique ifIndex assigned to the subinterface
    """


class InternalTagsContainer(BaseModel):
    """
    Configuration and state of internal tags
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    set_tag_set: Annotated[
        Optional[List[SetTagSetLeafList]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:set-tag-set'
        ),
    ] = []
    """
    Reference to a tag-set defined under routing-policy
    """


class Ipv4AddressUnicastType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    A unicast IPv4 address in dotted quad notation
    """


class Ipv6AddressUnicastType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$'
        ),
    ]
    """
    A unicast IPv6 address represented as either a full address, shortened or mixed-shortened formats
    """


class IsisContainer(BaseModel):
    """
    Container for specifying the ISIS members of the maintenance group
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instances: Annotated[
        Optional[List[NetworkInstancesLeafList]],
        Field(alias='srl_nokia-maintenance-mode:network-instances'),
    ] = []
    """
    List of network instances that should be part of the maintenance group.
    """


class IsisContainer2(BaseModel):
    """
    Container for ISIS configurations.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    overload: Annotated[
        Optional[OverloadContainer], Field(alias='srl_nokia-maintenance-mode:overload')
    ] = None


class LabelContainer(BaseModel):
    """
    The encoded label value and type in the EVPN NLRI
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    value: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:value',
            ge=0,
            le=16777215,
        ),
    ] = None
    """
    The value of the label field

    If the route is an EVPN MPLS route, the mpls-label is read out of the 20-bit high order value.
    If the route is an EVPN VXLAN route, the vni is read out of the 24-bit value. If the route is
    an EVPN SRv6 route, this field is set to zero if no transposition is used and set to a non-zero
    value if transposition is used. For all the cases, if this is an Auto-Discovery per ES route,
    this leaf is set to zero.
    """
    value_type: Annotated[
        Optional[EnumerationEnum65],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:value-type'
        ),
    ] = None
    """
    Whether the encoded label value is an mpls-label, a vni or a transposed function or argument
    """


class LacpContainer2(BaseModel):
    """
    Container for LACP.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Link Aggregation Control Protocol tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled LACP frames. LACP
    frames are identified by a destination MAC value of 01:80:c2:00:00:02, EtherType value
    of 0x8809 and slow protocol subtype 0x1.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming Link Aggregation Control Protocol frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu LACP frames. LACP
    frames are identified by a destination MAC value of 01:80:c2:00:00:02, EtherType value
    of 0x8809 and slow protocol subtype 0x1.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the LACP counters were cleared.
    """


class LastErroredExecutionContainer(BaseModel):
    """
    Operational state of the last errored execution of this instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    oper_down_reason: Annotated[
        Optional[EnumerationEnum100],
        Field(alias='srl_nokia-event-handler:oper-down-reason'),
    ] = None
    """
    Reason this instance is or was in its last operational state
    """
    oper_down_reason_detail: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:oper-down-reason-detail')
    ] = None
    """
    Any additional detail event handler can provide around the last operational state of this instance
    """
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time this instance last started execution
    """
    end_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:end-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time this instance last finished execution

    This timestamp includes any actions provided as output from the execution
    """
    upython_duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:upython-duration',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    Time taken for the instance to return output
    """
    input: Annotated[Optional[str], Field(alias='srl_nokia-event-handler:input')] = None
    """
    Input provided to the script
    """
    output: Annotated[Optional[str], Field(alias='srl_nokia-event-handler:output')] = (
        None
    )
    """
    Output received from the script

    If empty, no response was received.
    """
    stdout_stderr: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:stdout-stderr')
    ] = None
    """
    Output printed on STDOUT or STDERR during this execution
    """


class LastExecutionContainer(BaseModel):
    """
    Operational state of the last execution of this instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    oper_down_reason: Annotated[
        Optional[EnumerationEnum100],
        Field(alias='srl_nokia-event-handler:oper-down-reason'),
    ] = None
    """
    Reason this instance is or was in its last operational state
    """
    oper_down_reason_detail: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:oper-down-reason-detail')
    ] = None
    """
    Any additional detail event handler can provide around the last operational state of this instance
    """
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time this instance last started execution
    """
    end_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:end-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time this instance last finished execution

    This timestamp includes any actions provided as output from the execution
    """
    upython_duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:upython-duration',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    Time taken for the instance to return output
    """
    input: Annotated[Optional[str], Field(alias='srl_nokia-event-handler:input')] = None
    """
    Input provided to the script
    """
    output: Annotated[Optional[str], Field(alias='srl_nokia-event-handler:output')] = (
        None
    )
    """
    Output received from the script

    If empty, no response was received.
    """
    stdout_stderr: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:stdout-stderr')
    ] = None
    """
    Output printed on STDOUT or STDERR during this execution
    """


class Layer2InterfaceCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[List[InterfaceListEntry2]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:interface'
        ),
    ] = None


class LicenseListEntry(BaseModel):
    """
    List of licenses configured on the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        str,
        Field(
            alias='srl_nokia-license:id',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Unique identifier for this license
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-license:admin-state')
    ] = 'disable'
    """
    Enable or disable the use of this license
    """
    preferred: Annotated[Optional[bool], Field(alias='srl_nokia-license:preferred')] = (
        False
    )
    """
    Set a license as being preferred

    Amongst all valid licenses, the preferred license will be chosen to become active. If no license is set as preferred or the preferred license is not valid, the valid license with the most distant expiry is chosen to become active.

    Only a single license can be set as preferred.
    """
    data: Annotated[Optional[str], Field(alias='srl_nokia-license:data')] = None
    """
    Content of the license

    This content includes a preceding UUID, followed by a space and the license data.

    For example:
    00000000-0000-0000-0000-000000000000 aACUAx...rYzNRPT0AAAAA
    """
    description: Annotated[
        Optional[str],
        Field(alias='srl_nokia-license:description', max_length=255, min_length=1),
    ] = None
    """
    A user provided description for the license
    """
    issued_date: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-license:issued-date',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time the license was issued
    """
    expiration_date: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-license:expiration-date',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time the license will expire
    """
    expired: Annotated[Optional[bool], Field(alias='srl_nokia-license:expired')] = None
    """
    Indicates if the license has expired
    """
    valid: Annotated[Optional[bool], Field(alias='srl_nokia-license:valid')] = None
    """
    Indicates if the license is valid for use
    """
    in_use: Annotated[Optional[bool], Field(alias='srl_nokia-license:in-use')] = None
    """
    Indicates if the license is actively in use
    """


class LockoutContainer(BaseModel):
    """
    Information relating to the lockout state of this user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active: Annotated[Optional[bool], Field(alias='srl_nokia-aaa:active')] = None
    """
    Indicates if a lockout is active for the user

    Lockouts can occur after successive failed logins, and can be cleared by 'tools system aaa authentication user <username> unlock'
    """
    start: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:start',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user started
    """
    end: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:end',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user ended or will end
    """


class LockoutContainer2(BaseModel):
    """
    Information relating to the lockout state of this user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active: Annotated[Optional[bool], Field(alias='srl_nokia-aaa:active')] = None
    """
    Indicates if a lockout is active for the user

    Lockouts can occur after successive failed logins, and can be cleared by 'tools system aaa authentication user <username> unlock'
    """
    start: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:start',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user started
    """
    end: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:end',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user ended or will end
    """


class MacTypeListEntry(BaseModel):
    """
    the type of the mac in the system.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        EnumerationEnum18, Field(alias='srl_nokia-system-bridge-table:type')
    ]
    """
    type of mac addresses in the system
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of macs of this type on the system.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:total-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of macs of this type , active and inactive, on the system.
    """
    failed_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:failed-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of macs of this type, which have not been programmed on atleast one slot
    """


class MacsecContainer(BaseModel):
    """
    Container to configure macsec CAK and CAK Name.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    cak: Annotated[
        str, Field(alias='srl_nokia-keychains:cak', pattern='^(?=^[0-9a-fA-F]+$).*$')
    ]
    """
    MACsec CAK, a hexadecimal name is only valid
    """
    key_name: Annotated[
        str,
        Field(
            alias='srl_nokia-keychains:key-name',
            pattern='^(?=^([0-9a-fA-F][0-9a-fA-F])+$).*$',
        ),
    ]
    """
    MACsec CKN, a hexadecimal name is only valid
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-keychains:admin-state')
    ] = 'disable'
    """
    When set to disable, this key entry is inactive

    For macsec the cak and key-name can only be changed when the key entry id disabled
    """


class MaintenanceModeContainer(BaseModel):
    """
    Container with options for activating and deactivating maintenance mode for this group
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-maintenance-mode:admin-state'),
    ] = 'disable'
    """
    Enable or disable maintenance mode for this group

    The enable setting is blocked if there is another maintenance group with at least one BGP session in its scope that overlaps with this maintenance group and that other maintenance group is currently in maintenance mode.

    While a maintenance group is in maintenance mode it is not possible to modify the BGP configuration of its members.
    """


class ManagementAddressListEntry(BaseModel):
    """
    List of subinterfaces to source management addresses from

    This list is sent in the management address TLV by LLDP.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subinterface: Annotated[str, Field(alias='srl_nokia-lldp:subinterface')]
    """
    Reference to the subinterface to source management addresses
    """
    type: Annotated[
        Optional[List[EnumerationEnum88]], Field(alias='srl_nokia-lldp:type')
    ] = []
    """
    Types of addresses sent in the management address TLV

    The enumerated value for the network address type
    identified in this TLV. This enumeration is defined in the
    'Assigned Numbers' RFC [RFC3232] and the
    ianaAddressFamilyNumbers object.
    """


class ManagementAddressListEntry2(BaseModel):
    """
    List of management addresses received from the remote LLDP neighbor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    address: Annotated[str, Field(alias='srl_nokia-lldp:address')]
    """
    The management address received from the remote LLDP neighbor

    The Management Address is a mandatory TLV which identifies a
    network address associated with the LLDP agent, which
    can be used to reach the agent on the port identified in the
    Port ID TLV.
    """
    type: Annotated[Optional[EnumerationEnum88], Field(alias='srl_nokia-lldp:type')] = (
        None
    )
    """
    The type of management address referenced in the address field

    The enumerated value for the network address type
    identified in this TLV. This enumeration is defined in the
    'Assigned Numbers' RFC [RFC3232] and the
    ianaAddressFamilyNumbers object.
    """


class ManualAlgContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    primary_evi_range: Annotated[
        Optional[List[PrimaryEviRangeListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:primary-evi-range'
        ),
    ] = None


class MulticastIdUserTypeListEntry(BaseModel):
    """
    the type of the user of multicast id in the system.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    user: Annotated[EnumerationEnum43, Field(alias='srl_nokia-system-multicast:user')]
    """
    type of multicast ids users in the system
    """
    current_usage: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:current-usage',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of multicast ids that are in use on the system.
    """
    total_pending: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:total-pending',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of multicast ids pending allocation on the system.
    """


class NdkServerContainer(BaseModel):
    """
    Top-level container for configuration and state related to NDK server instance.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-ndk:admin-state')
    ] = 'disable'
    """
    Globally enable or disable the NDK server

    Disabling the NDK server will disable its unix domain and tcp/ip sockets.
    """


class NeighborOriginListEntry(BaseModel):
    """
    the origin of the proxy ARP installed in the table.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    origin: Annotated[
        EnumerationEnum19, Field(alias='srl_nokia-system-bridge-table-proxy-arp:origin')
    ]
    """
    The origin of the neighbor entry.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of proxy ARP entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of active proxy ARP entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of inactive proxy ARP entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of pending proxy ARP entries.
    """


class NeighborOriginListEntry2(BaseModel):
    """
    the origin of the proxy ARP installed in the table.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    origin: Annotated[
        EnumerationEnum19, Field(alias='srl_nokia-system-bridge-table-proxy-arp:origin')
    ]
    """
    The origin of the neighbor entry.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of proxy ARP entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of active proxy ARP entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of inactive proxy ARP entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of pending proxy ARP entries.
    """


class NeighborContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_identity: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:clock-identity', max_length=8, min_length=8),
    ] = None
    """
    The clockIdentity of this neighbor clock
    """
    port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:port-number', ge=0, le=65535)
    ] = None
    """
    The port number of this neighbor clock
    """


class NeighborContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_identity: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:clock-identity', max_length=8, min_length=8),
    ] = None
    """
    The clockIdentity of this neighbor clock
    """
    port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:port-number', ge=0, le=65535)
    ] = None
    """
    The port number of this neighbor clock
    """


class NetworkInstanceContainer(BaseModel):
    """
    Container for system wide Service Network Instance MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dynamic_label_block: Annotated[
        str,
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:dynamic-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Reference to the dynamic label block used by network-instances

    The label block is used by all the applications that require MPLS label allocation
    in a network-instance. For example, EVPN-MPLS services, IP-VPN or Pseudowires.
    """
    dynamic_evpn_inclusive_multicast_label_block: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:dynamic-evpn-inclusive-multicast-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to the dynamic evpn inclusive multicast label block used by EVPN MAC-VRFs

    The label block is used by EVPN-MPLS MAC-VRF services for the allocation of labels
    that are advertised in EVPN Inclusive Multicast Ethernet Tag routes and that identify
    incoming layer-2 Broadcast, Unknown unicast and Multicast traffic.
    """
    static_label_block: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:static-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to the static label block used by network-instances

    The label block is used by all the applications that require static MPLS label allocation
    in a network-instance. For example, Pseudowires with static vc labels.
    """


class NetworkInstanceListEntry3(BaseModel):
    """
    List of network instances with one or more peers to be placed in maintenance mode
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-maintenance-mode:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    A unique name identifying the network instance
    """
    peer_group: Annotated[
        Optional[List[PeerGroupLeafList]],
        Field(alias='srl_nokia-maintenance-mode:peer-group'),
    ] = []
    """
    List of BGP peer groups that belong to the network instance and that should be part of the maintenance group

    If this list is empty and so is the neighbor list, then the system interprets the meaning as ALL static and dynamic sessions belonging to the specified network-instance.
    """
    neighbor: Annotated[
        Optional[List[Union[Ipv4AddressWithZoneType, Ipv6AddressWithZoneType]]],
        Field(alias='srl_nokia-maintenance-mode:neighbor'),
    ] = []
    """
    List of BGP neighbors that belong to the network instance and that should be part of the maintenance group

    It is not necessary to list neighbors that are members of peer-groups that are already listed.

    If this list is empty and so is the group list, then the system interprets the meaning as ALL static and dynamic sessions belonging to the specified network-instance.
    """


class NetworkPolicyApplicationTypeListEntry(BaseModel):
    """
    List name
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-lldp:name')]
    """
    Application name in received network policy TLV
    """
    policy_flag: Annotated[
        Optional[EnumerationEnum96], Field(alias='srl_nokia-lldp:policy-flag')
    ] = None
    """
    State of the network policy received from the endpoint
    """
    vlan_tagging: Annotated[
        Optional[bool], Field(alias='srl_nokia-lldp:vlan-tagging')
    ] = None
    """
    VLAN tagging for the specified application
    """
    vlan_id: Annotated[
        Optional[int], Field(alias='srl_nokia-lldp:vlan-id', ge=0, le=4094)
    ] = None
    """
    VLAN ID used for tagged applications, conditional leaf
    """
    dot1p: Annotated[Optional[int], Field(alias='srl_nokia-lldp:dot1p', ge=0, le=7)] = 0
    """
    L2 QoS dot1p priority
    """
    dscp: Annotated[
        Optional[Union[DscpValueType, EnumerationEnum90]],
        Field(alias='srl_nokia-lldp:dscp'),
    ] = 'CS0'
    """
    L3 QoS DSCP value
    """


class NetworkPolicyListEntry(BaseModel):
    """
    Network policy distribution of configuration attributes based on application type
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-lldp:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    List name
    """
    application_type: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:application-type')
    ] = None
    """
    Application type for network policy
    """
    vlan_id: Annotated[
        Optional[Union[VlanIdLeaf1, EnumerationEnum89]],
        Field(alias='srl_nokia-lldp:vlan-id'),
    ] = 'untagged'
    """
    VLAN tagging requirements for the application type, VLAN-ID (range 0..4094) or untagged
    """
    dot1p: Annotated[Optional[int], Field(alias='srl_nokia-lldp:dot1p', ge=0, le=7)] = 0
    """
    L2 QoS dot1p priority
    """
    dscp: Annotated[
        Optional[Union[DscpValueType, EnumerationEnum90]],
        Field(alias='srl_nokia-lldp:dscp'),
    ] = 'CS0'
    """
    L3 QoS DSCP value
    """


class NextHopListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    l3_next_hop: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:l3-next-hop'
        ),
    ]
    """
    Layer-3 next-hop associated with the ethernet segment.
    """
    evi: Annotated[
        Optional[List[EviListEntry]],
        Field(alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:evi'),
    ] = None


class NtpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_time: Annotated[
        str,
        Field(
            alias='srl_nokia-packet-link-qual:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ]
    """
    Start time of the test
    """
    end_time: Annotated[
        str,
        Field(
            alias='srl_nokia-packet-link-qual:end-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ]
    """
    End time of the test
    """
    teardown_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-packet-link-qual:teardown-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time at which the test should be torn down
    """


class ObjectListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-event-handler:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Name of this object
    """
    object: Annotated[
        Optional[Union[ValuesCase, ValueCase]],
        Field(alias='srl_nokia-event-handler:object'),
    ] = None


class ObservationPointListEntry(BaseModel):
    """
    Observation Point of the Monitoring Device.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Key of this list.
    """
    observation_domain_id: Annotated[
        int, Field(alias='srl_nokia-ipfix:observation-domain-id', ge=0, le=4294967295)
    ]
    """
    The Observation Domain ID associates the Observation Point to an Observation Domain.

    Observation Points with identical Observation Domain IDs belong to the
    same Observation Domain.
    Note that this parameter corresponds to
    ipfixObservationPointObservationDomainId in the IPFIX MIB
    module.
    """
    interface: Annotated[
        Optional[List[InterfaceListEntry5]], Field(alias='srl_nokia-ipfix:interface')
    ] = None
    selection_process: Annotated[
        Optional[List[SelectionProcessLeafList]],
        Field(alias='srl_nokia-ipfix:selection-process'),
    ] = []
    """
    Selection Processes in this list process
    packets in parallel.
    """


class OnePpsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-sync:admin-state')
    ] = 'disable'
    """
    Configure the administrative state of the 1PPS (50 ohm) output port

    When enabled, output is enabled. Otherwise, the output is disabled.
    """


class OptionsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bootfile_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:bootfile-name', max_length=128, min_length=1
        ),
    ] = None
    """
    The name of the configuration file the client will use during booting - option 67
    """
    dns_server: Annotated[
        Optional[List[DnsServerLeafList]],
        Field(alias='srl_nokia-dhcp-server:dns-server'),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """
    domain_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:domain-name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
        ),
    ] = None
    """
    The domain name to return to the dhcp client that the client should use when resolving hostnames via the Domain Name System - option 15
    """
    domain_search_list: Annotated[
        Optional[List[DomainSearchListLeafList]],
        Field(alias='srl_nokia-dhcp-server:domain-search-list'),
    ] = []
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames - option 119
    """
    hostname: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:hostname',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
        ),
    ] = None
    """
    Host Name option of the dhcp client - option 12
    """
    interface_mtu: Annotated[
        Optional[int],
        Field(alias='srl_nokia-dhcp-server:interface-mtu', ge=68, le=9412),
    ] = None
    """
    This option specifies the MTU to use on this interface - option 26
    """
    ntp_server: Annotated[
        Optional[List[NtpServerLeafList]],
        Field(alias='srl_nokia-dhcp-server:ntp-server'),
    ] = []
    """
    List of NTP Servers to return to the dhcp client - option 42
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IPv4 address of the gateway for the dhcp client - option 3
    """
    server_id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:server-id',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IP address the dhcp server must match any address within the network_instance e.g. sub-interface primary address, loopback address,
    anycast gateway address in case of multihoming - option 54
    """
    static_route: Annotated[
        Optional[List[StaticRouteListEntry]],
        Field(alias='srl_nokia-dhcp-server:static-route'),
    ] = None
    tftp_server_address: Annotated[
        Optional[List[TftpServerAddressLeafList]],
        Field(alias='srl_nokia-dhcp-server:tftp-server-address'),
    ] = []
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """
    tftp_server_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:tftp-server-name',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
        ),
    ] = None
    """
    FQDN of the TFTP server the client will use to download bootfile/configuration script - option 66
    """
    lease_time: Annotated[
        Optional[int],
        Field(alias='srl_nokia-dhcp-server:lease-time', ge=60, le=4294967295),
    ] = 86400
    """
    The time in seconds that the client should use the IP address before it must renew its lease - option 51
    """
    next_server: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:next-server',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    The IP address of the next server to use for booting - option 54
    """
    custom: Annotated[
        Optional[List[CustomListEntry]], Field(alias='srl_nokia-dhcp-server:custom')
    ] = None


class OptionsContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bootfile_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:bootfile-name', max_length=128, min_length=1
        ),
    ] = None
    """
    The name of the configuration file the client will use during booting - option 67
    """
    dns_server: Annotated[
        Optional[List[DnsServerLeafList2]],
        Field(alias='srl_nokia-dhcp-server:dns-server'),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """
    domain_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:domain-name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
        ),
    ] = None
    """
    The domain name to return to the dhcp client that the client should use when resolving hostnames via the Domain Name System - option 15
    """
    domain_search_list: Annotated[
        Optional[List[DomainSearchListLeafList2]],
        Field(alias='srl_nokia-dhcp-server:domain-search-list'),
    ] = []
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames - option 119
    """
    hostname: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:hostname',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
        ),
    ] = None
    """
    Host Name option of the dhcp client - option 12
    """
    interface_mtu: Annotated[
        Optional[int],
        Field(alias='srl_nokia-dhcp-server:interface-mtu', ge=68, le=9412),
    ] = None
    """
    This option specifies the MTU to use on this interface - option 26
    """
    ntp_server: Annotated[
        Optional[List[NtpServerLeafList2]],
        Field(alias='srl_nokia-dhcp-server:ntp-server'),
    ] = []
    """
    List of NTP Servers to return to the dhcp client - option 42
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IPv4 address of the gateway for the dhcp client - option 3
    """
    server_id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:server-id',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IP address the dhcp server must match any address within the network_instance e.g. sub-interface primary address, loopback address,
    anycast gateway address in case of multihoming - option 54
    """
    static_route: Annotated[
        Optional[List[StaticRouteListEntry2]],
        Field(alias='srl_nokia-dhcp-server:static-route'),
    ] = None
    tftp_server_address: Annotated[
        Optional[List[TftpServerAddressLeafList2]],
        Field(alias='srl_nokia-dhcp-server:tftp-server-address'),
    ] = []
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """
    tftp_server_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:tftp-server-name',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
        ),
    ] = None
    """
    FQDN of the TFTP server the client will use to download bootfile/configuration script - option 66
    """
    lease_time: Annotated[
        Optional[int],
        Field(alias='srl_nokia-dhcp-server:lease-time', ge=60, le=4294967295),
    ] = 86400
    """
    The time in seconds that the client should use the IP address before it must renew its lease - option 51
    """
    next_server: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:next-server',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    The IP address of the next server to use for booting - option 54
    """
    custom: Annotated[
        Optional[List[CustomListEntry2]], Field(alias='srl_nokia-dhcp-server:custom')
    ] = None


class OptionsContainer3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bootfile_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:bootfile-name', max_length=128, min_length=1
        ),
    ] = None
    """
    The name of the configuration file the client will use during booting - option 67
    """
    dns_server: Annotated[
        Optional[List[DnsServerLeafList3]],
        Field(alias='srl_nokia-dhcp-server:dns-server'),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """
    domain_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:domain-name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
        ),
    ] = None
    """
    The domain name to return to the dhcp client that the client should use when resolving hostnames via the Domain Name System - option 15
    """
    domain_search_list: Annotated[
        Optional[List[DomainSearchListLeafList3]],
        Field(alias='srl_nokia-dhcp-server:domain-search-list'),
    ] = []
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames - option 119
    """
    hostname: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:hostname',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
        ),
    ] = None
    """
    Host Name option of the dhcp client - option 12
    """
    interface_mtu: Annotated[
        Optional[int],
        Field(alias='srl_nokia-dhcp-server:interface-mtu', ge=68, le=9412),
    ] = None
    """
    This option specifies the MTU to use on this interface - option 26
    """
    ntp_server: Annotated[
        Optional[List[NtpServerLeafList3]],
        Field(alias='srl_nokia-dhcp-server:ntp-server'),
    ] = []
    """
    List of NTP Servers to return to the dhcp client - option 42
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IPv4 address of the gateway for the dhcp client - option 3
    """
    server_id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:server-id',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    IP address the dhcp server must match any address within the network_instance e.g. sub-interface primary address, loopback address,
    anycast gateway address in case of multihoming - option 54
    """
    static_route: Annotated[
        Optional[List[StaticRouteListEntry3]],
        Field(alias='srl_nokia-dhcp-server:static-route'),
    ] = None
    tftp_server_address: Annotated[
        Optional[List[TftpServerAddressLeafList3]],
        Field(alias='srl_nokia-dhcp-server:tftp-server-address'),
    ] = []
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """
    tftp_server_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:tftp-server-name',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
        ),
    ] = None
    """
    FQDN of the TFTP server the client will use to download bootfile/configuration script - option 66
    """
    lease_time: Annotated[
        Optional[int],
        Field(alias='srl_nokia-dhcp-server:lease-time', ge=60, le=4294967295),
    ] = 86400
    """
    The time in seconds that the client should use the IP address before it must renew its lease - option 51
    """
    next_server: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:next-server',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    The IP address of the next server to use for booting - option 54
    """
    custom: Annotated[
        Optional[List[CustomListEntry3]], Field(alias='srl_nokia-dhcp-server:custom')
    ] = None


class OptionsContainer4(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dns_server: Annotated[
        Optional[List[DnsServerLeafList4]],
        Field(alias='srl_nokia-dhcp-server:dns-server'),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client
    """
    domain_search_list: Annotated[
        Optional[List[DomainSearchListLeafList4]],
        Field(alias='srl_nokia-dhcp-server:domain-search-list'),
    ] = []
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames
    """


class OptionsContainer5(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dns_server: Annotated[
        Optional[List[DnsServerLeafList5]],
        Field(alias='srl_nokia-dhcp-server:dns-server'),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client
    """
    domain_search_list: Annotated[
        Optional[List[DomainSearchListLeafList5]],
        Field(alias='srl_nokia-dhcp-server:domain-search-list'),
    ] = []
    """
    An ordered list of domains to return to the dhcp client that the client should search when resolving hostnames
    """


class OptionsContainer6(BaseModel):
    """
    Options to be passed on each execution of the script
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    object: Annotated[
        Optional[List[ObjectListEntry]], Field(alias='srl_nokia-event-handler:object')
    ] = None


class PacketGeneratorCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    packet_generator: Annotated[
        Optional[PacketGeneratorContainer],
        Field(alias='srl_nokia-packet-link-qual:packet-generator'),
    ] = None


class PasswordContainer(BaseModel):
    """
    State relating to the Password provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class PasswordContainer2(BaseModel):
    """
    State relating to the Password provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class PasswordContainer3(BaseModel):
    """
    State relating to the Password provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class PathListEntry(BaseModel):
    """
    A collection of counters collected by the gNSI.pathz module for a schema path identified by the `name`.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-gnsi-pathz:name')]
    """
    A schema path the counters were collected for.

    Uses xpath format.
    """
    reads: Annotated[
        Optional[ReadsContainer], Field(alias='srl_nokia-gnsi-pathz:reads')
    ] = None
    writes: Annotated[
        Optional[WritesContainer], Field(alias='srl_nokia-gnsi-pathz:writes')
    ] = None


class PeerContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    auto_negotiation_support: Annotated[
        Optional[EnumerationEnum91],
        Field(alias='srl_nokia-lldp:auto-negotiation-support'),
    ] = None
    """
    Support of auto-negotiation
    """
    auto_negotiation_enabled: Annotated[
        Optional[EnumerationEnum92],
        Field(alias='srl_nokia-lldp:auto-negotiation-enabled'),
    ] = None
    """
    Enable state of auto-negotiation
    """
    auto_negotiation_capabilities: Annotated[
        Optional[List[EnumerationEnum93]],
        Field(alias='srl_nokia-lldp:auto-negotiation-capabilities'),
    ] = []
    """
    List of auto-negotiation capabilities advertised
    """
    mau_type: Annotated[
        Optional[EnumerationEnum94], Field(alias='srl_nokia-lldp:mau-type')
    ] = None
    """
    Operational MAU type
    """


class PortDsInterfaceContainer(BaseModel):
    """
    Interface used as the source of PTP messages into the recovery engine
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_index: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:port-index', ge=1, le=999)
    ] = None
    """
    Physical interface used as the source of PTP messages into the recovery engine
    """
    neighbor: Annotated[
        Optional[NeighborContainer], Field(alias='srl_nokia-sync:neighbor')
    ] = None


class PortListEntry(BaseModel):
    """
    Information for the specific sync0 port

    This is used for both non-redundant and redundant platforms.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    sync0_id: Annotated[EnumerationEnum114, Field(alias='srl_nokia-sync:sync0-id')]
    ptp_port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:ptp-port-number', ge=0, le=65535)
    ] = None
    """
    IEEE Std 1588 portNumber

    This is the port-number that will appear in messages sent for this port-index.
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-sync:admin-state')
    ] = 'disable'
    """
    The administrative state of the ptp port
    """
    port_state: Annotated[
        Optional[EnumerationEnum118], Field(alias='srl_nokia-sync:port-state')
    ] = None
    """
    Current state associated with the port
    """
    best_master: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:best-master')
    ] = None
    """
    Indicates if this interface was selected by the BMCA to be the best master
    """
    parent_clock: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:parent-clock')
    ] = None
    """
    Indicates if this interface is the current parent clock of this PTP clock

    May differ from best-master due to use of local GNSS as time source.
    """
    log_announce_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-announce-interval', ge=-3, le=4)
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    Mean time interval between successive Announce messages. To change this setting,
    refer to log-announce-interval in the Default data set.
    """
    announce_receipt_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:announce-receipt-timeout', ge=2, le=10),
    ] = None
    """
    Sets the time limit for missed Announce packets before the master clock is deemed down

    This defines the number of Announce message intervals that must expire with no received
    Announce messages before declaring an ANNOUNCE_RECEIPT_TIMEOUT event. To change this
    setting, refer to announce-receipt-timeout in the Default data set.
    """
    major_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:major-version-number', ge=0, le=255)
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:minor-version-number', ge=0, le=255)
    ] = None
    """
    The PTP minor version number in use on the port
    """
    statistics: Annotated[
        Optional[StatisticsContainer24], Field(alias='srl_nokia-sync:statistics')
    ] = None
    neighbor_count: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:neighbor-count', ge=0, le=4294967295)
    ] = None
    """
    The number of neighbors for the port
    """
    neighbor_list: Annotated[
        Optional[List[NeighborListListEntry2]],
        Field(alias='srl_nokia-sync:neighbor-list'),
    ] = None


class PrefixContainer(BaseModel):
    """
    Enter the prefix context
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip_prefix: Annotated[
        str,
        Field(
            alias='srl_nokia-srv6:ip-prefix',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))$).*$',
        ),
    ]
    """
    SRv6 micro-segment block prefix
    """


class PrefixContainer2(BaseModel):
    """
    Enter the prefix context
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip_prefix: Annotated[
        str,
        Field(
            alias='srl_nokia-srv6:ip-prefix',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))$).*$',
        ),
    ]
    """
    SRv6 locator prefix
    """


class PriorityContainer(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer2(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer3(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer4(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer5(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer6(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer7(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer8(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class PriorityContainer9(BaseModel):
    """
    Narrows the capture to a given severity, a range or a specific set of severities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    match_above: Annotated[
        Optional[EnumerationEnum24], Field(alias='srl_nokia-logging:match-above')
    ] = None
    """
    At a given severity and above
    """
    match_exact: Annotated[
        Optional[List[EnumerationEnum24]], Field(alias='srl_nokia-logging:match-exact')
    ] = []
    """
    Individually specified severities
    """


class RaGuardPolicyListEntry(BaseModel):
    """
    List containing RA Guard Policy and parameters
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ra_guard:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    RA Guard Policy name
    """
    action: Annotated[
        Optional[EnumerationEnum58], Field(alias='srl_nokia-ra_guard:action')
    ] = 'discard'
    """
    Describes the RA Guard Policy action for RA Messages matching the specified attributes.
    RA Messages not matching the specified attributes will be handled in the opposite manner.
    """
    source_prefix_set: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ra_guard:source-prefix-set',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to a prefix set to match RA source address.
    If not specified the verification is skipped.
    """
    hop_limit: Annotated[
        Optional[int], Field(alias='srl_nokia-ra_guard:hop-limit', ge=1, le=255)
    ] = None
    """
    Verifies the minimum advertised hop count limit, RA message value must e equal to or greater than hop-limit.
    If not specified the verification is skipped.
    """
    managed_config_flag: Annotated[
        Optional[bool], Field(alias='srl_nokia-ra_guard:managed-config-flag')
    ] = None
    """
    Causes the RA Guard policy to match IPv6 RA messages with the M (Managed address) flag set.
    If not specified the verification is skipped.
    """
    other_config_flag: Annotated[
        Optional[bool], Field(alias='srl_nokia-ra_guard:other-config-flag')
    ] = None
    """
    Causes the RA Guard policy to match IPv6 RA messages with the O (Other config) flag set.
    If not specified the verification is skipped.
    """
    advertise_prefix_set: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ra_guard:advertise-prefix-set',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to a prefix set to match advertised address within RA message
    """
    router_preference: Annotated[
        Optional[EnumerationEnum59], Field(alias='srl_nokia-ra_guard:router-preference')
    ] = None
    """
    Verifies that the advertised default router preference parameter value is
    equal to or less than the specified limit.
    If not specified the verification is skipped.
    """


class ReceiveLifetimeContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time at which the key becomes valid for use in the receive direction

    If send-and-receive is true, this value is ignored. If send-and-receive is false the default is the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

    If there are multiple keys in the keychain the one used for checking received authentication information is the key with the most recent receive-lifetime start-time that is earlier than the current date and time and that has not exceeded its receive-lifetime end-time by more than 'tolerance' seconds
    """
    end_time: Annotated[
        Optional[Union[EnumerationEnum49, DateAndTimeDeltaType]],
        Field(alias='srl_nokia-keychains:end-time'),
    ] = None
    """
    The time at which the key becomes invalid for use in the receive direction

    The default is forever.
    """


class ReceiverListEntry(BaseModel):
    """
    Specific configuration and states of a specific receiver
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    gnss_id: Annotated[EnumerationEnum134, Field(alias='srl_nokia-sync:gnss-id')]
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-sync:admin-state')
    ] = 'disable'
    """
    Configure the administrative state of the GNSS port
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-sync:oper-state')
    ] = None
    """
    Operational state of the GNSS port
    """
    antenna_cable_delay: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:antenna-cable-delay', ge=0, le=1000)
    ] = 0
    """
    Sets the cable delay value (integer) in ns to the GNSS antenna
    """
    elevation_mask_angle: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:elevation-mask-angle', ge=0, le=89)
    ] = 10
    """
    Sets the elevation mask angle

    This provides a method of filtering satellites low on the horizon to be
    used by the system.
    """
    gnss_receiver_status: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:gnss-receiver-status')
    ] = None
    """
    Specifies the current state of the GNSS receiver module
    """
    gnss_sync_status: Annotated[
        Optional[EnumerationEnum135], Field(alias='srl_nokia-sync:gnss-sync-status')
    ] = None
    """
    Specifies the current state of the sync recovery from GNSS
    """
    gnss_antenna_status: Annotated[
        Optional[EnumerationEnum136], Field(alias='srl_nokia-sync:gnss-antenna-status')
    ] = None
    """
    Specifies the current state of the GNSS antenna
    """
    latitude_position: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:latitude-position',
            ge=-92233720368547.77,
            le=92233720368547.77,
        ),
    ] = None
    """
    Specifies the current latitude of the GNSS antenna
    """
    longitude_position: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:longitude-position',
            ge=-92233720368547.77,
            le=92233720368547.77,
        ),
    ] = None
    """
    Specifies the current longitude of the GNSS antenna
    """
    altitude_position: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:altitude-position',
            ge=-92233720368547.77,
            le=92233720368547.77,
        ),
    ] = None
    """
    Specifies the current altitude of the GNSS antenna
    """
    position_valid: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:position-valid')
    ] = None
    """
    Specifies if the current position information is valid
    """
    gnss_date_and_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:gnss-date-and-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Specifies the date and time as recovered from GNSS
    """
    gnss_utc_offset: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:gnss-utc-offset', ge=-32768, le=32767),
    ] = None
    """
    Specifies the UTC as recovered from GNSS
    """
    gnss_utc_offset_valid: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:gnss-utc-offset-valid')
    ] = None
    """
    Specifies the UTC offset is valid as recovered from GNSS
    """
    gnss_firmware: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:gnss-firmware')
    ] = None
    """
    Specifies the current firmware used by the GNSS receiver
    """
    number_of_satellites_visible: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:number-of-satellites-visible', ge=0, le=255),
    ] = None
    """
    The number of satellites currently visible
    """
    satellites_in_use: Annotated[
        Optional[SatellitesInUseContainer],
        Field(alias='srl_nokia-sync:satellites-in-use'),
    ] = None


class RelayInformationListEntry(BaseModel):
    """
    DHCPv4 relay information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    circuit_id: Annotated[
        str,
        Field(alias='srl_nokia-dhcp-server:circuit-id', max_length=255, min_length=1),
    ]
    """
    The circuit ID of the DHCPv4 relay agent
    """
    remote_id: Annotated[
        str,
        Field(alias='srl_nokia-dhcp-server:remote-id', max_length=255, min_length=1),
    ]
    """
    The remote ID of the DHCPv4 relay agent
    """
    ip_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:ip-address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))$).*$',
        ),
    ] = None
    """
    An IPv4 prefix with host bits.
    """
    options: Annotated[
        Optional[OptionsContainer3], Field(alias='srl_nokia-dhcp-server:options')
    ] = None


class ResourceListEntry(BaseModel):
    """
    List of system-wide resources
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-system-utilization:name')]
    """
    The name of the resource
    """
    upper_threshold_set: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-utilization:upper-threshold-set', ge=0, le=100),
    ] = 90
    """
    Sets the threshold that triggers the generation of a WARNING log and the setting of 'used-upper-threshold-exceeded' to 'true' whenever the utilization of the resource reaches this value in a rising direction
    """
    upper_threshold_clear: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-utilization:upper-threshold-clear', ge=0, le=100),
    ] = 70
    """
    Sets the threshold that triggers the generation of a NOTICE log and the setting of 'used-upper-threshold-exceeded' to 'false' whenever the utilization of the resource reaches this value in a falling direction
    """
    used_percent: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-utilization:used-percent', ge=0, le=100),
    ] = None
    """
    The percentage of the resource that is currently used
    """
    used_entries: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-utilization:used-entries', ge=0, le=4294967295),
    ] = None
    """
    The number of entries that are currently used
    """
    free_entries: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-utilization:free-entries', ge=0, le=4294967295),
    ] = None
    """
    The number of entries that are currently free
    """
    used_high_watermark: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-utilization:used-high-watermark',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    A watermark of highest number of entries used for this resource
    """
    used_last_high_watermark_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-utilization:used-last-high-watermark-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The timestamp when the high-watermark was last updated
    """
    used_upper_threshold_exceeded: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-system-utilization:used-upper-threshold-exceeded'),
    ] = None
    """
    This value is set to true when the used percentage value (used / (used + free) * 100) has reached (in a rising direction) the configured upper-threshold-set for this resource and false when the used percentage value has reached (in a falling direction) the configured upper-threshold-clear for this resource
    """


class RoleListEntry(BaseModel):
    """
    List of local roles configured on the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rolename: Annotated[
        str,
        Field(
            alias='srl_nokia-aaa:rolename',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Assigned rolename for this role
    """
    services: Annotated[
        Optional[List[EnumerationEnum10]], Field(alias='srl_nokia-aaa:services')
    ] = []
    """
    Services that members of this role are authorized for

    Services are additive, if a user is a member of multiple roles, the available services are merged.
    """
    superuser: Annotated[Optional[bool], Field(alias='srl_nokia-aaa:superuser')] = False
    """
    Indicates if users with this role are given superuser

    A superuser is granted implicit authorization to all YANG paths, has the ability to execute all CLI plugins, and by default is permitted to access the device through any interface.

    Additionally, users with the superuser attribute are able to execute 'sudo' in bash. A user may also be assigned a role or list of roles, but these are only evaluated for service authorization.
    """
    tacacs: Annotated[
        Optional[TacacsContainer], Field(alias='srl_nokia-aaa:tacacs')
    ] = None
    cli: Annotated[Optional[CliContainer], Field(alias='srl_nokia-aaa:cli')] = None
    netconf: Annotated[
        Optional[NetconfContainer], Field(alias='srl_nokia-aaa:netconf')
    ] = None


class RpcCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rpc: Annotated[
        Optional[RpcContainer], Field(alias='srl_nokia-packet-link-qual:rpc')
    ] = None


class RuleListEntry(BaseModel):
    """
    List of paths to perform access control against
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    path_reference: Annotated[
        str,
        Field(
            alias='srl_nokia-configuration-role:path-reference',
            pattern='^(?=^[A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?\\-{}*\\\\\\\\"\\[\\]]+$).*$',
        ),
    ]
    """
    Reference to a valid YANG path, in CLI notation

    This path may include keys, wildcards, ranges, and other management server supported constructs. Ranges will be expanded.
    The root path can be specified with '/'.

    E.g.
        /
        "/interface"
        "/acl ipv4-filter foo* description"
    """
    action: Annotated[
        EnumerationEnum53, Field(alias='srl_nokia-configuration-role:action')
    ]
    """
    Action to allow for this path
    """


class RxAnnounceContainer(BaseModel):
    """
    Statistics for receive announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum120], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxAnnounceContainer2(BaseModel):
    """
    Statistics for receive announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum126], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxDelayRespContainer(BaseModel):
    """
    Statistics for receive delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum122], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxDelayRespContainer2(BaseModel):
    """
    Statistics for receive delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum128], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxSyncContainer(BaseModel):
    """
    Statistics for receive sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum121], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxSyncContainer2(BaseModel):
    """
    Statistics for receive sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum127], Field(alias='srl_nokia-sync:state')
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-interval', ge=-128, le=127)
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:duration', ge=0, le=4294967295)
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class SeamlessBfdContainer(BaseModel):
    """
    When present, this node attempts to setup a seamless BFD session on every segment-list of every SR policy that uses protection-policy, but only if that SR policy is a primary or standby (secondary) candidate path. The transition of an SBFD session from up to down is a trigger for rerouting traffic around a failed primary path.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    detection_multiplier: Annotated[
        Optional[int],
        Field(alias='srl_nokia-protection-policies:detection-multiplier', ge=3, le=20),
    ] = 3
    """
    The number of packets that must be missed to declare this session as down

    The detection interval for the BFD session is calculated by multiplying the
    value of the negotiated transmission interval by this value.
    """
    desired_minimum_transmit_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-protection-policies:desired-minimum-transmit-interval',
            ge=10000,
            le=100000000,
        ),
    ] = 1000000
    """
    The minimum interval between transmission of BFD control packets

    This value is advertised to the peer, however the actual interval used is specified
    by taking the maximum of desired-minimum-transmit-interval and the value of the remote
    required-minimum-receive interval value.
    This value is specified as an integer number of microseconds.
    """
    hold_down_timer: Annotated[
        Optional[Union[HoldDownTimerLeaf1, EnumerationEnum55]],
        Field(alias='srl_nokia-protection-policies:hold-down-timer'),
    ] = '4'
    """
    Specifies a hold-down timer value when seamless-bfd is enabled

    The timer is started when the number of S-BFD sessions that are up drops below the threshold. The TE-policy path is not considered to be up again until the hold-down timer has expired and the number of S-BFD sessions that are up equals or exceeds the threshold.
    A grace preiod after session down such that sBFD session flaps does not impact active path.

    The default is 4 seconds.
    """
    wait_for_up_timer: Annotated[
        Optional[int],
        Field(alias='srl_nokia-protection-policies:wait-for-up-timer', ge=1, le=1800),
    ] = 4
    """
    Specifies a wait-for-up timer value when seamless-bfd is enabled

    This timer takes effect if BFD does not come up, or BFD goes from up to down. The timer is started when BFD is first enabled on a segment-list or BFD transitions from up to down. When the timer expires if BFD is not yet come up, then the path is torn down by removing it from the TTM and the PI and the retry timer is started.

    The default is 4 seconds.
    """
    mode: Annotated[
        Optional[EnumerationEnum56], Field(alias='srl_nokia-protection-policies:mode')
    ] = 'monitored'
    """
    Specifies requested protection method

    ecmp-protected is valid for colored te-policies and programs all the valid segment lists and manages their availability using seamless-BFD for each segment list. Switchover between candidate paths is triggered by the node if number of segment-lists up is less than the threshold on the active policy.ecmp-protected is not valid for uncolored sr-policies.

    linear is valid for uncolored te-policies and triggers fail-over among active segment-lists, primary to standby / secondary.
    """
    threshold: Annotated[
        Optional[int],
        Field(alias='srl_nokia-protection-policies:threshold', ge=1, le=32),
    ] = 1
    """
    Minimum number of up seamless-BFD sessions for up te-policy
    """


class SecondaryDefaultLookupContainer(BaseModel):
    """
    Container with options to control fallback routing achieved by doing a secondary FIB lookup in the default network-instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-system-datapath:admin-state')
    ] = 'disable'
    """
    Enable or disable the secondary lookup

    When set to enable all IPv4 and IPv6 routes of the default network-instance are programmed into the kaps-public table and fallback routing can be enabled in any ip-vrf network-instance by programming it with a default route having a redirect-to-default next-hop action.

    A change in the value of this leaf does not take effect until the next chassis reboot.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum28], Field(alias='srl_nokia-system-datapath:oper-state')
    ] = None
    """
    Indicates whether secondary default lookup is active in the system or not
    """
    chassis_reboot_required: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-datapath:chassis-reboot-required')
    ] = None
    """
    Reads true if the user has committed a change in the configuration of secondary-default-lookup but has not yet saved the config and restarted the system, so previous configuration is still in effect
    """


class SelectionProcessListEntry(BaseModel):
    """
    Selection Process of the Monitoring Device.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Key of this list.
    """
    selector: Annotated[
        Optional[List[SelectorListEntry]], Field(alias='srl_nokia-ipfix:selector')
    ] = None
    cache: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ipfix:cache',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Cache that receives the output of the
    Selection Process.
    """


class SendLifetimeContainer(BaseModel):
    """
    Specifies the lifetime of the key for sending authentication information to the peer
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time at which the key becomes valid for use in the send direction

    The default is the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

    If there are multiple keys in the keychain the one used for sending authentication information is the key with the most recent send-lifetime start-time that is earlier than the current date and time
    """
    send_and_receive: Annotated[
        Optional[bool], Field(alias='srl_nokia-keychains:send-and-receive')
    ] = None
    """
    When this is set to true (the default value), the specified start-time also applies to the receive direction

    When set to false, router uses the specific start-time for the receive direction (asymmetric mode).
    """


class ServicesContainer(BaseModel):
    """
    Container for system wide Services MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[NetworkInstanceContainer],
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:network-instance'
        ),
    ] = None
    evpn: Annotated[
        Optional[EvpnContainer2],
        Field(alias='srl_nokia-mpls-services-evpn-label-management:evpn'),
    ] = None


class SessionListEntry2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    session_id: Annotated[
        int, Field(alias='srl_nokia-netconf-server:session-id', ge=1, le=4294967295)
    ]
    process_id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:process-id', ge=0, le=4294967295),
    ] = None
    """
    The process ID of the NETCONF session
    """
    in_bad_hellos: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:in-bad-hellos', ge=0, le=4294967295),
    ] = 0
    """
    Inbound bad NETCONF hello messages

    Number of bad NETCONF hello messages that have been received by the NETCONF server
    """
    get_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:get-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <get> requests

    Number of <get> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    get_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:get-config-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <get-config> requests

    Number of <get-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    get_data_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:get-data-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <get-data> requests

    Number of <get-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    get_schema_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:get-schema-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <get-schema> requests

    Number of <get-schema> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:edit-config-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <edit-config> requests

    Number of <edit-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    failed_edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:failed-edit-config-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    Failed NETCONF <edit-config> requests

    Number of <edit-config> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    edit_data_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:edit-data-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <edit-data> requests

    Number of <edit-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    failed_edit_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:failed-edit-data-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    Failed NETCONF <edit-data> requests

    Number of <edit-data> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    kill_session_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:kill-session-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <kill-session> requests

    Number of <kill-session> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    copy_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:copy-config-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <copy-config> requests

    Number of copy-config NETCONF requests that have been accepted and processed by the NETCONF server
    """
    delete_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:delete-config-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <delete-config> requests

    Number of <delete-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    validate_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:validate-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <validate> requests

    Number of <validate> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    lock_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:lock-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <lock> requests

    Number of <lock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    failed_lock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:failed-lock-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    Failed NETCONF <lock> requests

    Number of <lock> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    unlock_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:unlock-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <unlock> requests

    Number of <unlock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    commit_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:commit-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <commit> requests

    Number of commit NETCONF requests that have been accepted and processed by the NETCONF server
    """
    discard_changes_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:discard-changes-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <discard-changes> requests

    Number of <discard-changes> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    action_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:action-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <action> requests

    Number of <action> NETCONF requests that have been accepted and processed by the NETCONF server
    """


class SessionListEntry3(BaseModel):
    """
    List of configuration sessions currently active
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[int, Field(alias='srl_nokia-configuration:id', ge=0, le=4294967295)]
    """
    System generated ID for the configuration session
    """
    type: Annotated[
        Optional[EnumerationEnum50], Field(alias='srl_nokia-configuration:type')
    ] = None
    """
    Type of configuration session
    """
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Name of the candidate the session is active on

    Set to 'default' if a non-named candidate is active
    """
    exclusive: Annotated[
        Optional[bool], Field(alias='srl_nokia-configuration:exclusive')
    ] = None
    """
    Details if this session is running in exclusive mode
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    User that started the configuration session
    """
    started: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:started',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Start date and time of the configuration session
    """


class StaticListEntry(BaseModel):
    """
    List of static label blocks

    When a client application binds its operation to a static label block that client application is expected to specify the exact label value it wants to use every time it requests a label within the static label block.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-mpls-label-management:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    The name of the static label block
    """
    shared: Annotated[
        Optional[bool], Field(alias='srl_nokia-mpls-label-management:shared')
    ] = True
    """
    When set to true, the label block can be shared by multiple protoccols. When set to false, the label block is dedicated to one protocol.
    """
    start_label: Annotated[
        int,
        Field(alias='srl_nokia-mpls-label-management:start-label', ge=16, le=1048575),
    ]
    """
    The starting label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    end_label: Annotated[
        int, Field(alias='srl_nokia-mpls-label-management:end-label', ge=16, le=1048575)
    ]
    """
    The ending label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    allocated_labels: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:allocated-labels',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    The number of labels that are currently used in this block
    """
    free_labels: Annotated[
        Optional[int],
        Field(alias='srl_nokia-mpls-label-management:free-labels', ge=0, le=4294967295),
    ] = None
    """
    The number of labels that are currently available and free in this block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    status: Annotated[
        Optional[EnumerationEnum44],
        Field(alias='srl_nokia-mpls-label-management:status'),
    ] = None
    """
    The status of the MPLS label block
    """
    user: Annotated[
        Optional[List[UserListEntry2]],
        Field(alias='srl_nokia-mpls-label-management:user'),
    ] = None


class StatisticsContainer(BaseModel):
    """
    Enclosing container for server statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    login_success: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:login-success', ge=0, le=4294967295)
    ] = 0
    """
    Number of login successes
    """
    login_connection_failures: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:login-connection-failures', ge=0, le=4294967295),
    ] = 0
    """
    Number of login connection failures
    """
    login_rejects: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:login-rejects', ge=0, le=4294967295)
    ] = 0
    """
    Number of login rejections
    """
    accounting_success: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:accounting-success', ge=0, le=4294967295),
    ] = 0
    """
    Number of accounting successes
    """
    accounting_rejects: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:accounting-rejects', ge=0, le=4294967295),
    ] = 0
    """
    Number of accounting rejections
    """
    accounting_connection_failures: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:accounting-connection-failures', ge=0, le=4294967295
        ),
    ] = 0
    """
    Number of accounting connection failures
    """
    authorization_success: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:authorization-success', ge=0, le=4294967295),
    ] = 0
    """
    Number of authorization successes
    """
    authorization_rejects: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:authorization-rejects', ge=0, le=4294967295),
    ] = 0
    """
    Number of authorization rejections
    """
    authorization_connection_failures: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:authorization-connection-failures', ge=0, le=4294967295
        ),
    ] = 0
    """
    Number of authorization connection failures
    """
    invalid_vsas: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:invalid-vsas', ge=0, le=4294967295)
    ] = 0
    """
    Number of invalid VSAs received
    """
    malformed_vsas: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:malformed-vsas', ge=0, le=4294967295)
    ] = 0
    """
    Number of malformed VSAs received
    """
    unknown_vsas: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:unknown-vsas', ge=0, le=4294967295)
    ] = 0
    """
    Number of unknown VSAs received
    """
    valid_vsas: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:valid-vsas', ge=0, le=4294967295)
    ] = 0
    """
    Number of valid VSAs received
    """


class StatisticsContainer11(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    maximum_ids: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:maximum-ids',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    Maximum number of multicast ids available in the system.
    """
    current_usage: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:current-usage',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of multicast ids that are in use on the system.
    """
    total_pending: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:total-pending',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of multicast ids pending allocation on the system.
    """
    multicast_id_user_type: Annotated[
        Optional[List[MulticastIdUserTypeListEntry]],
        Field(alias='srl_nokia-system-multicast:multicast-id-user-type'),
    ] = None


class StatisticsContainer12(BaseModel):
    """
    Packet transmition statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_bpdus_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:bad-bpdus-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of Invalid BPDUs received
    """
    cfg_bpdus_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:cfg-bpdus-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of configuration BPDUs received on this interface
    """
    cfg_bpdus_transmitted: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:cfg-bpdus-transmitted',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of configuration BPDUs sent on this interface
    """
    tcn_bpdus_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:tcn-bpdus-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of topology change notification BPDUs received on this interface
    """
    tcn_bpdus_transmitted: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:tcn-bpdus-transmitted',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of topology change notification BPDUs sent on this interface
    """
    tc_bit_bpdus_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:tc-bit-bpdus-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of BPDUs received on this interface with the Topology Change bit set
    """
    tc_bit_bpdus_transmitted: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:tc-bit-bpdus-transmitted',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of BPDUs sent on this interface with the Topology Change bit set
    """
    rst_bpdus_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:rst-bpdus-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of RST BPDUs received on this interface
    """
    rst_bpdus_transmitted: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:rst-bpdus-transmitted',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of RST BPDUs sent on this interface
    """
    mst_bpdus_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:mst-bpdus-received',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of MST BPDUs received on this interface
    """
    mst_bpdus_transmitted: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:mst-bpdus-transmitted',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of MST BPDUs sent on this interface
    """


class StatisticsContainer15(BaseModel):
    """
    Global LLDP counters
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    frame_in: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-in', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames received
    """
    frame_out: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-out', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames transmitted
    """
    frame_error_in: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-error-in', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames received with errors
    """
    frame_discard: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-discard', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames received and discarded
    """
    tlv_discard: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:tlv-discard', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of TLV frames received and discarded
    """
    tlv_unknown: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:tlv-unknown', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of frames received with unknown TLV
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the last time the counters were cleared
    """
    tlv_accepted: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:tlv-accepted', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of valid TLVs received.
    """
    entries_aged_out: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:entries-aged-out', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of entries aged out due to timeout.
    """


class StatisticsContainer16(BaseModel):
    """
    LLDP counters on each interface
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    frame_in: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-in', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames received
    """
    frame_out: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-out', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames transmitted
    """
    frame_error_in: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-error-in', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames received with errors
    """
    frame_discard: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-discard', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of LLDP frames received and discarded
    """
    tlv_discard: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:tlv-discard', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of TLV frames received and discarded
    """
    tlv_unknown: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:tlv-unknown', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of frames received with unknown TLV
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the last time the counters were cleared
    """
    frame_error_out: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:frame-error-out', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of frame transmit errors on the interface
    """


class StatisticsContainer18(BaseModel):
    """
    Aggregate statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:anno-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:sync-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-tx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:del-req-msg-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:del-resp-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:follow-up-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-tx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:signaling-msg-rx', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:other-rx', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer], Field(alias='srl_nokia-sync:discards')
    ] = None
    signaling_uni_neg_tlv: Annotated[
        Optional[SignalingUniNegTlvContainer],
        Field(alias='srl_nokia-sync:signaling-uni-neg-tlv'),
    ] = None
    sync_packet_loss: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:sync-packet-loss', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with detected packet loss of sync packets from the master clock
    """
    sync_high_packet_loss: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:sync-high-packet-loss', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with high packet loss of sync packets
    """
    delay_packet_loss: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:delay-packet-loss', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with detected packet loss for the delay request/response packets
    """
    delay_high_packet_loss: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:delay-high-packet-loss', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with high packet loss for delay req packets
    """
    unicast_msg_rate: Annotated[
        Optional[UnicastMsgRateContainer],
        Field(alias='srl_nokia-sync:unicast-msg-rate'),
    ] = None
    multicast_msg_rate: Annotated[
        Optional[MulticastMsgRateContainer],
        Field(alias='srl_nokia-sync:multicast-msg-rate'),
    ] = None


class StatisticsContainer19(BaseModel):
    """
    Time recovery engine state statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    time_in_initial: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-in-initial', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of seconds while in Initializing state
    """
    time_in_acquiring: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-in-acquiring', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of seconds while in Acquiring state
    """
    time_in_holdover: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-in-holdover', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of seconds while in Holdover state
    """
    time_in_locked: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:time-in-locked', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of seconds while in Locked state
    """
    sync_too_much_pdv: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:sync-too-much-pdv', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with high PDV for sync packets for time recovery
    """
    delay_too_much_pdv: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:delay-too-much-pdv', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with high PDV for delay request/response packets for time recovery
    """


class StatisticsContainer20(BaseModel):
    """
    Freq recovery engine state statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    time_in_initial: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-in-initial', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of seconds while in Initializing state
    """
    time_in_acquiring: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-in-acquiring', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of seconds while in Acquiring state
    """
    time_in_phase_tracking: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-in-phase-tracking', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of seconds while in Phase Tracking state
    """
    time_in_holdover: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:time-in-holdover', ge=0, le=4294967295),
    ] = None
    """
    Specifies the number of seconds while in Holdover state
    """
    time_in_locked: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:time-in-locked', ge=0, le=4294967295)
    ] = None
    """
    Specifies the number of seconds while in Locked state
    """
    sync_high_phase_shift: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:sync-high-phase-shift', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with large clock shift from sync packets for frequency recovery
    """
    sync_too_much_pdv: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:sync-too-much-pdv', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with high PDV for sync packets for frequency recovery
    """
    delay_high_phase_shift: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:delay-high-phase-shift', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with large clock shift for delay req packets for frequency recovery
    """
    delay_too_much_pdv: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:delay-too-much-pdv', ge=0, le=4294967295),
    ] = 0
    """
    The number of events with high PDV for delay req packets for frequency recovery
    """


class StatisticsContainer3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of macs that are active on the system.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:total-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of macs, active and inactive, on the system.
    """
    failed_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:failed-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of macs, which have not been programmed on atleast one slot
    """
    mac_type: Annotated[
        Optional[List[MacTypeListEntry]],
        Field(alias='srl_nokia-system-bridge-table:mac-type'),
    ] = None


class StatisticsContainer4(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    max_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:max-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The maximum number of BGP-EVPN MPLS multicast Termination EndPoints (TEPs) allowed in the system
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:total-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of BGP-EVPN MPLS multicast Termination EndPoints (TEPs)
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of active BGP-EVPN MPLS multicast Termination Endpoints (TEPs)
    """


class StatisticsContainer5(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of proxy ARP entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of active proxy ARP entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of inactive proxy ARP entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of pending proxy ARP entries.
    """
    neighbor_origin: Annotated[
        Optional[List[NeighborOriginListEntry]],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:neighbor-origin'),
    ] = None


class StatisticsContainer6(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of proxy ARP entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of active proxy ARP entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of inactive proxy ARP entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of pending proxy ARP entries.
    """
    neighbor_origin: Annotated[
        Optional[List[NeighborOriginListEntry2]],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:neighbor-origin'),
    ] = None


class StatisticsContainer7(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active_sessions: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:active-sessions', ge=0, le=64),
    ] = None
    """
    Active NETCONF sessions

    The total number of active NETCONF sessions.  A session is defined as an individual client connection
    over which a NETCONF session has been started by providing bi-directional <hello> messages
    """
    total_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:total-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF total requests

    Total number of NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_responses: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:total-responses', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF total responses

    Total number of NETCONF responses that have been generated and sent by the NETCONF server
    """
    total_error_responses: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-error-responses', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF error responses

    Total number of NETCONF error responses that have been generated and sent by the NETCONF server
    """
    total_close_session_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-close-session-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <close-session> requests

    Total number of <close-session> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_in_bad_hellos: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-in-bad-hellos', ge=0, le=4294967295
        ),
    ] = 0
    """
    Inbound bad NETCONF hello messages

    Total number of bad NETCONF hello messages that have been received by the NETCONF server
    """
    total_dropped_sessions: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-dropped-sessions', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF dropped sessions

    Total number of dropped NETCONF sessions
    """
    total_get_requests: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:total-get-requests', ge=0, le=4294967295),
    ] = 0
    """
    NETCONF <get> requests

    Total number of <get> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_get_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-get-config-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <get-config> requests

    Total number of <get-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_get_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-get-data-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <get-data> requests

    Total number of <get-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_get_schema_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-get-schema-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <get-schema> requests

    Total number of <get-schema> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-edit-config-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <edit-config> requests

    Total number of <edit-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_failed_edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-failed-edit-config-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    Failed NETCONF <edit-config> requests

    Total number of <edit-config> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    total_edit_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-edit-data-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <edit-data> requests

    Total number of <edit-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_failed_edit_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-failed-edit-data-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    Failed NETCONF <edit-data> requests

    Total number of <edit-data> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    total_kill_session_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-kill-session-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <kill-session> requests

    Total number of <kill-session> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_copy_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-copy-config-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <copy-config> requests

    Total number of copy-config NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_delete_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-delete-config-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <delete-config> requests

    Total number of <delete-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_validate_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-validate-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <validate> requests

    Total number of <validate> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_lock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-lock-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <lock> requests

    Total number of <lock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_failed_lock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-failed-lock-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    Failed NETCONF <lock> requests

    Total number of <lock> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    total_unlock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-unlock-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <unlock> requests

    Total number of <unlock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_commit_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-commit-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <commit> requests

    Total number of commit NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_discard_changes_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-discard-changes-requests',
            ge=0,
            le=4294967295,
        ),
    ] = 0
    """
    NETCONF <discard-changes> requests

    Total number of <discard-changes> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_action_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-action-requests', ge=0, le=4294967295
        ),
    ] = 0
    """
    NETCONF <action> requests

    Total number of <action> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    session: Annotated[
        Optional[List[SessionListEntry2]],
        Field(alias='srl_nokia-netconf-server:session'),
    ] = None


class SubinterfaceListEntry(BaseModel):
    """
    List of subinterfaces used as mirror source
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-mirroring:name')]
    """
    Reference type to a specific subinterface of the form <interface-name>.<subinterface-index>
    """
    direction: Annotated[
        Optional[EnumerationEnum30], Field(alias='srl_nokia-mirroring:direction')
    ] = 'egress-only'
    """
    The direction of traffic to be mirrored
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-mirroring:oper-state')
    ] = None
    """
    Indicates the operational state of the mirror subinterface
    """
    oper_down_reason: Annotated[
        Optional[EnumerationEnum31], Field(alias='srl_nokia-mirroring:oper-down-reason')
    ] = None
    """
    The reason for the mirror subinterface being operationally down.  The not-applicable reason is when mirror instance is shutdown or the mirror source is operational
    """


class SubscriberListEntry(BaseModel):
    """
    List of broadband network gateway (BNG) subscribers
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subscriber_name: Annotated[
        str,
        Field(
            alias='srl_nokia-lawful-intercept:subscriber-name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Name of the wireline subscriber
    """
    description: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lawful-intercept:description', max_length=255, min_length=1
        ),
    ] = None
    """
    Text description
    """
    intercept_id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lawful-intercept:intercept-id', ge=1, le=4294967295),
    ] = None
    """
    Intercept ID in the shim header
    """
    session_id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lawful-intercept:session-id', ge=1, le=4294967295),
    ] = None
    """
    Session ID in the shim header
    """
    direction: Annotated[
        EnumerationEnum85, Field(alias='srl_nokia-lawful-intercept:direction')
    ]
    """
    Direction of traffic to be mirrored
    """
    mirror_instance_name: Annotated[
        str,
        Field(
            alias='srl_nokia-lawful-intercept:mirror-instance-name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Name of the mirror instance target

    The name of the mirror instance must match the name of the mirror service on the MAG-u.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-lawful-intercept:oper-state')
    ] = None
    """
    Operational state
    """
    oper_down_reason: Annotated[
        Optional[str], Field(alias='srl_nokia-lawful-intercept:oper-down-reason')
    ] = None
    """
    Interception has not started because the subscriber is not online or a problem occurred
    """


class SubscribersContainer(BaseModel):
    """
    Subscriber statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_configured: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-configured',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total number of subscribers provisioned as LI targets in the system
    """
    total_active: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-active',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total number of subscribers in active LI sessions
    """
    total_down: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-down', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Total number of subscribers not in active LI sessions
    """
    total_error: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-error',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Total number of subscribers with failed LI sessions
    """


class SubsystemListEntry(BaseModel):
    """
    Entity or entities that may produce messages to be captured
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subsystem_name: Annotated[str, Field(alias='srl_nokia-logging:subsystem-name')]
    """
    Reference to an available subsystem to source messages from
    """
    priority: Annotated[
        Optional[PriorityContainer2], Field(alias='srl_nokia-logging:priority')
    ] = None


class SubsystemListEntry2(BaseModel):
    """
    Entity or entities that may produce messages to be captured
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subsystem_name: Annotated[str, Field(alias='srl_nokia-logging:subsystem-name')]
    """
    Reference to an available subsystem to source messages from
    """
    priority: Annotated[
        Optional[PriorityContainer5], Field(alias='srl_nokia-logging:priority')
    ] = None


class SubsystemListEntry3(BaseModel):
    """
    Entity or entities that may produce messages to be captured
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subsystem_name: Annotated[str, Field(alias='srl_nokia-logging:subsystem-name')]
    """
    Reference to an available subsystem to source messages from
    """
    priority: Annotated[
        Optional[PriorityContainer7], Field(alias='srl_nokia-logging:priority')
    ] = None


class SubsystemListEntry4(BaseModel):
    """
    Entity or entities that may produce messages to be captured
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subsystem_name: Annotated[str, Field(alias='srl_nokia-logging:subsystem-name')]
    """
    Reference to an available subsystem to source messages from
    """
    priority: Annotated[
        Optional[PriorityContainer9], Field(alias='srl_nokia-logging:priority')
    ] = None


class TepListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    tep: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:tep'),
    ]
    """
    The IP address that identifies the remote BGP-EVPN MPLS multicast Termination Endpoint (TEP)
    """
    index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:index',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    The hardware index (system allocated) for the BGP-EVPN MPLS multicast Termination Endpoint (TEP)

    If a non-zero hardware index is allocated, then there are available system resources and there is
    at least one BGP-EVPN MPLS multicast destination (using this TEP) ready to be programmed. If the
    hardware index is 0, there are not resources left and the TEP is not programmed, even if an Inclusive
    Multicast Ethernet Tag route was correctly imported from a peer.
    """
    last_changed: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:last-changed',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time of the last update of this BGP-EVPN MPLS multicast Termination Endpoint
    """


class TimePropertiesDsContainer(BaseModel):
    """
    The timeProperties data set of the clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    current_utc_offset_valid: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:current-utc-offset-valid')
    ] = None
    """
    When set to true, the current UTC offset is valid
    """
    current_utc_offset: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:current-utc-offset', ge=-32768, le=32767),
    ] = None
    """
    The offset between TAI and UTC

    Only applies when the epoch of the PTP system is the PTP epoch in units of seconds
    (i.e. when ptp-timescale is TRUE). Otherwise, the value has no meaning.
    """
    leap59: Annotated[Optional[bool], Field(alias='srl_nokia-sync:leap59')] = None
    """
    If true, the last minute of the current UTC day contains 59 seconds
    """
    leap61: Annotated[Optional[bool], Field(alias='srl_nokia-sync:leap61')] = None
    """
    If true, the last minute of the current UTC day contains 61 seconds
    """
    time_traceable: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:time-traceable')
    ] = None
    """
    If true, the timescale and the currentUtcOffset are traceable to a primary reference
    """
    frequency_traceable: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:frequency-traceable')
    ] = None
    """
    If true, the frequency determining the timescale is traceable to a primary reference
    """
    ptp_timescale: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:ptp-timescale')
    ] = None
    """
    If true clock timescale of the grandmaster is PTP; false it is ARB (arbitrary)
    """
    time_source: Annotated[
        Optional[EnumerationEnum117], Field(alias='srl_nokia-sync:time-source')
    ] = None
    """
    The source of time used by the grandmaster clock

    If a value is received that does not map to one of the enumerations, then the reserved value is used
    """


class TimeoutCacheCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    timeout_cache: Annotated[
        Optional[TimeoutCacheContainer], Field(alias='srl_nokia-ipfix:timeout-cache')
    ] = None


class TimersContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    boot_timer: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:boot-timer',
            ge=0,
            le=6000,
        ),
    ] = 10
    """
    Remaining time before running BGP EVPN multi-homing DF election algorithm
    """
    activation_timer: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:activation-timer',
            ge=0,
            le=100,
        ),
    ] = 3
    boot_remaining_time: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:boot-remaining-time',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    Indicates the number of seconds remaining for the boot timer to expire.
    """
    boot_start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:boot-start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the time at which the boot timer started.
    """


class TraceOptionsContainer(BaseModel):
    """
    Debug trace-options for NETCONF
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    direction: Annotated[
        Optional[EnumerationEnum20], Field(alias='srl_nokia-netconf-server:direction')
    ] = 'both'
    """
    Direction to trace messages
    """
    rpc: Annotated[
        Optional[List[EnumerationEnum21]], Field(alias='srl_nokia-netconf-server:rpc')
    ] = []
    """
    RPC messages to trace
    """


class TraceOptionsContainer2(BaseModel):
    """
    Container for tracing DHCP server operations instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace: Annotated[
        Optional[List[EnumerationEnum35]], Field(alias='srl_nokia-dhcp-server:trace')
    ] = []
    """
    List of events to trace
    """


class TraceOptionsContainer3(BaseModel):
    """
    Container for tracing DHCP server operations instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace: Annotated[
        Optional[List[EnumerationEnum36]], Field(alias='srl_nokia-dhcp-server:trace')
    ] = []
    """
    List of events to trace
    """


class TraceOptionsContainer4(BaseModel):
    """
    Interface Stp debug trace options
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace: Annotated[
        Optional[List[EnumerationEnum72]],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:trace'),
    ] = []
    """
    List of tracing options
    """


class TrustAnchorContainer(BaseModel):
    """
    State relating to the active trust anchor provided via Certz

    This is equivalent to the certificate authority bundle, and is the list of certificates used to validate clients in mTLS, and to validate servers in outbound TLS.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-gnsi-certz:version')] = (
        None
    )
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-certz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class TrustAnchorContainer2(BaseModel):
    """
    State relating to the active trust anchor provided via Certz

    This is equivalent to the certificate authority bundle, and is the list of certificates used to validate clients in mTLS, and to validate servers in outbound TLS.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-grpc:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class TrustedUserCaKeysContainer(BaseModel):
    """
    State relating to the Certificate Authorities provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-credentialz:version')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class UnContainer(BaseModel):
    """
    Enter the un context
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    srh_mode: Annotated[
        Optional[EnumerationEnum57], Field(alias='srl_nokia-srv6:srh-mode')
    ] = 'psp'
    """
    Segment Routing Header (SRH) mode
    """
    value: Annotated[int, Field(alias='srl_nokia-srv6:value', ge=1, le=1048575)]
    """
    SRv6 uN function value
    """


class UnicastNegotiationContainer(BaseModel):
    """
    Details of each negotiation session
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rx_announce: Annotated[
        Optional[RxAnnounceContainer], Field(alias='srl_nokia-sync:rx-announce')
    ] = None
    rx_sync: Annotated[
        Optional[RxSyncContainer], Field(alias='srl_nokia-sync:rx-sync')
    ] = None
    rx_delay_resp: Annotated[
        Optional[RxDelayRespContainer], Field(alias='srl_nokia-sync:rx-delay-resp')
    ] = None
    tx_announce: Annotated[
        Optional[TxAnnounceContainer], Field(alias='srl_nokia-sync:tx-announce')
    ] = None
    tx_sync: Annotated[
        Optional[TxSyncContainer], Field(alias='srl_nokia-sync:tx-sync')
    ] = None
    tx_delay_resp: Annotated[
        Optional[TxDelayRespContainer], Field(alias='srl_nokia-sync:tx-delay-resp')
    ] = None


class UnicastNegotiationContainer2(BaseModel):
    """
    Details of each negotiation session
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rx_announce: Annotated[
        Optional[RxAnnounceContainer2], Field(alias='srl_nokia-sync:rx-announce')
    ] = None
    rx_sync: Annotated[
        Optional[RxSyncContainer2], Field(alias='srl_nokia-sync:rx-sync')
    ] = None
    rx_delay_resp: Annotated[
        Optional[RxDelayRespContainer2], Field(alias='srl_nokia-sync:rx-delay-resp')
    ] = None
    tx_announce: Annotated[
        Optional[TxAnnounceContainer2], Field(alias='srl_nokia-sync:tx-announce')
    ] = None
    tx_sync: Annotated[
        Optional[TxSyncContainer2], Field(alias='srl_nokia-sync:tx-sync')
    ] = None
    tx_delay_resp: Annotated[
        Optional[TxDelayRespContainer2], Field(alias='srl_nokia-sync:tx-delay-resp')
    ] = None


class UnixSocketContainer(BaseModel):
    """
    Top-level container for configuration and state related to unix sockets
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-json-rpc:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable the JSON RPC server via unix socket
    This requires the JSON RPC server to be globally enabled
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-json-rpc:oper-state')
    ] = None
    """
    Details if the JSON RPC server is operationally available
    """
    use_authentication: Annotated[
        Optional[bool], Field(alias='srl_nokia-json-rpc:use-authentication')
    ] = True
    """
    Enable or disable the use of username/password authentication for every JSON RPC request
    """
    session_limit: Annotated[
        Optional[int], Field(alias='srl_nokia-json-rpc:session-limit', ge=1, le=100)
    ] = None
    """
    The number of concurrent requests the server will allow
    If a request comes in while this limit is reached, the request will block until another request is finished.
    """
    socket_path: Annotated[
        Optional[str], Field(alias='srl_nokia-json-rpc:socket-path')
    ] = None
    """
    Path to the unix socket used by JSON RPC
    """
    tls_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-json-rpc:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to the TLS profile to use on the JSON RPC unix socket server

    If none is specified, then TLS is not used.
    """


class UtilizationContainer(BaseModel):
    """
    Configuration and state for each system resource
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    resource: Annotated[
        Optional[List[ResourceListEntry]],
        Field(alias='srl_nokia-system-utilization:resource'),
    ] = None


class AclFilterListEntry(BaseModel):
    """
    List  IPv4, IPv6 ACL filters
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-mirroring:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    ACL Filter policy name
    """
    type: Annotated[EnumerationEnum32, Field(alias='srl_nokia-mirroring:type')]
    """
    Reference to the ACL filter policy type
    """
    entry: Annotated[
        Optional[List[EntryListEntry]], Field(alias='srl_nokia-mirroring:entry')
    ] = None


class AclContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    acl_filter: Annotated[
        Optional[List[AclFilterListEntry]],
        Field(alias='srl_nokia-mirroring:acl-filter'),
    ] = None


class AdvertiseIflHostAdRoutesContainer(BaseModel):
    """
    Enables the advertisement of IP AD per EVI/ES routes for IP Aliasing

    When configured, AD per-EVI/ES routes are advertised for the IP-VRF and bgp-evpn instances with MAC-VRFs
    attached to the Ethernet Segment. The AD per-EVI routes for the IP-VRFs contain the route distinguisher,
    route targets and label/VNI of the IP-VRF bgp-evpn instance (with the instance indicated in the
    bgp-evpn-instance command). The AD per-ES routes for the IP-VRFs contain the route distinguisher and
    route targets of the IP-VRF bgp-evpn-instance. On the remote PEs, the reception of BGP-EVPN-IFL-HOST routes
    with an ESI matching the ESI of the IP-VRF AD per-EVI/ES routes, will enable the IP Aliasing procedures for
    BGP-EVPN-IFL-HOST routes.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp_evpn_instance: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:bgp-evpn-instance',
            ge=1,
            le=2,
        ),
    ] = '1'
    """
    The bgp-evpn instance of the IP-VRF network-instance using the Ethernet Segment

    It indicates from which EVPN interface-less bgp-instance the label/VNI, route distinguisher and route
    targets are taken when advertising the AD per-EVI routes and the AD per-ES routes (except for the VNI/label
    in AD per-ES routes).
    """
    internal_tags: Annotated[
        Optional[InternalTagsContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:internal-tags'
        ),
    ] = None


class AlgorithmContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        Optional[EnumerationEnum62],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:type'
        ),
    ] = 'default'
    """
    Designated Forwarder algorithm type for this ethernet-segment.
    """
    oper_type: Annotated[
        Optional[EnumerationEnum62],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-type'
        ),
    ] = None
    """
    Operational Designated Forwarder algorithm type for this ethernet-segment.
    """
    preference_alg: Annotated[
        Optional[PreferenceAlgContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:preference-alg'
        ),
    ] = None
    manual_alg: Annotated[
        Optional[ManualAlgContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:manual-alg'
        ),
    ] = None


class ApplicationListEntry(BaseModel):
    """
    List of all applications managed by the application manager
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-app-mgmt:name')]
    """
    Unique name of this application instance
    """
    pid: Annotated[
        Optional[int], Field(alias='srl_nokia-app-mgmt:pid', ge=0, le=4294967295)
    ] = None
    """
    Process ID of this application instance
    """
    state: Annotated[
        Optional[EnumerationEnum81], Field(alias='srl_nokia-app-mgmt:state')
    ] = None
    """
    Current state of this application instance
    """
    synchronization_state: Annotated[
        Optional[EnumerationEnum82],
        Field(alias='srl_nokia-app-mgmt:synchronization-state'),
    ] = None
    """
    Indicates if this application is available for a warm or hot restart

    An application supports either hot or warm restarts, not both.
    """
    last_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-app-mgmt:last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time the application instance last changed state
    """
    last_start_type: Annotated[
        Optional[EnumerationEnum83], Field(alias='srl_nokia-app-mgmt:last-start-type')
    ] = None
    """
    Indicates the type of the most recent start or restart of this application instance
    """
    supported_restart_types: Annotated[
        Optional[List[EnumerationEnum83]],
        Field(alias='srl_nokia-app-mgmt:supported-restart-types'),
    ] = []
    """
    Indicates the supported restart types for this application
    """
    author: Annotated[Optional[str], Field(alias='srl_nokia-app-mgmt:author')] = None
    """
    The author of the application
    """
    failure_threshold: Annotated[
        Optional[int], Field(alias='srl_nokia-app-mgmt:failure-threshold', ge=0, le=255)
    ] = None
    """
    How many restarts within 'failure-window' are required to trigger the failure action

    Setting this value to 0 will result in no action taking place on application restarts
    """
    failure_window: Annotated[
        Optional[int],
        Field(alias='srl_nokia-app-mgmt:failure-window', ge=300, le=86400),
    ] = None
    """
    Sliding window in seconds, over which to count restarts towards failure-threshold
    """
    failure_action: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-app-mgmt:failure-action',
            pattern='^(?=^(reboot|wait=(forever|\\d*))$).*$',
        ),
    ] = None
    """
    The action taken after 'failure-threshold' failures within 'failure-window'

    This action can be to reboot the system, wait forever, or wait for a predefined number of seconds
    """
    path: Annotated[Optional[str], Field(alias='srl_nokia-app-mgmt:path')] = None
    """
    The directory where the application can be found
    """
    launch_command: Annotated[
        Optional[str], Field(alias='srl_nokia-app-mgmt:launch-command')
    ] = None
    """
    The command used to launch the application
    """
    search_command: Annotated[
        Optional[str], Field(alias='srl_nokia-app-mgmt:search-command')
    ] = None
    """
    The command used to search for the applications liveness
    """
    version: Annotated[Optional[str], Field(alias='srl_nokia-app-mgmt:version')] = None
    """
    The version of the application
    """
    restricted_operations: Annotated[
        Optional[List[EnumerationEnum84]],
        Field(alias='srl_nokia-app-mgmt:restricted-operations'),
    ] = []
    """
    The operations that may not be manually performed on this application
    """
    oom_score_adj: Annotated[
        Optional[int],
        Field(alias='srl_nokia-app-mgmt:oom-score-adj', ge=-2147483648, le=2147483647),
    ] = None
    """
    OOM score adj value set for this application
    """
    cgroup: Annotated[Optional[str], Field(alias='srl_nokia-app-mgmt:cgroup')] = None
    """
    Cgroup in with this application is started
    """
    statistics: Annotated[
        Optional[StatisticsContainer13], Field(alias='srl_nokia-app-mgmt:statistics')
    ] = None
    yang: Annotated[Optional[YangContainer], Field(alias='srl_nokia-app-mgmt:yang')] = (
        None
    )


class AuthorizedKeysContainer(BaseModel):
    """
    State relating to the Authorized Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedKeysContainer2(BaseModel):
    """
    State relating to the Authorized Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedKeysContainer3(BaseModel):
    """
    State relating to the Authorized Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedPrincipalsContainer(BaseModel):
    """
    State relating to the Authorized Principals provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedPrincipalsContainer2(BaseModel):
    """
    State relating to the Authorized Principals provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedPrincipalsContainer3(BaseModel):
    """
    State relating to the Authorized Principals provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-aaa:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthzPolicyContainer(BaseModel):
    """
    Information relating to the active gRPC authorization policy

    This policy is provided by the gNSI gRPC service, and can be changed using the gNSI.Authz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-gnsi-authz:version')] = (
        None
    )
    """
    The version string as provided by the gNSI client at the time of uploading the policy

    The maps to the version field within a UploadRequest message in the Authz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-authz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    This maps to the created_on field within a UploadRequest message in the Authz protobuf.
    """
    policy: Annotated[Optional[str], Field(alias='srl_nokia-gnsi-authz:policy')] = None
    """
    The policy definition

    This JSON string contains the full gRPC authorization rules conforming to the gRPC authorization policy schema.

    This maps to the policy field within a UploadRequest message in the Authz protobuf.
    """
    counters: Annotated[
        Optional[CountersContainer2], Field(alias='srl_nokia-gnsi-authz:counters')
    ] = None


class AutobootContainer(BaseModel):
    """
    Top-level container for configuration and state data related to autobooting the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-boot:admin-state')
    ] = None
    """
    Administratively enable or disable autoboot functionality
    """
    oper_state: Annotated[Optional[str], Field(alias='srl_nokia-boot:oper-state')] = (
        None
    )
    """
    The current operational status of the autoboot process
    """
    timeout: Annotated[
        Optional[int], Field(alias='srl_nokia-boot:timeout', ge=200, le=3600)
    ] = None
    """
    Sets the timeout for each attempt to autoboot
    """
    attempts: Annotated[
        Optional[int], Field(alias='srl_nokia-boot:attempts', ge=1, le=10)
    ] = None
    """
    Sets the amount of executions to try autoboot, before rebooting the system
    """
    interface: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-boot:interface')
    ] = ['mgmt0']
    """
    Sets the interface(s) to use for autoboot functionality
    """
    client_id: Annotated[
        Optional[EnumerationEnum98], Field(alias='srl_nokia-boot:client-id')
    ] = None
    """
    The client ID to use on outgoing DHCP requests
    """
    mode: Annotated[
        Optional[List[EnumerationEnum99]], Field(alias='srl_nokia-boot:mode')
    ] = []


class AutodiscoveryPerEthernetSegmentRoutesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    route_distinguisher: Annotated[
        Optional[
            Union[
                RouteDistinguisherType0Type,
                RouteDistinguisherType1Type,
                RouteDistinguisherType2Type,
                RouteDistinguisherType2bType,
            ]
        ],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:route-distinguisher'
        ),
    ] = None
    """
    The route distinguisher encoded in the NLRI
    """
    esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
        ),
    ] = None
    """
    The Ethernet Segment Identifier encoded in the NLRI
    """
    ethernet_tag_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-tag-id',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    The 32-bit Ethernet Tag ID encoded in the NLRI. The Ethernet Tag ID identifies a broadcast domain
    """
    neighbor: Annotated[
        Optional[Union[Ipv4AddressWithZoneType, Ipv6AddressWithZoneType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:neighbor'
        ),
    ] = None
    """
    If the route was learned from a BGP neighbor, this is the IPv4 or IPv6 address of that neighbor
    """
    path_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:path-id',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    Path identifier of the BGP route
    """
    label: Annotated[
        Optional[LabelContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:label'
        ),
    ] = None
    complete_srv6_sid: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:complete-srv6-sid',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$',
        ),
    ] = None
    """
    The entire 128 bit srv6 segment identifier included in srv6 routes

    It shows the complete srv6 sid value including locator, function and argument, even if transposition is
    used and the function or argument is encoded in the label field.
    """
    attr_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:attr-id',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    Leaf reference to networkinstance/protocols/bgp/rib/attr-sets/attr-set/index.
    """


class BgpAutoDiscoveryContainer2(BaseModel):
    """
    Configuration and state related to LLDP BGP auto discovery on the interface
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-lldp:admin-state')
    ] = 'enable'
    """
    Enable or disable LLDP BGP auto discovery on this interface
    """
    peering_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-lldp:peering-address'),
    ] = []
    """
    List of IP addresses to be sent for BGP auto discovery

    Default values for this sub-TLV is to populate the addresses
    of the first subinterface of the interface the LLDPDU is being
    generated from, along with a unicast AFI/SAFI for IPv4 if an IPv4
    address exists, and/or IPv6 if an IPv6 address exists.

    If neither of these exist in the system, LLDP will not add the TLV
    to outgoing LLDPDUs, unless the peering-address is manually configured
    on a per-LLDP-port basis.
    """
    group_id: Annotated[
        Optional[int], Field(alias='srl_nokia-lldp:group-id', ge=0, le=4294967295)
    ] = None
    """
    A four byte integer to send on outgoing LLDPDUs

    This value can be used on the remote end to do peer group association.
    This sub-TLV is not sent by default.
    """


class BgpContainer(BaseModel):
    """
    Container for specifying the BGP members of the maintenance group
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry3]],
        Field(alias='srl_nokia-maintenance-mode:network-instance'),
    ] = None


class BgpContainer2(BaseModel):
    """
    Container for BGP policies used to achieve traffic draining
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    import_policy: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:import-policy',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    A reference to the pre-configured routing policy to apply as an additional/final import policy on BGP sessions in the maintenance group
    """
    export_policy: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:export-policy',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    A reference to the pre-configured routing policy to apply as an additional/final export policy on BGP sessions in the maintenance group
    """


class BlockListEntry(BaseModel):
    """
    Enter the block list instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    block_name: Annotated[
        str,
        Field(
            alias='srl_nokia-srv6:block-name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Micro-SID block name
    """
    prefix: Annotated[
        Optional[PrefixContainer], Field(alias='srl_nokia-srv6:prefix')
    ] = None
    static_function: Annotated[
        Optional[StaticFunctionContainer], Field(alias='srl_nokia-srv6:static-function')
    ] = None


class CacheListEntry(BaseModel):
    """
    Cache of the Monitoring Device.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Key of this list.
    """
    data_records: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:data-records', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of Data Records generated by this Cache.

    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    cacheDiscontinuityTime.
    """
    cache_type: Annotated[TimeoutCacheCase, Field(alias='srl_nokia-ipfix:cache-type')]
    exporting_process: Annotated[
        Optional[List[ExportingProcessLeafList]],
        Field(alias='srl_nokia-ipfix:exporting-process'),
    ] = []
    """
    Records are exported by all Exporting Processes
    in the list.
    """


class CertificateContainer(BaseModel):
    """
    State relating to the active certificate provided via Certz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-gnsi-certz:version')] = (
        None
    )
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-certz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CertificateContainer2(BaseModel):
    """
    State relating to the active certificate provided via Certz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-grpc:version')] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CertzContainer(BaseModel):
    """
    Information relating to the active certificate and bundle/s as provided via Certz

    State is provided by the gNSI Certz service, and can be changed using the gNSI.Certz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ssl_profile_id: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-certz:ssl-profile-id')
    ] = None
    """
    The ID of this gRPC server's SSL profile as used by the gNSI Certz service
    """
    certificate: Annotated[
        Optional[CertificateContainer], Field(alias='srl_nokia-gnsi-certz:certificate')
    ] = None
    trust_anchor: Annotated[
        Optional[TrustAnchorContainer], Field(alias='srl_nokia-gnsi-certz:trust-anchor')
    ] = None
    crl: Annotated[Optional[CrlContainer], Field(alias='srl_nokia-gnsi-certz:crl')] = (
        None
    )


class CertzContainer2(BaseModel):
    """
    Information relating to the active certificate and bundle/s as provided via Certz

    State is provided by the gNSI Certz service, and can be changed using the gNSI.Certz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ssl_profile_id: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:ssl-profile-id')
    ] = None
    """
    The ID of this gRPC server's SSL profile as used by the gNSI Certz service
    """
    certificate: Annotated[
        Optional[CertificateContainer2], Field(alias='srl_nokia-grpc:certificate')
    ] = None
    trust_anchor: Annotated[
        Optional[TrustAnchorContainer2], Field(alias='srl_nokia-grpc:trust-anchor')
    ] = None
    crl: Annotated[Optional[CrlContainer2], Field(alias='srl_nokia-grpc:crl')] = None


class CheckpointListEntry(BaseModel):
    """
    List of current checkpoints present in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[int, Field(alias='srl_nokia-configuration:id', ge=0, le=255)]
    """
    System generated ID for the checkpoint
    """
    name: Annotated[
        Optional[str],
        Field(alias='srl_nokia-configuration:name', pattern='^(?=^[^0-9].*$).*$'),
    ] = None
    """
    User provided name of the checkpoint
    """
    comment: Annotated[
        Optional[str], Field(alias='srl_nokia-configuration:comment')
    ] = None
    """
    User provided annotations associated with the checkpoint
    """
    created: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:created',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time this checkpoint was created
    """
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-configuration:version')
    ] = None
    """
    System version that the checkpoint was generated on
    """
    tag: Annotated[Optional[str], Field(alias='srl_nokia-configuration:tag')] = None
    """
    Full system version that the checkpoint was generated on
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Username that created this checkpoint
    """
    size: Annotated[
        Optional[int],
        Field(alias='srl_nokia-configuration:size', ge=0, le=18446744073709551615),
    ] = None
    """
    Size of the checkpoint configuration file
    """


class CliContainer2(BaseModel):
    """
    Top-level container for CLI services
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    environment: Annotated[
        Optional[EnvironmentContainer], Field(alias='srl_nokia-system-cli:environment')
    ] = None


class ClientListEntry(BaseModel):
    """
    List of active gRPC client sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[int, Field(alias='srl_nokia-grpc:id', ge=0, le=4294967295)]
    """
    System generated ID for for the client
    """
    type: Annotated[Optional[EnumerationEnum15], Field(alias='srl_nokia-grpc:type')] = (
        None
    )
    user: Annotated[Optional[str], Field(alias='srl_nokia-grpc:user')] = None
    """
    Authenticated username for the client
    """
    user_agent: Annotated[Optional[str], Field(alias='srl_nokia-grpc:user-agent')] = (
        None
    )
    """
    User agent used for the client
    """
    remote_host: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-grpc:remote-host'),
    ] = None
    """
    Remote host of the client
    """
    remote_port: Annotated[
        Optional[int], Field(alias='srl_nokia-grpc:remote-port', ge=0, le=65535)
    ] = None
    """
    Remote port of the client
    """
    election_id: Annotated[Optional[str], Field(alias='srl_nokia-grpc:election-id')] = (
        None
    )
    """
    Election ID of this client

    Provided only for services supporting an election ID
    """
    acctz_starting_point: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:acctz-starting-point',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time of the acctz accounting subscription starting point
    """
    rpc: Annotated[Optional[str], Field(alias='srl_nokia-grpc:rpc')] = None
    """
    The called package, service, and RPC

    For example gnmi.gNMI.Subscribe
    """
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time of the subscription creation
    """
    gnmi: Annotated[Optional[GnmiContainer2], Field(alias='srl_nokia-grpc:gnmi')] = None
    gribi: Annotated[Optional[GribiContainer], Field(alias='srl_nokia-grpc:gribi')] = (
        None
    )
    p4rt: Annotated[Optional[P4rtContainer], Field(alias='srl_nokia-grpc:p4rt')] = None


class CountersContainer3(BaseModel):
    """
    A collection of per-schema path counters collected by the gNSI.pathz module.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    path: Annotated[
        Optional[List[PathListEntry]], Field(alias='srl_nokia-gnsi-pathz:path')
    ] = None


class CredentialzContainer(BaseModel):
    """
    Information relating to the active host keys and certificates as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateHostParameters RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trusted_user_ca_keys: Annotated[
        Optional[TrustedUserCaKeysContainer],
        Field(alias='srl_nokia-gnsi-credentialz:trusted-user-ca-keys'),
    ] = None
    host_certificate: Annotated[
        Optional[HostCertificateContainer],
        Field(alias='srl_nokia-gnsi-credentialz:host-certificate'),
    ] = None
    host_key: Annotated[
        Optional[HostKeyContainer2], Field(alias='srl_nokia-gnsi-credentialz:host-key')
    ] = None


class CredentialzContainer2(BaseModel):
    """
    Information relating to the active user credentials as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateAccountCredentials RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    password: Annotated[
        Optional[PasswordContainer], Field(alias='srl_nokia-aaa:password')
    ] = None
    authorized_keys: Annotated[
        Optional[AuthorizedKeysContainer], Field(alias='srl_nokia-aaa:authorized-keys')
    ] = None
    authorized_principals: Annotated[
        Optional[AuthorizedPrincipalsContainer],
        Field(alias='srl_nokia-aaa:authorized-principals'),
    ] = None


class CredentialzContainer3(BaseModel):
    """
    Information relating to the active user credentials as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateAccountCredentials RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    password: Annotated[
        Optional[PasswordContainer2], Field(alias='srl_nokia-aaa:password')
    ] = None
    authorized_keys: Annotated[
        Optional[AuthorizedKeysContainer2], Field(alias='srl_nokia-aaa:authorized-keys')
    ] = None
    authorized_principals: Annotated[
        Optional[AuthorizedPrincipalsContainer2],
        Field(alias='srl_nokia-aaa:authorized-principals'),
    ] = None


class CredentialzContainer4(BaseModel):
    """
    Information relating to the active user credentials as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateAccountCredentials RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    password: Annotated[
        Optional[PasswordContainer3], Field(alias='srl_nokia-aaa:password')
    ] = None
    authorized_keys: Annotated[
        Optional[AuthorizedKeysContainer3], Field(alias='srl_nokia-aaa:authorized-keys')
    ] = None
    authorized_principals: Annotated[
        Optional[AuthorizedPrincipalsContainer3],
        Field(alias='srl_nokia-aaa:authorized-principals'),
    ] = None


class DatapathContainer(BaseModel):
    """
    Context for system wide forwarding options
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    forwarding_mode: Annotated[
        Optional[EnumerationEnum27],
        Field(alias='srl_nokia-system-datapath:forwarding-mode'),
    ] = 'store-and-forward'
    """
    The forwarding mode for Ethernet frames received on all eligible ports of the system

    In store-and-forward mode, the forwarding of an Ethernet frame received on a particular port must wait until the entire Ethernet frame has been received, including the trailing 4-byte CRC; if the CRC is valid the packet is forwarded to the egress port based on the L2/L3 lookup result but if the CRC is invalid the frame is discarded and the in-error-packets counter is incremented.

    In cut-through mode, the forwarding ASIC does the L2/L3 forwarding lookup as soon as it has read the necessary packet headers. If the target egress queue of the egress port is not congested the bytes of the received frame are transmitted across the switch fabric as they are received. The fully intact frame is transmitted from the egress port as soon as all the bytes have been received.
    """
    icmp: Annotated[
        Optional[IcmpContainer], Field(alias='srl_nokia-system-datapath:icmp')
    ] = None
    icmp6: Annotated[
        Optional[Icmp6Container], Field(alias='srl_nokia-system-datapath:icmp6')
    ] = None
    secondary_default_lookup: Annotated[
        Optional[SecondaryDefaultLookupContainer],
        Field(alias='srl_nokia-system-datapath:secondary-default-lookup'),
    ] = None


class DesignatedForwarderCandidateListEntry(BaseModel):
    """
    designated forwarder candidates for this evi
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    address: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:address'
        ),
    ]
    """
    An IPv4 or IPv6 address with no prefix specified.
    """
    add_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:add-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time when the designated-forwarder-candidate was added to the designated forwarder candidate list for this evi
    """
    designated_forwarder: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder'
        ),
    ] = False
    """
    Indicates if this designated-forwarder-candidate is the designated-forwarder.
    """


class DfElectionContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    timers: Annotated[
        Optional[TimersContainer2],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:timers'
        ),
    ] = None
    interface_standby_signaling_on_non_df: Annotated[
        Optional[InterfaceStandbySignalingOnNonDfContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:interface-standby-signaling-on-non-df'
        ),
    ] = None
    algorithm: Annotated[
        Optional[AlgorithmContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:algorithm'
        ),
    ] = None


class EthernetSegmentRoutesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    route_distinguisher: Annotated[
        Optional[
            Union[
                RouteDistinguisherType0Type,
                RouteDistinguisherType1Type,
                RouteDistinguisherType2Type,
                RouteDistinguisherType2bType,
            ]
        ],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:route-distinguisher'
        ),
    ] = None
    """
    The route distinguisher encoded in the NLRI
    """
    esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
        ),
    ] = None
    """
    The Ethernet Segment Identifier
    """
    originating_router: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:originating-router'
        ),
    ] = None
    """
    The IPv4 or IPv6 address of the originating router
    """
    neighbor: Annotated[
        Optional[Union[Ipv4AddressWithZoneType, Ipv6AddressWithZoneType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:neighbor'
        ),
    ] = None
    """
    If the route was learned from a BGP neighbor, this is the IPv4 or IPv6 address of that neighbor
    """
    path_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:path-id',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    Path identifier of the BGP route
    """
    attr_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:attr-id',
            ge=0,
            le=18446744073709551615,
        ),
    ] = None
    """
    Leaf reference to networkinstance/protocols/bgp/rib/attr-sets/attr-set/index
    """


class EthernetSegmentContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    originating_ip: Annotated[
        Optional[Union[EnumerationEnum64, Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:originating-ip'
        ),
    ] = 'use-system-ipv4-address'
    """
    The originating ip-address with which the Ethernet Segment route will be advertised in this evpn instance
    """


class FacilityListEntry(BaseModel):
    """
    List of facilities to source messages from
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    facility_name: Annotated[
        EnumerationEnum23, Field(alias='srl_nokia-logging:facility-name')
    ]
    """
    Name of a Linux syslog facility
    """
    priority: Annotated[
        Optional[PriorityContainer], Field(alias='srl_nokia-logging:priority')
    ] = None


class FacilityListEntry2(BaseModel):
    """
    List of facilities to source messages from
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    facility_name: Annotated[
        EnumerationEnum23, Field(alias='srl_nokia-logging:facility-name')
    ]
    """
    Name of a Linux syslog facility
    """
    priority: Annotated[
        Optional[PriorityContainer3], Field(alias='srl_nokia-logging:priority')
    ] = None


class FacilityListEntry3(BaseModel):
    """
    List of facilities to source messages from
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    facility_name: Annotated[
        EnumerationEnum23, Field(alias='srl_nokia-logging:facility-name')
    ]
    """
    Name of a Linux syslog facility
    """
    priority: Annotated[
        Optional[PriorityContainer4], Field(alias='srl_nokia-logging:priority')
    ] = None


class FacilityListEntry4(BaseModel):
    """
    List of facilities to source messages from
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    facility_name: Annotated[
        EnumerationEnum23, Field(alias='srl_nokia-logging:facility-name')
    ]
    """
    Name of a Linux syslog facility
    """
    priority: Annotated[
        Optional[PriorityContainer6], Field(alias='srl_nokia-logging:priority')
    ] = None


class FacilityListEntry5(BaseModel):
    """
    List of facilities to source messages from
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    facility_name: Annotated[
        EnumerationEnum23, Field(alias='srl_nokia-logging:facility-name')
    ]
    """
    Name of a Linux syslog facility
    """
    priority: Annotated[
        Optional[PriorityContainer8], Field(alias='srl_nokia-logging:priority')
    ] = None


class FileListEntry(BaseModel):
    """
    Log files maintained on disk, persistent across system reboots

    When a maximum file size is reached, the file is renamed and a maximum
    rotate number of them are kept.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    file_name: Annotated[
        str,
        Field(
            alias='srl_nokia-logging:file-name',
            pattern='^(?=^([^./][^/]*)|(\\.[^\\./]+)|(\\.\\.[^/])+$).*$',
        ),
    ]
    """
    Base name of the file(s) to be stored on disk
    """
    directory: Annotated[
        Optional[str],
        Field(alias='srl_nokia-logging:directory', pattern='^(?=^/(.)*$).*$'),
    ] = '/var/log/srlinux/file'
    """
    Fully qualified path of a directory where the log file(s) shall be maintained
    """
    format: Annotated[
        Optional[Union[str, EnumerationEnum22]], Field(alias='srl_nokia-logging:format')
    ] = 'RSYSLOG_FileFormat'
    """
    Text format of syslog messages to a local output (buffer, file or console), in legacy rsyslog $template style or one of the predefined templates

    The default presents a date timestamp according to rfc3339.
    The predefined templates are the ones supported by rsyslogd.
    """
    rotate: Annotated[
        Optional[int], Field(alias='srl_nokia-logging:rotate', ge=0, le=65535)
    ] = 4
    """
    Number of files to keep in rotation when a maximum file size is reached
    """
    rotations: Annotated[
        Optional[int],
        Field(alias='srl_nokia-logging:rotations', ge=0, le=18446744073709551615),
    ] = 0
    """
    Number of file rotations occurred
    """
    size: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-logging:size',
            pattern='^(?=^[1-9][0-9]{0,15}(K|M|G){0,1}$).*$',
        ),
    ] = '10M'
    """
    Number of bytes an individual output file cannot exceed

    The field allows the 'K, M, or G' suffixes as shorthand.
    When reaching that size, a rotation happens and subsequent data is stored
    in a new file with the same base name.
    """
    facility: Annotated[
        Optional[List[FacilityListEntry4]], Field(alias='srl_nokia-logging:facility')
    ] = None
    subsystem: Annotated[
        Optional[List[SubsystemListEntry3]], Field(alias='srl_nokia-logging:subsystem')
    ] = None
    filter: Annotated[
        Optional[List[FilterLeafList3]], Field(alias='srl_nokia-logging:filter')
    ] = []
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class FilterListEntry(BaseModel):
    """
    Describes a set of critieria that captured messages are required to fulfill
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    filter_name: Annotated[
        str,
        Field(
            alias='srl_nokia-logging:filter-name',
            pattern='^(?=^([0-9a-zA-Z\\-_.@!%^*()\\[\\]{}|\\\\/<>,;])+$).*$',
        ),
    ]
    """
    Name of the filter
    """
    prefix: Annotated[Optional[str], Field(alias='srl_nokia-logging:prefix')] = None
    """
    Text to be present at the beginning of the MSG property of a message
    This is a fast lookup.
    """
    not_prefix: Annotated[
        Optional[str], Field(alias='srl_nokia-logging:not-prefix')
    ] = None
    """
    Text to be not present at the beginning of the MSG property of a message
    This is a fast lookup.
    """
    contains: Annotated[Optional[str], Field(alias='srl_nokia-logging:contains')] = None
    """
    Text to find in the MSG property of messages to capture from the stream
    This is slower than prefix.
    """
    not_contains: Annotated[
        Optional[str], Field(alias='srl_nokia-logging:not-contains')
    ] = None
    """
    Text to not find in the MSG property of messages to capture from the stream
    This is slower than prefix.
    """
    tag: Annotated[Optional[str], Field(alias='srl_nokia-logging:tag')] = None
    """
    Text to be searched in the SYSLOGTAG property of messages
    Usually a program name or part of it.
    """
    regex: Annotated[Optional[str], Field(alias='srl_nokia-logging:regex')] = None
    """
    Extended regular expression to search in the MSG property of messages
    """
    not_regex: Annotated[Optional[str], Field(alias='srl_nokia-logging:not-regex')] = (
        None
    )
    """
    Extended regular expression to not have in the MSG property of messages
    """
    facility: Annotated[
        Optional[List[FacilityListEntry2]], Field(alias='srl_nokia-logging:facility')
    ] = None


class Fips140Container(BaseModel):
    """
    Boot up the router in fips-provider mode

    In fips-provider mode only fips approved algorithms are allowed.
    In addition for fip-provider mode to take effect a reboot is of the router is needed.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-boot:admin-state')
    ] = 'disable'
    """
    This leaf contains the configured, desired state of the fips-provider.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-boot:oper-state')
    ] = None
    """
    This leaf contains the operational state of fips-provider.
    """
    oper_down_reason: Annotated[
        Optional[EnumerationEnum97], Field(alias='srl_nokia-boot:oper-down-reason')
    ] = None
    """
    The reason for not enabling fips operational down
    """


class FreqClockContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ql_input_threshold: Annotated[
        Optional[EnumerationEnum104], Field(alias='srl_nokia-sync:ql-input-threshold')
    ] = 'unused'
    """
    This command configures the minimum acceptable QL value
    Frequency references with lower QL will not be considered for selection
    by the system timing module.
    Options: unused, prs, stu, st2, tnc, st3e, st3, prc, ssua, ssub, sec, eec1, eec2
    """
    network_type: Annotated[
        Optional[EnumerationEnum108], Field(alias='srl_nokia-sync:network-type')
    ] = 'sonet'
    """
    Configures SyncE for SSM code-type as SONET or SDH mode
    sdh specifies the values corresponding to ITU-T G.781 Option 1 compliant networks.
    sonet specifies the values corresponding to ITU-T G.781 Option 2 compliant networks.
    """
    ql_selection: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:ql-selection')
    ] = False
    """
    Configures if frequency reference selection takes the QL (Quality Level) into account
    When enabled, the selection of system timing reference and BITS output timing reference
    takes into account quality level. Quality level is conveyed via the SSM or forced using
    the ql-override command..
    """
    wait_to_restore: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:wait-to-restore', ge=0, le=12)
    ] = 5
    """
    This command configures the time for the Wait to Restore timer
    A previously failed input reference must be valid for the time specified before it is
    used for the clock input reference.
    """
    revert: Annotated[Optional[bool], Field(alias='srl_nokia-sync:revert')] = False
    """
    This command configures if the frequency clock is in revertive mode
    In revertive mode, when a failed reference becomes operational, the system will
    automatically switch to the recovered reference if it is of higher priority and/or QL.
    When the mode is non-revertive, a failed clock source is not automatically selected.
    """
    active_reference: Annotated[
        Optional[EnumerationEnum109], Field(alias='srl_nokia-sync:active-reference')
    ] = None
    """
    Indicates the current selected reference

    This will be an instance-number; or internal for the case of holdover or freerun.
    """
    freq_offset: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:freq-offset',
            ge=-9223372036854776.0,
            le=9223372036854776.0,
        ),
    ] = None
    """
    The frequency offset between the central frequency clock and the selected reference in ppb
    """
    freq_clock_state: Annotated[
        Optional[EnumerationEnum110], Field(alias='srl_nokia-sync:freq-clock-state')
    ] = None
    """
    Shows the frequency clock mode state
    """
    system_ql_value: Annotated[
        Optional[EnumerationEnum105], Field(alias='srl_nokia-sync:system-ql-value')
    ] = None
    """
    System QL value based on the reference selected
    """


class FreqRecoveryEngineContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    recovery_state: Annotated[
        Optional[EnumerationEnum116], Field(alias='srl_nokia-sync:recovery-state')
    ] = None
    """
    Specifies the current state of the time recovery engine in the PTP clock
    """
    state_last_changed: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:state-last-changed',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Specifies the last occurrence of a ptp state change for the time recovery engine
    """
    frequency_offset: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:frequency-offset',
            ge=-9223372036854776.0,
            le=9223372036854776.0,
        ),
    ] = None
    """
    The frequency offset of the recovered PTP clock

     Positive values indicate that the recovered clock is faster than nominal,
     negative values indicate that the recovered clock is slower than nominal.
    """
    last_adjustment_timestamp: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:last-adjustment-timestamp',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when last-adjustment was last calculated
    """
    statistics: Annotated[
        Optional[StatisticsContainer20], Field(alias='srl_nokia-sync:statistics')
    ] = None


class FullSegmentContainer(BaseModel):
    """
    Enter the context to configure the full-segment locator
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    block_length: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:block-length', ge=0, le=96)
    ] = 0
    """
    SRv6 locator block address length
    """
    function_length: Annotated[
        int, Field(alias='srl_nokia-srv6:function-length', ge=16, le=16)
    ]
    """
    Function length
    """
    argument_length: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:argument-length', ge=0, le=16)
    ] = 0
    """
    Argument length
    """
    algorithm: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:algorithm', ge=0, le=255)
    ] = 0
    """
    IGP flexible algorithm ID
    """
    prefix: Annotated[
        Optional[PrefixContainer2], Field(alias='srl_nokia-srv6:prefix')
    ] = None
    static_function: Annotated[
        Optional[StaticFunctionContainer2],
        Field(alias='srl_nokia-srv6:static-function'),
    ] = None


class GnssContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    constellation: Annotated[
        Optional[ConstellationContainer], Field(alias='srl_nokia-sync:constellation')
    ] = None
    receiver: Annotated[
        Optional[List[ReceiverListEntry]], Field(alias='srl_nokia-sync:receiver')
    ] = None


class HostListEntry(BaseModel):
    """
    host name for static ip allocations
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac: Annotated[
        str,
        Field(
            alias='srl_nokia-dhcp-server:mac',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ]
    """
    The mac-address type represents an IEEE 802 MAC address.
    The canonical representation uses lowercase characters.

    In the value set and its semantics, this type is equivalent
    to the MacAddress textual convention of the SMIv2.
    """
    ip_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:ip-address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))$).*$',
        ),
    ] = None
    """
    An IPv4 prefix with host bits.
    """
    options: Annotated[
        Optional[OptionsContainer2], Field(alias='srl_nokia-dhcp-server:options')
    ] = None


class HostListEntry2(BaseModel):
    """
    host name for static ip allocations
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac: Annotated[
        str,
        Field(
            alias='srl_nokia-dhcp-server:mac',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ]
    """
    The mac-address type represents an IEEE 802 MAC address.
    The canonical representation uses lowercase characters.

    In the value set and its semantics, this type is equivalent
    to the MacAddress textual convention of the SMIv2.
    """
    ip_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:ip-address',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))$).*$',
        ),
    ] = None
    """
    An IPv6 prefix with host bits.
    """
    options: Annotated[
        Optional[OptionsContainer5], Field(alias='srl_nokia-dhcp-server:options')
    ] = None


class HttpContainer(BaseModel):
    """
    Top-level container for the JSON RPC HTTP server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-json-rpc:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable the HTTP JSON RPC server
    This requires the JSON RPC server to be globally enabled
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-json-rpc:oper-state')
    ] = None
    """
    Details if the JSON RPC server is operationally available
    """
    source_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-json-rpc:source-address'),
    ] = ['::']
    """
    List of IP addresses the JSON RPC server will listen on within the network instance
    """
    use_authentication: Annotated[
        Optional[bool], Field(alias='srl_nokia-json-rpc:use-authentication')
    ] = True
    """
    Enable or disable the use of username/password authentication for every JSON RPC request
    """
    session_limit: Annotated[
        Optional[int], Field(alias='srl_nokia-json-rpc:session-limit', ge=1, le=100)
    ] = None
    """
    The number of concurrent requests the server will allow
    If a request comes in while this limit is reached, the request will block until another request is finished.
    """
    port: Annotated[
        Optional[int], Field(alias='srl_nokia-json-rpc:port', ge=0, le=65535)
    ] = 80
    """
    The port the HTTP JSON RPC server will listen on for incoming connections
    """


class HttpsContainer(BaseModel):
    """
    Top-level container for the JSON-RPC HTTPS server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-json-rpc:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable the HTTPS JSON RPC server
    This requires the JSON RPC server to be globally enabled
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-json-rpc:oper-state')
    ] = None
    """
    Details if the JSON RPC server is operationally available
    """
    source_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-json-rpc:source-address'),
    ] = ['::']
    """
    List of IP addresses the JSON RPC server will listen on within the network instance
    """
    use_authentication: Annotated[
        Optional[bool], Field(alias='srl_nokia-json-rpc:use-authentication')
    ] = True
    """
    Enable or disable the use of username/password authentication for every JSON RPC request
    """
    session_limit: Annotated[
        Optional[int], Field(alias='srl_nokia-json-rpc:session-limit', ge=1, le=100)
    ] = None
    """
    The number of concurrent requests the server will allow
    If a request comes in while this limit is reached, the request will block until another request is finished.
    """
    port: Annotated[
        Optional[int], Field(alias='srl_nokia-json-rpc:port', ge=0, le=65535)
    ] = 443
    """
    Port the HTTPS JSON RPC server will listen on for incoming connections
    """
    tls_profile: Annotated[
        str,
        Field(
            alias='srl_nokia-json-rpc:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Reference to the TLS profile to use on the HTTP JSON RPC server
    """


class InstanceListEntry(BaseModel):
    """
    List of all event handler instances

    An event handler instance consists of a set of paths monitored for changes and a Python script to execute if changes occur.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-event-handler:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    User-defined name for this event handler instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-event-handler:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable this event handler instance
    """
    paths: Annotated[
        Optional[List[PathsLeafList]], Field(alias='srl_nokia-event-handler:paths')
    ] = []
    """
    List of valid YANG paths in CLI notation to monitor for changes

    If any events are received on any of the provided paths, the configured script will be executed.

    This path may include keys, wildcards, ranges, and other management server supported constructs.

    E.g.
        "interface * oper-state"
        "acl ipv4-filter foo* description"
    """
    options: Annotated[
        Optional[OptionsContainer6], Field(alias='srl_nokia-event-handler:options')
    ] = None
    upython_script: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:upython-script',
            pattern='^(?=^([^./][^/]*)|(\\.[^\\./]+)|(\\.\\.[^/])+$).*$',
        ),
    ] = None
    """
    File name of a MicroPython script, including .py suffix

    This script should already exist in /etc/opt/srlinux/eventmgr or /opt/srlinux/eventmgr directories.
    Explicit paths outside of these two directories are not permitted.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-event-handler:oper-state')
    ] = None
    """
    Details if this event handler instance is operationally available
    """
    last_execution: Annotated[
        Optional[LastExecutionContainer],
        Field(alias='srl_nokia-event-handler:last-execution'),
    ] = None
    last_errored_execution: Annotated[
        Optional[LastErroredExecutionContainer],
        Field(alias='srl_nokia-event-handler:last-errored-execution'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer17],
        Field(alias='srl_nokia-event-handler:statistics'),
    ] = None


class InterfaceRefContainer(BaseModel):
    """
    Reference to an interface
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:interface')
    ] = None
    """
    Reference to a base interface
    """


class InterfaceCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[Optional[str], Field(alias='srl_nokia-sync:interface')] = None
    """
    The name of the interface

    Valid options are:
    irb<N>, N=0..255
    lif-<lif_name>
    enp<bus>s<dev>f<fn>, bus=0..255, dev=0..31, fn=0..7
    vhn-<vhn_name>
    lag<N>, N=1..1000 [note1]
    lo<N>, N=0..255
    mgmt0
    mgmt0-standby
    mgmtA
    mgmtB
    ethernet-<slot>/<port>
    ethernet-<slot>/<connector>/<port>
    ethernet-<slot>/m<mda>/<port>
    ethernet-<slot>/m<mda>/<connector>/<port>
    system0
    sync0-a
    sync0-b

    <lif_name>=Linux interface name
    <vhn_name>=vhost interface name
    <slot>=slot number {1,2,3,..}
    <mda>=mda id {1,2,3,..}
    <connector>=connector id {1,2,3,..}
    <port>=port id {1,2,3,..}

    [note1] The maximum number of LAGs per platform is as follows:
     D1: 32 (N must be 1..32)
     D2-D3: 128 (N must be 1..1000)
     D4-D5: 64 (N must be 1..64)
     H2-H3: 127 (N must be 1..127)
     H4-32D: 127 (N must be 1..127)
     H4: 255 (N must be 1..255)
     H5-32D: 127 (N must be 1..127)
     H5-64D: 127 (N must be 1..127)
     H5-64O: 127 (N must be 1..127)
     IXR: 512 (N must be 1..512)
     SXR-1d-32D: 128 (N must be 1..128)
     SXR-1x-44S: 128 (N must be 1..128)
     vSRL: 8 (N must be 1..8)
     A1: 10 (N must be 1..10)
     IXR-X1b: 512 (N must be 1..512)
     IXR-X3b: 512 (N must be 1..512)
     SSE-T8164: 127 (N must be 1..127)
    """


class IpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ] = None
    """
    Network instance containing the IP address
    """
    ip_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-sync:ip-address'),
    ] = None
    """
    IP address for the PTP peer
    """


class KeyListEntry(BaseModel):
    """
    List of keys in the keychain
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    index: Annotated[int, Field(alias='srl_nokia-keychains:index', ge=0, le=255)]
    """
    Each key in a keychain requires a unique identifier, the index value specifies this identifier
    """
    algorithm: Annotated[
        Optional[EnumerationEnum48], Field(alias='srl_nokia-keychains:algorithm')
    ] = None
    """
    The cryptographic algorithm used with the keying material to secure the messages
    """
    authentication_key: Annotated[
        Optional[str], Field(alias='srl_nokia-keychains:authentication-key')
    ] = None
    """
    The secret key to use for authentication
    """
    macsec: Annotated[
        Optional[MacsecContainer], Field(alias='srl_nokia-keychains:macsec')
    ] = None
    send_lifetime: Annotated[
        Optional[SendLifetimeContainer],
        Field(alias='srl_nokia-keychains:send-lifetime'),
    ] = None
    receive_lifetime: Annotated[
        Optional[ReceiveLifetimeContainer],
        Field(alias='srl_nokia-keychains:receive-lifetime'),
    ] = None


class KeychainListEntry(BaseModel):
    """
    List of system keychains
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-keychains:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    The user configured name for the keychain
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-keychains:admin-state')
    ] = 'disable'
    """
    When set to disable, the keychain is inactive

    When a protocol refers to a keychain that is inactive, no authentication data is added to the outbound messages and/or all inbound messages with authentication data are dropped, depending on the context.

    A keychain is operationally disabled in a particular direction (send/receive) if:
    - the keychain is administratively disabled
    - no keys are configured
    - all of the keys are administratively disabled
    - all of the  keys are inactive because their start-times are in the future
    - all of the keys are inactive because their end-times (plus tolerance) are in the past (applies only to receive direction)
    """
    description: Annotated[
        Optional[str],
        Field(alias='srl_nokia-keychains:description', max_length=255, min_length=1),
    ] = None
    """
    The user configured description for the keychain
    """
    tolerance: Annotated[
        Optional[int], Field(alias='srl_nokia-keychains:tolerance', ge=0, le=4294967295)
    ] = 0
    """
    Tolerance for receive keys

    If tolerance is Z then all receive keys remain valid up to the configured/applicable end-time plus an additional Z seconds.
    """
    type: Annotated[
        Optional[EnumerationEnum46], Field(alias='srl_nokia-keychains:type')
    ] = None
    """
    Specifies the intended use of the keychain

    The type constrains the set of crypto algorithms that are available to use with each key in the keychain. It is also used to ensure that this keychain is only used by protocols for which it is intended.
    """
    usable: Annotated[Optional[bool], Field(alias='srl_nokia-keychains:usable')] = None
    """
    The value of this object indicates if the keychain is usable for authentication
    """
    expired: Annotated[Optional[bool], Field(alias='srl_nokia-keychains:expired')] = (
        None
    )
    """
    The value of this object indicates whether the keychain is expired

    Expired can mean past end-time or prior to start-time.
    """
    active_key_for_send: Annotated[
        Optional[Union[EnumerationEnum47, IndexLeaf4]],
        Field(alias='srl_nokia-keychains:active-key-for-send'),
    ] = None
    """
    Provides the key index of the currently active Keychain key
    """
    key: Annotated[
        Optional[List[KeyListEntry]], Field(alias='srl_nokia-keychains:key')
    ] = None


class L2cpStatisticsContainer(BaseModel):
    """
    Container for Layer-2 Control Plane protocol statistics.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_in_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level total incoming L2CP frames.

    Cumulative of all Ethernet interfaces including the tunneled, discarded and copy-to-cpu
    L2CP frames. L2CP frames are identified by a destination MAC value of 01:80:c2:00:00:0X
    or 01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    total_in_discarded_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-discarded-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming L2CP discarded frames.

    Cumulative of all Ethernet interfaces including all the discarded L2CP frames. L2CP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0X or
    01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    total_in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming L2CP tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled L2CP frames. L2CP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0X or
    01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    total_in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    System level incoming L2CP copy-to-cpu frames.

    Cumulative of all Ethernet interfaces including all the L2CP frames that are copied
    to CPU. L2CP frames are identified by a destination MAC value of 01:80:c2:00:00:0X or
    01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the last time the L2CP counters were cleared.
    """
    lldp: Annotated[
        Optional[LldpContainer2], Field(alias='srl_nokia-interfaces-l2cp:lldp')
    ] = None
    lacp: Annotated[
        Optional[LacpContainer2], Field(alias='srl_nokia-interfaces-l2cp:lacp')
    ] = None
    xstp: Annotated[
        Optional[XstpContainer], Field(alias='srl_nokia-interfaces-l2cp:xstp')
    ] = None
    ptp: Annotated[
        Optional[PtpContainer], Field(alias='srl_nokia-interfaces-l2cp:ptp')
    ] = None
    esmc: Annotated[
        Optional[EsmcContainer], Field(alias='srl_nokia-interfaces-l2cp:esmc')
    ] = None
    elmi: Annotated[
        Optional[ElmiContainer], Field(alias='srl_nokia-interfaces-l2cp:elmi')
    ] = None
    efm_oam: Annotated[
        Optional[EfmOamContainer], Field(alias='srl_nokia-interfaces-l2cp:efm-oam')
    ] = None


class L2cpTransparencyContainer(BaseModel):
    """
    Enclosing container for system level Layer-2 Control Protocol transparency.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    l2cp_statistics: Annotated[
        Optional[L2cpStatisticsContainer],
        Field(alias='srl_nokia-interfaces-l2cp:l2cp-statistics'),
    ] = None


class LabelRangesContainer(BaseModel):
    """
    Container for managing MPLS label blocks
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    static: Annotated[
        Optional[List[StaticListEntry]],
        Field(alias='srl_nokia-mpls-label-management:static'),
    ] = None
    dynamic: Annotated[
        Optional[List[DynamicListEntry]],
        Field(alias='srl_nokia-mpls-label-management:dynamic'),
    ] = None


class Layer3NextHopCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    next_hop: Annotated[
        Optional[List[NextHopListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:next-hop'
        ),
    ] = None


class LinuxadminUserContainer(BaseModel):
    """
    Enclosing container for linuxadmin user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[Optional[str], Field(alias='srl_nokia-aaa:username')] = (
        'linuxadmin'
    )
    """
    Assigned username for linuxadmin user
    """
    password: Annotated[Optional[str], Field(alias='srl_nokia-aaa:password')] = (
        '$y$j9T$l/vKPXdvWQKKPH8qPzbLs0$Hz98mmTg.j87QMZlTqY2ieGWa3Ed7kzHkp5z6kROEy4'
    )
    """
    The linuxadmin password, supplied either as cleartext or as a hashed value

    If provided as cleartext, the system will hash the value on input, storing only the hashed value.
    If provided as a hashed value, the value should include any '$' characters, for example '$6$c66a15569d3f5952$kA2WPt9iqR5uMbaCUBNxsjKyXROQFdJtV1HX0CFY9wk7F326/yB3h.dERX9cH7YpeJ1N872hjzTb2tlaZFwwg0'.
    """
    ssh_principals: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-principals')
    ] = []
    """
    List of principals to associate with this user

    If any of the principals in the list are matched in a SSH client's certificate, and that clients username matches this user, and the certificate is verified, the client will authenticate.
    """
    ssh_key: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-key')] = []
    """
    SSH public key(s) for the user

    If defined, the user may login to the system over SSH with this key. This should use the SSH public authorized key format.
    """
    credentialz: Annotated[
        Optional[CredentialzContainer3], Field(alias='srl_nokia-aaa:credentialz')
    ] = None


class LldpMedContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    med_fast_transmit_interval: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:med-fast-transmit-interval', ge=1, le=3600),
    ] = 1
    """
    Transmit interval activated whenever an LLDP-MED Capabilities TLV received is not associated with a remote system
    """
    med_fast_transmit_repeat_count: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:med-fast-transmit-repeat-count', ge=1, le=8),
    ] = 4
    """
    Duration of the fast-start process, in number of packets
    """
    topology_change_notification: Annotated[
        Optional[bool], Field(alias='srl_nokia-lldp:topology-change-notification')
    ] = False
    """
    Indicate whether to generate topology change notifications for endpoints

    Used to track the movement of portable equipment using of events.
    """
    network_policy: Annotated[
        Optional[List[NetworkPolicyListEntry]],
        Field(alias='srl_nokia-lldp:network-policy'),
    ] = None


class LldpMedContainer3(BaseModel):
    """
    LLDP-MED neighbor state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    capabilities: Annotated[
        Optional[List[CapabilitiesListEntry]],
        Field(alias='srl_nokia-lldp:capabilities'),
    ] = None
    network_policy_application_type: Annotated[
        Optional[List[NetworkPolicyApplicationTypeListEntry]],
        Field(alias='srl_nokia-lldp:network-policy-application-type'),
    ] = None
    inventory: Annotated[
        Optional[InventoryContainer], Field(alias='srl_nokia-lldp:inventory')
    ] = None


class MacPhyConfigurationStatusContainer(BaseModel):
    """
    MAC/PHY Configuration/Status TLV information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[InterfaceContainer], Field(alias='srl_nokia-lldp:interface')
    ] = None
    peer: Annotated[Optional[PeerContainer], Field(alias='srl_nokia-lldp:peer')] = None


class MembersContainer(BaseModel):
    """
    Container for specifying the members of the maintenance group - i.e. the components that will eventually be taken out of service for repair or replacement.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp: Annotated[
        Optional[BgpContainer], Field(alias='srl_nokia-maintenance-mode:bgp')
    ] = None
    isis: Annotated[
        Optional[IsisContainer], Field(alias='srl_nokia-maintenance-mode:isis')
    ] = None


class MicroSegmentContainer(BaseModel):
    """
    Enter the micro-segment context
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    block_length: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:block-length', ge=32, le=32)
    ] = 32
    """
    Micro-SID block length
    """
    gib_size: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:gib-size', ge=4, le=60)
    ] = 16
    """
    Maximum number of micro-segment locators network wide (x 1024)
    """
    sid_length: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:sid-length', ge=16, le=16)
    ] = 16
    """
    Micro-SID length
    """
    block: Annotated[
        Optional[List[BlockListEntry]], Field(alias='srl_nokia-srv6:block')
    ] = None


class MicroSegmentContainer2(BaseModel):
    """
    Enter the context to configure the micro-segment locator
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    block: Annotated[
        str,
        Field(
            alias='srl_nokia-srv6:block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Pre-defined micro-SID block
    """
    argument_length: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:argument-length', ge=0, le=16)
    ] = 0
    """
    Argument length
    """
    algorithm: Annotated[
        Optional[int], Field(alias='srl_nokia-srv6:algorithm', ge=0, le=255)
    ] = 0
    """
    IGP flexible algorithm ID
    """
    un: Annotated[Optional[UnContainer], Field(alias='srl_nokia-srv6:un')] = None


class MirrorSourceContainer(BaseModel):
    """
    Configure mirror source(s)
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[List[InterfaceListEntry]], Field(alias='srl_nokia-mirroring:interface')
    ] = None
    subinterface: Annotated[
        Optional[List[SubinterfaceListEntry]],
        Field(alias='srl_nokia-mirroring:subinterface'),
    ] = None
    acl: Annotated[Optional[AclContainer], Field(alias='srl_nokia-mirroring:acl')] = (
        None
    )


class ModuleListEntry(BaseModel):
    """
    Information for the specific gnss port

    This is used for both non-redundant and redundant platforms.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    gnss_id: Annotated[EnumerationEnum133, Field(alias='srl_nokia-sync:gnss-id')]
    ptp_port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:ptp-port-number', ge=0, le=65535)
    ] = None
    """
    IEEE Std 1588 portNumber
    """
    port_state: Annotated[
        Optional[EnumerationEnum118], Field(alias='srl_nokia-sync:port-state')
    ] = None
    """
    Current state associated with the port
    """
    best_master: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:best-master')
    ] = None
    """
    Indicates if this peer was selected by the BMCA to be the best master
    """
    parent_clock: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:parent-clock')
    ] = None
    """
    Indicates if this peer is the current parent clock of this PTP clock

    May differ from best-master due to use of local GNSS as time source.
    """
    major_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:major-version-number', ge=0, le=255)
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:minor-version-number', ge=0, le=255)
    ] = None
    """
    The PTP minor version number in use on the port
    """


class MplsMulticastTepContainer(BaseModel):
    """
    System bridge-table BGP-EVPN MPLS multicast Termination Endpoint information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer4],
        Field(alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:statistics'),
    ] = None
    tep: Annotated[
        Optional[List[TepListEntry]],
        Field(alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:tep'),
    ] = None


class MplsContainer(BaseModel):
    """
    Container for system wide MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    label_ranges: Annotated[
        Optional[LabelRangesContainer],
        Field(alias='srl_nokia-mpls-label-management:label-ranges'),
    ] = None
    services: Annotated[
        Optional[ServicesContainer],
        Field(alias='srl_nokia-mpls-label-management:services'),
    ] = None


class MstInstanceListEntry2(BaseModel):
    """
    List of the mstp instances
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mst_id: Annotated[
        int, Field(alias='srl_nokia-system-protocols-mgmt-stp:mst-id', ge=1, le=15)
    ]
    """
    In an MSTP Bridge, an MST-ID, is used to identify a multiple-spanning-tree-instance
    """
    mst_path_cost: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:mst-path-cost',
            ge=1,
            le=200000000,
        ),
    ] = 10
    """
    Indicates the path cost of the interface
    """
    mst_port_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:mst-port-priority', ge=0, le=255
        ),
    ] = 128
    """
    Indicates the port priority of the interface
    """
    oper_mst_port_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:oper-mst-port-priority',
            ge=0,
            le=255,
        ),
    ] = None
    """
    Mst instance interface stp operational Port Priority
    """
    port_state: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:port-state')
    ] = None
    """
    Interface Stp Port state
    """
    port_num: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:port-num', ge=0, le=4094),
    ] = None
    """
    Interface Stp Port Number
    """
    oper_port_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:oper-port-priority', ge=0, le=255
        ),
    ] = None
    """
    Interface Stp operational Port Priority
    """
    port_role: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:port-role')
    ] = None
    """
    Interface Stp Port role
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-state'),
    ] = None
    """
    Stp Operational status
    """
    designated_bridge: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:designated-bridge'),
    ] = None
    """
    The bridge identifier of the designated bridge

    The bridge identifer of the bridge recorded as the
    root in the configuration BPDUs transmitted by the designated
    bridge for the segment to which the port is attached.
    format: bridge-priority.extended-system-id.mac-address
    """
    designated_port: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:designated-port',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The identifier of the port on the designated bridge
    """
    designated_port_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:designated-port-priority',
            ge=0,
            le=255,
        ),
    ] = None
    """
    The Port priority of the port on the Designated Bridge for this port's segment
    """
    designated_port_num: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:designated-port-num',
            ge=0,
            le=4094,
        ),
    ] = None
    """
    The Port number of the port on the Designated Bridge for this port's segment
    """
    oper_protocol: Annotated[
        Optional[EnumerationEnum74],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-protocol'),
    ] = None
    """
    The protocol running on this interface
    """
    oper_bpdu_encap: Annotated[
        Optional[EnumerationEnum75],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-bpdu-encap'),
    ] = None
    """
    The operating encsapsulation type used on BPDUs sent and received on this interface
    """
    oper_edge: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-edge')
    ] = None
    """
    The protocol running on this interface
    """
    forward_transitions: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:forward-transitions',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of times this port has transitioned from the Learning state to the Forwarding state
    """


class MulticastIdsContainer(BaseModel):
    """
    system multicast id information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer11],
        Field(alias='srl_nokia-system-multicast:statistics'),
    ] = None


class MulticastRouteListEntry(BaseModel):
    """
    List of all the MFIB entries in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        str,
        Field(
            alias='srl_nokia-system-multicast-mfib-table:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    Indicates that the MFIB entry is associated to this network instance
    """
    source: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(alias='srl_nokia-system-multicast-mfib-table:source'),
    ]
    """
    Source IP address of the MFIB entry
    """
    group: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(alias='srl_nokia-system-multicast-mfib-table:group'),
    ]
    """
    Multicast group address of the MFIB entry
    """
    line_card_replication_index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast-mfib-table:line-card-replication-index',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    Line card Replication Index (LRID) allocated by mfib_mgr

    Upon programming an MFIB entry, mfib_mgr requests a Multicast Identifier (MCID) to mcid_mgr
    and based on the response with an allocated MCID, mfib_mgr allocates a LRID for the entry.
    A value 0 indicates that no MCID was received for the entry, and therefore the MFIB entry
    cannot forward multicast traffic.
    """
    last_update: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-multicast-mfib-table:last-update',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Last update of this MFIB entry
    """


class MulticastContainer(BaseModel):
    """
    system multicast information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    multicast_ids: Annotated[
        Optional[MulticastIdsContainer],
        Field(alias='srl_nokia-system-multicast:multicast-ids'),
    ] = None


class NeighborListEntry(BaseModel):
    """
    List of LLDP neighbors on this interface
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[str, Field(alias='srl_nokia-lldp:id')]
    """
    System generated identifier for the remote neighbor
    """
    first_message: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:first-message',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time of the first message from neighbor
    """
    last_update: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:last-update',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time of the last update from neighbor
    """
    system_name: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:system-name', max_length=255, min_length=0),
    ] = None
    """
    The administratively assigned name of the remote neighbor

    The system name field shall contain an alpha-numeric string
    that indicates the system's administratively assigned name.
    The system name should be the system's fully qualified domain
    name. If implementations support IETF RFC 3418, the sysName
    object should be used for this field.
    """
    system_description: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:system-description', max_length=255, min_length=0),
    ] = None
    """
    The system description of the remote neighbor

    The system description field shall contain an alpha-numeric
    string that is the textual description of the network entity.
    The system description should include the full name and
    version identification of the system's hardware type,
    software operating system, and networking software. If
    implementations support IETF RFC 3418, the sysDescr object
    should be used for this field.
    """
    chassis_id: Annotated[Optional[str], Field(alias='srl_nokia-lldp:chassis-id')] = (
        None
    )
    """
    The chassis ID of the remote neighbor

    The Chassis ID is a mandatory TLV which identifies the
    chassis component of the endpoint identifier associated with
    the transmitting LLDP agent
    """
    chassis_id_type: Annotated[
        Optional[EnumerationEnum87], Field(alias='srl_nokia-lldp:chassis-id-type')
    ] = 'MAC_ADDRESS'
    """
    The type of identifier used in the chassis-id field

    This field identifies the format and source of the chassis
    identifier string. It is an enumerator defined by the
    LldpChassisIdSubtype object from IEEE 802.1AB MIB.
    """
    port_id: Annotated[
        Optional[Union[str, StringOrBinaryType1]], Field(alias='srl_nokia-lldp:port-id')
    ] = None
    """
    The Port ID of the remote neighbor

    The Port ID is a mandatory TLV which identifies the port
    component of the endpoint identifier associated with the
    transmitting LLDP agent. If the specified port is an IEEE
    802.3 Repeater port, then this TLV is optional.
    """
    port_id_type: Annotated[
        Optional[EnumerationEnum95], Field(alias='srl_nokia-lldp:port-id-type')
    ] = None
    """
    The type of identifier used in the port-id field

    This field identifies the format and source of the port
    identifier string. It is an enumerator defined by the
    PtopoPortIdType object from RFC2922.
    """
    port_description: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:port-description')
    ] = None
    """
    The description of the port referenced in the port-id field

    The binary string containing the actual port identifier for
    the port which this LLDP PDU was transmitted. The source and
    format of this field is defined by PtopoPortId from
    RFC2922.
    """
    management_address: Annotated[
        Optional[List[ManagementAddressListEntry2]],
        Field(alias='srl_nokia-lldp:management-address'),
    ] = None
    bgp_auto_discovery: Annotated[
        Optional[BgpAutoDiscoveryContainer3],
        Field(alias='srl_nokia-lldp:bgp-auto-discovery'),
    ] = None
    custom_tlv: Annotated[
        Optional[List[CustomTlvListEntry]], Field(alias='srl_nokia-lldp:custom-tlv')
    ] = None
    capability: Annotated[
        Optional[List[CapabilityListEntry]], Field(alias='srl_nokia-lldp:capability')
    ] = None
    lldp_med: Annotated[
        Optional[LldpMedContainer3], Field(alias='srl_nokia-lldp:lldp-med')
    ] = None


class NetconfServerListEntry(BaseModel):
    """
    Configures the NETCONF server instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-netconf-server:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    NETCONF service instance name
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-netconf-server:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable the NETCONF server instance
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-netconf-server:oper-state')
    ] = None
    """
    Details if the NETCONF server instance is operationally available
    """
    oper_down_reason: Annotated[
        Optional[str], Field(alias='srl_nokia-netconf-server:oper-down-reason')
    ] = None
    """
    Details why the NETCONF server instance is operationally unavailable
    """
    last_oper_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-netconf-server:last-oper-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    NETCONF last operational state change

     Time of last change of operational state of NETCONF server instance
    """
    trace_options: Annotated[
        Optional[TraceOptionsContainer],
        Field(alias='srl_nokia-netconf-server:trace-options'),
    ] = None
    transport: Annotated[
        Union[SshCase, TlsCase], Field(alias='srl_nokia-netconf-server:transport')
    ]
    session_limit: Annotated[
        Optional[int],
        Field(alias='srl_nokia-netconf-server:session-limit', ge=1, le=64),
    ] = 64
    """
    Set a limit on the number of simultaneous active NETCONF sessions

     A session is defined as an individual client connection over which a NETCONF session has been started
     by providing bi-directional <hello> messages
    """
    statistics: Annotated[
        Optional[StatisticsContainer7],
        Field(alias='srl_nokia-netconf-server:statistics'),
    ] = None


class NetworkInstanceListEntry4(BaseModel):
    """
    List of network instances to run a TFTP server in
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-tftp:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    Reference to a configured network-instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-tftp:admin-state')
    ] = 'disable'
    """
    Administratively enables or disables the TFTP server
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-tftp:oper-state')
    ] = None
    """
    Details if the server is operationally available
    """
    root_directory: Annotated[
        Optional[str], Field(alias='srl_nokia-tftp:root-directory')
    ] = '/srv/tftpboot'
    """
    Set the root directory of the TFTP server. If the directory needs to be synchronized to the secondary control card,
    it is recommended to use a directory under /opt or /srv.
    """


class NetworkInstanceListEntry5(BaseModel):
    """
    List of network instances to run the JSON RPC server in
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-json-rpc:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    Reference to a configured network-instance
    """
    http: Annotated[Optional[HttpContainer], Field(alias='srl_nokia-json-rpc:http')] = (
        None
    )
    https: Annotated[
        Optional[HttpsContainer], Field(alias='srl_nokia-json-rpc:https')
    ] = None


class NtpCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ntp: Annotated[
        Optional[NtpContainer], Field(alias='srl_nokia-packet-link-qual:ntp')
    ] = None


class PathzContainer(BaseModel):
    """
    Information relating to the active Pathz authorization policy instances

    This policies is provided by the gNSI gRPC service, and can be changed using the gNSI.Pathz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[Optional[str], Field(alias='srl_nokia-gnsi-pathz:version')] = (
        None
    )
    """
    The version of the Pathz authorization policy (sent by the gNSI client).
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The timestamp of the moment when the Pathz policy was created (sent by the gNSI client).
    """
    policy: Annotated[Optional[str], Field(alias='srl_nokia-gnsi-pathz:policy')] = None
    """
    The policy definition

    This JSON string contains the full gRPC authorization policy conforming to the gRPC Path-based authorization
    policy schema.

    This maps to the policy field within a UploadRequest message in the Pathz protobuf.
    """
    counters: Annotated[
        Optional[CountersContainer3], Field(alias='srl_nokia-gnsi-pathz:counters')
    ] = None


class PeerContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ] = None
    """
    Network instance used by this peer

    All configured peers use the same network-instance.   It can be configured at the top level of the ptp tree.
    """
    ip_address: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(alias='srl_nokia-sync:ip-address'),
    ]
    """
    IP address for the PTP peer

    Only Unicast addresses are supported
    """


class PeerContainer3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ] = None
    """
    Network instance that owns the PTP peer
    """
    ip_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-sync:ip-address'),
    ] = None
    """
    IP address for the PTP peer

    Only Unicast addresses are supported
    """


class PolicyListEntry(BaseModel):
    """
    Information about freshness of an schema-path-based Pathz authorization policy that have been installed
    on the device using the gNSI schema-path-based Pathz authorization policy management service.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance: Annotated[
        EnumerationEnum52, Field(alias='srl_nokia-configuration:instance')
    ]
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-configuration:version')
    ] = None
    """
    The version of the Pathz authorization policy (sent by the gNSI client).
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The timestamp of the moment when the Pathz policy was created (sent by the gNSI client).
    """
    policy: Annotated[Optional[str], Field(alias='srl_nokia-configuration:policy')] = (
        None
    )
    """
    The policy definition

    This JSON string contains the full gRPC authorization policy conforming to the gRPC Path-based authorization
    policy schema.

    This maps to the policy field within a UploadRequest message in the Pathz protobuf.
    """


class PolicyListEntry2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    protection_policy_name: Annotated[
        str,
        Field(
            alias='srl_nokia-protection-policies:protection-policy-name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    A unique identifying name for the protection policy
    """
    revert_timer: Annotated[
        Optional[Union[RevertTimerLeaf1, EnumerationEnum54]],
        Field(alias='srl_nokia-protection-policies:revert-timer'),
    ] = 'disable'
    """
    Revert timer for the segment-list.

    Timer till a revert to primary/best path after it is recovered from a failure. In case of uncolored te-policy, applies to primary segment-list and in case of colored te-policy applies to best candidate path.

    The default is 0 seconds.
    """
    seamless_bfd: Annotated[
        Optional[SeamlessBfdContainer],
        Field(alias='srl_nokia-protection-policies:seamless-bfd'),
    ] = None


class PortDsCfgIpListListEntry(BaseModel):
    """
    List of port data sets for configured IP peers
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_index: Annotated[int, Field(alias='srl_nokia-sync:port-index', ge=1, le=999)]
    """
    Index into the port-ds list

    This is not the PTP port number.
    Configurable ports use port indices 1 through 999 but there is a limit on the overall number of these configured ports based on the platform and software release.

    The data sets (i.e., information model) of IEEE Std
    1588-2008 specify a member portDS.portIdentity, which
    uses a typed struct with members clockIdentity and
    portNumber.

    In this YANG data model, portIdentity is not modeled
    in the port-ds.  However, its members are provided
    as follows:
    portIdentity.portNumber is provided as this
    ptp-port-number leaf in port-ds, and
    portIdentity.clockIdentity is provided as the
    clock-identity leaf in default-ds of the instance
    (i.e., ../../default-ds/clock-identity).
    """
    ptp_port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:ptp-port-number', ge=0, le=65535)
    ] = None
    """
    IEEE Std 1588 portNumber

    This is the port-number that will appear in messages sent for this port-index.
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-sync:admin-state')
    ] = 'disable'
    """
    The administrative state of the ptp port
    """
    port_state: Annotated[
        Optional[EnumerationEnum118], Field(alias='srl_nokia-sync:port-state')
    ] = None
    """
    Current state associated with the port
    """
    peer: Annotated[Optional[PeerContainer2], Field(alias='srl_nokia-sync:peer')] = None
    best_master: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:best-master')
    ] = None
    """
    Indicates if this peer was selected by the BMCA to be the best master
    """
    parent_clock: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:parent-clock')
    ] = None
    """
    Indicates if this peer is the current parent clock of this PTP clock

    May differ from best-master due to use of local GNSS as time source.
    """
    log_min_delay_req_interval: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:log-min-delay-req-interval', ge=-6, le=0),
    ] = None
    """
    The base-2 logarithm of the minDelayReqInterval

    The minimum permitted mean time interval between successive Delay_Req messages.
    The value is not configurable.  The delay messages use the same interval as for Sync messages (log-sync-interval)
    """
    log_announce_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-announce-interval', ge=-3, le=4)
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    Mean time interval between successive Announce messages. To change this setting,
    refer to log-announce-interval in the Default data set.
    """
    announce_receipt_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:announce-receipt-timeout', ge=2, le=10),
    ] = None
    """
    Sets the time limit for missed Announce packets before the master clock is deemed down

    This command configures the announceReceiptTimeout value for all peer associations.
    This defines the number of Announce message intervals that must expire with no received
    Announce messages before declaring an ANNOUNCE_RECEIPT_TIMEOUT event. To change this
    setting, refer to announce-receipt-timeout in the Default data set.
    """
    log_sync_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-sync-interval', ge=-6, le=0)
    ] = None
    """
    The base-2 logarithm of the mean SyncInterval for multicast messages

    The default log sync interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    The rates for unicast transmissions are negotiated separately on a per-port
    basis and are not constrained by this attribute.
    """
    major_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:major-version-number', ge=0, le=255)
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:minor-version-number', ge=0, le=255)
    ] = None
    """
    The PTP minor version number in use on the port
    """
    local_priority: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:local-priority', ge=1, le=255)
    ] = 128
    """
    Specifies the local priority of the ptp port
    """
    clock_identity: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:clock-identity', max_length=8, min_length=8),
    ] = None
    """
    Identity of the peer clock
    """
    port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:port-number', ge=0, le=65535)
    ] = None
    """
    Port number of the peer clock
    """
    grandmaster_identity: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:grandmaster-identity', max_length=8, min_length=8),
    ] = None
    """
    The clockIdentity of the grandmaster clock in the last Announce message received from this peer
    """
    grandmaster_clock_quality: Annotated[
        Optional[GrandmasterClockQualityContainer2],
        Field(alias='srl_nokia-sync:grandmaster-clock-quality'),
    ] = None
    grandmaster_priority1: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:grandmaster-priority1', ge=0, le=255)
    ] = None
    """
    The priority1 of the grandmaster clock in the last Announce message received from this peer
    """
    grandmaster_priority2: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:grandmaster-priority2', ge=0, le=255)
    ] = None
    """
    The priority2 of the grandmaster clock in the last Announce message received from this peer
    """
    steps_removed: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:steps-removed', ge=0, le=65535)
    ] = None
    """
    The stepsRemoved in the last Announce message received from this peer
    """
    last_rx_interface: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:last-rx-interface')
    ] = None
    """
    Interface used for the last PTP message received from this peer
    """
    last_tx_interface: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:last-tx-interface')
    ] = None
    """
    Interface used for the last PTP message transmitted to this peer
    """
    rx_port_timestamping: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:rx-port-timestamping')
    ] = None
    """
    Indicates if the port that received the last PTP over IP message supports timestamping

    If this value is false, this is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """
    tx_port_timestamping: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:tx-port-timestamping')
    ] = None
    """
    Indicates if the port selected by routing for the last transmitted PTP over IP message supports timestamping

    If this value is false, this is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """
    backup_source: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:backup-source')
    ] = None
    """
    Indicates if this peer was selected as the reference to be used as the backup source
    """
    offset_from_local_clock: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:offset-from-local-clock',
            ge=-9223372036854775808,
            le=9223372036854775807,
        ),
    ] = None
    """
    Indicates the time offset between the clock recovered from the peer and the local clock's time

    This time offset may be caused by delay asymmetry in the path between the peer clock and the local clock.
    The local clock would be referencing GNSS in the case of G.8275.2 APTS.
    """
    offset_last_update: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:offset-last-update',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time the offset-from-local-clock was last computed.
    """
    statistics: Annotated[
        Optional[StatisticsContainer22], Field(alias='srl_nokia-sync:statistics')
    ] = None
    unicast_negotiation: Annotated[
        Optional[UnicastNegotiationContainer],
        Field(alias='srl_nokia-sync:unicast-negotiation'),
    ] = None


class PortDsDscIpListListEntry(BaseModel):
    """
    List of port data sets for discovered IP peers
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_index: Annotated[int, Field(alias='srl_nokia-sync:port-index', ge=0, le=65535)]
    """
    Index into the port-ds list

    This is not the PTP port number.
    Discovered IP peer ports are created based on Unicast negotiation.

    If an IP peer is a discovered IP peer and later that IP address is entered as a configured peer, then
    port DS information will move from this list to teh port-ds-cfg-ip-list to cover both aspects of communication with this peer.

    The data sets (i.e., information model) of IEEE Std
    1588-2008 specify a member portDS.portIdentity, which
    uses a typed struct with members clockIdentity and
    portNumber.

    In this YANG data model, portIdentity is not modeled
    in the port-ds.  However, its members are provided
    as follows:
    portIdentity.portNumber is provided as this
    ptp-port-number leaf in port-ds, and
    portIdentity.clockIdentity is provided as the
    clock-identity leaf in default-ds of the instance
    (i.e., ../../default-ds/clock-identity).
    """
    ptp_port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:ptp-port-number', ge=0, le=65535)
    ] = None
    """
    IEEE Std 1588 portNumber

    This is the port-number that will appear in messages sent for this port-index.
    """
    port_state: Annotated[
        Optional[EnumerationEnum118], Field(alias='srl_nokia-sync:port-state')
    ] = None
    """
    Current state associated with the port
    """
    peer: Annotated[Optional[PeerContainer3], Field(alias='srl_nokia-sync:peer')] = None
    log_min_delay_req_interval: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:log-min-delay-req-interval', ge=-6, le=0),
    ] = None
    """
    The base-2 logarithm of the minDelayReqInterval

    This reports the value that was established during the unicast negotiation.
    """
    log_announce_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-announce-interval', ge=-3, le=4)
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    Mean time interval between successive Announce messages.
    This reports the value that was established during the unicast negotiation.
    """
    log_sync_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-sync-interval', ge=-6, le=0)
    ] = None
    """
    The base-2 logarithm of the mean SyncInterval for multicast messages

    This reports the value that was established during the unicast negotiation.
    """
    major_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:major-version-number', ge=0, le=255)
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:minor-version-number', ge=0, le=255)
    ] = None
    """
    The PTP minor version number in use on the port
    """
    last_rx_interface: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:last-rx-interface')
    ] = None
    """
    Interface used for the last PTP message received from this peer
    """
    last_tx_interface: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:last-tx-interface')
    ] = None
    """
    Interface used for the last PTP message transmitted to this peer
    """
    rx_port_timestamping: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:rx-port-timestamping')
    ] = None
    """
    Indicates if the port that received the last PTP over IP message supports timestamping

    If this value is false, this is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """
    tx_port_timestamping: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:tx-port-timestamping')
    ] = None
    """
    Indicates if the port selected by routing for the last transmitted PTP over IP message supports timestamping

    If this value is false, this is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """
    statistics: Annotated[
        Optional[StatisticsContainer23], Field(alias='srl_nokia-sync:statistics')
    ] = None
    unicast_negotiation: Annotated[
        Optional[UnicastNegotiationContainer2],
        Field(alias='srl_nokia-sync:unicast-negotiation'),
    ] = None


class PortDsGnssContainer(BaseModel):
    """
    List of port data sets for the GNSS special PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    module: Annotated[
        Optional[List[ModuleListEntry]], Field(alias='srl_nokia-sync:module')
    ] = None


class PortDsInterfaceListListEntry(BaseModel):
    """
    List of port data sets for interfaces
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_index: Annotated[int, Field(alias='srl_nokia-sync:port-index', ge=1, le=999)]
    """
    Index into the port-ds list

    This is not the PTP port number.
    Configurable ports use port indices 1 through 999 but there is a limit on the overall number of these configured ports based on the platform and software release.

    The data sets (i.e., information model) of IEEE Std
    1588-2008 specify a member portDS.portIdentity, which
    uses a typed struct with members clockIdentity and
    portNumber.

    In this YANG data model, portIdentity is not modeled
    in the port-ds.  However, its members are provided
    as follows:
    portIdentity.portNumber is provided as this
    ptp-port-number leaf in port-ds, and
    portIdentity.clockIdentity is provided as the
    clock-identity leaf in default-ds of the instance
    (i.e., ../../default-ds/clock-identity).
    """
    ptp_port_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:ptp-port-number', ge=0, le=65535)
    ] = None
    """
    IEEE Std 1588 portNumber

    This is the port-number that will appear in messages sent for this port-index.
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-sync:admin-state')
    ] = 'disable'
    """
    The administrative state of the ptp port
    """
    port_state: Annotated[
        Optional[EnumerationEnum118], Field(alias='srl_nokia-sync:port-state')
    ] = None
    """
    Current state associated with the port
    """
    interface: Annotated[str, Field(alias='srl_nokia-sync:interface')]
    """
    Local interface used for ptp over ethernet communication
    """
    best_master: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:best-master')
    ] = None
    """
    Indicates if this interface was selected by the BMCA to be the best master
    """
    parent_clock: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:parent-clock')
    ] = None
    """
    Indicates if this interface is the current parent clock of this PTP clock

    May differ from best-master due to use of local GNSS as time source.
    """
    log_min_delay_req_interval: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:log-min-delay-req-interval', ge=-6, le=0),
    ] = None
    """
    The base-2 logarithm of the minDelayReqInterval

    The minimum permitted mean time interval between successive Delay_Req messages.
    The default log-min-delay-req-interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    """
    log_announce_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-announce-interval', ge=-3, le=4)
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    Mean time interval between successive Announce messages. To change this setting,
    refer to log-announce-interval in the Default data set.
    """
    announce_receipt_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:announce-receipt-timeout', ge=2, le=10),
    ] = None
    """
    Sets the time limit for missed Announce packets before the master clock is deemed down

    This defines the number of Announce message intervals that must expire with no received
    Announce messages before declaring an ANNOUNCE_RECEIPT_TIMEOUT event. To change this
    setting, refer to announce-receipt-timeout in the Default data set.
    """
    log_sync_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-sync-interval', ge=-6, le=0)
    ] = None
    """
    The base-2 logarithm of the mean SyncInterval for multicast messages

    The default log sync interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    """
    major_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:major-version-number', ge=0, le=255)
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:minor-version-number', ge=0, le=255)
    ] = None
    """
    The PTP minor version number in use on the port
    """
    local_priority: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:local-priority', ge=1, le=255)
    ] = 128
    """
    Specifies the local priority of the ptp port
    """
    master_only: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:master-only')
    ] = True
    """
    Specifies the masterOnly attribute of the ptp port
    """
    dest_mac: Annotated[
        Optional[EnumerationEnum119], Field(alias='srl_nokia-sync:dest-mac')
    ] = 'forwardable'
    """
    Configure the MAC address associated with forwardable or non-forwardable
    """
    statistics: Annotated[
        Optional[StatisticsContainer21], Field(alias='srl_nokia-sync:statistics')
    ] = None
    neighbor_count: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:neighbor-count', ge=0, le=4294967295)
    ] = None
    """
    The number of neighbors for the port
    """
    neighbor_list: Annotated[
        Optional[List[NeighborListListEntry]],
        Field(alias='srl_nokia-sync:neighbor-list'),
    ] = None


class PortDsSync0Container(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port: Annotated[
        Optional[EnumerationEnum114], Field(alias='srl_nokia-sync:port')
    ] = None
    """
    Physical interface used as the source of PTP messages into the recovery engine
    """
    neighbor: Annotated[
        Optional[NeighborContainer2], Field(alias='srl_nokia-sync:neighbor')
    ] = None


class PortDsSync0Container2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    log_sync_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-sync-interval', ge=-6, le=0)
    ] = None
    """
    The base-2 logarithm of the mean SyncInterval for multicast messages

    The default log sync interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    """
    log_min_delay_req_interval: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:log-min-delay-req-interval', ge=-6, le=0),
    ] = None
    """
    The base-2 logarithm of the minDelayReqInterval

    The minimum permitted mean time interval between successive Delay_Req messages.
    The default log-min-delay-req-interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    """
    local_priority: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:local-priority', ge=1, le=255)
    ] = 128
    """
    Specifies the local priority of the ptp port
    """
    master_only: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:master-only')
    ] = True
    """
    Specifies the masterOnly attribute of the ptp port
    """
    dest_mac: Annotated[
        Optional[EnumerationEnum132], Field(alias='srl_nokia-sync:dest-mac')
    ] = 'forwardable'
    """
    Configure the MAC address associated with forwardable or non-forwardable
    """
    port: Annotated[
        Optional[List[PortListEntry]], Field(alias='srl_nokia-sync:port')
    ] = None


class ProfileListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-maintenance-mode:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Name of the maintenance profile
    """
    bgp: Annotated[
        Optional[BgpContainer2], Field(alias='srl_nokia-maintenance-mode:bgp')
    ] = None
    isis: Annotated[
        Optional[IsisContainer2], Field(alias='srl_nokia-maintenance-mode:isis')
    ] = None


class ProfileListEntry2(BaseModel):
    """
    List of configured Packet Link Qualification profiles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-packet-link-qual:name',
            pattern="^(?=^[<>A-Za-z0-9!@#$%^&()|+=`~.,'/_:;?-][<>A-Za-z0-9 !@#$%^&()|+=`~.,'/_:;?-]*$).*$",
        ),
    ]
    """
    Name of the Packet Link Qualification profile
    """
    timing: Annotated[
        Union[NtpCase, RpcCase], Field(alias='srl_nokia-packet-link-qual:timing')
    ]
    endpoint_type: Annotated[
        Union[PacketGeneratorCase, AsicLoopbackCase],
        Field(alias='srl_nokia-packet-link-qual:endpoint-type'),
    ]


class ProtectionPoliciesContainer(BaseModel):
    """
    Container with protection policies
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    policy: Annotated[
        Optional[List[PolicyListEntry2]],
        Field(alias='srl_nokia-protection-policies:policy'),
    ] = None


class ProtocolAddressContainer(BaseModel):
    """
    The protocol address of the PTP Port that issues the Sync messages
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_protocol: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:network-protocol')
    ] = None
    """
    Protocol used by a PTP instance to transport PTP messages
    """
    mac_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:mac-address',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ] = None
    """
    The MAC address of the PTP port

    This is only valid for PTP over ethernet encapsulation.
    """
    ip: Annotated[Optional[IpContainer], Field(alias='srl_nokia-sync:ip')] = None


class ProxyArpContainer(BaseModel):
    """
    system bridge-table proxy ARP information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer5],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:statistics'),
    ] = None


class ProxyNdContainer(BaseModel):
    """
    system bridge-table proxy ND entry information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer6],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:statistics'),
    ] = None


class RemoteServerListEntry(BaseModel):
    """
    List of output remote syslog servers
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    host: Annotated[
        Union[Ipv4Type, Ipv6Type, DomainNameType], Field(alias='srl_nokia-logging:host')
    ]
    """
    Domain or IP address of a remote syslog server destination
    """
    transport: Annotated[
        Optional[EnumerationEnum25], Field(alias='srl_nokia-logging:transport')
    ] = 'udp'
    """
    Transport protocol for syslog to use for messages sent to a remote server
    """
    tls_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-logging:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to a TLS profile to use for the transport of syslog messages

    If none is specified, then TLS is not used.
    """
    remote_port: Annotated[
        Optional[int], Field(alias='srl_nokia-logging:remote-port', ge=0, le=65535)
    ] = None
    """
    Transport port for syslog to use for messages sent to a remote server
    By default, UDP/TCP uses port 514 and TLS uses port 6514.
    """
    format: Annotated[
        Optional[Union[str, EnumerationEnum26]], Field(alias='srl_nokia-logging:format')
    ] = 'RSYSLOG_SyslogProtocol23Format'
    """
    Text format of syslog messages to a remote server, in legacy rsyslog $template style or one of the predefined templates

    The default presents a date timestamp according to rfc3339.
    The predefined templates are the ones supported by rsyslogd.
    """
    facility: Annotated[
        Optional[List[FacilityListEntry5]], Field(alias='srl_nokia-logging:facility')
    ] = None
    subsystem: Annotated[
        Optional[List[SubsystemListEntry4]], Field(alias='srl_nokia-logging:subsystem')
    ] = None
    filter: Annotated[
        Optional[List[FilterLeafList4]], Field(alias='srl_nokia-logging:filter')
    ] = []
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class RoleListEntry2(BaseModel):
    """
    List of roles configured in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-configuration-role:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Assigned rolename for this role
    """
    rule: Annotated[
        Optional[List[RuleListEntry]], Field(alias='srl_nokia-configuration-role:rule')
    ] = None


class RoutesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ethernet_segment: Annotated[
        Optional[EthernetSegmentContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segment'
        ),
    ] = None
    next_hop: Annotated[
        Optional[Union[EnumerationEnum64, Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:next-hop'
        ),
    ] = 'use-system-ipv4-address'
    """
    The ip-address that will be used as the bgp-next hop for all ES and AD per-ES routes advertised for this Ethernet Segment.
    """


class ServerProfileListEntry(BaseModel):
    """
    List of configured TLS server profiles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-tls:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Name of the TLS server-profile
    """
    key: Annotated[Optional[str], Field(alias='srl_nokia-tls:key')] = None
    """
    Base64 encoded key to use with the server certificate

    This includes the '-----BEGIN PRIVATE KEY-----', and '-----END PRIVATE KEY-----' header and footer.
    The value is hashed, and only the hashed value is kept.
    """
    certificate: Annotated[Optional[str], Field(alias='srl_nokia-tls:certificate')] = (
        None
    )
    """
    Base64 encoded certificate to use with the private key

    This includes the '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----' header and footer.
    Can contain a certificate chain containing multiple certificates separated by '-----BEGIN CERTIFICATE-----'
    and '-----END CERTIFICATE-----' headers and footers. Must start with the client certificate.
    """
    use_tpm_devid: Annotated[
        Optional[EnumerationEnum2], Field(alias='srl_nokia-tls:use-tpm-devid')
    ] = None
    """
    Defines if the server profile key and certificate uses the TPM idevid or oidevid
    """
    authenticate_client: Annotated[
        Optional[bool], Field(alias='srl_nokia-tls:authenticate-client')
    ] = False
    """
    Defines if the server should authenticate the identity of connecting clients using the trust anchor
    """
    trust_anchor: Annotated[
        Optional[str], Field(alias='srl_nokia-tls:trust-anchor')
    ] = None
    """
    Base64 encoded certificate to use as a trust anchor

    This includes the '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----' header and footer.
    Can contain multiple trust anchors separated by '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----'
    headers and footers.
    """
    certificate_revocation_list: Annotated[
        Optional[str], Field(alias='srl_nokia-tls:certificate-revocation-list')
    ] = None
    """
    Base64 encoded certificate revocation list

    This includes the '-----BEGIN X509 CRL' and '-----END X509 CRL' header and footer.
    Can contain multiple crls separated by '-----BEGIN X509 CRL' and '-----END X509 CRL' headers and footers.
    If empty, then no CRL verification is performed.
    """
    relaxed_crl_verification: Annotated[
        Optional[bool], Field(alias='srl_nokia-tls:relaxed-crl-verification')
    ] = False
    """
    Defines if the CRL verification is done in a relaxed (non-strict) way.

    If set to true, the CRL verification allows nonexistent and/or expired CRLs in the client certificate chain.
    If set to false, the CRL verification will fail if any CRL in the client certificate chain is not found or
    expired.
    """
    cipher_list: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-tls:cipher-list')
    ] = [
        'ecdhe-ecdsa-aes256-gcm-sha384',
        'ecdhe-ecdsa-aes128-gcm-sha256',
        'ecdhe-rsa-aes256-gcm-sha384',
        'ecdhe-rsa-aes128-gcm-sha256',
    ]
    """
    List of ciphers to use when negotiating TLS 1.2 with clients

    TLS 1.3 cipher suites are always enabled:
        tls_aes_256_gcm_sha384, tls_aes_128_gcm_sha256, tls_chacha20_poly1305_sha256
    """
    dynamic: Annotated[Optional[bool], Field(alias='srl_nokia-tls:dynamic')] = None
    """
    Defines if the profile was dynamically created by service (for example gNSI Authz/Certz)
    """
    valid_after: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-tls:valid-after',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time the certificate becomes valid
    """
    expiration: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-tls:expiration',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time the certificate expires
    """
    expired: Annotated[Optional[bool], Field(alias='srl_nokia-tls:expired')] = None
    """
    Indicates whether the certificate is expired.

    The certificate is expired if current time is before valid-after time or current
    time is after expiration time
    """
    certz: Annotated[
        Optional[CertzContainer], Field(alias='srl_nokia-gnsi-certz:certz')
    ] = None


class ServerListEntry(BaseModel):
    """
    List of AAA servers to use within this server-group

    Servers are tried in a round-robin fashion, with the first server always being tried if it is operationally available
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    User defined name assigned to the server
    """
    address: Annotated[
        Union[Ipv4Type, Ipv6Type, DomainNameType], Field(alias='srl_nokia-aaa:address')
    ]
    """
    Address or domain name used to reach the server
    """
    tls_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    TLS profile used to set up a TLS connection with this server
    """
    timeout: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:timeout', ge=1, le=3600)
    ] = None
    """
    Set the timeout in seconds on responses from the server. If not specified, the timeout is taken from the value specified for the server-group
    """
    tacacs: Annotated[
        Optional[TacacsContainer3], Field(alias='srl_nokia-aaa:tacacs')
    ] = None
    radius: Annotated[
        Optional[RadiusContainer], Field(alias='srl_nokia-aaa:radius')
    ] = None
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-aaa:oper-state')
    ] = None
    """
    Details the operational state of the server

    A server is defined as being down if it fails to respond before the timeout period, or if a path towards the server is not available.
    """
    statistics: Annotated[
        Optional[StatisticsContainer], Field(alias='srl_nokia-aaa:statistics')
    ] = None


class SourceAddressListEntry(BaseModel):
    """
    List of sourcess addresses
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip_address: Annotated[
        str,
        Field(
            alias='srl_nokia-srv6:ip-address',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$',
        ),
    ]
    """
    Source address used in the SRv6 packet
    """


class SourceContainer(BaseModel):
    """
    Source for this input frequency reference

    This shall be either a leafref to an interface or an application.  The leafref must point to an existing physical ethernet interface.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface_or_other: Annotated[
        Union[InterfaceCase, PtpCase, Sync0Case, GnssCase],
        Field(alias='srl_nokia-sync:interface-or-other'),
    ]


class SshServerListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ssh:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    User-provided name of this server instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-ssh:admin-state')
    ] = 'disable'
    """
    Enable or disable the SSH server instance
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-ssh:oper-state')
    ] = None
    """
    Operational state of the SSH server instance
    """
    port: Annotated[
        Optional[int], Field(alias='srl_nokia-ssh:port', ge=0, le=65535)
    ] = 22
    """
    Port the SSH server instance will listen on for incoming connections
    """
    disable_shell: Annotated[
        Optional[bool], Field(alias='srl_nokia-ssh:disable-shell')
    ] = False
    """
    Disable the ability to spawn a shell for incoming connections
    """
    timeout: Annotated[
        Optional[int], Field(alias='srl_nokia-ssh:timeout', ge=0, le=65535)
    ] = 0
    """
    Set the idle timeout in seconds on SSH connections
    """
    rate_limit: Annotated[
        Optional[int], Field(alias='srl_nokia-ssh:rate-limit', ge=0, le=65535)
    ] = 20
    """
    Set a limit on the number of unauthenticated sessions to the SSH server
     after this number is met, the server will start dropping connection attempts
    """
    protocol_version: Annotated[
        Optional[int], Field(alias='srl_nokia-ssh:protocol-version', ge=0, le=255)
    ] = None
    """
    Protocol version in use by the SSH server
    """
    use_credentialz: Annotated[
        Optional[bool], Field(alias='srl_nokia-ssh:use-credentialz')
    ] = None
    """
    Use the gNSI Credentialz service global SSH configuration for this SSH server instance

    Setting this to true will apply any gNSI Credentialz configuration for this SSH server instance. Static
    configuration will override any gNSI Credentialz configuration.
    """
    trust_anchors: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-ssh:trust-anchors')
    ] = []
    """
    List of public keys used to verify user certificates during authentication

     Each items value should be the public key of a CA, e.g. 'ssh-rsa AAAA<...>= comment'. If no trust anchors are configured, authentication using SSH certificates will not function.

     This sets the TrustedUserCAKeys option within each SSH servers configuration file.
    """
    revoked_keys: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-ssh:revoked-keys')
    ] = []
    """
    List of revoked public keys

     Each items value should be the public key of a revoked keypair, e.g. 'ssh-rsa AAAA<...>= comment'. Any keys provided here cannot be used for public key authentication.

     This sets the RevokedKeys option within each SSH servers configuration file.
    """
    allowed_authentication_types: Annotated[
        Optional[List[EnumerationEnum5]],
        Field(alias='srl_nokia-ssh:allowed-authentication-types'),
    ] = ['publickey', 'password']
    """
    List of allowed authentication types

     This sets the AuthenticationMethods option within each SSH servers configuration file. Also sets
     PasswordAuthentication PubkeyAuthentication KbdInteractiveAuthentication options within each SSH servers
     configuration file.
    """
    authorized_principal_check_tool: Annotated[
        Optional[EnumerationEnum6],
        Field(alias='srl_nokia-ssh:authorized-principal-check-tool'),
    ] = None
    """
    Configure the tool used to check the authorized principals

    Setting the value to hiba-chk sets the AuthorizedPrincipalsCommand to hiba-chk tool. If
    unset, the aaamgr will do the principal checking.
    """
    host_key: Annotated[
        Optional[HostKeyContainer], Field(alias='srl_nokia-ssh:host-key')
    ] = None
    credentialz: Annotated[
        Optional[CredentialzContainer],
        Field(alias='srl_nokia-gnsi-credentialz:credentialz'),
    ] = None
    counters: Annotated[
        Optional[CountersContainer], Field(alias='srl_nokia-gnsi-credentialz:counters')
    ] = None


class StaticAllocationContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    host: Annotated[
        Optional[List[HostListEntry]], Field(alias='srl_nokia-dhcp-server:host')
    ] = None
    relay_information: Annotated[
        Optional[List[RelayInformationListEntry]],
        Field(alias='srl_nokia-dhcp-server:relay-information'),
    ] = None


class StaticAllocationContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    host: Annotated[
        Optional[List[HostListEntry2]], Field(alias='srl_nokia-dhcp-server:host')
    ] = None


class StatisticsContainer14(BaseModel):
    """
    LI statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subscribers: Annotated[
        Optional[SubscribersContainer],
        Field(alias='srl_nokia-lawful-intercept:subscribers'),
    ] = None


class TargetsContainer(BaseModel):
    """
    Properties of LI targets on the local system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subscriber: Annotated[
        Optional[List[SubscriberListEntry]],
        Field(alias='srl_nokia-lawful-intercept:subscriber'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer14],
        Field(alias='srl_nokia-lawful-intercept:statistics'),
    ] = None


class TftpServerContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry4]],
        Field(alias='srl_nokia-tftp:network-instance'),
    ] = None


class TlsContainer(BaseModel):
    """
    Top-level container for TLS configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    server_profile: Annotated[
        Optional[List[ServerProfileListEntry]],
        Field(alias='srl_nokia-tls:server-profile'),
    ] = None


class TransportSessionContainer(BaseModel):
    """
    State parameters of the Transport Session
    directed to the given destination.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ipfix_version: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:ipfix-version', ge=0, le=65535)
    ] = None
    """
    This parameters contains the version of the IPFIX protocol

    Used for Exporting Processes, this parameter contains the version number of the IPFIX protocol that the Exporter uses to export its data in this Transport Session
    """
    source_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-ipfix:source-address'),
    ] = None
    """
    The source address of the Exporter of the IPFIX Transport Session
    """
    destination_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-ipfix:destination-address'),
    ] = None
    """
    The destination address of the Collector of the IPFIX Transport Session
    """
    source_port: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:source-port', ge=0, le=65535)
    ] = None
    """
    The transport-protocol port number of the Exporter of the IPFIX Transport Session
    """
    destination_port: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:destination-port', ge=0, le=65535)
    ] = None
    """
    The transport-protocol port number of the Collector of the IPFIX Transport Session
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-ipfix:oper-state')
    ] = None
    """
    Status of the Transport Session

    Note that this parameter corresponds to
    ipfixTransportSessionStatus in the IPFIX MIB module.
    """
    rate: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:rate', ge=0, le=4294967295)
    ] = None
    """
    The number of bytes per second transmitted by the
    Exporting Process or received by the Collecting Process

    This parameter is updated every second.
    Note that this parameter corresponds to
    ipfixTransportSessionRate in the IPFIX MIB module.
    """
    bytes: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:bytes', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of bytes transmitted by the
    Exporting Process or received by the Collecting Process

    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    transportSessionDiscontinuityTime.
    Note that this parameter corresponds to
    ipfixTransportSessionBytes in the IPFIX MIB module.
    """
    messages: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:messages', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of messages transmitted by the
    Exporting Process or received by the Collecting Process

    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    transportSessionDiscontinuityTime.
    Note that this parameter corresponds to
    ipfixTransportSessionMessages in the IPFIX MIB module.
    """
    discarded_messages: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ipfix:discarded-messages', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    The number of messages that could not be sent to a collector

    Used for Exporting Processes, this parameter
    indicates the number of messages that could not be sent due
    to internal buffer overflows, network congestion, routing
    issues, etc.  Used for Collecting Process, this parameter
    indicates the number of received IPFIX Message that are
    malformed, cannot be decoded, are received in the wrong
    order or are missing according to the sequence number.
    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    transportSessionDiscontinuityTime.
    """
    records: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:records', ge=0, le=18446744073709551615),
    ] = 0
    """
    The number of Data Records transmitted by the Exporting Process

    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    transportSessionDiscontinuityTime.
    """
    templates: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:templates', ge=0, le=4294967295)
    ] = 0
    """
    The number of Templates transmitted by the
    Exporting Process or received by the Collecting Process.
    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    transportSessionDiscontinuityTime.
    """
    options_templates: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:options-templates', ge=0, le=4294967295),
    ] = 0
    """
    The number of Option Templates transmitted by the
    Exporting Process or received by the Collecting Process.
    Discontinuities in the value of this counter can occur at
    re-initialization of the management system, and at other
    times as indicated by the value of
    transportSessionDiscontinuityTime.
    """
    transport_session_start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ipfix:transport-session-start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the start of the given Transport
    Session.
    This state parameter does not correspond to any object in
    the IPFIX MIB module.
    """
    transport_session_discontinuity_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ipfix:transport-session-discontinuity-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Timestamp of the most recent occasion at which
    one or more of the Transport Session counters suffered a
    discontinuity.
    """
    template: Annotated[
        Optional[List[TemplateListEntry]], Field(alias='srl_nokia-ipfix:template')
    ] = None


class TunnelEndPointsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    source_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-mirroring:source-address'),
    ] = None
    """
    remote mirror tunnel source endpoint ip-address
    """
    destination_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-mirroring:destination-address'),
    ] = None
    """
    remote mirror tunnel destination endpoint ip-address
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-mirroring:admin-state')
    ] = 'enable'
    """
    This leaf contains the configured, desired state of the remote mirror tunnel
    """
    service_label: Annotated[
        int, Field(alias='srl_nokia-mirroring:service-label', ge=16, le=1048575)
    ]
    """
    Service label for encapsultion type mpls-gre tunnel
    """
    allowed_tunnel_types: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-mirroring:allowed-tunnel-types')
    ] = []
    """
    List of allowed transport tunnel types for the mirroring traffic.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-mirroring:oper-state')
    ] = None
    """
    This leaf contains the operational state of the remote mirror tunnel
    """
    oper_down_reason: Annotated[
        Optional[EnumerationEnum34], Field(alias='srl_nokia-mirroring:oper-down-reason')
    ] = None
    """
    The reason for the mirror-destination being operational down.  When the reason is not applicable, it is due to the mirroring-instance being shutdown or the mirror-destination is operational up.
    """
    operational_tunnel_type: Annotated[
        Optional[str], Field(alias='srl_nokia-mirroring:operational-tunnel-type')
    ] = None
    """
    The tunnel that is being used for mirroring traffic.
    """
    operational_tunnel_id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-mirroring:operational-tunnel-id', ge=0, le=4294967295),
    ] = None
    """
    The owner-assigned tunnel table index value that identifies
    the tunnel used by mirror-destination.
    """


class UdpExporterContainer(BaseModel):
    """
    UDP parameters.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ipfix_version: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:ipfix-version', ge=9, le=10)
    ] = 10
    """
    IPFIX version number.
    """
    destination_port: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:destination-port', ge=0, le=65535)
    ] = 4739
    """
    If not configured by the user, the Monitoring
    Device uses the default port number for IPFIX, which is
    4739 without TLS or DTLS and 4740 if TLS or DTLS is
    activated.
    """
    transport_session: Annotated[
        Optional[TransportSessionContainer],
        Field(alias='srl_nokia-ipfix:transport-session'),
    ] = None
    source_ip_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-ipfix:source-ip-address'),
    ] = None
    """
    Source IP address used by the Exporting Process.
    If not configured, the IP address assigned to the outgoing
    interface is used as source IP address.
    """
    destination_ip_address: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(alias='srl_nokia-ipfix:destination-ip-address'),
    ]
    """
    IP address of the Collection Process to which
    IPFIX Messages are sent.
    """
    max_packet_size: Annotated[
        Optional[int], Field(alias='srl_nokia-ipfix:max-packet-size', ge=0, le=65535)
    ] = None
    """
    This parameter specifies the maximum size of
    IP packets sent to the Collector.  If set to zero, the
    Exporting Device MUST derive the maximum packet size
    from path MTU discovery mechanisms.
    If not configured by the user, this parameter is set by
    the Monitoring Device.
    """
    template_refresh_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:template-refresh-timeout', ge=0, le=4294967295),
    ] = 600
    """
    Sets time after which Templates are resent in the
    UDP Transport Session.
    Note that the configured lifetime MUST be adapted to the
    templateLifeTime parameter value at the receiving Collecting
    Process.
    """
    options_template_refresh_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ipfix:options-template-refresh-timeout',
            ge=0,
            le=4294967295,
        ),
    ] = 600
    """
    Sets time after which Options Templates are
    resent in the UDP Transport Session.
    Note that the configured lifetime MUST be adapted to the
    optionsTemplateLifeTime parameter value at the receiving
    Collecting Process.
    Note that this parameter corresponds to
    ipfixTransportSessionOptionsTemplateRefreshTimeout in the
    IPFIX MIB module.
    """
    network_instance: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    Reference to a configured network-instance
    """


class UserListEntry(BaseModel):
    """
    List of local users configured on the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[
        str,
        Field(
            alias='srl_nokia-aaa:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Assigned username for this user
    """
    password: Annotated[Optional[str], Field(alias='srl_nokia-aaa:password')] = None
    """
    The user password, supplied either as cleartext or as a hashed value

    If provided as cleartext, the system will hash the value on input, storing only the hashed value.
    If provided as a hashed value, the value should include any '$' characters, for example '$ar2$aOvsuj0ALlU=$r750fMa3ZEA/Di8dIfU2fQ=='.
    """
    role: Annotated[
        Optional[List[RoleLeafList2]], Field(alias='srl_nokia-aaa:role')
    ] = []
    """
    List of roles to assign to this user

    The most specific rule for a particular role takes precedence.
    Rules from all user roles are evaluated together, most permissive privilege taking precedence.
    """
    superuser: Annotated[Optional[bool], Field(alias='srl_nokia-aaa:superuser')] = False
    """
    Indicates that this user is a superuser

    A superuser is granted implicit authorization to all YANG paths, has the ability to execute all CLI plugins, and by default is permitted to access the device through any interface.

    Additionally, users with the superuser attribute are able to execute 'sudo' in bash. A user may also be assigned a role or list of roles, but these are only evaluated for service authorization.
    """
    ssh_principals: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-principals')
    ] = []
    """
    List of principals to associate with this user

    If any of the principals in the list are matched in a SSH client's certificate, and that clients username matches this user, and the certificate is verified, the client will authenticate.
    """
    ssh_key: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-key')] = []
    """
    SSH public key(s) for the user

    If defined, the user may login to the system over SSH with this key. This should use the SSH public authorized key format.
    """
    failed_login_attempts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:failed-login-attempts', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Number of failed login attempts from the user
    """
    last_failed_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-failed-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time of the last login failure from this user
    """
    last_successful_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-successful-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time of the last successful login from this user
    """
    password_change_required: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:password-change-required')
    ] = None
    """
    Indicates if the user must change their password on next login
    """
    lockout: Annotated[
        Optional[LockoutContainer2], Field(alias='srl_nokia-aaa:lockout')
    ] = None
    credentialz: Annotated[
        Optional[CredentialzContainer4], Field(alias='srl_nokia-aaa:credentialz')
    ] = None


class AdminUserContainer(BaseModel):
    """
    Enclosing container for admin user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[Optional[str], Field(alias='srl_nokia-aaa:username')] = 'admin'
    """
    Assigned username for admin user
    """
    password: Annotated[Optional[str], Field(alias='srl_nokia-aaa:password')] = (
        '$y$j9T$pNVjOgcNNGIWjBcdDfK/7.$Ir4uYxszxtqzVj5AGiZvdWJGs.bpLWBJvHON3YgqnC2'
    )
    """
    The admin password, supplied either as cleartext or as a hashed value

    If provided as cleartext, the system will hash the value on input, storing only the hashed value.
    If provided as a hashed value, the value should include any '$' characters, for example '$ar2$aOvsuj0ALlU=$r750fMa3ZEA/Di8dIfU2fQ=='.
    """
    role: Annotated[Optional[List[RoleLeafList]], Field(alias='srl_nokia-aaa:role')] = (
        []
    )
    """
    List of roles to assign to this user

    The most specific rule for a particular role takes precedence.
    Rules from all user roles are evaluated together, most permissive privilege taking precedence.
    """
    superuser: Annotated[Optional[bool], Field(alias='srl_nokia-aaa:superuser')] = True
    """
    Indicates if the admin user is a superuser

    A superuser is granted implicit authorization to all YANG paths, has the ability to execute all CLI plugins, and by default is permitted to access the device through any interface.

    Additionally, users with the superuser attribute are able to execute 'sudo' in bash. A user may also be assigned a role or list of roles, but these are only evaluated for service authorization.
    """
    spiffe_ids: Annotated[
        Optional[List[SpiffeIdsLeafList]], Field(alias='srl_nokia-aaa:spiffe-ids')
    ] = []
    """
    The SPIFFE ID list for the user, including the spiffe:// URI

    This list of IDs is evaluated by TLS-consuming servers (e.g. gNMI, JSON-RPC) that use a TLS server-profile with authenticate-client set to true.

    If a match is found in any incoming offered client certificates, the provider of the certificate is associated with this local user, and given resulting permissions.
    """
    ssh_principals: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-principals')
    ] = []
    """
    List of principals to associate with this user

    If any of the principals in the list are matched in a SSH client's certificate, and that clients username matches this user, and the certificate is verified, the client will authenticate.
    """
    ssh_key: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-key')] = []
    """
    SSH public key(s) for the user

    If defined, the user may login to the system over SSH with this key. This should use the SSH public authorized key format.
    """
    failed_login_attempts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:failed-login-attempts', ge=0, le=18446744073709551615
        ),
    ] = 0
    """
    Number of failed login attempts from the user
    """
    last_failed_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-failed-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time of the last login failure from this user
    """
    last_successful_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-successful-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The date and time of the last successful login from this user
    """
    password_change_required: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:password-change-required')
    ] = None
    """
    Indicates if the user must change their password on next login
    """
    lockout: Annotated[
        Optional[LockoutContainer], Field(alias='srl_nokia-aaa:lockout')
    ] = None
    credentialz: Annotated[
        Optional[CredentialzContainer2], Field(alias='srl_nokia-aaa:credentialz')
    ] = None


class AppManagementContainer(BaseModel):
    """
    Top-level container for application configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    application: Annotated[
        Optional[List[ApplicationListEntry]],
        Field(alias='srl_nokia-app-mgmt:application'),
    ] = None


class AuthenticationContainer(BaseModel):
    """
    Top-level container for global authentication data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    authentication_method: Annotated[
        Optional[List[AuthenticationMethodLeafList]],
        Field(alias='srl_nokia-aaa:authentication-method'),
    ] = []
    """
    Ordered list of server-groups to be used during user authentication

    If authentication fails with one method, the next defined method is tried -- failure of all methods results in the user being denied access.
    """
    exit_on_reject: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:exit-on-reject')
    ] = False
    """
    Enable/disable exit-on-reject behaviour for authentication attempts

    With this behaviour enabled, when a reject is received from any server the system will not try further methods, and will reject the user authentication attempt. Default behaviour is to continue trying methods until one accepts the user, or the system runs out of methods to try.
    """
    idle_timeout: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:idle-timeout', ge=0, le=4294967295)
    ] = 600
    """
    Set the idle timeout of all CLI sessions

    After the timeout is reached, the session is disconnected from the system.
    """
    admin_user: Annotated[
        Optional[AdminUserContainer], Field(alias='srl_nokia-aaa:admin-user')
    ] = None
    linuxadmin_user: Annotated[
        Optional[LinuxadminUserContainer], Field(alias='srl_nokia-aaa:linuxadmin-user')
    ] = None
    local_linux_users: Annotated[
        Optional[LocalLinuxUsersContainer],
        Field(alias='srl_nokia-aaa:local-linux-users'),
    ] = None
    user: Annotated[
        Optional[List[UserListEntry]], Field(alias='srl_nokia-aaa:user')
    ] = None
    session: Annotated[
        Optional[List[SessionListEntry]], Field(alias='srl_nokia-aaa:session')
    ] = None
    password: Annotated[
        Optional[PasswordContainer4], Field(alias='srl_nokia-aaa:password')
    ] = None


class AuthenticationContainer2(BaseModel):
    """
    Container for protocol authentication options available system wide
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    keychain: Annotated[
        Optional[List[KeychainListEntry]], Field(alias='srl_nokia-keychains:keychain')
    ] = None


class AuthorizationContainer(BaseModel):
    """
    Top-level container for authorization configuration and operational state data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    role: Annotated[
        Optional[List[RoleListEntry]], Field(alias='srl_nokia-aaa:role')
    ] = None
    authz_policy: Annotated[
        Optional[AuthzPolicyContainer], Field(alias='srl_nokia-gnsi-authz:authz-policy')
    ] = None


class BindingTableListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac_address: Annotated[
        str,
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:mac-address',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ]
    """
    MAC address of the endpoint
    """
    network_instance: Annotated[
        str,
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    Network instance where the endpoint is connected
    """
    subinterface: Annotated[
        Optional[str],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:subinterface'),
    ] = None
    """
    Subnterface where the endpoint is connected
    """
    ip_address: Annotated[
        Union[Ipv4AddressUnicastType, Ipv6AddressUnicastType],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:ip-address'),
    ]
    """
    IP address associated with the endpoint
    """
    binding_type: Annotated[
        Optional[EnumerationEnum76],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:binding-type'),
    ] = None
    """
    Indicates protocol used to learn this IP-MAC association entry
    """
    lease_time_start: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:lease-time-start',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Start of time when DHCP server provided IP address lease.
    """
    lease_time_end: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:lease-time-end',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time beyond which the DHCP provided IP address lease expires.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum78],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:oper-state'),
    ] = None
    """
    Indicates the operational state of this IP-MAC association entry
    """
    config_updated: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:config_updated'),
    ] = None
    bridge_updated: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:bridge_updated'),
    ] = None
    """
    Indicates that the MAC and subinterface is present in the bridge tables
    """
    message_type: Annotated[
        Optional[EnumerationEnum79],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:message_type'),
    ] = None
    message6_type: Annotated[
        Optional[EnumerationEnum80],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:message6_type'),
    ] = None


class BootContainer(BaseModel):
    """
    Top-level container for configuration and state data related to booting the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    image: Annotated[
        Optional[List[ImageLeafList]], Field(alias='srl_nokia-boot:image')
    ] = []
    """
    Ordered list of local images used to boot the system

          This directly translates into boot configuration in grub, where the images are tried in the order specified by the user. Images are sourced via the internal SD card, and the value passed is the folder that contains the initramfs, kernel, and squashfs image. The search path for these directories is /mnt/nokiaos/<folder>
    """
    golden_image: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-boot:golden-image', pattern='^(?=^[0-9A-Za-z_\\-\\.]*$).*$'
        ),
    ] = None
    """
    The local image the system reverts to when a factory reset operation is requested

    The value is the folder that contains the initramfs, kernel, and squashfs image.
    The search path for these directories is /mnt/nokiaos/<folder>
    """
    fips_140: Annotated[
        Optional[Fips140Container], Field(alias='srl_nokia-boot:fips-140')
    ] = None
    autoboot: Annotated[
        Optional[AutobootContainer], Field(alias='srl_nokia-boot:autoboot')
    ] = None
    grub_password: Annotated[
        Optional[str], Field(alias='srl_nokia-boot:grub-password')
    ] = None
    """
    The leaf container grub boot password
    """


class BufferListEntry(BaseModel):
    """
    Log files maintained in memory, non-persistent across system reboots

    These files are stored at directory /var/log/srlinux/buffer. Rotation into multiple files is available.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    buffer_name: Annotated[
        str,
        Field(
            alias='srl_nokia-logging:buffer-name',
            pattern='^(?=^([^./][^/]*)|(\\.[^\\./]+)|(\\.\\.[^/])+$).*$',
        ),
    ]
    """
    Base name of the file(s) to be stored in memory
    """
    persist: Annotated[
        Optional[int], Field(alias='srl_nokia-logging:persist', ge=0, le=604800)
    ] = 0
    """
    Time in seconds to shadow the buffer to persistent storage

    Setting this field to 0 results in the buffer not being persisted. A value other than 0 will result in the log being persisted to disk based on the configured value. Logs with a non-zero persist value are persisted automatically on rollover, or at the configured value.
    """
    format: Annotated[
        Optional[Union[str, EnumerationEnum22]], Field(alias='srl_nokia-logging:format')
    ] = 'RSYSLOG_FileFormat'
    """
    Text format of syslog messages to a local output (buffer, file or console), in legacy rsyslog $template style or one of the predefined templates

    The default presents a date timestamp according to rfc3339.
    The predefined templates are the ones supported by rsyslogd.
    """
    rotate: Annotated[
        Optional[int], Field(alias='srl_nokia-logging:rotate', ge=0, le=65535)
    ] = 4
    """
    Number of files to keep in rotation when a maximum file size is reached
    """
    rotations: Annotated[
        Optional[int],
        Field(alias='srl_nokia-logging:rotations', ge=0, le=18446744073709551615),
    ] = 0
    """
    Number of file rotations occurred
    """
    size: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-logging:size',
            pattern='^(?=^[1-9][0-9]{0,15}(K|M|G){0,1}$).*$',
        ),
    ] = '10M'
    """
    Number of bytes an individual output file cannot exceed

    The field allows the 'K, M, or G' suffixes as shorthand.
    When reaching that size, a rotation happens and subsequent data is stored
    in a new file with the same base name.
    """
    facility: Annotated[
        Optional[List[FacilityListEntry3]], Field(alias='srl_nokia-logging:facility')
    ] = None
    subsystem: Annotated[
        Optional[List[SubsystemListEntry2]], Field(alias='srl_nokia-logging:subsystem')
    ] = None
    filter: Annotated[
        Optional[List[FilterLeafList2]], Field(alias='srl_nokia-logging:filter')
    ] = []
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class ClockSourceContainer(BaseModel):
    """
    Identifies the source of PTP messages into PTP the time recovery engine

    Only one of peer, interface, or sync0-neighbor will be populated
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_ds_cfg_ip: Annotated[
        Optional[PortDsCfgIpContainer], Field(alias='srl_nokia-sync:port-ds-cfg-ip')
    ] = None
    port_ds_interface: Annotated[
        Optional[PortDsInterfaceContainer],
        Field(alias='srl_nokia-sync:port-ds-interface'),
    ] = None
    port_ds_sync0: Annotated[
        Optional[PortDsSync0Container], Field(alias='srl_nokia-sync:port-ds-sync0')
    ] = None


class ComputedDesignatedForwarderCandidatesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    designated_forwarder_candidate: Annotated[
        Optional[List[DesignatedForwarderCandidateListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-candidate'
        ),
    ] = None


class ConsoleContainer(BaseModel):
    """
    Hardware serial device normally used for bring-up and diagnostics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    format: Annotated[
        Optional[Union[str, EnumerationEnum22]], Field(alias='srl_nokia-logging:format')
    ] = 'RSYSLOG_FileFormat'
    """
    Text format of syslog messages to a local output (buffer, file or console), in legacy rsyslog $template style or one of the predefined templates

    The default presents a date timestamp according to rfc3339.
    The predefined templates are the ones supported by rsyslogd.
    """
    facility: Annotated[
        Optional[List[FacilityListEntry]], Field(alias='srl_nokia-logging:facility')
    ] = None
    subsystem: Annotated[
        Optional[List[SubsystemListEntry]], Field(alias='srl_nokia-logging:subsystem')
    ] = None
    filter: Annotated[
        Optional[List[FilterLeafList]], Field(alias='srl_nokia-logging:filter')
    ] = []
    """
    A set of all-matching criteria that messages must fulfill in order to be captured
    """


class Dhcpv4Container(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-dhcp-server:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable the dhcp server
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-dhcp-server:oper-state')
    ] = None
    """
    Details if the dhcp server is operationally available
    """
    trace_options: Annotated[
        Optional[TraceOptionsContainer2],
        Field(alias='srl_nokia-dhcp-server:trace-options'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer9], Field(alias='srl_nokia-dhcp-server:statistics')
    ] = None
    options: Annotated[
        Optional[OptionsContainer], Field(alias='srl_nokia-dhcp-server:options')
    ] = None
    static_allocation: Annotated[
        Optional[StaticAllocationContainer],
        Field(alias='srl_nokia-dhcp-server:static-allocation'),
    ] = None


class Dhcpv6Container(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-dhcp-server:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable the dhcp server
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-dhcp-server:oper-state')
    ] = None
    """
    Details if the dhcp server is operationally available
    """
    trace_options: Annotated[
        Optional[TraceOptionsContainer3],
        Field(alias='srl_nokia-dhcp-server:trace-options'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer10], Field(alias='srl_nokia-dhcp-server:statistics')
    ] = None
    options: Annotated[
        Optional[OptionsContainer4], Field(alias='srl_nokia-dhcp-server:options')
    ] = None
    static_allocation: Annotated[
        Optional[StaticAllocationContainer2],
        Field(alias='srl_nokia-dhcp-server:static-allocation'),
    ] = None


class EventHandlerContainer(BaseModel):
    """
    Top-level container for configuration and state of event handler and event handling instances
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    run_as_user: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:run-as-user',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    User configured to run event handler instances

    If no user is configured, scripts are executed as the 'admin' user.
    """
    instance: Annotated[
        Optional[List[InstanceListEntry]],
        Field(alias='srl_nokia-event-handler:instance'),
    ] = None


class EvpnContainer(BaseModel):
    """
    System bridge-table BGP-EVPN information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mpls_multicast_tep: Annotated[
        Optional[MplsMulticastTepContainer],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:mpls-multicast-tep'
        ),
    ] = None


class FhsIpMacBindingsContainer(BaseModel):
    """
    List of First Hop Security IP-MAC association in the database.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    binding_table: Annotated[
        Optional[List[BindingTableListEntry]],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:binding-table'),
    ] = None


class GroupListEntry(BaseModel):
    """
    List of user-configured maintenance groups
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-maintenance-mode:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Name of the maintenance group.
    """
    maintenance_mode: Annotated[
        Optional[MaintenanceModeContainer],
        Field(alias='srl_nokia-maintenance-mode:maintenance-mode'),
    ] = None
    maintenance_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:maintenance-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Leaf reference to /system/maintenance/profile/name
    """
    members: Annotated[
        Optional[MembersContainer], Field(alias='srl_nokia-maintenance-mode:members')
    ] = None


class GrpcServerListEntry(BaseModel):
    """
    List of configured gRPC server instances
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-grpc:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    User-provided name of this server instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-grpc:admin-state')
    ] = 'disable'
    """
    Globally enable or disable the gRPC server instance

    Disabling this will disable all gRPC server sockets in all network instances, and any configured unix domain sockets.
    """
    trace_options: Annotated[
        Optional[List[EnumerationEnum13]], Field(alias='srl_nokia-grpc:trace-options')
    ] = []
    """
    gRPC trace options
    """
    timeout: Annotated[
        Optional[int], Field(alias='srl_nokia-grpc:timeout', ge=0, le=65535)
    ] = 7200
    """
    Set the idle timeout in seconds on gRPC connections
    """
    rate_limit: Annotated[
        Optional[int], Field(alias='srl_nokia-grpc:rate-limit', ge=0, le=65535)
    ] = 60
    """
    Set a limit on the number of RPC calls per minute
    """
    session_limit: Annotated[
        Optional[int], Field(alias='srl_nokia-grpc:session-limit', ge=0, le=65535)
    ] = 20
    """
    Set a limit on the number of simultaneous active gRPC sessions

    A session is defined as an individual RPC invocation, which could result in a single client generating multiple sessions.
    In the context of a Subscribe RPC this is the number of simultaneously active SubscribeRequests across all Subscribe RPCs.
    """
    max_concurrent_streams: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:max-concurrent-streams', ge=0, le=2147483647),
    ] = 65535
    """
    Set a limit on the maximum number of concurrent streams allowed on a single gRPC connection

    This value is signaled to the clients in a SETTINGS frame.
    """
    metadata_authentication: Annotated[
        Optional[bool], Field(alias='srl_nokia-grpc:metadata-authentication')
    ] = True
    """
    Enable or disable the use of username/password metadata authentication for every gRPC request
    """
    yang_models: Annotated[
        Optional[EnumerationEnum14], Field(alias='srl_nokia-grpc:yang-models')
    ] = 'native'
    """
    Specify yang-models to be used when origin field is not present in requests
    """
    services: Annotated[Optional[List[str]], Field(alias='srl_nokia-grpc:services')] = (
        []
    )
    """
    The gRPC service definitions that should be enabled for this gRPC server instance
    """
    tls_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Reference to the TLS profile to use on the gRPC server

    If none is specified, then TLS is not used.
    """
    default_tls_profile: Annotated[
        Optional[bool], Field(alias='srl_nokia-grpc:default-tls-profile')
    ] = False
    """
    Whether to use default TLS profile (generated by the system) if none is configured via tls-profile field
    """
    gnmi: Annotated[Optional[GnmiContainer], Field(alias='srl_nokia-grpc:gnmi')] = None
    port: Annotated[
        Optional[int], Field(alias='srl_nokia-grpc:port', ge=0, le=65535)
    ] = 57400
    """
    Port the gRPC server will listen on for incoming connections
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-grpc:oper-state')
    ] = None
    """
    Details if the gRPC server is operationally available
    """
    statistics: Annotated[
        Optional[StatisticsContainer2], Field(alias='srl_nokia-grpc:statistics')
    ] = None
    certz: Annotated[Optional[CertzContainer2], Field(alias='srl_nokia-grpc:certz')] = (
        None
    )
    client: Annotated[
        Optional[List[ClientListEntry]], Field(alias='srl_nokia-grpc:client')
    ] = None
    pathz: Annotated[
        Optional[PathzContainer], Field(alias='srl_nokia-gnsi-pathz:pathz')
    ] = None


class InstanceListEntry2(BaseModel):
    """
    List of line references configured for frequency
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_number: Annotated[
        int, Field(alias='srl_nokia-sync:instance-number', ge=1, le=5)
    ]
    """
    The instance number of the each line reference
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-sync:admin-state')
    ] = 'disable'
    """
    Configure the administrative state of this frequency reference instance
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-sync:oper-state')
    ] = None
    """
    Indicates the operational state of this line reference
    """
    source: Annotated[
        Optional[SourceContainer], Field(alias='srl_nokia-sync:source')
    ] = None
    priority: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:priority', ge=1, le=5)
    ] = 3
    """
    Sets the priority of this line timing reference for the system timing selection process
    1 = highest priority
    5 = lowest priority
    Duplicate numbers are not allowed
    """
    ql_override: Annotated[
        Optional[EnumerationEnum104], Field(alias='srl_nokia-sync:ql-override')
    ] = 'unused'
    """
    Override the incoming QL/SSM value for this line reference
    Quality level override of a timing reference
    Options are unused, prs, stu, st2, tnc, st3e, st3, prc, ssua, ssub, sec, eec1, eec2
    """
    ql_value: Annotated[
        Optional[EnumerationEnum105], Field(alias='srl_nokia-sync:ql-value')
    ] = None
    """
    The incoming QL/SSM value from this line reference
    """
    reference_status: Annotated[
        Optional[EnumerationEnum106], Field(alias='srl_nokia-sync:reference-status')
    ] = None
    """
    The current status this line reference
    """
    not_qualified_reason: Annotated[
        Optional[EnumerationEnum107], Field(alias='srl_nokia-sync:not-qualified-reason')
    ] = None
    """
    If the reference is not qualified, this identifies the reason
    """


class InterfaceListEntry3(BaseModel):
    """
    List of Interfaces to be managed by Mgmt-Stp
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:admin-state'),
    ] = 'disable'
    """
    Administratively enable or disable the Mgmt-STP protocol interface
    """
    interface_name: Annotated[
        str,
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:interface-name',
            max_length=255,
            min_length=1,
        ),
    ]
    """
    Name of the MSTP interface
    """
    interface_ref: Annotated[
        Optional[InterfaceRefContainer],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:interface-ref'),
    ] = None
    port_number: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:port-number', ge=1, le=2047),
    ] = None
    """
    Port Number associated with this interface
    """
    priority: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:priority', ge=0, le=255),
    ] = 128
    """
    Priority value coupled with port number forms 16-bit port-identifier field
    """
    path_cost: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:path-cost', ge=1, le=200000000
        ),
    ] = 10
    """
    The interface path-cost is used by STP to calculate the path cost to the root bridge
    """
    edge_port: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:edge-port')
    ] = 'oc-stp-types:EDGE_AUTO'
    """
    Modes of Edge-Port
    """
    link_type: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:link-type')
    ] = None
    """
    Indicates the number of bridges behind the subinterface
    """
    guard: Annotated[
        Optional[EnumerationEnum73],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:guard'),
    ] = 'NONE'
    """
    Enable Guard
    """
    bpdu_guard: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-protocols-mgmt-stp:bpdu-guard')
    ] = False
    """
    Enable edge port BPDU guard
    """
    port_state: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:port-state')
    ] = None
    """
    Interface Stp Port state
    """
    port_num: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:port-num', ge=0, le=4094),
    ] = None
    """
    Interface Stp Port Number
    """
    oper_port_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:oper-port-priority', ge=0, le=255
        ),
    ] = None
    """
    Interface Stp operational Port Priority
    """
    port_role: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:port-role')
    ] = None
    """
    Interface Stp Port role
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-state'),
    ] = None
    """
    Stp Operational status
    """
    designated_bridge: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:designated-bridge'),
    ] = None
    """
    The bridge identifier of the designated bridge

    The bridge identifer of the bridge recorded as the
    root in the configuration BPDUs transmitted by the designated
    bridge for the segment to which the port is attached.
    format: bridge-priority.extended-system-id.mac-address
    """
    designated_port: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:designated-port',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The identifier of the port on the designated bridge
    """
    designated_port_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:designated-port-priority',
            ge=0,
            le=255,
        ),
    ] = None
    """
    The Port priority of the port on the Designated Bridge for this port's segment
    """
    designated_port_num: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:designated-port-num',
            ge=0,
            le=4094,
        ),
    ] = None
    """
    The Port number of the port on the Designated Bridge for this port's segment
    """
    oper_protocol: Annotated[
        Optional[EnumerationEnum74],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-protocol'),
    ] = None
    """
    The protocol running on this interface
    """
    oper_bpdu_encap: Annotated[
        Optional[EnumerationEnum75],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-bpdu-encap'),
    ] = None
    """
    The operating encsapsulation type used on BPDUs sent and received on this interface
    """
    oper_edge: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-edge')
    ] = None
    """
    The protocol running on this interface
    """
    forward_transitions: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:forward-transitions',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The number of times this port has transitioned from the Learning state to the Forwarding state
    """
    bpdu_guard_error: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:bpdu-guard-error'),
    ] = None
    """
    Displays True when the interface is operationally down due to stp bpdu guard error
    """
    bpdu_guard_recovery_time_expires: Annotated[
        Optional[Union[BpduGuardRecoveryTimeExpiresLeaf1, DateAndTimeDeltaType]],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:bpdu-guard-recovery-time-expires'
        ),
    ] = None
    """
    The remaining time until the bpdu-guard-down-time expires and the error is cleared on the interface
    """
    statistics: Annotated[
        Optional[StatisticsContainer12],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:statistics'),
    ] = None
    inside_region: Annotated[
        Optional[bool], Field(alias='srl_nokia-system-protocols-mgmt-stp:inside-region')
    ] = None
    """
    Indicates if Mst instance interface is inside MST region
    """
    mst_instance: Annotated[
        Optional[List[MstInstanceListEntry2]],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:mst-instance'),
    ] = None


class JsonRpcServerContainer(BaseModel):
    """
    Configures the JSON RPC access API
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-json-rpc:admin-state')
    ] = 'disable'
    """
    Globally enable or disable the JSON RPC server
    Disabling this will disable all JSON RPC servers.
    """
    commit_confirmed_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-json-rpc:commit-confirmed-timeout', ge=0, le=86400),
    ] = 0
    """
    Number of seconds to wait for confirmation. A value of 0 means commit confirmed is not used
    """
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry5]],
        Field(alias='srl_nokia-json-rpc:network-instance'),
    ] = None
    trace_options: Annotated[
        Optional[List[EnumerationEnum101]],
        Field(alias='srl_nokia-json-rpc:trace-options'),
    ] = []
    """
    JSON RPC trace options
    """
    unix_socket: Annotated[
        Optional[UnixSocketContainer], Field(alias='srl_nokia-json-rpc:unix-socket')
    ] = None


class LawfulInterceptContainer(BaseModel):
    """
    LI properties
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    targets: Annotated[
        Optional[TargetsContainer], Field(alias='srl_nokia-lawful-intercept:targets')
    ] = None
    system: Annotated[
        Optional[SystemContainer], Field(alias='srl_nokia-lawful-intercept:system')
    ] = None
    pfcp: Annotated[
        Optional[PfcpContainer], Field(alias='srl_nokia-lawful-intercept:pfcp')
    ] = None
    admf: Annotated[
        Optional[AdmfContainer], Field(alias='srl_nokia-lawful-intercept:admf')
    ] = None
    admin_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-lawful-intercept:admin-state'),
    ] = 'enable'
    """
    Administrative state
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-lawful-intercept:oper-state')
    ] = None
    """
    Operational state
    """


class LldpMedContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-lldp:admin-state')
    ] = 'disable'
    """
    Enable or disable LLDP-MED on the interface

    When 'enable' the capability TLV will be transmitted.  Other LLDP-MED TLVs must be included
    in the lldp-med-tlv list to be transmitted to an endpoint.  Value 'disable' stops the
    transmission and processing of LLDP-MED TLVs.  The base LLDP protocol admin-state must be 'enable'
    for LLDP-MED to be operationally up.
    """
    network_policy: Annotated[
        Optional[List[NetworkPolicyLeafList]],
        Field(alias='srl_nokia-lldp:network-policy'),
    ] = []
    """
    Name of the network policy for a specific application type

    Multiple network policies can be assigned to a single interface, one per application type.
    """
    lldp_med_tlvs: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-lldp:lldp-med-tlvs')
    ] = []
    """
    List of supported LLDP-MED tlvs on the interface
    """
    location: Annotated[
        Optional[LocationContainer], Field(alias='srl_nokia-lldp:location')
    ] = None
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-lldp:oper-state')
    ] = None
    """
    Details the operational state of LLDP MED on the interface

    Global lldp, interface lldp and interface lldp-med must be admin-state 'enable' to achieve oper-state 'up'
    """
    mac_phy_configuration_status: Annotated[
        Optional[MacPhyConfigurationStatusContainer],
        Field(alias='srl_nokia-lldp:mac-phy-configuration-status'),
    ] = None


class LocatorListEntry(BaseModel):
    """
    Enter the locator list instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    locator_name: Annotated[
        str,
        Field(
            alias='srl_nokia-srv6:locator-name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    SRv6 locator name
    """
    full_segment: Annotated[
        Optional[FullSegmentContainer], Field(alias='srl_nokia-srv6:full-segment')
    ] = None
    micro_segment: Annotated[
        Optional[MicroSegmentContainer2], Field(alias='srl_nokia-srv6:micro-segment')
    ] = None


class LoggingContainer(BaseModel):
    """
    System logging provides the interface to syslog services
    to setup output entities on a selection of log sources.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    console: Annotated[
        Optional[ConsoleContainer], Field(alias='srl_nokia-logging:console')
    ] = None
    filter: Annotated[
        Optional[List[FilterListEntry]], Field(alias='srl_nokia-logging:filter')
    ] = None
    buffer: Annotated[
        Optional[List[BufferListEntry]], Field(alias='srl_nokia-logging:buffer')
    ] = None
    file: Annotated[
        Optional[List[FileListEntry]], Field(alias='srl_nokia-logging:file')
    ] = None
    remote_server: Annotated[
        Optional[List[RemoteServerListEntry]],
        Field(alias='srl_nokia-logging:remote-server'),
    ] = None
    subsystem_facility: Annotated[
        Optional[EnumerationEnum23], Field(alias='srl_nokia-logging:subsystem-facility')
    ] = 'local6'
    """
    Linux facility that internal application subsystems will use
    """


class MaintenanceContainer(BaseModel):
    """
    Top-level container for Maintenance Mode configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    group: Annotated[
        Optional[List[GroupListEntry]], Field(alias='srl_nokia-maintenance-mode:group')
    ] = None
    profile: Annotated[
        Optional[List[ProfileListEntry]],
        Field(alias='srl_nokia-maintenance-mode:profile'),
    ] = None


class MgmtStpListEntry(BaseModel):
    """
    Management Stp Instance configured on the local system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    A unique name identifying the mgmt-stp-instance
    """
    mode: Annotated[
        Optional[EnumerationEnum71],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:mode'),
    ] = 'mstp'
    """
    Protocol Mode Supported
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:admin-state'),
    ] = 'disable'
    """
    Administratively enable or disable the stp instance

    When STP on the network instance is administratively disabled,
    any BPDUs are forwarded transparently.
    When STP on the network instance is administratively enabled,
    but the administrative state on a sub-interface is disabled,
    BPDUs received on such a subinterface are discarded.
    """
    bridge_priority: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:bridge-priority'),
    ] = None
    """
    Priority component of the Bridge Identifier
    """
    bridge_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:bridge-address',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
        ),
    ] = None
    """
    A 48-bit administered MAC Address assigned to the bridge

    The bridge mac address cannot be a broadcast or multicast address. The default is
    the base mac address of the switch. On configuring bridge-address, reserved(0) extended-system-id
    will be used in the bridge-identifier 
    """
    forward_delay: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:forward-delay', ge=4, le=30),
    ] = 15
    """
    The delay used by STP bridges to transition root and designated ports to forwarding
    """
    hello_time: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:hello-time', ge=1, le=10),
    ] = 2
    """
    The interval between periodic transmissions of configuration messages by designated ports
    """
    hold_count: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:hold-count', ge=1, le=10),
    ] = 6
    """
    The maximum number of BPDUs per second that the switch can send from an interface
    """
    max_age: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:max-age', ge=6, le=40),
    ] = 20
    """
    The maximum age of the information transmitted by the bridge when it is the root bridge
    """
    mst_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:mst-name',
            max_length=32,
            min_length=1,
        ),
    ] = None
    """
    The Configuration Name in the MST Configuration Identifier
    """
    mst_revision: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:mst-revision', ge=0, le=65535),
    ] = 0
    """
    The Revision Level in the MST Configuration Identifier
    """
    mst_max_hops: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:mst-max-hops', ge=1, le=255),
    ] = 20
    """
    The max hop determines the number of bridges in an MST region that a BPDU can traverse before it is discarded
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-state'),
    ] = None
    """
    Stp Operational status
    """
    bridge_id: Annotated[
        Optional[str], Field(alias='srl_nokia-system-protocols-mgmt-stp:bridge-id')
    ] = None
    """
    The identifier of the bridge

    The bridge identifier of the bridge in the configuration BPDUs
    transmitted for the segment to which the port is attached
    """
    designated_root: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:designated-root'),
    ] = None
    """
    The identifier of the designated bridge

    The bridge identifier of the bridge recorded as the
    root in the configuration BPDUs transmitted by the designated
    bridge for the segment to which the port is attached
    """
    root_port: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:root-port', ge=0, le=4294967295
        ),
    ] = None
    """
    The port number of the port which offers the lowest cost path from this bridge to the root bridge
    """
    root_cost: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:root-cost',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The cost of the path to the root as seen from this bridge
    """
    hold_time: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:hold-time', ge=0, le=255),
    ] = None
    """
    This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node
    """
    topology_changes: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:topology-changes',
            ge=0,
            le=18446744073709551615,
        ),
    ] = 0
    """
    The total number of topology changes detected by this bridge since the management entity was last reset or initialized
    """
    topology_change_active: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:topology-change-active'),
    ] = None
    """
    Indication topology change is currently in progress
    """
    time_since_topology_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:time-since-topology-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Time since last topology change was detected by bridge entity
    """
    oper_max_age: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:oper-max-age', ge=0, le=255),
    ] = None
    """
    The maximum age of the stp information learned
    """
    oper_hello_time: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:oper-hello-time', ge=0, le=255
        ),
    ] = None
    """
    The amount of time between the transmission of Configuration BPDUs
    """
    oper_forward_delay: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:oper-forward-delay',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The amount of time it takes to change its state when moving towards the forwarding state
    """
    cist_regional_root: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:cist-regional-root'),
    ] = None
    """
    The bridge identifier of the regional root of the CIST spanning tree
    """
    cist_internal_root_cost: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:cist-internal-root-cost',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The cost of the path to the CIST regional root bridge
    """
    cist_remaining_hop_count: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:cist-remaining-hop-count',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The remaining number of hops
    """
    cist_regional_root_port: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-protocols-mgmt-stp:cist-regional-root-port',
            ge=-2147483648,
            le=2147483647,
        ),
    ] = None
    """
    The port number of the port with the lowest cost path
    """
    trace_options: Annotated[
        Optional[TraceOptionsContainer4],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:trace-options'),
    ] = None
    mst_instance: Annotated[
        Optional[List[MstInstanceListEntry]],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:mst-instance'),
    ] = None
    interface: Annotated[
        Optional[List[InterfaceListEntry3]],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:interface'),
    ] = None


class MulticastForwardingInformationBaseContainer(BaseModel):
    """
    System Multicast Forwarding Information Base table
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    multicast_route: Annotated[
        Optional[List[MulticastRouteListEntry]],
        Field(alias='srl_nokia-system-multicast-mfib-table:multicast-route'),
    ] = None


class NetworkInstanceListEntry(BaseModel):
    """
    List of network instances to run a dhcp server in
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-dhcp-server:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    Reference to a configured network instance
    """
    dhcpv4: Annotated[
        Optional[Dhcpv4Container], Field(alias='srl_nokia-dhcp-server:dhcpv4')
    ] = None
    dhcpv6: Annotated[
        Optional[Dhcpv6Container], Field(alias='srl_nokia-dhcp-server:dhcpv6')
    ] = None


class PacketLinkQualificationContainer(BaseModel):
    """
    Top-level container for gNOI Packet Link Qualification profiles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    profile: Annotated[
        Optional[List[ProfileListEntry2]],
        Field(alias='srl_nokia-packet-link-qual:profile'),
    ] = None


class ParentDsContainer(BaseModel):
    """
    The parent data set of the clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    parent_port_identity: Annotated[
        Optional[ParentPortIdentityContainer],
        Field(alias='srl_nokia-sync:parent-port-identity'),
    ] = None
    grandmaster_identity: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:grandmaster-identity', max_length=8, min_length=8),
    ] = None
    """
    The clockIdentity of the grandmaster clock
    """
    grandmaster_clock_quality: Annotated[
        Optional[GrandmasterClockQualityContainer],
        Field(alias='srl_nokia-sync:grandmaster-clock-quality'),
    ] = None
    grandmaster_priority1: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:grandmaster-priority1', ge=0, le=255)
    ] = None
    """
    The priority1 attribute of the grandmaster clock
    """
    grandmaster_priority2: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:grandmaster-priority2', ge=0, le=255)
    ] = None
    """
    The priority2 attribute of the grandmaster clock
    """
    protocol_address: Annotated[
        Optional[ProtocolAddressContainer],
        Field(alias='srl_nokia-sync:protocol-address'),
    ] = None


class PathzContainer2(BaseModel):
    """
    Information relating to the active Pathz authorization policy instances

    This policies is provided by the gNSI gRPC service, and can be changed using the gNSI.Pathz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    collect_policy_success_failure_counters: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-configuration:collect-policy-success-failure-counters'),
    ] = False
    """
    Indicates whether the gNSI.pathz module should collect access counters information.
    """
    use_exclusively: Annotated[
        Optional[bool], Field(alias='srl_nokia-configuration:use-exclusively')
    ] = False
    """
    Indicates whether the Pathz authorization policy should be used exclusively for access authorization.

    If set to true, the Pathz authorization policy will be used exclusively, any statically configured RBAC
    rules will be ignored. If set to false, the Pathz authorization policy will be used together with the
    statically configured RBAC rules (evaluating both policies and taking the logical conjunction of the
    results).
    """
    policy: Annotated[
        Optional[List[PolicyListEntry]], Field(alias='srl_nokia-configuration:policy')
    ] = None


class RemoteContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    encap: Annotated[EnumerationEnum33, Field(alias='srl_nokia-mirroring:encap')]
    """
    Encapsulation to use for this mirror destination
    """
    network_instance: Annotated[
        str,
        Field(
            alias='srl_nokia-mirroring:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ]
    """
    network instance to intitiate remote mirror tunnel
    """
    tunnel_end_points: Annotated[
        Optional[TunnelEndPointsContainer],
        Field(alias='srl_nokia-mirroring:tunnel-end-points'),
    ] = None


class ServerGroupListEntry(BaseModel):
    """
    List of AAA server-groups in the system

    Each server group specifies a type, of which all servers must use. If using the 'local' type, then no servers may be specified.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-aaa:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    User defined name for the server group
    """
    type: Annotated[str, Field(alias='srl_nokia-aaa:type')]
    """
    AAA server type -- all servers in the group must be of this type
    """
    timeout: Annotated[
        Optional[int], Field(alias='srl_nokia-aaa:timeout', ge=1, le=3600)
    ] = 10
    """
    Set the timeout in seconds on responses from servers in this group
    """
    priv_lvl_authorization: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:priv-lvl-authorization')
    ] = False
    """
    Use TACACS+ priv-lvl based authorization

    If false, then authorization is skipped for TACACS+ users granting full admin access for those users.
    """
    health_check: Annotated[
        Optional[Union[HealthCheckLeaf1, EnumerationEnum12]],
        Field(alias='srl_nokia-aaa:health-check'),
    ] = '30'
    """
    RADIUS and TACACS+ health check interval
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-aaa:oper-state')
    ] = None
    """
    Details the operational state of the server group

    A server group is defined as being down if all servers in the server group are down.
    """
    tacacs: Annotated[
        Optional[TacacsContainer2], Field(alias='srl_nokia-aaa:tacacs')
    ] = None
    server: Annotated[
        Optional[List[ServerListEntry]], Field(alias='srl_nokia-aaa:server')
    ] = None


class Srv6Container(BaseModel):
    """
    Enter the srv6 context to configure locators and other SRv6 functionalities
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    source_address: Annotated[
        Optional[List[SourceAddressListEntry]],
        Field(alias='srl_nokia-srv6:source-address'),
    ] = None
    default_source_address: Annotated[
        str,
        Field(
            alias='srl_nokia-srv6:default-source-address',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$',
        ),
    ]
    """
    Default source address
    """
    micro_segment: Annotated[
        Optional[MicroSegmentContainer], Field(alias='srl_nokia-srv6:micro-segment')
    ] = None
    locator: Annotated[
        Optional[List[LocatorListEntry]], Field(alias='srl_nokia-srv6:locator')
    ] = None


class TimeRecoveryEngineContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    role: Annotated[
        Optional[EnumerationEnum113], Field(alias='srl_nokia-sync:role')
    ] = None
    clock_source: Annotated[
        Optional[ClockSourceContainer], Field(alias='srl_nokia-sync:clock-source')
    ] = None
    recovery_state: Annotated[
        Optional[EnumerationEnum115], Field(alias='srl_nokia-sync:recovery-state')
    ] = None
    """
    Specifies the current state of the time recovery engine in the PTP clock
    """
    state_last_changed: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:state-last-changed',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Specifies the last occurrence of a ptp state change for the time recovery engine
    """
    last_adjustment: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:last-adjustment',
            ge=-9223372036854775808,
            le=9223372036854775807,
        ),
    ] = None
    """
    Specifies the last adjustment in nanoseconds to the local time of the PTP clock
    """
    last_adjustment_timestamp: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:last-adjustment-timestamp',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time when last-adjustment was last calculated
    """
    statistics: Annotated[
        Optional[StatisticsContainer19], Field(alias='srl_nokia-sync:statistics')
    ] = None


class UdpExporterCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    udp_exporter: Annotated[
        Optional[UdpExporterContainer], Field(alias='srl_nokia-ipfix:udp-exporter')
    ] = None


class AaaContainer(BaseModel):
    """
    Top-level container for AAA services
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    authentication: Annotated[
        Optional[AuthenticationContainer], Field(alias='srl_nokia-aaa:authentication')
    ] = None
    authorization: Annotated[
        Optional[AuthorizationContainer], Field(alias='srl_nokia-aaa:authorization')
    ] = None
    accounting: Annotated[
        Optional[AccountingContainer], Field(alias='srl_nokia-aaa:accounting')
    ] = None
    server_group: Annotated[
        Optional[List[ServerGroupListEntry]], Field(alias='srl_nokia-aaa:server-group')
    ] = None


class BgpInstanceListEntry(BaseModel):
    """
    bgp-instance associated to this ethernet-segment
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance: Annotated[
        int,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:instance',
            ge=0,
            le=4294967295,
        ),
    ]
    designated_forwarder_role_last_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-role-last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the time at which the designated-forwarder role was changed.
    """
    designated_forwarder_activation_start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-activation-start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Indicates the time at which the designated-forwarder activation timer started.
    """
    designated_forwarder_activation_time: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-activation-time',
            ge=0,
            le=4294967295,
        ),
    ] = None
    """
    Indicates the number of seconds for the activation timer to run, for this node to become the designated forwarder for this bgp instance.
    """
    computed_designated_forwarder_candidates: Annotated[
        Optional[ComputedDesignatedForwarderCandidatesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:computed-designated-forwarder-candidates'
        ),
    ] = None


class BridgeTableContainer(BaseModel):
    """
    system bridge-table information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac_learning: Annotated[
        Optional[MacLearningContainer],
        Field(alias='srl_nokia-system-bridge-table:mac-learning'),
    ] = None
    mac_limit: Annotated[
        Optional[MacLimitContainer],
        Field(alias='srl_nokia-system-bridge-table:mac-limit'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer3],
        Field(alias='srl_nokia-system-bridge-table:statistics'),
    ] = None
    evpn: Annotated[
        Optional[EvpnContainer], Field(alias='srl_nokia-system-bridge-table-evpn:evpn')
    ] = None
    proxy_arp: Annotated[
        Optional[ProxyArpContainer],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:proxy-arp'),
    ] = None
    proxy_nd: Annotated[
        Optional[ProxyNdContainer],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:proxy-nd'),
    ] = None


class ConfigurationContainer(BaseModel):
    """
    Top-level container for configuration and state data related to the system configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    last_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    Date and time of the last successful commit

    Set to the time the configuration was loaded by management server, so is refreshed at boot time.
    """
    max_checkpoints: Annotated[
        Optional[int],
        Field(alias='srl_nokia-configuration:max-checkpoints', ge=1, le=255),
    ] = 10
    """
    The number of checkpoints kept by the system
    """
    max_candidates: Annotated[
        Optional[int],
        Field(alias='srl_nokia-configuration:max-candidates', ge=1, le=255),
    ] = 10
    """
    The maximum number of combined private and shared candidates
    """
    idle_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-configuration:idle-timeout', ge=0, le=65535),
    ] = 10080
    """
    The idle timeout of configuration candidates

    After this period of no activity, the candidate is emptied and removed from the system.
    """
    auto_checkpoint: Annotated[
        Optional[bool], Field(alias='srl_nokia-configuration:auto-checkpoint')
    ] = False
    """
    Configuration checkpoint will be automatically created after every successful commit (if set to true).
    """
    auto_save: Annotated[
        Optional[bool], Field(alias='srl_nokia-configuration:auto-save')
    ] = False
    """
    Configuration save will be automatically done after every successful commit (if set to true).
    """
    max_paths_per_subscription_request: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-configuration:max-paths-per-subscription-request',
            ge=1,
            le=500,
        ),
    ] = 36
    """
    The maximum number of paths that can be subscribed to in a single subscription request
    """
    checkpoint: Annotated[
        Optional[List[CheckpointListEntry]],
        Field(alias='srl_nokia-configuration:checkpoint'),
    ] = None
    session: Annotated[
        Optional[List[SessionListEntry3]],
        Field(alias='srl_nokia-configuration:session'),
    ] = None
    candidate: Annotated[
        Optional[List[CandidateListEntry]],
        Field(alias='srl_nokia-configuration:candidate'),
    ] = None
    commit: Annotated[
        Optional[List[CommitListEntry]], Field(alias='srl_nokia-configuration:commit')
    ] = None
    pathz: Annotated[
        Optional[PathzContainer2], Field(alias='srl_nokia-configuration:pathz')
    ] = None
    role: Annotated[
        Optional[List[RoleListEntry2]], Field(alias='srl_nokia-configuration-role:role')
    ] = None


class DefaultDsContainer(BaseModel):
    """
    The default data set of the PTP instance

    In the context of the protocol, this data set is required
    for an Ordinary Clock or Boundary Clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_type: Annotated[
        Optional[EnumerationEnum112], Field(alias='srl_nokia-sync:instance-type')
    ] = 'bc'
    """
    The type of PTP instance as per IEEE1588 standard

    For G.8275.1:
     oc is for T-GM,
     bc is for T-BC;
     T-TSC not supported since T-BC can be used for this role
    For G.8275.2:
     oc is for T-GM,
     bc is for T-BC-A and T-BC-P;
     T-TSC-A and T-TSC-P are not supported since T-BC-A or T-BC-P can be used for this role
    """
    instance_enable: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:instance-enable')
    ] = False
    """
    Enable PTP clock
    """
    clock_identity: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:clock-identity', max_length=8, min_length=8),
    ] = None
    """
    The clockIdentity of the local clock
    """
    number_ports: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:number-ports', ge=0, le=65535)
    ] = None
    """
    The number of PTP ports on the instance
    """
    clock_quality: Annotated[
        Optional[ClockQualityContainer], Field(alias='srl_nokia-sync:clock-quality')
    ] = None
    priority1: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:priority1', ge=0, le=255)
    ] = 128
    """
    The IEEE Std 1588 priority1 of the PTP instance

    Since priority1 is one of the first comparisons
    performed by the Best Master Clock Algorithm (BMCA).
    Range is 0-255.
    """
    priority2: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:priority2', ge=0, le=255)
    ] = 128
    """
    The IEEE Std 1588 priority2 of the PTP instance

    The priority2 member is compared by the Best Master
    Clock Algorithm (BMCA) after priority1 and clockQuality.
    Lower values take precedence.
    """
    domain_number: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:domain-number', ge=0, le=255)
    ] = None
    """
    The IEEE Std 1588 domainNumber of the PTP instance

    A domain consists of one or more PTP instances
    communicating with each other as defined by the
    protocol. A domain shall define the scope of PTP message
    communication, state, operations, data sets, and
    timescale. Therefore, each domain represents a distinct
    time.
    The default domain number is defined by the profile.
       itug8275dot1: 24
       itug8275dot2: 44
    """
    log_announce_interval: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:log-announce-interval', ge=-3, le=4)
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    This is the mean time interval between successive Announce messages.
    The default log announce interval is defined by the profile.
       itug8275dot1: -3 (8 messages per second)
       itug8275dot2: 1 (1 message every two seconds)
    """
    announce_receipt_timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:announce-receipt-timeout', ge=2, le=10),
    ] = 3
    """
    Sets the time limit for missed Announce packets before the master clock is deemed down

    This command configures the announceReceiptTimeout value for all peer associations.
    This defines the number of Announce message intervals that must expire with no received
    Announce messages before declaring an ANNOUNCE_RECEIPT_TIMEOUT event.
    """
    current_time: Annotated[
        Optional[CurrentTimeContainer], Field(alias='srl_nokia-sync:current-time')
    ] = None
    local_priority: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:local-priority', ge=1, le=255)
    ] = 128
    """
    The IEEE Std 1588 priority2 of the PTP instance

    The priority2 member is compared by the Best Master
    Clock Algorithm (BMCA) after priority1 and clockQuality.
    Lower values take precedence.
    """
    two_step_flag: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:two-step-flag')
    ] = None
    """
    Indicates if the clock is operating in two-step mode
    """
    statistics: Annotated[
        Optional[StatisticsContainer18], Field(alias='srl_nokia-sync:statistics')
    ] = None
    time_recovery_engine: Annotated[
        Optional[TimeRecoveryEngineContainer],
        Field(alias='srl_nokia-sync:time-recovery-engine'),
    ] = None
    freq_recovery_engine: Annotated[
        Optional[FreqRecoveryEngineContainer],
        Field(alias='srl_nokia-sync:freq-recovery-engine'),
    ] = None


class DestinationListEntry(BaseModel):
    """
    List of export destinations.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Key of this list.
    """
    destination_parameters: Annotated[
        UdpExporterCase, Field(alias='srl_nokia-ipfix:destination-parameters')
    ]


class DhcpServerContainer(BaseModel):
    """
    Configures the dhcp server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-dhcp-server:admin-state')
    ] = 'disable'
    """
    Globally enable or disable the dhcp server
    Disabling this will disable all dhcp servers.
    """
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry]],
        Field(alias='srl_nokia-dhcp-server:network-instance'),
    ] = None


class ExportingProcessListEntry(BaseModel):
    """
    Exporting Process of the Monitoring Device.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-ipfix:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    Key of this list.
    """
    exporting_process_id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ipfix:exporting-process-id', ge=0, le=4294967295),
    ] = None
    """
    The identifier of the Exporting Process.
    This parameter corresponds to the Information Element
    exportingProcessId.  Its occurrence helps to associate
    Exporting Process parameters with Exporing Process
    statistics exported by the Monitoring Device using the
    Exporting Process Reliability Statistics Template as
    defined by the IPFIX protocol specification.
    """
    export_mode: Annotated[
        Optional[str], Field(alias='srl_nokia-ipfix:export-mode')
    ] = 'parallel'
    """
    This parameter determines to which configured
    destination(s) the incoming Data Records are exported.
    """
    destination: Annotated[
        Optional[List[DestinationListEntry]], Field(alias='srl_nokia-ipfix:destination')
    ] = None
    options: Annotated[
        Optional[List[OptionsListEntry]], Field(alias='srl_nokia-ipfix:options')
    ] = None


class FreqReferencesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance: Annotated[
        Optional[List[InstanceListEntry2]], Field(alias='srl_nokia-sync:instance')
    ] = None


class InstanceListEntry3(BaseModel):
    """
    List of one or more PTP instances in the product (PTP Node)

    Each PTP instance represents a distinct instance of PTP
    implementation (i.e. distinct Ordinary Clock, Boundary Clock,
    or Transparent Clock), maintaining a distinct time.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_index: Annotated[
        int, Field(alias='srl_nokia-sync:instance-index', ge=1, le=2)
    ]
    """
    The instance index of the current PTP instance

    This instance index is used for management purposes
    only.  This instance index does not represent the PTP
    domain number and is not used in PTP messages.
    """
    default_ds: Annotated[
        Optional[DefaultDsContainer], Field(alias='srl_nokia-sync:default-ds')
    ] = None
    current_ds: Annotated[
        Optional[CurrentDsContainer], Field(alias='srl_nokia-sync:current-ds')
    ] = None
    parent_ds: Annotated[
        Optional[ParentDsContainer], Field(alias='srl_nokia-sync:parent-ds')
    ] = None
    time_properties_ds: Annotated[
        Optional[TimePropertiesDsContainer],
        Field(alias='srl_nokia-sync:time-properties-ds'),
    ] = None
    port_ds_interface_list: Annotated[
        Optional[List[PortDsInterfaceListListEntry]],
        Field(alias='srl_nokia-sync:port-ds-interface-list'),
    ] = None
    port_ds_cfg_ip_list: Annotated[
        Optional[List[PortDsCfgIpListListEntry]],
        Field(alias='srl_nokia-sync:port-ds-cfg-ip-list'),
    ] = None
    port_ds_dsc_ip_list: Annotated[
        Optional[List[PortDsDscIpListListEntry]],
        Field(alias='srl_nokia-sync:port-ds-dsc-ip-list'),
    ] = None
    port_ds_sync0: Annotated[
        Optional[PortDsSync0Container2], Field(alias='srl_nokia-sync:port-ds-sync0')
    ] = None
    port_ds_gnss: Annotated[
        Optional[PortDsGnssContainer], Field(alias='srl_nokia-sync:port-ds-gnss')
    ] = None


class InterfaceListEntry4(BaseModel):
    """
    List of interfaces on which LLDP can be enabled
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='srl_nokia-lldp:name')]
    """
    Reference to the LLDP Ethernet interface
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-lldp:admin-state')
    ] = 'enable'
    """
    Enable or disable LLDP on the interface
    """
    bgp_auto_discovery: Annotated[
        Optional[BgpAutoDiscoveryContainer2],
        Field(alias='srl_nokia-lldp:bgp-auto-discovery'),
    ] = None
    lldp_med: Annotated[
        Optional[LldpMedContainer2], Field(alias='srl_nokia-lldp:lldp-med')
    ] = None
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-lldp:oper-state')
    ] = None
    """
    Details the operational state of LLDP on the interface
    """
    statistics: Annotated[
        Optional[StatisticsContainer16], Field(alias='srl_nokia-lldp:statistics')
    ] = None
    neighbor: Annotated[
        Optional[List[NeighborListEntry]], Field(alias='srl_nokia-lldp:neighbor')
    ] = None


class IpfixContainer(BaseModel):
    """
    Top-level node of the IPFIX configuration
    data model.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-ipfix:admin-state')
    ] = 'disable'
    """
    Administratively enable or disable IPFIX for the system
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-ipfix:oper-state')
    ] = None
    """
    Details if IPFIX is operationally available
    """
    observation_point: Annotated[
        Optional[List[ObservationPointListEntry]],
        Field(alias='srl_nokia-ipfix:observation-point'),
    ] = None
    selection_process: Annotated[
        Optional[List[SelectionProcessListEntry]],
        Field(alias='srl_nokia-ipfix:selection-process'),
    ] = None
    cache: Annotated[
        Optional[List[CacheListEntry]], Field(alias='srl_nokia-ipfix:cache')
    ] = None
    exporting_process: Annotated[
        Optional[List[ExportingProcessListEntry]],
        Field(alias='srl_nokia-ipfix:exporting-process'),
    ] = None


class LldpContainer(BaseModel):
    """
    Top-level container for LLDP configuration and state data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace_options: Annotated[
        Optional[List[EnumerationEnum86]], Field(alias='srl_nokia-lldp:trace-options')
    ] = []
    """
    LLDP trace options
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-lldp:admin-state')
    ] = 'enable'
    """
    Enable or disable LLDP at the system level
    """
    hello_timer: Annotated[
        Optional[int],
        Field(alias='srl_nokia-lldp:hello-timer', ge=0, le=18446744073709551615),
    ] = 30
    """
    System level hello timer for the LLDP protocol
    """
    hold_multiplier: Annotated[
        Optional[int], Field(alias='srl_nokia-lldp:hold-multiplier', ge=0, le=255)
    ] = 4
    """
    System level hold multiplier, used to define neighbor aging

    This field defines how many hellos need to be missed before
    a neighbor is aged out.

    This field also is used along with the 'hello-timer' field
    to define the TTL TLV in outgoing LLDPDUs.
    """
    bgp_auto_discovery: Annotated[
        Optional[BgpAutoDiscoveryContainer],
        Field(alias='srl_nokia-lldp:bgp-auto-discovery'),
    ] = None
    system_name: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:system-name', max_length=255, min_length=0),
    ] = None
    """
    The systems administratively assigned name

    The system name field shall contain an alpha-numeric string
    that indicates the system's administratively assigned name.
    The system name should be the system's fully qualified domain
    name.
    """
    system_description: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:system-description', max_length=255, min_length=0),
    ] = None
    """
    Field detailing system description, including name and versions

    The system description field shall contain an alpha-numeric
    string that is the textual description of the network entity.
    The system description should include the full name and
    version identification of the system's hardware type,
    software operating system, and networking software.
    """
    chassis_id: Annotated[Optional[str], Field(alias='srl_nokia-lldp:chassis-id')] = (
        None
    )
    """
    The Chassis ID is a mandatory TLV which identifies the
    chassis component of the endpoint identifier associated with
    the transmitting LLDP agent
    """
    chassis_id_type: Annotated[
        Optional[EnumerationEnum87], Field(alias='srl_nokia-lldp:chassis-id-type')
    ] = 'MAC_ADDRESS'
    """
    The source for the chassis identifier string

    It is an enumerator defined by the LldpChassisIdSubtype object
    from IEEE 802.1AB MIB.
    """
    management_address: Annotated[
        Optional[List[ManagementAddressListEntry]],
        Field(alias='srl_nokia-lldp:management-address'),
    ] = None
    lldp_med: Annotated[
        Optional[LldpMedContainer], Field(alias='srl_nokia-lldp:lldp-med')
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer15], Field(alias='srl_nokia-lldp:statistics')
    ] = None
    interface: Annotated[
        Optional[List[InterfaceListEntry4]], Field(alias='srl_nokia-lldp:interface')
    ] = None


class MirrorDestinationContainer(BaseModel):
    """
    Configure mirror destination
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    slice_size: Annotated[
        Optional[int], Field(alias='srl_nokia-mirroring:slice-size', ge=0, le=512)
    ] = 0
    """
    Specify mirrored pacekt slice size. This value specifies number of bytes that should be mirrored from the beginning of the original data packet.
    """
    local: Annotated[Optional[str], Field(alias='srl_nokia-mirroring:local')] = None
    """
    subinterface of type local-mirror-dest used as local mirror destination
    """
    remote: Annotated[
        Optional[RemoteContainer], Field(alias='srl_nokia-mirroring:remote')
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer8], Field(alias='srl_nokia-mirroring:statistics')
    ] = None


class MirroringInstanceListEntry(BaseModel):
    """
    Mirroring instances configured on the local system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-mirroring:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    A unique name identifying the mirroring instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3], Field(alias='srl_nokia-mirroring:admin-state')
    ] = 'enable'
    """
    This leaf contains the configured, desired state of the mirroring instance.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4], Field(alias='srl_nokia-mirroring:oper-state')
    ] = None
    """
    This leaf contains the operational state of the mirroring instance.
    """
    description: Annotated[
        Optional[str],
        Field(alias='srl_nokia-mirroring:description', max_length=255, min_length=1),
    ] = None
    """
    A user-entered description of this mirroring instance.
    """
    oper_down_reason: Annotated[
        Optional[EnumerationEnum29], Field(alias='srl_nokia-mirroring:oper-down-reason')
    ] = None
    """
    The reason for the mirroring instance being operational down
    """
    mirror_source: Annotated[
        Optional[MirrorSourceContainer],
        Field(alias='srl_nokia-mirroring:mirror-source'),
    ] = None
    mirror_destination: Annotated[
        Optional[MirrorDestinationContainer],
        Field(alias='srl_nokia-mirroring:mirror-destination'),
    ] = None


class MirroringContainer(BaseModel):
    """
    Top level container for configuration and operational state for mirroring
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mirroring_instance: Annotated[
        Optional[List[MirroringInstanceListEntry]],
        Field(alias='srl_nokia-mirroring:mirroring-instance'),
    ] = None


class NetworkInstanceListEntry2(BaseModel):
    """
    network instance associated to this ethernet-segment
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:name'
        ),
    ]
    bgp_instance: Annotated[
        Optional[List[BgpInstanceListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:bgp-instance'
        ),
    ] = None


class PtpContainer3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ptp_profile: Annotated[
        Optional[EnumerationEnum111], Field(alias='srl_nokia-sync:ptp-profile')
    ] = 'itug8275dot1'
    """
    Specifies the PTP profile mode for the PTP clock
    """
    timing_source_net_inst: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:timing-source-net-inst',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ] = None
    """
    Network instance to be used for configured peers

    This is the network instance that will be used to provide timing into the local clock via PTP over IP.
    """
    instance: Annotated[
        Optional[List[InstanceListEntry3]], Field(alias='srl_nokia-sync:instance')
    ] = None


class SyncContainer(BaseModel):
    """
    Context to configure sync parameters and report sessions state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    freq_references: Annotated[
        Optional[FreqReferencesContainer], Field(alias='srl_nokia-sync:freq-references')
    ] = None
    freq_clock: Annotated[
        Optional[FreqClockContainer], Field(alias='srl_nokia-sync:freq-clock')
    ] = None
    ptp: Annotated[Optional[PtpContainer3], Field(alias='srl_nokia-sync:ptp')] = None
    gnss: Annotated[Optional[GnssContainer2], Field(alias='srl_nokia-sync:gnss')] = None
    one_pps: Annotated[
        Optional[OnePpsContainer], Field(alias='srl_nokia-sync:one-pps')
    ] = None


class AssociationContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry2]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:network-instance'
        ),
    ] = None


class EthernetSegmentListEntry(BaseModel):
    """
    Ethernet Segment configuration and state.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        str,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ]
    """
    A unique name identifying the ethernet segment.
    """
    type: Annotated[
        Optional[EnumerationEnum60],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:type'
        ),
    ] = 'none'
    """
    Ethernet Segment type.
    """
    admin_state: Annotated[
        Optional[EnumerationEnum3],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:admin-state'
        ),
    ] = 'disable'
    """
    Admin state of the ethernet segment
    """
    oper_state: Annotated[
        Optional[EnumerationEnum4],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-state'
        ),
    ] = None
    """
    This leaf contains the operational state of ethernet segment.
    """
    esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
        ),
    ] = None
    """
    The 10-byte Ethernet Segment Identifier of the ethernet segment.

    ESI-0 or MAX-ESI values are not allowed.
    ESI values with bytes 1-6 all zeros are not allowed since they would produce a null ESI-import route-target.
    """
    use_esi_label: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:use-esi-label'
        ),
    ] = True
    """
    Indicates if an ESI label is used for the ethernet segment

    When set to true, the ESI label is used for split-horizon filtering within the Ethernet Segment. 'True' is mandatory for
    all-active multi-homing mode Ethernet Segments connected to MAC-VRF network-instances using MPLS encapsulation. For all-active
    Ethernet Segments connected to VPWS network-instances with any encapsulation or MAC-VRFs using VXLAN encapsulation, as well as
    for single-active Ethernet Segments, the use of the ESI label is optional.
    """
    oper_esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
        ),
    ] = None
    """
    The operational Ethernet Segment Identifier used in the ethernet segment.
    """
    esi_label: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi-label',
            ge=16,
            le=1048575,
        ),
    ] = None
    """
    The esi label allocated for this ethernet-segment.

    The esi-label is advertised by the EVPN Auto-Discovery-Ethernet-Segment
    Advertisement routes and it is expected on received EVPN packets
    that were generated as multicast packets from this ethernet-segments peers.
    """
    interface_association: Annotated[
        Optional[Union[Layer2InterfaceCase, Layer3NextHopCase]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:interface-association'
        ),
    ] = None
    multi_homing_mode: Annotated[
        Optional[EnumerationEnum61],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:multi-homing-mode'
        ),
    ] = 'all-active'
    """
    Multi-homing mode of the ethernet segment.

    The state of this leaf can be different than the configured value in cases where the configured value is 'all-active' and the
    multi-homing mode advertised by the ES peers in the AD per-ES routes is 'single-active'. In this case, the state of this
    leaf will show 'single-active'.

    When an Ethernet Segment (ES) is configured as either all-active-no-esi-label or single-active-no-esi-label, no ESI (Ethernet
    Segment Identifier) label is allocated. This configuration is suitable for Ethernet segments connected exclusively to VXLAN or
    VPWS network instances.
    """
    oper_multi_homing_mode: Annotated[
        Optional[EnumerationEnum61],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-multi-homing-mode'
        ),
    ] = None
    """
    Operational Multi-homing mode of the ethernet segment.

    The state of this leaf can be different than the configured value in cases where the configured value is 'all-active' and the
    multi-homing mode advertised by the ES peers in the AD per-ES routes is 'single-active'. In this case, the state of this leaf
    will show 'single-active'.
    """
    advertise_ifl_host_ad_routes: Annotated[
        Optional[AdvertiseIflHostAdRoutesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:advertise-ifl-host-ad-routes'
        ),
    ] = None
    df_election: Annotated[
        Optional[DfElectionContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:df-election'
        ),
    ] = None
    routes: Annotated[
        Optional[RoutesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:routes'
        ),
    ] = None
    autodiscovery_per_ethernet_segment_routes: Annotated[
        Optional[AutodiscoveryPerEthernetSegmentRoutesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:autodiscovery-per-ethernet-segment-routes'
        ),
    ] = None
    ethernet_segment_routes: Annotated[
        Optional[EthernetSegmentRoutesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segment-routes'
        ),
    ] = None
    oper_down_reason: Annotated[
        Optional[EnumerationEnum66],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-down-reason'
        ),
    ] = None
    """
    The reason for the ethernet-segment being down in the bgp-instance
    """
    association: Annotated[
        Optional[AssociationContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:association'
        ),
    ] = None


class BgpInstanceListEntry2(BaseModel):
    """
    bgp global instances configured in net-instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        int,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:id',
            ge=1,
            le=2,
        ),
    ]
    """
    The index of the bgp-vpn instance
    """
    ethernet_segment: Annotated[
        Optional[List[EthernetSegmentListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segment'
        ),
    ] = None


class EthernetSegmentsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    timers: Annotated[
        Optional[TimersContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:timers'
        ),
    ] = None
    bgp_instance: Annotated[
        Optional[List[BgpInstanceListEntry2]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:bgp-instance'
        ),
    ] = None


class EvpnContainer3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ethernet_segments: Annotated[
        Optional[EthernetSegmentsContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segments'
        ),
    ] = None
    multicast: Annotated[
        Optional[MulticastContainer2],
        Field(alias='srl_nokia-system-network-instance-bgp-evpn-multicast:multicast'),
    ] = None


class ProtocolsContainer(BaseModel):
    """
    The routing protocols that are enabled for this
    network-instance.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    evpn: Annotated[
        Optional[EvpnContainer3], Field(alias='srl_nokia-system-network-instance:evpn')
    ] = None
    bgp_vpn: Annotated[
        Optional[BgpVpnContainer],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:bgp-vpn'),
    ] = None
    mgmt_stp: Annotated[
        Optional[List[MgmtStpListEntry]],
        Field(alias='srl_nokia-system-protocols-mgmt-stp:mgmt-stp'),
    ] = None


class NetworkInstanceContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    protocols: Annotated[
        Optional[ProtocolsContainer],
        Field(alias='srl_nokia-system-network-instance:protocols'),
    ] = None


class SystemContainer2(BaseModel):
    """
    Enclosing container for system management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace_options: Annotated[
        Optional[List[EnumerationEnum]], Field(alias='srl_nokia-system:trace-options')
    ] = []
    """
    Management server trace options
    """
    tls: Annotated[Optional[TlsContainer], Field(alias='srl_nokia-tls:tls')] = None
    ssh_server: Annotated[
        Optional[List[SshServerListEntry]], Field(alias='srl_nokia-ssh:ssh-server')
    ] = None
    aaa: Annotated[Optional[AaaContainer], Field(alias='srl_nokia-aaa:aaa')] = None
    grpc_server: Annotated[
        Optional[List[GrpcServerListEntry]], Field(alias='srl_nokia-grpc:grpc-server')
    ] = None
    ndk_server: Annotated[
        Optional[NdkServerContainer], Field(alias='srl_nokia-ndk:ndk-server')
    ] = None
    license: Annotated[
        Optional[List[LicenseListEntry]], Field(alias='srl_nokia-license:license')
    ] = None
    information: Annotated[
        Optional[InformationContainer], Field(alias='srl_nokia-system-info:information')
    ] = None
    bridge_table: Annotated[
        Optional[BridgeTableContainer],
        Field(alias='srl_nokia-system-bridge-table:bridge-table'),
    ] = None
    netconf_server: Annotated[
        Optional[List[NetconfServerListEntry]],
        Field(alias='srl_nokia-netconf-server:netconf-server'),
    ] = None
    logging: Annotated[
        Optional[LoggingContainer], Field(alias='srl_nokia-logging:logging')
    ] = None
    datapath: Annotated[
        Optional[DatapathContainer], Field(alias='srl_nokia-system-datapath:datapath')
    ] = None
    utilization: Annotated[
        Optional[UtilizationContainer],
        Field(alias='srl_nokia-system-utilization:utilization'),
    ] = None
    mirroring: Annotated[
        Optional[MirroringContainer], Field(alias='srl_nokia-mirroring:mirroring')
    ] = None
    dhcp_server: Annotated[
        Optional[DhcpServerContainer], Field(alias='srl_nokia-dhcp-server:dhcp-server')
    ] = None
    cli: Annotated[Optional[CliContainer2], Field(alias='srl_nokia-system-cli:cli')] = (
        None
    )
    name: Annotated[
        Optional[NameContainer], Field(alias='srl_nokia-system-name:name')
    ] = None
    multicast: Annotated[
        Optional[MulticastContainer],
        Field(alias='srl_nokia-system-multicast:multicast'),
    ] = None
    mpls: Annotated[
        Optional[MplsContainer], Field(alias='srl_nokia-mpls-label-management:mpls')
    ] = None
    multicast_forwarding_information_base: Annotated[
        Optional[MulticastForwardingInformationBaseContainer],
        Field(
            alias='srl_nokia-system-multicast-mfib-table:multicast-forwarding-information-base'
        ),
    ] = None
    authentication: Annotated[
        Optional[AuthenticationContainer2],
        Field(alias='srl_nokia-keychains:authentication'),
    ] = None
    configuration: Annotated[
        Optional[ConfigurationContainer],
        Field(alias='srl_nokia-configuration:configuration'),
    ] = None
    protection_policies: Annotated[
        Optional[ProtectionPoliciesContainer],
        Field(alias='srl_nokia-protection-policies:protection-policies'),
    ] = None
    srv6: Annotated[Optional[Srv6Container], Field(alias='srl_nokia-srv6:srv6')] = None
    ra_guard_policy: Annotated[
        Optional[List[RaGuardPolicyListEntry]],
        Field(alias='srl_nokia-ra_guard:ra-guard-policy'),
    ] = None
    network_instance: Annotated[
        Optional[NetworkInstanceContainer2],
        Field(alias='srl_nokia-system-network-instance:network-instance'),
    ] = None
    fhs_classid_mgmt: Annotated[
        Optional[FhsClassidMgmtContainer],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:fhs-classid-mgmt'),
    ] = None
    first_hop_security_policy: Annotated[
        Optional[List[FirstHopSecurityPolicyListEntry]],
        Field(
            alias='srl_nokia-first-hop-security-ip-mac-binding:first-hop-security-policy'
        ),
    ] = None
    fhs_ip_mac_bindings: Annotated[
        Optional[FhsIpMacBindingsContainer],
        Field(alias='srl_nokia-first-hop-security-ip-mac-binding:fhs-ip-mac-bindings'),
    ] = None
    app_management: Annotated[
        Optional[AppManagementContainer],
        Field(alias='srl_nokia-app-mgmt:app-management'),
    ] = None
    maintenance: Annotated[
        Optional[MaintenanceContainer],
        Field(alias='srl_nokia-maintenance-mode:maintenance'),
    ] = None
    banner: Annotated[
        Optional[BannerContainer], Field(alias='srl_nokia-system-banner:banner')
    ] = None
    mtu: Annotated[Optional[MtuContainer], Field(alias='srl_nokia-mtu:mtu')] = None
    tftp_server: Annotated[
        Optional[TftpServerContainer], Field(alias='srl_nokia-tftp:tftp-server')
    ] = None
    lawful_intercept: Annotated[
        Optional[LawfulInterceptContainer],
        Field(alias='srl_nokia-lawful-intercept:lawful-intercept'),
    ] = None
    lldp: Annotated[Optional[LldpContainer], Field(alias='srl_nokia-lldp:lldp')] = None
    boot: Annotated[Optional[BootContainer], Field(alias='srl_nokia-boot:boot')] = None
    event_handler: Annotated[
        Optional[EventHandlerContainer],
        Field(alias='srl_nokia-event-handler:event-handler'),
    ] = None
    json_rpc_server: Annotated[
        Optional[JsonRpcServerContainer],
        Field(alias='srl_nokia-json-rpc:json-rpc-server'),
    ] = None
    dhcp_server_guard_policy: Annotated[
        Optional[List[DhcpServerGuardPolicyListEntry]],
        Field(alias='srl_nokia-dhcp-server-guard:dhcp-server-guard-policy'),
    ] = None
    ipfix: Annotated[Optional[IpfixContainer], Field(alias='srl_nokia-ipfix:ipfix')] = (
        None
    )
    packet_link_qualification: Annotated[
        Optional[PacketLinkQualificationContainer],
        Field(alias='srl_nokia-packet-link-qual:packet-link-qualification'),
    ] = None
    lacp: Annotated[Optional[LacpContainer], Field(alias='srl_nokia-lacp:lacp')] = None
    l2cp_transparency: Annotated[
        Optional[L2cpTransparencyContainer],
        Field(alias='srl_nokia-interfaces-l2cp:l2cp-transparency'),
    ] = None
    sync: Annotated[Optional[SyncContainer], Field(alias='srl_nokia-sync:sync')] = None
    dot1x: Annotated[Optional[Dot1xContainer], Field(alias='srl_nokia-dot1x:dot1x')] = (
        None
    )


class Model(BaseModel):
    """
    Initialize an instance of this class and serialize it to JSON; this results in a RESTCONF payload.

    ## Tips
    Initialization:
    - all values have to be set via keyword arguments
    - if a class contains only a `root` field, it can be initialized as follows:
        - `member=MyNode(root=<value>)`
        - `member=<value>`

    Serialziation:
    - `exclude_defaults=True` omits fields set to their default value (recommended)
    - `by_alias=True` ensures qualified names are used (necessary)
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    system: Annotated[
        Optional[SystemContainer2], Field(alias='srl_nokia-system:system')
    ] = None


if __name__ == "__main__":
    model = Model(
        # <Initialize model here>
    )

    restconf_payload = model.model_dump_json(
        exclude_defaults=True, by_alias=True, indent=2
    )

    print(f"Generated output: {restconf_payload}")

    # Send config to network device:
    # from pydantify.utility import restconf_patch_request
    # restconf_patch_request(url='...', user_pw_auth=('usr', 'pw'), data=restconf_payload)