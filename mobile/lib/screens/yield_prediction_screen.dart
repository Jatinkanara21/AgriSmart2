import 'package:flutter/material.dart';
import '../services/yield_service.dart';
class YieldPredictionScreen extends StatefulWidget {
  const YieldPredictionScreen({super.key});
  @override State<YieldPredictionScreen> createState() => _YieldPredictionScreenState();
}
class _YieldPredictionScreenState extends State<YieldPredictionScreen> {
  final _formKey = GlobalKey<FormState>();
  final _area = TextEditingController(), _rainfall = TextEditingController(), _temperature = TextEditingController(), _ph = TextEditingController();
  final _service = YieldService(); bool _loading = false; String? _result; String? _error;
  @override void dispose() { _area.dispose(); _rainfall.dispose(); _temperature.dispose(); _ph.dispose(); super.dispose(); }
  String? _number(String? v) => v == null || v.trim().isEmpty || double.tryParse(v) == null ? 'Enter a valid number' : null;
  Future<void> _predict() async {
    if (!_formKey.currentState!.validate()) return;
    setState(() { _loading = true; _error = null; _result = null; });
    try {
      final data = await _service.predict(areaAcres: double.parse(_area.text), rainfall: double.parse(_rainfall.text), temperature: double.parse(_temperature.text), soilPh: double.parse(_ph.text));
      setState(() => _result = data['predicted_yield'].toString() + ' ' + (data['unit'] ?? '').toString());
    } catch (e) { setState(() => _error = e.toString().replaceFirst('Exception: ', '')); }
    finally { if (mounted) setState(() => _loading = false); }
  }
  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Yield Prediction')),
    body: Form(key: _formKey, child: ListView(padding: const EdgeInsets.all(16), children: [
      const Text('Enter your farm conditions to estimate yield.', style: TextStyle(fontSize: 16)), const SizedBox(height: 16),
      TextFormField(controller: _area, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Area (acres)'), validator: _number),
      TextFormField(controller: _rainfall, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Rainfall'), validator: _number),
      TextFormField(controller: _temperature, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Temperature (°C)'), validator: _number),
      TextFormField(controller: _ph, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Soil pH (0–14)'), validator: (v) { final e = _number(v); if (e != null) return e; final n = double.parse(v!); return n < 0 || n > 14 ? 'pH must be between 0 and 14' : null; }),
      const SizedBox(height: 20),
      FilledButton.icon(onPressed: _loading ? null : _predict, icon: _loading ? const SizedBox(width:18,height:18,child:CircularProgressIndicator(strokeWidth:2)) : const Icon(Icons.analytics), label: Text(_loading ? 'Predicting...' : 'Predict Yield')),
      if (_result != null) Card(margin: const EdgeInsets.only(top:20), child: Padding(padding: const EdgeInsets.all(16), child: Text('Predicted yield: ' + _result!, style: const TextStyle(fontSize:18,fontWeight:FontWeight.bold)))),
      if (_error != null) Padding(padding: const EdgeInsets.only(top:16), child: Text(_error!, style: TextStyle(color: Theme.of(context).colorScheme.error))),
    ])));
}
