// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:cyberspyder/Components/form_Text.dart';
import 'package:cyberspyder/Components/form_Text_dash.dart';
import 'package:cyberspyder/Screens/Dashboard/table_screen.dart';
import 'package:cyberspyder/Screens/Home/Components/navigation_dash.dart';
import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';

import '../../Components/table_text.dart';

class dashboard extends StatefulWidget {
  const dashboard({super.key});

  @override
  State<dashboard> createState() => _dashboardState();
}

class _dashboardState extends State<dashboard> {
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
          NavigationDash(),
          SizedBox(
            height: 50,
          ),
          Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  width: 1000,
                  height: 230,
                  decoration: BoxDecoration(
                    color: Color(0xFFF2F2F2).withOpacity(0.26),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        'Enter the Details',
                        style: TextStyle(
                          fontSize: 28,
                          fontFamily: 'Poppins',
                          fontWeight: FontWeight.w500,
                          color: Color(0xFFf2f2f2),
                        ),
                      ),
                      SizedBox(
                        height: 28,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Phone Number',
                                style: TextStyle(
                                  fontSize: 18,
                                  fontFamily: 'Poppins',
                                  fontWeight: FontWeight.w500,
                                  color: Color(0xFFf2f2f2),
                                ),
                              ),
                              FormTextDash(),
                            ],
                          ),
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Email-Id',
                                style: TextStyle(
                                  fontSize: 18,
                                  fontFamily: 'Poppins',
                                  fontWeight: FontWeight.w500,
                                  color: Color(0xFFf2f2f2),
                                ),
                              ),
                              FormTextDash(),
                            ],
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
                SizedBox(
                  height: 50,
                ),
                TextButton(
                  style: TextButton.styleFrom(
                    padding:
                        EdgeInsets.symmetric(horizontal: 40, vertical: 15.5),
                    backgroundColor: Color(0xFF037C99),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20),
                    ),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => TableOutput(),
                      ),
                    );
                  },
                  child: Text(
                    'Submit',
                    style: TextStyle(
                      fontFamily: 'Poppins',
                      fontSize: 18,
                      fontWeight: FontWeight.w400,
                      color: textPrimary,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
