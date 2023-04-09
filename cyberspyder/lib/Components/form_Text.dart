// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';

class FormText extends StatelessWidget {
  const FormText({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(left: 55.0, top: 15),
      child: SizedBox(
        width: 384,
        height: 56,
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
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: Color(0xFFF2F2F2).withOpacity(0.26),
              ),
            ),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
            ),
          ),
        ),
      ),
    );
  }
}
