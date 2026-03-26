# Design Pattern: Creator

## Class diagram

<b>Creator</b> is a <i>creational</i> design pattern
- constructing complex objects
- producing different types and representations
- using a base construction code


```mermaid
---
title: Creator
---
classDiagram
     note "Example diagram for pattern 'Creator'"

    class Creator
    <<interface>> Creator
    Creator : + reset()
    Creator : + setAttr(string attrNm, mixed value)

    class Architect {
      + Architect(string type, Creator instance)
      + getResults()
    }


    class Foo {
        + reset()
        + setAttr(string attrNm, mixed value)
        - debug()
    }

    class Bar {
        + reset()
        + setAttr(string attrNm, mixed value)
        - debug()
    }
    
    Creator <|--  Bar: implements
    Creator <|-- Foo : implements
    Architect ..|> Creator: composes

    note for Architect "new Architect ('Foo', new Creator())"
```


## Implementations


### Java

### PHP

### Python 
