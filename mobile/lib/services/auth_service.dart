import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../config/api_config.dart';

class AuthService {
  Future<String?> login(String email, String password) async {
    final response = await http.post(Uri.parse(ApiConfig.baseUrl + '/auth/login'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'email': email, 'password': password}));
    if (response.statusCode != 200) return null;
    final data = jsonDecode(response.body) as Map<String, dynamic>;
    final token = data['access_token'] as String?;
    if (token == null) return null;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('access_token', token);
    return token;
  }

  Future<String?> register(String name, String email, String password) async {
    final response = await http.post(Uri.parse(ApiConfig.baseUrl + '/auth/register'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'full_name': name, 'email': email, 'password': password}));
    if (response.statusCode != 201) return null;
    return login(email, password);
  }

  Future<bool> isLoggedIn() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');
    return token != null && token.isNotEmpty;
  }

  Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('access_token');
  }

  Future<Map<String, dynamic>?> me() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');
    if (token == null || token.isEmpty) return null;
    final response = await http.get(Uri.parse(ApiConfig.baseUrl + '/auth/me'), headers: {'Authorization': 'Bearer ' + token});
    if (response.statusCode == 200) return jsonDecode(response.body) as Map<String, dynamic>;
    if (response.statusCode == 401) await logout();
    return null;
  }
}
