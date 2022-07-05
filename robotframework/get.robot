*** Settings ***
Library    String
Library    REST		 http://echo.jsontest.com	   ssl_verify=false


*** Test Cases ***

Get Employee
  GET       employee/1001
  Output    response  body
  String    response body employee	1001
  Integer    response status    200

  