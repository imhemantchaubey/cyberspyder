// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';

import '../constant.dart';

class TableText extends StatelessWidget {
  final String title;
  const TableText({
    super.key,
    required this.title,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(top: 18.0),
      child: Text(
        title,
        textAlign: TextAlign.center,
        style: TextStyle(fontWeight: FontWeight.bold, color: textPrimary),
      ),
    );
  }
}
