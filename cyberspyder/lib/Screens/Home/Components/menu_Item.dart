// ignore_for_file: prefer_const_constructors

import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';

class MenuItem extends StatelessWidget {
  final String title;
  final Function press;
  const MenuItem({
    super.key,
    required this.title,
    required this.press,
  });

  @override
  Widget build(BuildContext context) {
    return InkWell(
      // onTap: press(),
      onTap: press(),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 15.0),
        child: Text(
          title,
          style: TextStyle(
            fontSize: 18,
            color: textPrimary,
          ),
        ),
      ),
    );
  }
}
