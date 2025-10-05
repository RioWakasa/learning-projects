import 'package:flutter/material.dart';

void main() {
  runApp(
    MyApp(), // 先ほど作った MyApp() を表示したいので runApp() の中に書きます。
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            'こんぶ @ Flutter大学',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 16,
            ),
          ),
        ),
        // body プロパティに Row を与えます。
        body: Column(
          children: [
            Row(
          // children プロパティに Text のリストを与えます。
              children: [
                Text('こんぶ @ Flutter大学'),
                Text('2022/05/05'),
              ],
            ),
            Text('最高でした')
          ],
        ),
      ),
    );
  }
}