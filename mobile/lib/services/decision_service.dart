import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';

class DecisionService {
  Future<List<String>> analyze({required double temperature,required double humidity,required double rainfall,required double soilMoisture,required double soilPh}) async {
    final prefs=await SharedPreferences.getInstance();
    final token=prefs.getString('access_token')??'';
    final response=await http.post(Uri.parse(ApiConfig.baseUrl+'/decision-engine/analyze'),
      headers:{'Authorization':'Bearer '+token,'Content-Type':'application/json'},
      body:jsonEncode({'temperature':temperature,'humidity':humidity,'rainfall':rainfall,'soil_moisture':soilMoisture,'soil_ph':soilPh}));
    final data=jsonDecode(response.body);
    if(response.statusCode!=200) throw Exception(data['detail']??'Decision analysis failed');
    return List<String>.from(data['recommendations']??[]);
  }
}
