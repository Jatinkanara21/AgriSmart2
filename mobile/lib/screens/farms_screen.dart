import 'package:flutter/material.dart';
import '../services/farm_service.dart';

class FarmsScreen extends StatefulWidget {
  const FarmsScreen({super.key});
  @override State<FarmsScreen> createState() => _FarmsScreenState();
}
class _FarmsScreenState extends State<FarmsScreen> {
  final service = FarmService();
  final name = TextEditingController(), area = TextEditingController(), location = TextEditingController(), soil = TextEditingController();

  Future<void> addFarm() async {
    final ok = await service.createFarm(name.text, double.tryParse(area.text) ?? 0, location.text, soil.text);
    if (!mounted) return;
    if (ok) { name.clear(); area.clear(); location.clear(); soil.clear(); setState(() {}); }
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(ok ? 'Farm added' : 'Could not add farm')));
  }

  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('My Farms')),
    body: FutureBuilder<List<dynamic>>(
      future: service.listFarms(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) return const Center(child: CircularProgressIndicator());
        if (snapshot.hasError) return Center(child: Text(snapshot.error.toString()));
        final farms = snapshot.data ?? [];
        return ListView(padding: const EdgeInsets.all(16), children: [
          ...farms.map((f) => Card(child: ListTile(
            leading: const Icon(Icons.agriculture),
            title: Text(f['name'] ?? ''),
            subtitle: Text(f['area_acres'].toString() + ' acres • ' + (f['soil_type'] ?? 'Soil not set')),
          ))),
          const SizedBox(height: 16),
          Text('Add Farm', style: Theme.of(context).textTheme.titleLarge),
          const SizedBox(height: 12),
          TextField(controller: name, decoration: const InputDecoration(labelText: 'Farm name', border: OutlineInputBorder())),
          const SizedBox(height: 10),
          TextField(controller: area, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Area (acres)', border: OutlineInputBorder())),
          const SizedBox(height: 10),
          TextField(controller: location, decoration: const InputDecoration(labelText: 'Location', border: OutlineInputBorder())),
          const SizedBox(height: 10),
          TextField(controller: soil, decoration: const InputDecoration(labelText: 'Soil type', border: OutlineInputBorder())),
          const SizedBox(height: 12),
          FilledButton(onPressed: addFarm, child: const Text('Save Farm')),
        ]);
      },
    ),
  );
}
