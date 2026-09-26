import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';
class DiseaseService {
  Future<Map<String, dynamic>> detect(File image) async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token') ?? '';
    final request = http.MultipartRequest('POST', Uri.parse(ApiConfig.baseUrl + '/disease-detection'));
    request.headers['Authorization'] = 'Bearer ' + token;
    request.files.add(await http.MultipartFile.fromPath('image', image.path));
    final streamed = await request.send();
    final response = await http.Response.fromStream(streamed);
    final data = jsonDecode(response.body);
    if (response.statusCode != 200) throw Exception(data['detail'] ?? 'Disease detection unavailable');
    return data as Map<String, dynamic>;
  }
}
