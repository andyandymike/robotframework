| *** Settings *** |
| Library | C:\\Users\\i067382\\PycharmProjects\\eztestRobot\\OSHelper.py

| *** Variables *** |
| ${VT} | Hello World
| ${COUNT} | 0

| *** Keywords *** |
| My Keywords |
|  | Shell Command | echo ${VT} | False | True | True | True

| *** Test Cases *** |
| tcase01 |
|  | [Documentation] | hive_query03 SUM and GROUP BY
|  | My Keywords
|  | ${result} = | Shell Command | echo hello | False | True | True | True
|  | Should Contain | ${result} | hello
|  | :FOR | ${COUNT} | IN RANGE | 5
|  | \ | Shell Command | echo ${COUNT} | False | True | True | True
|  | \ | ${COUNT} = | Evaluate | ${COUNT} + 1