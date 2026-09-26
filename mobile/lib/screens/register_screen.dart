import 'package:flutter/material.dart';
import '../services/auth_service.dart';
import 'dashboard_screen.dart';
class RegisterScreen extends StatefulWidget { const RegisterScreen({super.key}); @override State<RegisterScreen> createState()=>_RegisterScreenState(); }
class _RegisterScreenState extends State<RegisterScreen>{
 final _formKey=GlobalKey<FormState>(); final _name=TextEditingController(),_email=TextEditingController(),_password=TextEditingController(),_confirm=TextEditingController(); bool _loading=false;
 @override void dispose(){_name.dispose();_email.dispose();_password.dispose();_confirm.dispose();super.dispose();}
 Future<void> _register() async { if(!_formKey.currentState!.validate())return; setState(()=>_loading=true); final token=await AuthService().register(_name.text.trim(),_email.text.trim(),_password.text); if(!mounted)return; setState(()=>_loading=false); if(token!=null){Navigator.pushAndRemoveUntil(context,MaterialPageRoute(builder:(_)=>const DashboardScreen()),(_)=>false);}else{ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content:Text('Registration failed. Email may already be registered.')));}}
 @override Widget build(BuildContext context)=>Scaffold(appBar:AppBar(title:const Text('Create Account')),body:Form(key:_formKey,child:ListView(padding:const EdgeInsets.all(24),children:[
 TextFormField(controller:_name,decoration:const InputDecoration(labelText:'Full name',border:OutlineInputBorder()),validator:(v)=>v==null||v.trim().length<2?'Enter your full name':null),const SizedBox(height:16),
 TextFormField(controller:_email,keyboardType:TextInputType.emailAddress,decoration:const InputDecoration(labelText:'Email',border:OutlineInputBorder()),validator:(v)=>v==null||!v.contains('@')?'Enter a valid email':null),const SizedBox(height:16),
 TextFormField(controller:_password,obscureText:true,decoration:const InputDecoration(labelText:'Password',border:OutlineInputBorder()),validator:(v)=>v==null||v.length<8?'Use at least 8 characters':null),const SizedBox(height:16),
 TextFormField(controller:_confirm,obscureText:true,decoration:const InputDecoration(labelText:'Confirm password',border:OutlineInputBorder()),validator:(v)=>v!=_password.text?'Passwords do not match':null),const SizedBox(height:24),
 FilledButton(onPressed:_loading?null:_register,child:Text(_loading?'Creating account...':'Create account'))])); }