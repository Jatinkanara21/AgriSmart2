import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';
class AgriBotService {
 Future<String> chat(String message) async {
  final prefs=await SharedPreferences.getInstance(); final token=prefs.getString('access_token')??''; final session=prefs.getString('agribot_session_id');
  final body={'message':message}; if(session!=null) body['session_id']=session;
  final response=await http.post(Uri.parse(ApiConfig.baseUrl+'/agribot/chat'),headers:{'Authorization':'Bearer '+token,'Content-Type':'application/json'},body:jsonEncode(body));
  final data=jsonDecode(response.body); if(response.statusCode!=200)throw Exception(data['detail']??'AgriBot unavailable');
  if(data['session_id']!=null)await prefs.setString('agribot_session_id',data['session_id'].toString());
  return data['reply']?.toString()??'No response';
 }
 Future<void> clearSession() async { final prefs=await SharedPreferences.getInstance(); await prefs.remove('agribot_session_id'); }
}
