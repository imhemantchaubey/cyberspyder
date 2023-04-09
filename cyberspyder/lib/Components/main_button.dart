// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';

import '../constant.dart';

class MainButton extends StatefulWidget {
  final String title;
  final Function pressed;
  const MainButton({
    super.key,
    required this.title,
    required this.pressed,
  });

  @override
  State<MainButton> createState() => _MainButtonState();
}

class _MainButtonState extends State<MainButton> {
  @override
  Widget build(BuildContext context) {
    return TextButton(
      style: TextButton.styleFrom(
        padding: EdgeInsets.symmetric(horizontal: 40, vertical: 15.5),
        backgroundColor: Color(0xFF037C99),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
        ),
      ),
      onPressed: () {},
      child: Text(
        widget.title,
        style: TextStyle(
          fontFamily: 'Poppins',
          fontSize: 18,
          fontWeight: FontWeight.w400,
          color: textPrimary,
        ),
      ),
    );
  }
}
