from app import calculate_bmi, app

def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 2) == 22.86

def test_bmi_api():
    client = app.test_client()
    response = client.post("/bmi", json={"weight": 70, "height": 1.75})
    assert response.status_code == 200
    assert round(response.get_json()["bmi"], 2) == 22.86
