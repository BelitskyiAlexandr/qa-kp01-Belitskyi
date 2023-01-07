*** Settings ***
Library    Process
Suite Teardown  Terminate All Processes     kill=True

*** Test Cases ***
RunTest
    ${result}=  Start Process  ${CURDIR}/main.py  print('exit')
    Log    ${result.stdout}
    Terminate All Processes

MkDirTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mkdir')
    Log    ${result.stdout}
    Terminate All Processes

MkDirTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mkdir gg')
    Log    ${result.stdout}
    Terminate All Processes

PrintDirTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('rddir home')
    Log    ${result.stdout}
    Terminate All Processes

RdDirTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('rddir')
    Log    ${result.stdout}
    Terminate All Processes

MvDirTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvdir gg hh')
    Log    ${result.stdout}
    Terminate All Processes

MvDirTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvdir')
    Log    ${result.stdout}
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvdir gg')
    Log    ${result.stdout}
    Terminate All Processes

DelDirTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('deldir gg')
    Log    ${result.stdout}
    Terminate All Processes

DelDirTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('deldir')
    Log    ${result.stdout}
    Terminate All Processes


#bin
MkBinTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mkbin')
    Log    ${result.stdout}
    Terminate All Processes

MkBinTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mkbin gg')
    Log    ${result.stdout}
    Terminate All Processes

PrintBinTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('rdbin home')
    Log    ${result.stdout}
    Terminate All Processes

RdBinTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('rdbin')
    Log    ${result.stdout}
    Terminate All Processes

MvBinTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvbin Binn hh')
    Log    ${result.stdout}
    Terminate All Processes

MvBinTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvbin')
    Log    ${result.stdout}
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvbin Binn')
    Log    ${result.stdout}
    Terminate All Processes

DelBinTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('delbin Binn')
    Log    ${result.stdout}
    Terminate All Processes

DelBinTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('delbin')
    Log    ${result.stdout}
    Terminate All Processes


#buf
MkBufTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mkbuf')
    Log    ${result.stdout}
    Terminate All Processes

MkBufTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mkbuf Buffer')
    Log    ${result.stdout}
    Terminate All Processes

PrintBufTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('rdbuf Buffer')
    Log    ${result.stdout}
    Terminate All Processes

RdBufTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('rdbuf')
    Log    ${result.stdout}
    Terminate All Processes

MvBufTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvbuf Buffer hh')
    Log    ${result.stdout}
    Terminate All Processes

MvBufTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvbuf')
    Log    ${result.stdout}
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvbuf Buffer')
    Log    ${result.stdout}
    Terminate All Processes

AppBufTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('appqu Buffer 2')
    Log    ${result.stdout}
    Terminate All Processes

AppBufTestIncorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('appqu Buffer')
    Log    ${result.stdout}
    Terminate All Processes

PopBufTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('popqu Buffer')
    Log    ${result.stdout}
    Terminate All Processes

DelBufTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('delbuf Buffer')
    Log    ${result.stdout}
    Terminate All Processes

DelBufTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('delbuf')
    Log    ${result.stdout}
    Terminate All Processes


#logger
MkLogTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mklog')
    Log    ${result.stdout}
    Terminate All Processes

MkLogTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mklog logg')
    Log    ${result.stdout}
    Terminate All Processes

PrintLogTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('rdlog logg')
    Log    ${result.stdout}
    Terminate All Processes

RdLogTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('rdlog')
    Log    ${result.stdout}
    Terminate All Processes

MvLogTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvlog Logg hh')
    Log    ${result.stdout}
    Terminate All Processes

MvLogTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvlog')
    Log    ${result.stdout}
    ${result}=  Start Process  ${CURDIR}/main.py  print('mvlog Logg')
    Log    ${result.stdout}
    Terminate All Processes

DelLogTestCorrect
    ${result}=  Start Process  ${CURDIR}/main.py  print('dellog Logg')
    Log    ${result.stdout}
    Terminate All Processes

DelLogTestIncorrectValue
    ${result}=  Start Process  ${CURDIR}/main.py  print('dellog')
    Log    ${result.stdout}
    Terminate All Processes

IncorrectCommand
    ${result}=  Start Process  ${CURDIR}/main.py  print('Something here')
    Log    ${result.stdout}
    Terminate All Processes
