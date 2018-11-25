# Email reader and writer to Sqlite database
# Author: Carl Brockwell
# Date: January 2018

import imaplib
import email
import sqlite3

mail = imaplib.IMAP4_SSL('imap.gmail.com')
email_user = input('Email: ')
email_pass = input('Password: ')
mail.login(email_user, email_pass)
mail.list()
mail.select('inbox')

# Setup database,  unless already created.
db = sqlite3.connect("emails.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS emails(to_address TEXT, from_address TEXT, date TEXT, subject TEXT, body TEXT)")
cursor = db.cursor()

result, data = mail.uid('search', None, "ALL")
i = len(data[0].split())

# Iterate through emails ,parse data into relevant variables
for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = email_data[0][1]

    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    to_string = email_message['to']  # 'ooo@a1.local.tld'
    from_string = email_message['from']  # 'root@a1.local.tld'
    date_string = email_message['date']
    subject_string = email_message['subject']

    # Print out to screen parsed email(s) in unicode format into an SQLite Database.
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            body_string = (str(body, 'utf-8'))
            cursor.execute("INSERT INTO emails VALUES(?, ?, ?, ?, ?)", (to_string, from_string,
                                                                        date_string, subject_string, body_string))
        else:
            continue

    # Print typical email fields to screen for review
    print("*" * 50)
    print("Date/time: " + date_string)
    print("From: " + from_string)
    print("To: " + to_string)
    print("Subject: " + subject_string)
    print(body_string)
    print("#" * 50)
    print("\n\n\n\n")


# Print out database rows to screen for review.
print("DATABASE RECORDS")
print("*" * 50)
cursor.execute("SELECT * FROM emails")
for row in cursor:
    print(row)

cursor.close()
db.close()
