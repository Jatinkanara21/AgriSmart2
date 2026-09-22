import 'package:flutter/material.dart';
import '../services/agribot_service.dart';

class AgriBotScreen extends StatefulWidget {
  const AgriBotScreen({super.key});
  @override State<AgriBotScreen> createState()=>_AgriBotScreenState();
}
class _AgriBotScreenState extends State<AgriBotScreen> {
  final input=TextEditingController();
  final messages=<Map<String,String>>[];
  bool loading=false;

  Future<void> send() async {
    final text=input.text.trim();
    if(text.isEmpty||loading)return;
    setState((){messages.add({'role':'user','text':text});input.clear();loading=true;});
    try {
      final reply=await AgriBotService().chat(text);
      if(mounted)setState(()=>messages.add({'role':'bot','text':reply}));
    } catch(e) {
      if(mounted)setState(()=>messages.add({'role':'bot','text':e.toString().replaceFirst('Exception: ','')}));
    }
    if(mounted)setState(()=>loading=false);
  }

  @override Widget build(BuildContext context)=>Scaffold(
    appBar:AppBar(title:const Text('AgriBot')),
    body:Column(children:[
      Expanded(child:ListView.builder(padding:const EdgeInsets.all(12),itemCount:messages.length,itemBuilder:(_,i){
        final m=messages[i];
        return Align(alignment:m['role']=='user'?Alignment.centerRight:Alignment.centerLeft,child:Card(child:Padding(padding:const EdgeInsets.all(12),child:Text(m['text']??''))));
      })),
      SafeArea(child:Padding(padding:const EdgeInsets.all(12),child:Row(children:[
        Expanded(child:TextField(controller:input,onSubmitted:(_)=>send(),decoration:const InputDecoration(hintText:'Ask about farming...',border:OutlineInputBorder()))),
        const SizedBox(width:8),IconButton(onPressed:loading?null:send,icon:const Icon(Icons.send))
      ])))
    ]));
}
