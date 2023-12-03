from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
# from dotenv import load_dotenv
import os
# load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_KEY')


PROJECT = [
    {
    'title': 'Simple Calculator',
    'img_url': 'images/calculator.jpg',
    'demo_link': 'https://gopiranganathan.github.io/Calculator/',
    'github': 'https://github.com/GopiRanganathan/Calculator',
    'web_dev': ['HTML', 'CSS', 'JavaScript']
   },

   {
       'title': 'Weather App',
       'img_url': 'images/weatherapp.png',
       'demo_link': 'https://gopiranganathan.github.io/Weather-App/',
       'github': 'https://github.com/GopiRanganathan/Weather-App',
       'web_dev': ['HTML', 'CSS', 'JavaScript']
       
   },

   {
       'title': 'Personal Blog',
       'img_url': 'images/blog.jpg',
       'demo_link': 'https://know-more-blog.onrender.com/',
       'github': 'https://github.com/GopiRanganathan/blog', 
       'web_dev': ['Flask']
   },

   {
       'title': 'Portfolio 2',
       'img_url': 'images/portfolio-2.png',
       'demo_link': 'https://gopiranganathan.github.io/portfolio_react/',
       'github': 'https://github.com/GopiRanganathan/portfolio_react',
       'web_dev': ['HTML', 'CSS', 'JavaScript', 'ReactJS']
   },

   {
       'title': 'Portfolio 1',
       'img_url': 'images/portfolio-1.png',
       'demo_link': 'https://gopiranganathan.github.io/portfolio/',
       'github': 'https://github.com/GopiRanganathan/portfolio',
       'web_dev': ['HTML', 'CSS']
   }, 

   {
       'title': 'Markdown Previewer', 
       'img_url': 'images/markdown-previewer.png',
       'demo_link': 'https://gopiranganathan.github.io/markdown-previewer/',
       'github': 'https://github.com/GopiRanganathan/markdown-previewer',
       'web_dev': ['HTML', 'CSS', 'JavaScript', 'ReactJS']
   }, 

   {
       'title': 'Random Quote Machine',
       'img_url': 'images/random-quote-machine.png',
       'demo_link': 'https://gopiranganathan.github.io/random-quote-machine/',
       'github': 'https://github.com/GopiRanganathan/random-quote-machine',
       'web_dev': ['HTML', 'CSS', 'JavaScript', 'ReactJS']
   }

 ]

def send_mail(msg):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=os.environ.get('FROM_EMAIL'), password=os.environ.get('PASSWORD'))
        connection.sendmail(from_addr=os.environ.get('FROM_EMAIL'), to_addrs=os.environ.get('TO_EMAIL'), msg=msg)
        print('Email sent')

@app.route('/')
def home():
    active_page = 'home'
    return render_template('index.html', active=active_page)

@app.route('/projects')
def project():
    active_page = 'project'
    return render_template('project.html', projects=PROJECT, active=active_page)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    active_page = 'contact'
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        msg=f'Subject: Client from your portfolio!!!\n\nName: {name}\nEmail: {email}\nMessage: {message}.'
        send_mail(msg)
        flash('Message sent succesfully!')
        redirect(url_for('contact'))

    return render_template('contact.html', active=active_page)

if __name__ == '__main__':
    app.run(debug=False)
