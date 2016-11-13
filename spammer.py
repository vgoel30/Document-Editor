import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from random import randint
import os
#this shall fetch a lame aunty joke
def get_auntyjoke():
    numjokes = 0;
    for f in os.listdir('auntyjokes'):
        if os.path.isfile(f):
            numjokes += 1
    filenum = randint(1,numjokes+1)
    filename = str(filenum) + '.txt'
    with open('auntyjokes/'+filename) as f:
        return f.read()
 
def main():
  print("LOL CATS")

  sender = "varun.goel.458@gmail.com"
  recievers = ["saudamini_19@hotmail.com","aditya.potdar@stonybrook.edu"]
  msg = MIMEMultipart()
  msg['From'] = sender
  msg['To'] = ", ".join(recievers)
  #msg['To'] = ", ".join(recievers)
  msg['Subject'] = "A nice joke for you"

  body = "Hello People\n\n" + get_auntyjoke()
  msg.attach(MIMEText(body, 'plain'))

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("varun.goel.458@gmail.com", "#")
 
  text = msg.as_string()
  #for x in range(0, 4):
  server.sendmail(sender, recievers, text)
  server.quit()

if __name__ == '__main__':
    main()