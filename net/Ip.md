# Internet Protocol

This article is about **IP (*V.6*)** as descibed in [RFC 8200](https://datatracker.ietf.org/doc/html/rfc8200)

## Header


```mermaid
---
title: "IPv6 Header Format"
---
packet
+4: "Version"
+8: "Traffic class"
+20: "Flow Label"
+16: "Payload Length"
+8: "Next Header"
+8: "Hop Limit"
+128: "Source Address"
+128: "Destination Address"

```

## Extension Header

Extension headers are numbered from IANA IP Protocol Numbers [IANA-PN](https://datatracker.ietf.org/doc/html/rfc8200#ref-IANA-PN)

## Options


``` mermaid
packet
+8: "OptionType"
+8: "Opt. Data Len"
+24: "Opt. Dta ( Variable-length field)"
 ```



## Message Formats

### Router Solicitation Message Format

``` mermaid
packet
+8: "Type"
+8: "Code"
+16: "Checksum"  
+32: "Reserved"
+23: "Options (var. len) .."
```

### Router Advertisement Message Format

Routers send messages (<i>'Advertisements'</i>) periodically, or in response to <i>Router Solicitations</i>.


``` mermaid
packet
+8: "Type"
+8: "Code"
+16: "Checksum"  
+32: "Reachable Time"
+32: "Retrans Timer"
```






 ## Address stuff

 ### Neighbor Discovery Protocol

 As described in [Request for Comments: 4861 ](https://datatracker.ietf.org/doc/html/rfc4861) nodes on the same link use Neighbor Discovery to
   - determine each other's link-layer
   - addresses
   - find routers
   - maintain info on reachability 


#### Router Solicitation – Type 133