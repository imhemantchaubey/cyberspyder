// ignore_for_file: prefer_const_constructors

import 'package:cyberspyder/Screens/Signin/sign_in_screen.dart';
import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';

class BlackButton extends StatefulWidget {
  final String title;
  const BlackButton({
    super.key,
    required this.title,
  });

  @override
  State<BlackButton> createState() => _BlackButtonState();
}

class _BlackButtonState extends State<BlackButton> {
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
              builder: (context) => SignINPage(),
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
