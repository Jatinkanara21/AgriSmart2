import 'package:flutter/material.dart';
import 'farms_screen.dart';
import 'crop_recommendation_screen.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});
  @override Widget build(BuildContext context) {
    final modules=[('Crop Recommendation',Icons.eco,const CropRecommendationScreen()),('Disease Detection',Icons.document_scanner,null),('Yield Prediction',Icons.analytics,null),('Weather',Icons.cloud,null),('AgriBot',Icons.smart_toy,null),('Farm Management',Icons.agriculture,const FarmsScreen())];
    return Scaffold(appBar:AppBar(title:const Text('AgriSmart Dashboard')),body:GridView.builder(padding:const EdgeInsets.all(16),gridDelegate:const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount:2,crossAxisSpacing:12,mainAxisSpacing:12,childAspectRatio:1.15),itemCount:modules.length,itemBuilder:(_,i)=>Card(child:InkWell(onTap:modules[i].$3==null?null:()=>Navigator.push(context,MaterialPageRoute(builder:(_)=>modules[i].$3!)),child:Column(mainAxisAlignment:MainAxisAlignment.center,children:[Icon(modules[i].$2,size:42,color:const Color(0xFF2E7D32)),const SizedBox(height:12),Padding(padding:const EdgeInsets.all(8),child:Text(modules[i].$1,textAlign:TextAlign.center))])))));
  }
}
