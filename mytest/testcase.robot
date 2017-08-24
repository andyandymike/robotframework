| *** Settings *** |
| Library | C:\\Users\\i067382\\PycharmProjects\\eztestRobot\\OSHelper.py

| *** Variables *** |
| ${VT} | Hello World

| *** Keywords *** |
| My Keywords |
| | Shell Command | echo my keywords

| *** Test Cases *** |
| tcase01 |
|  | [Documentation] | hive_query03 SUM and GROUP BY
|  | ${result} = | Shell Command | echo hello | False | True | True | True
|  | Should Contain | ${result} | hello
