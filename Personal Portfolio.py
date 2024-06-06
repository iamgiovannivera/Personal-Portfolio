# 1. Setup Flask


# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/resume')
# def resume():
#     return render_template('resume.html')

# @app.route('/projects')
# def projects():
#     return render_template('projects.html')

# @app.route('/skills')
# def skills():
#     return render_template('skills.html')

# @app.route('/blog')
# def blog():
#     return render_template('blog.html')

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         # handle form submission
#         pass
#     return render_template('contact.html')

# @app.route('/testimonials')
# def testimonials():
#     return render_template('testimonials.html')

# @app.route('/in_progress')
# def in_progress():
#     return render_template('in_progress.html')

# @app.route('/archive')
# def archive():
#     return render_template('archive.html')

# @app.route('/gallery')
# def gallery():
#     return render_template('gallery.html')

# @app.route('/certificates')
# def certificates():
#     return render_template('certificates.html')

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
# 2. Create HTML Templates



# <!-- home.html -->
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Home - My Portfolio</title>
#     <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
# </head>
# <body>
#     <header>
#         <h1>Welcome to My Portfolio</h1>
#         <nav>
#             <ul>
#                 <li><a href="{{ url_for('home') }}">Home</a></li>
#                 <li><a href="{{ url_for('about') }}">About Me</a></li>
#                 <li><a href="{{ url_for('resume') }}">Resume</a></li>
#                 <li><a href="{{ url_for('projects') }}">Projects</a></li>
#                 <li><a href="{{ url_for('skills') }}">Skills</a></li>
#                 <li><a href="{{ url_for('blog') }}">Blog</a></li>
#                 <li><a href="{{ url_for('contact') }}">Contact</a></li>
#                 <li><a href="{{ url_for('testimonials') }}">Testimonials</a></li>
#                 <li><a href="{{ url_for('in_progress') }}">In Progress</a></li>
#                 <li><a href="{{ url_for('archive') }}">Archive</a></li>
#                 <li><a href="{{ url_for('gallery') }}">Gallery</a></li>
#                 <li><a href="{{ url_for('certificates') }}">Certificates</a></li>
#             </ul>
#         </nav>
#     </header>
#     <main>
#         <section>
#             <h2>About Me</h2>
#             <p>This is the main landing page of my portfolio.</p>
#             <img src="{{ url_for('static', filename='profile.jpg') }}" alt="Profile Picture">
#         </section>
#     </main>
#     <footer>
#         <p>&copy; 2024 My Portfolio</p>
#     </footer>
# </body>
# </html>






# 3. Style the Pages




# css


# /* styles.css */
# body {
#     font-family: Arial, sans-serif;
#     margin: 0;
#     padding: 0;
#     background-color: #f4f4f4;
# }

# header {
#     background-color: #333;
#     color: #fff;
#     padding: 1em 0;
#     text-align: center;
# }

# nav ul {
#     list-style-type: none;
#     padding: 0;
# }

# nav ul li {
#     display: inline;
#     margin: 0 1em;
# }

# nav ul li a {
#     color: #fff;
#     text-decoration: none;
# }

# main {
#     padding: 2em;
#     text-align: center;
# }

# footer {
#     background-color: #333;
#     color: #fff;
#     text-align: center;
#     padding: 1em 0;
#     position: absolute;
#     bottom: 0;
#     width: 100%;
# }


# 4. Handle Form Submissions


    

# html



# <!-- contact.html -->
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Contact - My Portfolio</title>
#     <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
# </head>
# <body>
#     <header>
#         <h1>Contact Me</h1>
#         <nav>
#             <!-- Navigation links -->
#         </nav>
#     </header>
#     <main>
#         <section>
#             <h2>Get in Touch</h2>
#             <form method="POST" action="{{ url_for('contact') }}">
#                 <label for="name">Name:</label>
#                 <input type="text" id="name" name="name" required>
#                 <label for="email">Email:</label>
#                 <input type="email" id="email" name="email" required>
#                 <label for="message">Message:</label>
#                 <textarea id="message" name="message" required></textarea>
#                 <button type="submit">Send</button>
#             </form>
#         </section>
#     </main>
#     <footer>
#         <p>&copy; 2024 My Portfolio</p>
#     </footer>
# </body>
# </html>


# 5. Implement Contact Form Handling

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#         # Handle form submission (e.g., send an email, save to database)
#         return redirect(url_for('home'))
#     return render_template('contact.html')



# 6. Deploy and Document

# #Markdown

# # My Personal Portfolio

# ## Introduction

# This is my personal portfolio website built with Flask.

# ## Features

# - Home Page
# - About Me Page
# - Resume/CV Page
# - Portfolio Projects Page
# - Skills Page
# - Blog/Articles Page
# - Contact Page
# - Testimonials/Recommendations Page
# - Projects in Progress Page
# - Portfolio Archive Page
# - Photography/Art Gallery Page
# - Certificates and Awards Page

# ## Running the Application

# 1. Clone the repository.
# 2. Install the required packages: `pip install -r requirements.txt`
# 3. Run the application: `python app.py`
# 4. Open your browser and navigate to `http://localhost:5000`

# ## Contact

# For any inquiries, please contact me at [your email address].