def test_user_data():
    user = {
        "name": "Prashant",
        "role": "Developer"
    }

    assert user["name"] == "Prashant"
    assert user["role"] == "Developer"
