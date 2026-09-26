import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';
class FarmService {
  Future<String?> _token() async { final prefs=await SharedPreferences.getInstance(); return prefs.getString('access_token'); }
  Future<List<Map<String,dynamic>>> listFarms() async { final token=await _token(); final r=await http.get(Uri.parse(ApiConfig.baseUrl+'/farms'),headers:{'Authorization':'Bearer '+(token??'')}); final d=jsonDecode(r.body); if(r.statusCode!=200)throw Exception(d['detail']??'Could not load farms'); return (d as List).cast<Map<String,dynamic>>(); }
  Future<bool> createFarm(String name,double areaAcres,String location,String soilType) async { final token=await _token(); final r=await http.post(Uri.parse(ApiConfig.baseUrl+'/farms'),headers:{'Authorization':'Bearer '+(token??''),'Content-Type':'application/json'},body:jsonEncode({'name':name,'area_acres':areaAcres,'location':location.isEmpty?null:location,'soil_type':soilType.isEmpty?null:soilType})); return r.statusCode==201; }
  Future<bool> deleteFarm(String farmId) async { final token=await _token(); final r=await http.delete(Uri.parse(ApiConfig.baseUrl+'/farms/'+farmId),headers:{'Authorization':'Bearer '+(token??'')}); return r.statusCode==204; }
}