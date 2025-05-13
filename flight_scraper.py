def get_mock_flights(from_city, to_city, date):
    return [
        {
            "flight_no": "PR361",
            "airline": "菲律宾航空",
            "depart_time": "08:20",
            "arrive_time": "13:15",
            "price": 830,
            "direct": True
        },
        {
            "flight_no": "CZ3091",
            "airline": "中国南方航空",
            "depart_time": "06:30",
            "arrive_time": "15:50",
            "price": 710,
            "direct": False
        },
        {
            "flight_no": "CA179",
            "airline": "中国国航",
            "depart_time": "15:00",
            "arrive_time": "19:40",
            "price": 910,
            "direct": True
        }
    ]
