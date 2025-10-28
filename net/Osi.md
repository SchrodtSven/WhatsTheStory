# Open Systems Interconnection model

```mermaid
---
config:
  look: handDrawn
  theme: neutral
---
block
  columns 3
  7. Application .7
  6. Presentation .6
  5. Session .5
  4. Transport .4
  3. Network .3
  2. Data_Link .2
  1. Physical .1

  classDef app fill:#696,stroke:#333;
  classDef transp fill:#969,stroke:#333;
  class 7.,6.,5. app
  class 1.,2.,3.,4. transp

```
