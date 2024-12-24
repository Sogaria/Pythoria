import smtplib, random
import datetime as dt

my_email = "te2t3k53@gmail.com"
my_pw = "qcuf pbrg uvtk wycr"

#try:
 #   with smtplib.SMTP("smtp.gmail.com", 587) as connection:
  #      connection.starttls()
   #     connection.login(user=my_email, password=my_pw)
    #    connection.sendmail(from_addr=my_email, to_addrs="w0e9rtj4@yahoo.com", msg="Subject:Mr. Peter\n\nMR. PETERR")
#except smtplib.SMTPException:
 #   print("No viable account data given.")
list_quotes = []
try:
    with open("quotes.txt") as file:
        list_quotes = file.readlines()
        random.shuffle(list_quotes)
except FileNotFoundError:
    print("File does not exist.")

if list_quotes:
    current_date = dt.datetime.now()
    if current_date.weekday() == 1:
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pw)
                connection.sendmail(from_addr=my_email, to_addrs="scarevenage@gmail.com", msg=f"Subject: Sup Sup\n\n{list_quotes[0].strip("\n")}")
        except smtplib.SMTPException:
            print("Exception while sending E-Mail.")
else:
    print("No quotes available in the file.")
