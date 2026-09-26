import 'package:flutter/material.dart';
import 'screens/auth_gate.dart';
void main()=>runApp(const AgriSmartApp());
class AgriSmartApp extends StatelessWidget{const AgriSmartApp({super.key});@override Widget build(BuildContext context)=>MaterialApp(title:'AgriSmart',debugShowCheckedModeBanner:false,theme:ThemeData(colorScheme:ColorScheme.fromSeed(seedColor:const Color(0xFF2E7D32)),useMaterial3:true),home:const AuthGate());}