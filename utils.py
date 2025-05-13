def filter_flights(flights, max_price, direct_only):
    result = []
    for f in flights:
        if f["price"] <= max_price and (not direct_only or f["direct"]):
            result.append(f)
    return result
