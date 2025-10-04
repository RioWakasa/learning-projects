import 'package:flutter/material.dart';
import 'package:reservation_project/main.dart';

class BookingPage extends StatefulWidget {
  @override
  State<BookingPage> createState() => _BookingPageState();
}

class _BookingPageState extends State<BookingPage> {
  final myController = TextEditingController();
  DateTime selectedDate = DateTime.now();
  var first_name;
  var last_name;
  var tell;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('予約'),
      ),
      body: SingleChildScrollView(  
        padding: const EdgeInsets.all(32.0),
        child: Column(
          children: [
            Container(
              padding: const EdgeInsets.all(8.0),
              child: MyTextField(
                txt: '姓',
                onChanged: (name) =>
                  first_name = name
              ),
            ),
            Container(
              padding: const EdgeInsets.all(8.0),
              child: MyTextField(
                txt: '名',
                onChanged: (name) =>
                  last_name = name
              ),
            ),
            Container(
              padding: const EdgeInsets.all(8.0),
              child: MyTextField(
                txt: '電話番号',
                onChanged: (name) =>
                  tell = name
              ),
            ),
            Text('選択した日付: ${selectedDate.year}/${selectedDate.month}/${selectedDate.day}'),
            ElevatedButton(
              onPressed: () => _selectDate(context),
              child: const Text('日付選択'),
            ),
            Container (
              padding: const EdgeInsets.all(32.0),
              child: ElevatedButton(
                child: const Text('予約する'),
                onPressed: () {
                  print(first_name);
                  print(last_name);
                  print(tell);
                  print(selectedDate);
                },
            )
            )
          ]
        ),
      )
    );
  }

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: selectedDate,
      firstDate: DateTime(2024),
      lastDate: DateTime(2025),
    );

    if (picked != null) {
      setState(() {
        selectedDate = picked;
      });
    }
  }
}