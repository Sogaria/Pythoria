import smtplib

my_email = "te2t3k53@gmail.com"
my_pw = "qcuf pbrg uvtk wycr"

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pw)
        connection.sendmail(from_addr=my_email, to_addrs="w0e9rtj4@yahoo.com", msg="Subject:Mr. Peter\n\nMR. PETERR")
except smtplib.SMTPException:
    print("No viable account data given.")
