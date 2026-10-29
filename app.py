from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    student_name = request.form['student_name']
    student_id = request.form['student_id']
    email = request.form['email']
    year = request.form['year']
    return render_template('success.html', student_name=student_name, student_id=student_id, email=email, year=year)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)