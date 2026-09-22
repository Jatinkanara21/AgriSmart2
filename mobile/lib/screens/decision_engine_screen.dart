import 'package:flutter/material.dart';
import '../services/decision_service.dart';

class DecisionEngineScreen extends StatefulWidget {
  const DecisionEngineScreen({super.key});
  @override State<DecisionEngineScreen> createState()=>_DecisionEngineScreenState();
}
class _DecisionEngineScreenState extends State<DecisionEngineScreen>{
  final temp=TextEditingController(),hum=TextEditingController(),rain=TextEditingController(),moist=TextEditingController(),ph=TextEditingController();
  List<String> results=[]; bool loading=false;
  Future<void> analyze() async {
    setState(()=>loading=true);
    try{results=await DecisionService().analyze(temperature:double.parse(temp.text),humidity:double.parse(hum.text),rainfall:double.parse(rain.text),soilMoisture:double.parse(moist.text),soilPh:double.parse(ph.text));}
    catch(e){results=[e.toString().replaceFirst('Exception: ','')];}
    if(mounted)setState(()=>loading=false);
  }
  Widget field(TextEditingController c,String label)=>Padding(padding:const EdgeInsets.only(bottom:10),child:TextField(controller:c,keyboardType:const TextInputType.numberWithOptions(decimal:true),decoration:InputDecoration(labelText:label,border:const OutlineInputBorder())));
  @override Widget build(BuildContext context)=>Scaffold(appBar:AppBar(title:const Text('Smart Farming Decision Engine')),body:ListView(padding:const EdgeInsets.all(16),children:[field(temp,'Temperature °C'),field(hum,'Humidity %'),field(rain,'Rainfall mm'),field(moist,'Soil Moisture %'),field(ph,'Soil pH'),FilledButton(onPressed:loading?null:analyze,child:Text(loading?'Analyzing...':'Analyze Farm')),const SizedBox(height:16),...results.map((x)=>Card(child:ListTile(leading:const Icon(Icons.lightbulb),title:Text(x))))]));
}
