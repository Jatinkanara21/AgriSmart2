import 'package:flutter/material.dart';
import '../services/auth_service.dart';
import 'farms_screen.dart';
import 'crop_recommendation_screen.dart';
import 'disease_detection_screen.dart';
import 'yield_prediction_screen.dart';
import 'weather_screen.dart';
import 'agribot_screen.dart';
import 'decision_engine_screen.dart';
import 'login_screen.dart';
class DashboardScreen extends StatelessWidget{
 const DashboardScreen({super.key});
 Future<void> _logout(BuildContext context)async{await AuthService().logout();if(!context.mounted)return;Navigator.pushAndRemoveUntil(context,MaterialPageRoute(builder:(_)=>const LoginScreen()),(_)=>false);}
 @override Widget build(BuildContext context){final modules=[('Crop Recommendation',Icons.eco,const CropRecommendationScreen()),('Disease Detection',Icons.document_scanner,const DiseaseDetectionScreen()),('Yield Prediction',Icons.analytics,const YieldPredictionScreen()),('Weather',Icons.cloud,const WeatherScreen()),('AgriBot',Icons.smart_toy,const AgriBotScreen()),('Farm Management',Icons.agriculture,const FarmsScreen()),('Smart Decision Engine',Icons.psychology,const DecisionEngineScreen())];return Scaffold(appBar:AppBar(title:const Text('AgriSmart Dashboard'),actions:[IconButton(tooltip:'Logout',onPressed:()=>_logout(context),icon:const Icon(Icons.logout))]),body:GridView.builder(padding:const EdgeInsets.all(16),gridDelegate:const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount:2,crossAxisSpacing:12,mainAxisSpacing:12,childAspectRatio:1.1),itemCount:modules.length,itemBuilder:(_,i)=>Card(child:InkWell(onTap:()=>Navigator.push(context,MaterialPageRoute(builder:(_)=>modules[i].$3)),child:Column(mainAxisAlignment:MainAxisAlignment.center,children:[Icon(modules[i].$2,size:40,color:const Color(0xFF2E7D32)),const SizedBox(height:10),Padding(padding:const EdgeInsets.all(8),child:Text(modules[i].$1,textAlign:TextAlign.center))])))));}}
