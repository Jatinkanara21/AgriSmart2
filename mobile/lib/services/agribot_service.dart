import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';

class AgriBotService {
  Future<String> chat(String message) async {
    final prefs=await SharedPreferences.getInstance();
    final token=prefs.getString('access_token')??'';
    final response=await http.post(Uri.parse(ApiConfig.baseUrl+'/agribot/chat'),
      headers:{'Authorization':'Bearer '+token,'Content-Type':'application/json'},
      body:jsonEncode({'message':message}));
    final data=jsonDecode(response.body);
    if(response.statusCode!=200) throw Exception(data['detail']??'AgriBot unavailable');
    return data['reply']?.toString()??'No response';
  }
}
