import 'package:flutter/material.dart';

class AgriBotScreen extends StatelessWidget {
  const AgriBotScreen({super.key});
  @override Widget build(BuildContext context)=>Scaffold(
    appBar:AppBar(title:const Text('AgriBot')),
    body:const Center(child:Padding(padding:EdgeInsets.all(24),child:Text('AgriBot chat UI is ready for provider integration.'))),
  );
}
