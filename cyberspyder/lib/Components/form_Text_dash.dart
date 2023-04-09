// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';

class FormTextDash extends StatefulWidget {
  const FormTextDash({
    super.key,
  });

  @override
  State<FormTextDash> createState() => _FormTextDashState();
}

class _FormTextDashState extends State<FormTextDash> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(top: 15),
      child: SizedBox(
        width: 320,
        height: 46,
        child: TextField(
          style: TextStyle(
            fontSize: 16,
            fontFamily: 'Poppins',
            color: Color(0xFFF2F2F2),
          ),
          cursorColor: Color(0xFFF2F2F2),
          decoration: InputDecoration(
            filled: true,
            fillColor: Color(0xFFF2F2F2).withOpacity(0.26),
            enabled: true,
            enabledBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: Color(0xFFF2F2F2).withOpacity(0.26),
              ),
            ),
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: Color(0xFFF2F2F2).withOpacity(0.26),
              ),
            ),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(15),
            ),
          ),
        ),
      ),
    );
  }
}
