import datetime
current_date = datetime.date.today()
print(current_date)

mood = input("Enter your current mood: ")
journal = input("Let your thoughts flow:\n")

with open(f"../Journal/{current_date}.txt",'w') as file:
    file.write("Mood: "+mood+2*"\n")
    file.write("Journal:\n"+journal.capitalize())