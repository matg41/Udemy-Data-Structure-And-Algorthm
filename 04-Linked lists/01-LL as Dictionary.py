head = {
    "value":11,
    "next":{
        "value":2,
        "next":{
            "value":23,
            "next":{"value":7,
                    "next":None
            }
        }

    }
}

print(head["next"]["next"]["next"]['value'])