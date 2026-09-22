import 'package:flutter/material.dart';
import '../services/weather_service.dart';

class WeatherScreen extends StatefulWidget {
  const WeatherScreen({super.key});
  @override State<WeatherScreen> createState()=>_WeatherScreenState();
}
class _WeatherScreenState extends State<WeatherScreen> {
  final lat=TextEditingController(),lon=TextEditingController();
  Map<String,dynamic>? data; String? error; bool loading=false;

  Future<void> loadWeather() async {
    setState((){loading=true;error=null;});
    try { data=await WeatherService().getWeather(double.parse(lat.text),double.parse(lon.text)); }
    catch(e){error=e.toString().replaceFirst('Exception: ','');}
    if(mounted)setState(()=>loading=false);
  }

  @override Widget build(BuildContext context)=>Scaffold(
    appBar:AppBar(title:const Text('Weather')),
    body:ListView(padding:const EdgeInsets.all(16),children:[
      TextField(controller:lat,keyboardType:const TextInputType.numberWithOptions(decimal:true),decoration:const InputDecoration(labelText:'Latitude',border:OutlineInputBorder())),
      const SizedBox(height:10),
      TextField(controller:lon,keyboardType:const TextInputType.numberWithOptions(decimal:true),decoration:const InputDecoration(labelText:'Longitude',border:OutlineInputBorder())),
      const SizedBox(height:12),
      FilledButton(onPressed:loading?null:loadWeather,child:Text(loading?'Loading...':'Get Weather')),
      if(error!=null) Padding(padding:const EdgeInsets.only(top:16),child:Text(error!)),
      if(data!=null) Card(child:Padding(padding:const EdgeInsets.all(18),child:Text(data.toString())))
    ]));
}
