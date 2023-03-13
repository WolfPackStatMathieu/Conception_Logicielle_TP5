def get_ingredients(request_json):
    print(request_json["product"]["ingredients"])
    return request_json["product"]["ingredients"]

