from flask import Flask, render_template, request, flash, redirect, url_for
# from dotenv import load_dotenv
import os
# load_dotenv()
from flask_mail import Mail, Message

mail=Mail()
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_KEY')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('FROM_EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)

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
       'title': 'Todo List',
       'img_url': 'images/todo.png',
       'demo_link': 'https://todo-ghbn.onrender.com/',
       'github': 'https://github.com/GopiRanganathan/todo',
       'web_dev': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'Bootstrap']
   },

    {
       'title': 'Image Watermarking App',
       'img_url': 'images/watermarking.png',
       'demo_link': '#',
       'github': 'https://github.com/GopiRanganathan/image-watermark',
       'web_dev': ['Python', 'Tkinter', 'Pillow']
   },
    {
       'title': 'Typing Speed Test App',
       'img_url': 'images/typing-speed-test.png',
       'demo_link': '#',
       'github': 'https://github.com/GopiRanganathan/typing-speed-test',
       'web_dev': ['Python', 'Tkinter']
   },
   {
       'title': 'Breakout Game',
       'img_url': 'images/breakout-game.png',
       'demo_link': '#',
       'github': 'https://github.com/GopiRanganathan/breakout-game',
       'web_dev': ['Python', 'Turtle']
   },
   {
       'title': 'Cafe & Wifi API',
       'img_url': 'images/cafe-api.png',
       'demo_link': 'https://cafe-api-nzxp.onrender.com/',
       'github': 'https://github.com/GopiRanganathan/cafe-api',
       'web_dev': ['Python', 'Flask']
   },
   {
       'title': 'Cafe website using Cafe & Wifi API',
       'img_url': 'images/cafe-wifi.png',
       'demo_link': 'https://cafe-wifi-gr.onrender.com/',
       'github': 'https://github.com/GopiRanganathan/cafe-wifi',
       'web_dev': ['Python', 'Flask', 'HTML', 'CSS', 'Bootstrap']
   },
     {
       'title': 'Dangerous Writing App',
       'img_url': 'images/text-disappearing-app.png',
       'demo_link': '#',
       'github': 'https://github.com/GopiRanganathan/text-disappearing-app',
       'web_dev': ['Python', 'Tkinter']
   },
     {
       'title': 'PDF to Audio',
       'img_url': 'images/pdf-to-audio.png',
       'demo_link': '#',
       'github': 'https://github.com/GopiRanganathan/text-to-audio',
       'web_dev': ['Python', 'Tkinter']
   },
        {
       'title': 'Web Scrape Prof. Course',
       'img_url': 'images/web-scrape-coursera.png',
       'demo_link': '#',
       'github': 'https://github.com/GopiRanganathan/web-scrape-coursera',
       'web_dev': ['Python', 'BeautifulSoup4']
   },
     {
       'title': 'Space Invaders',
       'img_url': 'images/space-invaders.png',
       'demo_link': '#',
       'github': 'https://github.com/GopiRanganathan/space-invaders',
       'web_dev': ['Python', 'pygame']
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
        msg = Message("Client from your portfolio!!!",
                  sender=os.environ.get('FROM_EMAIL'),
                  recipients=[os.environ.get('TO_EMAIL')])
        msg.body=f'Name: {name}\nEmail: {email}\nMessage: {message}.'
        mail.send(msg)
        
        flash('Message sent succesfully!')
        redirect(url_for('contact'))

    return render_template('contact.html', active=active_page)

if __name__ == '__main__':
    app.run(debug=False)
