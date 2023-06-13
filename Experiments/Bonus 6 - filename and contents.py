
content = ["File created","File reported","Presentation created"]

filename = ["doc.txt","report.txt","presentation.txt"]

for content,filename in zip(content,filename):
    file = open(f"../Files/{filename}",'w')
    file.write(content)
    file.close()
