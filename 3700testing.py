import re
String1 = "----- Block 0000011 ------- dsakjlfadjkfldajflkadj"
pattern = re.compile(r'[0][0][0][0][0]\d\d')
match = re.findall(pattern, String1)
list1 = ["0000010", "00000001"]
print(match in list1)
