import 'package:flutter/material.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});
  @override
  Widget build(BuildContext context) {
    final modules = [
      ('Crop Recommendation', Icons.eco),
      ('Disease Detection', Icons.document_scanner),
      ('Yield Prediction', Icons.analytics),
      ('Weather', Icons.cloud),
      ('AgriBot', Icons.smart_toy),
      ('Farm Management', Icons.agriculture),
    ];
    return Scaffold(
      appBar: AppBar(title: const Text('AgriSmart Dashboard')),
      body: GridView.builder(
        padding: const EdgeInsets.all(16),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, crossAxisSpacing: 12, mainAxisSpacing: 12, childAspectRatio: 1.15),
        itemCount: modules.length,
        itemBuilder: (_, index) => Card(
          child: InkWell(
            onTap: () {},
            child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              Icon(modules[index].$2, size: 42, color: const Color(0xFF2E7D32)),
              const SizedBox(height: 12),
              Padding(padding: const EdgeInsets.all(8), child: Text(modules[index].$1, textAlign: TextAlign.center)),
            ]),
          ),
        ),
      ),
    );
  }
}
