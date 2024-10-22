from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    course_categories = {
        'Programming': ['Python', 'JavaScript'],
        'Web Design': ['HTML/CSS', 'UI/UX Design'],
        'Data Science': ['Data Analysis', 'Machine Learning']
    }
    return render_template('courses.html', categories=course_categories)

@app.route('/courses/<category>/<course_name>')
def course_detail(category, course_name):
    return render_template('course_detail.html', category=category, course_name=course_name)

if __name__ == '__main__':
    app.run(debug=True)
