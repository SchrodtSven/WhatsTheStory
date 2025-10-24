# Multi Tier Architektur 

## Client-Server Model


```mermaid
---
config:
  look: handDrawn
  theme: neutral
---
sequenceDiagram
autonumber
    participant UserAgent@{ "type" : "boundary"}
    participant Webserver@{ "type" : "control" }
    participant ApplicationServer@{ "type" : "queue" }
    participant RDBMS@{ "type" : "database" }
    UserAgent->>Webserver: http://Loki/Api/Entry/items/new 
    Webserver->>ApplicationServer: get data for product ABC
    ApplicationServer->>RDBMS:SQL
    RDBMS->>ApplicationServer: Send result set
    ApplicationServer->>Webserver: Resond with data
    Webserver->>UserAgent: HTTP Response (JSON Payload or HTML Payload etc.)
    
```
