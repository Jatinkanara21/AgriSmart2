from app.services.decision_engine import basic_recommendations

def test_low_moisture_recommendation():
    result=basic_recommendations(25,60,10,20,6.5)
    assert any("irrigation" in item.lower() for item in result)

def test_normal_conditions():
    result=basic_recommendations(25,60,10,50,6.5)
    assert result
