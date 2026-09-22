import 'package:flutter/material.dart';
import '../services/ai_service.dart';

class CropRecommendationScreen extends StatefulWidget {
  const CropRecommendationScreen({super.key});
  @override State<CropRecommendationScreen> createState() => _CropRecommendationScreenState();
}
class _CropRecommendationScreenState extends State<CropRecommendationScreen> {
  final service=AiService();
  final n=TextEditingController(),p=TextEditingController(),k=TextEditingController(),temp=TextEditingController(),hum=TextEditingController(),ph=TextEditingController(),rain=TextEditingController();
  String? result; bool loading=false;
  Future<void> predict() async {
    setState((){loading=true;result=null;});
    try {
      final r=await service.cropRecommendation(nitrogen:double.parse(n.text),phosphorus:double.parse(p.text),potassium:double.parse(k.text),temperature:double.parse(temp.text),humidity:double.parse(hum.text),ph:double.parse(ph.text),rainfall:double.parse(rain.text));
      result='Recommended crop: ' + r['crop'].toString();
    } catch(e){result=e.toString().replaceFirst('Exception: ','');}
    if(mounted)setState(()=>loading=false);
  }
  Widget field(TextEditingController c,String label)=>Padding(padding:const EdgeInsets.only(bottom:10),child:TextField(controller:c,keyboardType:const TextInputType.numberWithOptions(decimal:true),decoration:InputDecoration(labelText:label,border:const OutlineInputBorder())));
  @override Widget build(BuildContext context)=>Scaffold(appBar:AppBar(title:const Text('Crop Recommendation')),body:ListView(padding:const EdgeInsets.all(16),children:[field(n,'Nitrogen (N)'),field(p,'Phosphorus (P)'),field(k,'Potassium (K)'),field(temp,'Temperature °C'),field(hum,'Humidity %'),field(ph,'Soil pH'),field(rain,'Rainfall mm'),FilledButton(onPressed:loading?null:predict,child:Text(loading?'Analyzing...':'Recommend Crop')),if(result!=null)Card(child:Padding(padding:const EdgeInsets.all(18),child:Text(result!))) ]));
}
