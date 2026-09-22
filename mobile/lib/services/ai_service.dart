import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';

class AiService {
  Future<Map<String, dynamic>> cropRecommendation({required double nitrogen, required double phosphorus, required double potassium, required double temperature, required double humidity, required double ph, required double rainfall}) async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token') ?? '';
    final response = await http.post(Uri.parse(ApiConfig.baseUrl + '/crop-recommendation'),
      headers: {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'},
      body: jsonEncode({'nitrogen': nitrogen, 'phosphorus': phosphorus, 'potassium': potassium, 'temperature': temperature, 'humidity': humidity, 'ph': ph, 'rainfall': rainfall}));
    final data = jsonDecode(response.body);
    if (response.statusCode != 200) throw Exception(data['detail'] ?? 'Recommendation unavailable');
    return data as Map<String, dynamic>;
  }
}
