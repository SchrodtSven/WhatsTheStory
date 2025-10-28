# List

```mermaid
flowchart LR
    43 -- next --> 98
    98 -- next --> 33
    33 -- next --> 666
    666 -- next --> 23
    23 --x Null@{shape: cross-circ}

    classDef someclass fill:#f96
```


 33 -- next --> 666@{ shape: notch-rect }