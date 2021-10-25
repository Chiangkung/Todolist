import 'package:flutter/material.dart';
import 'package:todolist/pages/todolist.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  //const ({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Todolist",
      home: Todolist(),
    );
  }
}