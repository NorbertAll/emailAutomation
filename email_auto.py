import smtplib, ssl
import pandas as pd
import os
import locale
os.environ["PYTHONIOENCODING"] = "utf-8"
scriptLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8")

emails = pd.read_excel("email_list.xlsx")
message = """\
Subject: This is subject.
To: norbert_gutkowski@interia.pl

Cześć ziomek."""

port =465

context= ssl.create_default_context()

server=smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
server.login("norbert.gutk@gmail.com", "arhnflqbmyiofvgj")

server.sendmail("norbert.gutk@gmail.com", "norbert_gutkowski@interia.pl", message.encode('ascii', 'ignore').decode('ascii')
)