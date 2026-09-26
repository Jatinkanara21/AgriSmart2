import 'package:flutter/material.dart';
import '../services/auth_service.dart';
import 'dashboard_screen.dart';
import 'login_screen.dart';
class AuthGate extends StatefulWidget {const AuthGate({super.key});@override State<AuthGate> createState()=>_AuthGateState();}
class _AuthGateState extends State<AuthGate>{late Future<bool> _session;@override void initState(){super.initState();_session=AuthService().isLoggedIn();}@override Widget build(BuildContext context)=>FutureBuilder<bool>(future:_session,builder:(_,s){if(s.connectionState!=ConnectionState.done)return const Scaffold(body:Center(child:CircularProgressIndicator()));return s.data==true?const DashboardScreen():const LoginScreen();});}