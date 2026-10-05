from extract import transform


def test_transform():
    data = [
        {
            "id": "1",
            "product": "Laptop",
            "quantity": "2",
            "price": "50000"
        }
    ]

    result = transform(data)

    assert result[0]["quantity"] == 100
    assert result[0]["price"] == 50000.0