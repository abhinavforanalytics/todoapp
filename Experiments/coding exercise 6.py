# file = open("../files/essay.txt",'w')
# token = file.write()
# file.write(token.title())
# file.close()

#members.txt
# import os
# user_input = input("Enter a name to be added")
# file = open(os.path.expanduser("~/Downloads/members.txt"),'a')
# file.write("\n"+user_input)
# file.close()


# filenames = ['my.txt', 'report.txt', 'presentation.txt']
#
# for filenames in filenames:
#     file = open(f"../Files/{filenames}","w")
#     file.write("Hello")
#     file.close()

filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    file = open(f"../Files/{filename}","r")
    content = file.read()
    print(content)
    file.close()