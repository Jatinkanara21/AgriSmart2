import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../services/disease_service.dart';
class DiseaseDetectionScreen extends StatefulWidget {
  const DiseaseDetectionScreen({super.key});
  @override State<DiseaseDetectionScreen> createState() => _DiseaseDetectionScreenState();
}
class _DiseaseDetectionScreenState extends State<DiseaseDetectionScreen> {
  final _picker = ImagePicker(); final _service = DiseaseService(); File? _image; bool _loading = false; String? _message; String? _error;
  Future<void> _pick(ImageSource source) async {
    final picked = await _picker.pickImage(source: source, imageQuality: 85); if (picked == null) return;
    setState(() { _image = File(picked.path); _message = null; _error = null; });
  }
  Future<void> _detect() async {
    if (_image == null) { setState(() => _error = 'Select a crop image first.'); return; }
    setState(() { _loading = true; _error = null; _message = null; });
    try { final data = await _service.detect(_image!); setState(() => _message = data['message']?.toString() ?? 'Analysis completed.'); }
    catch (e) { setState(() => _error = e.toString().replaceFirst('Exception: ', '')); }
    finally { if (mounted) setState(() => _loading = false); }
  }
  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Disease Detection')),
    body: ListView(padding: const EdgeInsets.all(16), children: [
      const Text('Upload a crop or plant image for disease analysis.', style: TextStyle(fontSize:16)), const SizedBox(height:16),
      Container(height:280, decoration: BoxDecoration(borderRadius:BorderRadius.circular(16), border:Border.all(color:Theme.of(context).colorScheme.outline)), clipBehavior:Clip.antiAlias, child: _image == null ? const Center(child:Icon(Icons.image_search,size:72)) : Image.file(_image!,fit:BoxFit.cover)),
      const SizedBox(height:16),
      Row(children:[Expanded(child:OutlinedButton.icon(onPressed:_loading?null:()=>_pick(ImageSource.camera),icon:const Icon(Icons.camera_alt),label:const Text('Camera'))),const SizedBox(width:12),Expanded(child:OutlinedButton.icon(onPressed:_loading?null:()=>_pick(ImageSource.gallery),icon:const Icon(Icons.photo_library),label:const Text('Gallery')))]),
      const SizedBox(height:12),
      FilledButton.icon(onPressed:_loading?null:_detect,icon:_loading?const SizedBox(width:18,height:18,child:CircularProgressIndicator(strokeWidth:2)):const Icon(Icons.biotech),label:Text(_loading?'Analyzing...':'Analyze Image')),
      if (_message != null) Card(margin:const EdgeInsets.only(top:20),child:Padding(padding:const EdgeInsets.all(16),child:Text(_message!))),
      if (_error != null) Padding(padding:const EdgeInsets.only(top:16),child:Text(_error!,style:TextStyle(color:Theme.of(context).colorScheme.error))),
    ]));
}
