// ignore_for_file: prefer_const_constructors

import 'package:cyberspyder/Screens/Dashboard/dashboard_screen.dart';
import 'package:cyberspyder/Screens/Dashboard/table_screen.dart';
import 'package:cyberspyder/Screens/Signin/sign_in_screen.dart';
import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';

import 'Screens/Home/home_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(fontFamily: 'Poppins', primaryColor: textPrimary),
      debugShowCheckedModeBanner: false,
      home: HomeScreen(),
      // home: SignINPage(),
      // home: dashboard(),
      // home: TableOutput(),
    );
  }
}
