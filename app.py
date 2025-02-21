from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def arun():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project():
    return render_template('project.html')

@app.route('/skills')
def skills():
    return render_template('skill.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)