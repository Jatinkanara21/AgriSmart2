import 'package:flutter/material.dart';
import '../services/auth_service.dart';
import 'dashboard_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}
class _LoginScreenState extends State<LoginScreen> {
  final email = TextEditingController();
  final password = TextEditingController();
  bool loading = false;

  Future<void> login() async {
    setState(() => loading = true);
    final ok = await AuthService().login(email.text.trim(), password.text);
    if (!mounted) return;
    setState(() => loading = false);
    if (ok) {
      Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const DashboardScreen()));
    } else {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Login failed. Check your credentials.')));
    }
  }

  @override
  Widget build(BuildContext context) => Scaffold(
    body: SafeArea(child: Center(child: SingleChildScrollView(
      padding: const EdgeInsets.all(24),
      child: Column(children: [
        const Icon(Icons.agriculture, size: 80, color: Color(0xFF2E7D32)),
        const SizedBox(height: 16),
        Text('AgriSmart', style: Theme.of(context).textTheme.headlineLarge),
        const Text('Smart farming. Better decisions.'),
        const SizedBox(height: 32),
        TextField(controller: email, decoration: const InputDecoration(labelText: 'Email', border: OutlineInputBorder())),
        const SizedBox(height: 16),
        TextField(controller: password, obscureText: true, decoration: const InputDecoration(labelText: 'Password', border: OutlineInputBorder())),
        const SizedBox(height: 24),
        SizedBox(width: double.infinity, child: FilledButton(onPressed: loading ? null : login, child: Text(loading ? 'Signing in...' : 'Sign in'))),
      ]),
    ))),
  );
}
