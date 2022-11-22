#example 02
from nhatvd2_lib import print_from_lib
print_from_lib()
print ("hello Nhatvd2!! from python code")
sourceFile = open('nhatvd2.txt', 'w')
print("hello Nhatvd2!! from python code", file = sourceFile)
sourceFile.close()


