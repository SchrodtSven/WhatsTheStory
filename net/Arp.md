# ARP Address Resolution Protocol

[RFC 6747](https://datatracker.ietf.org/doc/html/rfc6747)

```mermaid
---
title: "ILNPv4 ARP Request packet format"
---
packet
0-15: "Hardware Type"
16-31: "Protocol Type"
+8: "Hardware Address Length"
+8: "Protocol Address Length"
+16: "OP"
+32: "S_HA Sender Hardware Address (*)"
+16: "S_L32 Sender L32 (* same as Sender IPv4 address for ARP)"
+16: "S_NID Sender Node Identifier (8 bytes)"
+16: "S_NID Sender Node Identifier (8 bytes)"
+16: "T_HA Target Hardware Address (*)"
+32: "T_L32 Target L32 (* same as Target IPv4 address for ARP)"
+32: "T_NID Target Node Identifier (8 bytes)"
```

- HT Hardware Type (*)
- PT Protocol Type (*)
- HAL Hardware Address Length (*)
- PAL Protocol Address Length (uses new value 12)
- OP Operation Code (uses experimental value OP_EXP1=24)
- S_HA Sender Hardware Address (*)
- S_L32 Sender L32 (* same as Sender IPv4 address for ARP)
- S_NID Sender Node Identifier (8 bytes)
- T_HA Target Hardware Address (*)
- T_L32 Target L32 (* same as Target IPv4 address for ARP)
- T_NID Target Node Identifier (8 bytes)

