import 'package:flutter/material.dart';
import 'package:reservation_project/account.dart';
import './booking.dart';
import './about.dart';
import './account.dart';

void main() {
  runApp(const MyApp());
}
// 画面が変化しない時はStatelessWidget変化する時はStatefullWidget
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const MainPage(),
      theme: ThemeData(
        appBarTheme: AppBarTheme(color: Color.fromARGB(202, 255, 162, 0)),
        colorScheme: ColorScheme.fromSeed(seedColor:Color.fromARGB(255, 255, 166, 0)),
      ),
      routes: <String, WidgetBuilder> {
        '/home': (BuildContext context) => const MainPage(),
      },
    );
  }
}

class MainPage extends StatelessWidget {
  const MainPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text('Home'),
      ),
      drawer: Drawer(
        child: ListView(
          children: [
            DrawerHeader(
              decoration: const BoxDecoration(
                color: Colors.amber,
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    height: 100,
                    width: 120,
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(500),
                      child: Image.asset('images/sample.png',
                        fit: BoxFit.contain,), 
                    ),
                  ),
                  const Text(
                    'Menu',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ]
              ),
            ),
            Card(
              child: ListTile(
                title: const Text('Home'),
                onTap: () {
                Navigator.of(context).pushNamed("/home");
                },
              ),
            ),
            Card(
              child: ListTile(
                title: const Text("Booking"),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(builder: (context) {
                return BookingPage();
              })),
              ),
            ),
            Card(
              child: ListTile(
                title: const Text("About us"),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(builder: (context) {
                return AboutPage();
              })),
              ),
            ),
            Card(
              child: ListTile(
                title: const Text("Account"),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(builder: (context) {
                return AccountPage();
              })),
              ),
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(10.0),
        child: Center(
          child: Column(
            children: <Widget>[
              Container(
                height: 150,
                width: 150,
                child: Image.asset('images/sample.png',
                fit: BoxFit.contain,),  
                ),
              Container(
                padding: const EdgeInsets.all(10.0),
                child: Image.asset('images/cafe.jpg'),
              ),
              Container(
                padding: const EdgeInsets.all(10.0),
                child: Image.asset('images/coffee.jpg'),
              ),
            ],
          )
        )
      )
    );
  }
}

class MyTextField extends StatefulWidget {
  final String txt;
  final void Function(String text) onChanged;

  const MyTextField({Key? key, required this.txt, required this.onChanged,}) : super(key: key);

  @override
  State<MyTextField> createState() => _MyTextFieldState();
}

class _MyTextFieldState extends State<MyTextField> {
  final TextEditingController _controller = TextEditingController();

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _controller,
      decoration: InputDecoration(
        labelText: widget.txt,
        border: const OutlineInputBorder(),
      ),
      onChanged: widget.onChanged,
    );
  }
}

