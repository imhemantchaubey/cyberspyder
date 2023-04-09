import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';

class BodyContent extends StatefulWidget {
  const BodyContent({super.key});

  @override
  State<BodyContent> createState() => _BodyContentState();
}

class _BodyContentState extends State<BodyContent> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 5),
          child: Column(
            children: <Widget>[
              Text(
                'Unlock the Hidden Value in Web Data',
                style: TextStyle(
                    fontSize: 48, fontFamily: 'Poppins', color: textPrimary),
              )
            ],
          ),
        ),
      ),
    );
  }
}
