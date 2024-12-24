import pandas, smtplib, random
import datetime as dt

my_email = "te2t3k53@gmail.com"
my_pw = "qcuf pbrg uvtk wycr"

#csv birthday file
header = ["name", "mail", "year", "month", "day"]
list_birthdays = []
list_birthdays.append(["Max Mustermann", "hackermaus@gmail.com", 2001, 12, 24])
list_birthdays.append(["Maxine Musterfrau", "hackermaus@gmail.com", 2002, 8, 3])
data = pandas.DataFrame(list_birthdays, columns=header)
data.to_csv("Data/birthday.csv")

current_date = dt.datetime.now()

for index, row in data.iterrows():
    if row.day == current_date.day and row.month == current_date.month:
        letter_template = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_template}.txt") as file:
            letter = file.readlines()
        #for line in range(0, len(letter)):
           ## letter[line] = letter[line].strip('\n')
        letter[0] = letter[0].replace("[NAME]", row['name'])
        letter_string = ""
        for line in letter:
            letter_string += line
        
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pw)
                connection.sendmail(from_addr=my_email, to_addrs=row['mail'],
                                    msg=f"Subject: Happy Birthday!\n\n{letter_string}")
            print("Send Birthday Wishes to", row['name'])
        except smtplib.SMTPException:
            print("Failed sending Mail")