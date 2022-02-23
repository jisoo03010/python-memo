#  파이썬으로 메모장 만들어보기
import time
import tkinter.font as tkFont
from colorama import Fore, Back, Style

print(+ 'some red text')

# option = sys.argv[1]
# if option == '-a':
text = input("제목을 작성하시오 :")
content = input("내용 작성하시오 :")

times = time.strftime('%x %X', time.localtime(time.time()))
f = open("./memo.txt", 'w',  encoding="UTF-8")

f.write("제목 : %s" % text)
f.write("\n\n")
f.write("내용 : %s" % content)

f.write("\n")
f.write("\n")
f.write("작성 일자 : %s" % times)
f.close()
