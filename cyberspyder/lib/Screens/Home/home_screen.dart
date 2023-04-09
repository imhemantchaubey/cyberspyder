// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:cyberspyder/Screens/Home/Components/navigation.dart';
import 'package:cyberspyder/constant.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:flutter/material.dart';

import '../../Components/main_button.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          Container(
            decoration: BoxDecoration(
              image: DecorationImage(
                image: AssetImage(
                  "assets/images/background.png",
                ),
                fit: BoxFit.cover,
              ),
            ),
          ),
          Column(
            children: [
              SingleChildScrollView(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 45.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    // mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      Navigation(),
                      Padding(
                        padding: const EdgeInsets.only(
                            top: 60.0, right: 109, bottom: 95),
                        child: SingleChildScrollView(
                          child: Row(
                            children: [
                              Expanded(
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      '''Unlock the Hidden\nValue in Web Data''',
                                      style: TextStyle(
                                          fontSize: 56,
                                          fontFamily: 'Poppins',
                                          color: textPrimary,
                                          fontWeight: FontWeight.bold),
                                    ),
                                    Padding(
                                      padding:
                                          const EdgeInsets.only(right: 80.0),
                                      child: Text(
                                        ''' We specialize in providing advanced web scraping solutions and tools\n to help businesses automate their data collection process and gain\n valuable insights from web data.''',
                                        style: TextStyle(
                                            fontSize: 14,
                                            fontFamily: 'Poppins',
                                            color: textPrimary,
                                            fontWeight: FontWeight.w400),
                                      ),
                                    ),
                                    SizedBox(
                                      height: 20,
                                    ),
                                    MainButton(
                                      title: 'Sign up for Free',
                                      pressed: () {},
                                    ),
                                  ],
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.only(left: 63.0),
                                child: Image.asset(
                                  'images/cselement.png',
                                  width: 700,
                                  height: 446,
                                  // fit: BoxFit.cover,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
      // body: Stack(
      //   children: <Widget>[
      //     SvgPicture.asset('assets/images/gradient.svg'),
      //     Column(
      //       crossAxisAlignment: CrossAxisAlignment.start,
      //       children: <Widget>[
      //         Navigation(),
      //         Text(
      //           'Unlock the Hidden Value in Web Data',
      //           style: TextStyle(
      //               fontSize: 38, fontFamily: 'Poppins', color: textPrimary),
      //         ),
      //       ],
      //     ),
      //   ],
      // ),
    );
  }
}
