// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:cyberspyder/Screens/Dashboard/dashboard_screen.dart';
import 'package:cyberspyder/Screens/Home/Components/navigation.dart';
import 'package:flutter/material.dart';

import '../../Components/form_Text.dart';
import '../../Components/main_button.dart';
import '../../constant.dart';

class SignINPage extends StatefulWidget {
  const SignINPage({super.key});

  @override
  State<SignINPage> createState() => _SignINPageState();
}

class _SignINPageState extends State<SignINPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: <Widget>[
          Container(
            decoration: BoxDecoration(
              image: DecorationImage(
                image: AssetImage('images/background2.png'),
                fit: BoxFit.cover,
              ),
            ),
          ),
          Navigation(),
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Container(
                    width: 500,
                    height: 450,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                      color: Color(0xFF2B2B2B).withOpacity(0.65),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Padding(
                          padding: const EdgeInsets.only(top: 15.0),
                          child: Center(
                            child: Text(
                              "Login",
                              style: TextStyle(
                                fontSize: 28,
                                fontFamily: 'Poppins',
                                fontWeight: FontWeight.w600,
                                color: Color(0xFFF2F2F2),
                              ),
                            ),
                          ),
                        ),
                        Padding(
                          padding: const EdgeInsets.only(left: 59.0, top: 35),
                          child: Text(
                            "Username",
                            textAlign: TextAlign.left,
                            style: TextStyle(
                              fontSize: 18,
                              fontFamily: 'Poppins',
                              fontWeight: FontWeight.w400,
                              color: Color(0xFFF2F2F2),
                            ),
                          ),
                        ),
                        FormText(),
                        Padding(
                          padding: const EdgeInsets.only(left: 59.0, top: 15),
                          child: Text(
                            "Password",
                            textAlign: TextAlign.left,
                            style: TextStyle(
                              fontSize: 18,
                              fontFamily: 'Poppins',
                              fontWeight: FontWeight.w400,
                              color: Color(0xFFF2F2F2),
                            ),
                          ),
                        ),
                        FormText(),
                        InkWell(
                          onTap: () {},
                          child: Padding(
                            padding: const EdgeInsets.only(left: 310, top: 10),
                            child: Text(
                              'Forgot Password?',
                              style: TextStyle(
                                fontSize: 14,
                                color: Color(0xfff2f2f2),
                              ),
                            ),
                          ),
                        ),
                        Center(
                          child: Padding(
                            padding: const EdgeInsets.only(top: 28.0),
                            child: TextButton(
                              style: TextButton.styleFrom(
                                padding: EdgeInsets.symmetric(
                                    horizontal: 40, vertical: 15.5),
                                backgroundColor: Color(0xFF037C99),
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(20),
                                ),
                              ),
                              onPressed: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => dashboard(),
                                  ),
                                );
                              },
                              child: Text(
                                'Login',
                                style: TextStyle(
                                  fontFamily: 'Poppins',
                                  fontSize: 18,
                                  fontWeight: FontWeight.w400,
                                  color: textPrimary,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    width: 2,
                    height: 390,
                    color: Color(0xFFF2F2F2),
                    alignment: Alignment.center,
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 75.0),
                    child: Container(
                      width: 500,
                      height: 550,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(10),
                        color: Color(0xFF2B2B2B).withOpacity(0.65),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Padding(
                            padding: const EdgeInsets.only(top: 15.0),
                            child: Center(
                              child: Text(
                                "Sign up",
                                style: TextStyle(
                                  fontSize: 28,
                                  fontFamily: 'Poppins',
                                  fontWeight: FontWeight.w600,
                                  color: Color(0xFFF2F2F2),
                                ),
                              ),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.only(left: 59.0, top: 35),
                            child: Text(
                              "Username",
                              textAlign: TextAlign.left,
                              style: TextStyle(
                                fontSize: 18,
                                fontFamily: 'Poppins',
                                fontWeight: FontWeight.w400,
                                color: Color(0xFFF2F2F2),
                              ),
                            ),
                          ),
                          FormText(),
                          Padding(
                            padding: const EdgeInsets.only(left: 59.0, top: 35),
                            child: Text(
                              "Email",
                              textAlign: TextAlign.left,
                              style: TextStyle(
                                fontSize: 18,
                                fontFamily: 'Poppins',
                                fontWeight: FontWeight.w400,
                                color: Color(0xFFF2F2F2),
                              ),
                            ),
                          ),
                          FormText(),
                          Padding(
                            padding: const EdgeInsets.only(left: 59.0, top: 15),
                            child: Text(
                              "Password",
                              textAlign: TextAlign.left,
                              style: TextStyle(
                                fontSize: 18,
                                fontFamily: 'Poppins',
                                fontWeight: FontWeight.w400,
                                color: Color(0xFFF2F2F2),
                              ),
                            ),
                          ),
                          FormText(),
                          Center(
                            child: Padding(
                              padding: const EdgeInsets.only(top: 28.0),
                              child: TextButton(
                                style: TextButton.styleFrom(
                                  padding: EdgeInsets.symmetric(
                                      horizontal: 40, vertical: 15.5),
                                  backgroundColor: Color(0xFF037C99),
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(20),
                                  ),
                                ),
                                onPressed: () {
                                  Navigator.push(
                                    context,
                                    MaterialPageRoute(
                                      builder: (context) => dashboard(),
                                    ),
                                  );
                                },
                                child: Text(
                                  'Sign Up',
                                  style: TextStyle(
                                    fontFamily: 'Poppins',
                                    fontSize: 18,
                                    fontWeight: FontWeight.w400,
                                    color: textPrimary,
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              )
            ],
          )
        ],
      ),
    );
  }
}
