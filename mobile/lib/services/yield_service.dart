import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';
class YieldService {
  Future<Map<String, dynamic>> predict({required double areaAcres, required double rainfall, required double temperature, required double soilPh}) async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token') ?? '';
    final response = await http.post(Uri.parse(ApiConfig.baseUrl + '/yield-prediction'), headers: {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}, body: jsonEncode({'area_acres': areaAcres, 'rainfall': rainfall, 'temperature': temperature, 'soil_ph': soilPh}));
    final data = jsonDecode(response.body);
    if (response.statusCode != 200) throw Exception(data['detail'] ?? 'Yield prediction unavailable');
    return data as Map<String, dynamic>;
  }
}
