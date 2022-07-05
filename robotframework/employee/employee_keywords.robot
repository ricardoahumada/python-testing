| *** Settings ***   |
| Documentation      | Test the employee Python script
| Library            | OperatingSystem
 
| *** Variables ***  |
| ${APPLICATION}     | py ./employee.py

| *** Keywords ***              |
| Clear Employees List          | [Documentation] | Clears the list of employees
| | ${rc}                       | ${output} =     | Run and Return RC and Output | ${APPLICATION} remove_all_employees
| | Should Be Equal As Integers | ${rc}           | 0

| *** Test Cases ***            |                 |
| Empty Employees List          | [Documentation] | Verify the output of an empty employees list
| | [Setup]                     | Clear Employees List
| | Should Be Equal             | ${output}       | []
| Add Employee                  | [Documentation] | Verify adding an employee
| | [Setup]                     | Clear Employees List
| | Should Be Equal             | ${output}       | ['John Doe']
