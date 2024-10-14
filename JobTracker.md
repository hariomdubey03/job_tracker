

# JobTracker

Base URLs: http://localhost:8000

# Authentication

# Candidates

## GET Search

GET /candidates/search

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|name|query|string| yes |none|

> Response Examples

```json
{
  "message": "Candidates found successfully",
  "data": [
    {
      "candidate_id": 1,
      "name": "Ajay Kumar Yadav"
    },
    {
      "candidate_id": 2,
      "name": "Ajay Kumar"
    },
    {
      "candidate_id": 4,
      "name": "Kumar Yadav"
    },
    {
      "candidate_id": 3,
      "name": "Ajay Yadav"
    },
    {
      "candidate_id": 5,
      "name": "Ramesh Yadav"
    },
    {
      "candidate_id": 6,
      "name": "Ajay Singh"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|[object]|true|none||none|
|»» candidate_id|integer|true|none||none|
|»» name|string|true|none||none|

## POST Add

POST /candidates/create

> Body Parameters

```json
{
  "name": "Ajay Kumar Yadav",
  "age": 28,
  "gender": "Male",
  "email": "ajay.2@example.com",
  "phone_number": "9876543210"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |none|
|» age|body|integer| yes |none|
|» gender|body|string| yes |none|
|» email|body|string| yes |none|
|» phone_number|body|string| yes |none|

> Response Examples

```json
{
  "message": "Candidate created successfully",
  "data": {
    "id": 10
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» id|integer|true|none||none|

## PATCH Modify

PATCH /candidates/1

> Body Parameters

```json
{
  "name": "Ajay Kumar Yadav",
  "age": 28,
  "gender": "Male",
  "email": "ajay.kumar.yadav@example.com",
  "phone_number": "9876543210"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |none|
|» age|body|integer| yes |none|
|» gender|body|string| yes |none|
|» email|body|string| yes |none|
|» phone_number|body|string| yes |none|

> Response Examples

```json
{
  "message": "Candidate updated successfully",
  "data": {
    "candidate_id": 1,
    "name": "Ajay Kumar Yadav"
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» candidate_id|integer|true|none||none|
|»» name|string|true|none||none|

## DELETE Discard

DELETE /candidates/1

> Response Examples

```json
{
  "message": "Candidate deleted successfully",
  "data": null
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|null|true|none||none|