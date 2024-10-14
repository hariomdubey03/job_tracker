CANDIDATE_GET = {
    "name": {
        "type": "string",
        "required": True,
        "minlength": 1,
    }
}

CANDIDATE_POST = {
    "name": {
        "type": "string",
        "required": True,
        "minlength": 1,
    },
    "age": {
        "type": "integer",
        "required": True,
        "min": 1,
    },
    "gender": {
        "type": "string",
        "required": True,
        "gender": True,
    },
    "email": {
        "type": "string",
        "required": True,
        "regex": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    },
    "phone_number": {
        "type": "string",
        "required": True,
        "regex": r"^\d+$",
        "minlength": 10,
        "maxlength": 15,
    },
}

CANDIDATE_PATCH = {
    "name": {
        "type": "string",
        "required": False,
        "minlength": 1,
    },
    "age": {
        "type": "integer",
        "required": False,
        "min": 1,
    },
    "gender": {
        "type": "string",
        "required": False,
        "gender": True,
    },
    "email": {
        "type": "string",
        "required": False,
        "regex": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    },
    "phone_number": {
        "type": "string",
        "required": False,
        "regex": r"^\d+$",
        "minlength": 10,
        "maxlength": 15,
    },
}
