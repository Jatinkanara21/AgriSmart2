def basic_recommendations(temperature: float, humidity: float, rainfall: float, soil_moisture: float, soil_ph: float) -> list[str]:
    recommendations=[]
    if soil_moisture < 30:
        recommendations.append("Consider irrigation; soil moisture is low.")
    if rainfall > 80:
        recommendations.append("Monitor drainage because rainfall is high.")
    if soil_ph < 5.5:
        recommendations.append("Consider a soil-management plan for acidic soil.")
    if soil_ph > 7.5:
        recommendations.append("Consider a soil-management plan for alkaline soil.")
    return recommendations or ["No basic risk rule was triggered."]
