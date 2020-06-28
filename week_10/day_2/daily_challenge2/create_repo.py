from github import Github
import smtplib
import email

user_name = "ssyelenik"
token ="703215299eda225978f13786065c615d1f2ab504"
g=Github(token)

print(g.get_user())


    
user = g.get_user()
path = "C:\BootCamp\di_exercise\week_10\day_2\daily_challenge2"


repo_name = "SharonYelenik"
repo = user.create_repo(repo_name)

commit_message = "controling Github with Python"
content = "Learning how to create a file on Github using Python"


repo.create_file("text.py", commit_message, content, branch="test")



gmail_user = 'ssyelenik@gmail.com'
gmail_password = 'mnisghh2'

sent_from = gmail_user
to = ['ssyelenik@gmail.com', 'love.lrning@gmail.com']
subject = 'OMG Super Important Message'
body = f'This is my daily challenge email. See my daily challenge here: '

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP('Smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user,gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
