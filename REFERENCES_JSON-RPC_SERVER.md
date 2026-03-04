# REFERENCES JSON-RPC SERVER


## Quick start with clab
SRL_VERSION=25.10.1 SRL_TYPE=ixr-d2l clab deploy -c -t srlinux.dev/clab-srl

SRL_VERSION=25.10.1 SRL_TYPE=ixr-d2l clab destroy -c -t srlinux.dev/clab-srl

**NOTE:** IXR-D2L platform has 58 ports (48 SFP28, 8 QSFP28, 2 SFP+), IXR-D3L platform has 34 ports (32 QSFP28, 2 SFP+)

```
name: srl
# node name will be srl unless overridden by CLAB_PREFIX
prefix: ${CLAB_PREFIX:=""}

topology:
  nodes:
    srl:
      kind: nokia_srlinux
      image: ${SRL_IMAGE:=ghcr.io/nokia/srlinux}:${SRL_VERSION:=latest}
      type: ${SRL_TYPE:=ixr-d3l}
```

## Start with docker container
docker run -t -d --rm --privileged   -u 0:0   --name leaf1 ghcr.io/nokia/srlinux:25.10.1   sudo bash /opt/srlinux/bin/sr_linux

OR from the guide
**REF:** https://documentation.nokia.com/srlinux/25-10/books/software-install/install-containers.html#ariaid-title3
sudo docker run -t -d --rm --privileged \ -u 0:0 \ -v srl23-7-1.json:/etc/opt/srlinux/config.json \ --name srlinux ghcr.io/nokia/srlinux:23.7.1 \ sudo bash /opt/srlinux/bin/sr_linux

OR using topology file
```
cat >> topo_d2l.yml << EOF
platform:
  type: ixr-d2l
EOF
```
docker run -d --name srlinux \
  --privileged \
  -v "$(pwd)/topo_d2l.yml:/tmp/topology.yml" \
  -u "$(id -u):$(id -g)" \
  ghcr.io/nokia/srlinux:25.10.1 \
  sudo bash /opt/srlinux/bin/sr_linux


## Configure
### json-rpc server
    ```
    enter candidate
    system json-rpc-server admin-state enable network-instance mgmt http admin-state enable
    commit stay
    ```
    OR
    ```
    "srl_nokia-json-rpc:json-rpc-server": {
        "admin-state": "enable",
        "network-instance": [
            {
            "name": "mgmt",
            "http": {
                "admin-state": "enable"
            }
            }
        ]
        }
    ```
### acl

    ```
    {
        "sequence-id": 158,
        "description": "Containerlab-added rule: Accept incoming HTTP(JSON-RPC) when the other host initiates the TCP connection",
        "match": {
            "ipv4": {
            "protocol": "tcp"
            },
            "transport": {
            "destination-port": {
                "operator": "eq",
                "value": 80
            }
            }
        },
        "action": {
            "accept": {

            }
        }
        },
        {
        "sequence-id": 160,
        "description": "Accept incoming HTTP(JSON-RPC) when this router initiates the TCP connection",
        "match": {
            "ipv4": {
            "protocol": "tcp"
            },
            "transport": {
            "source-port": {
                "operator": "eq",
                "value": 80
            }
            }
        },
        "action": {
            "accept": {

            }
        }
    }
    ```

## Verification

```
curl -s 'http://admin:NokiaSrl1!@172.17.0.2/jsonrpc' -d @- <<EOF | jq
{
    "jsonrpc": "2.0",
    "id": 0,
    "method": "get",
    "params": {
        "commands": [
            {
                "path": "/system/information/version",
                "datastore": "state"
            }
        ]
    }
}
EOF
```

## Revert

docker exec ${name} sr_cli /tools system configuration checkpoint clab-initial revert
docker exec leaf1 sr_cli /tools system configuration checkpoint clab-initial revert
docker exec srl sr_cli /tools system configuration checkpoint clab-initial revert

REF:
https://learn.srlinux.dev/tutorials/programmability/json-rpc/basics/
https://github.com/srl-labs/pydantic-srlinux/blob/main/example/revert.sh
https://containerlab.dev/manual/kinds/srl/#container-configuration

