// ignore_for_file: prefer_const_constructors

import 'package:cyberspyder/Screens/Home/home_screen.dart';
import 'package:cyberspyder/Screens/Signin/sign_in_screen.dart';
import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';

class BlackButtonDash extends StatefulWidget {
  final String title;
  const BlackButtonDash({
    super.key,
    required this.title,
  });

  @override
  State<BlackButtonDash> createState() => _BlackButtonDashState();
}

class _BlackButtonDashState extends State<BlackButtonDash> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(left: 12.0),
      child: TextButton(
        style: TextButton.styleFrom(
          padding: EdgeInsets.symmetric(horizontal: 25, vertical: 12),
          backgroundColor: Color(0xFF121212),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
          ),
        ),
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => HomeScreen(),
            ),
          );
        },
        child: Text(
          widget.title,
          style: TextStyle(
            fontFamily: 'Poppins',
            fontSize: 18,
            fontWeight: FontWeight.w400,
            color: textPrimary,
          ),
        ),
      ),
    );
  }
}
