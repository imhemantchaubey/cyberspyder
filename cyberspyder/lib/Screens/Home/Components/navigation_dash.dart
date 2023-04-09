// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:cyberspyder/Screens/Home/Components/menu_Item.dart';
import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';
import 'package:cyberspyder/Screens/Signin/sign_in_screen.dart';
import '../../../Components/black_Button_Dash.dart';

class NavigationDash extends StatefulWidget {
  const NavigationDash({super.key});

  @override
  State<NavigationDash> createState() => _NavigationDashState();
}

class _NavigationDashState extends State<NavigationDash> {
  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.topCenter,
      // height: MediaQuery.of(context).size.height,
      // width: MediaQuery.of(context).size.width,
      margin: EdgeInsets.all(20),
      padding: EdgeInsets.all(20),
      child: Row(
        children: <Widget>[
          Text(
            'CyberSpyder',
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: textPrimary,
            ),
          ),
          Spacer(
            flex: 1,
          ),
          MenuItem(
            title: 'Home',
            press: () {},
          ),
          MenuItem(
            title: 'Dashboard',
            press: () {},
          ),
          MenuItem(
            title: 'About Us',
            press: () {},
          ),
          MenuItem(
            title: 'Pricing',
            press: () {},
          ),
          MenuItem(
            title: 'Contact Us',
            press: () {},
          ),
          Spacer(),
          BlackButtonDash(
            title: 'Sign Out',
          ),
        ],
      ),
    );
  }
}
