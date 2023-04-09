// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:cyberspyder/Components/table_text.dart';
import 'package:cyberspyder/constant.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart';
import '../Home/Components/navigation_dash.dart';

class TableOutput extends StatefulWidget {
  const TableOutput({super.key});

  @override
  State<TableOutput> createState() => _TableOutputState();
}

class _TableOutputState extends State<TableOutput> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // body: Stack(
      //   children: [
      //     Container(
      //       decoration: BoxDecoration(
      //         image: DecorationImage(
      //           image: AssetImage(
      //             "assets/images/background.png",
      //           ),
      //           fit: BoxFit.cover,
      //         ),
      //       ),
      //     ),
      //     NavigationDash(),
      //     SizedBox(
      //       height: 50,
      //     ),
      //     Center(
      //       child: Padding(
      //         padding: const EdgeInsets.only(top: 110.0, bottom: 25.0),
      //         child: Column(
      //           mainAxisAlignment: MainAxisAlignment.start,
      //           children: [
      //             Expanded(
      //               child: Container(
      //                 width: 1500,
      //                 height: MediaQuery.of(context).size.height,
      //                 decoration: BoxDecoration(
      //                   color: Color(0xFFF2F2F2).withOpacity(0.26),
      //                   borderRadius: BorderRadius.circular(6),
      //                 ),
      //                 child: Column(
      //                   children: [
      //                     SizedBox(
      //                       height: 20,
      //                     ),
      //                     Center(
      //                       child: Text(
      //                         'Data of the User',
      //                         textAlign: TextAlign.center,
      //                         style: TextStyle(
      //                           fontSize: 24,
      //                           color: textPrimary,
      //                           fontFamily: 'Poppins',
      //                           fontWeight: FontWeight.w500,
      //                         ),
      //                       ),
      //                     ),
      //                     SizedBox(
      //                       height: 30,
      //                     ),
      //                     Table(
      //                       border: TableBorder.all(
      //                         width: 1.0,
      //                         borderRadius: BorderRadius.circular(10),
      //                         color: Color(0xff2b2b2c),
      //                       ),
      //                       children: [
      //                         TableRow(
      //                           children: [
      //                             TableText(title: 'Sr.No'),
      //                             TableText(title: 'Phone Number'),
      //                             TableText(title: 'Email-ID'),
      //                             TableText(title: 'Facebook'),
      //                             TableText(title: 'Instagram'),
      //                             TableText(title: 'Twitter'),
      //                             TableText(title: 'Yahoo'),
      //                             TableText(title: 'Microsoft'),
      //                             TableText(title: 'Snapchat'),
      //                             TableText(title: 'Telegram'),
      //                             TableText(title: 'Flipkart'),
      //                             TableText(title: 'Apple'),
      //                             TableText(title: 'Github'),
      //                             TableText(title: 'Google'),
      //                             TableText(title: 'LinkedIn'),
      //                             TableText(title: 'Spotify'),
      //                             TableText(title: 'Pinterest'),
      //                           ],
      //                         ),
      //                       ],
      //                     ),
      //                   ],
      //                 ),
      //               ),
      //             ),
      //           ],
      //         ),
      //       ),
      //     ),
      //   ],
      // ),
      body: FutureBuilder<List<PhoneNo>>(
          future: ApiManager().fetchData(),
          builder:
              (BuildContext context, AsyncSnapshot<List<PhoneNo>> snapshot) {
            if (!snapshot.hasData) {
              return const Center(
                child: CircularProgressIndicator.adaptive(),
              );
            } else {
              return Container(
                padding: const EdgeInsets.all(5),
                child: DataClass(datalist: snapshot.data as List<PhoneNo>),
              );
            },
          },),
    );
  }
}
