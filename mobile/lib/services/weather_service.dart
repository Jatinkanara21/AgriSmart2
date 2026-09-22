import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';

class WeatherService {
  Future<Map<String,dynamic>> getWeather(double latitude,double longitude) async {
    final prefs=await SharedPreferences.getInstance();
    final token=prefs.getString('access_token')??'';
    final response=await http.post(
      Uri.parse(ApiConfig.baseUrl+'/weather'),
      headers:{'Authorization':'Bearer '+token,'Content-Type':'application/json'},
      body:jsonEncode({'latitude':latitude,'longitude':longitude}),
    );
    final data=jsonDecode(response.body);
    if(response.statusCode!=200) throw Exception(data['detail']??'Weather unavailable');
    return data as Map<String,dynamic>;
  }
}
