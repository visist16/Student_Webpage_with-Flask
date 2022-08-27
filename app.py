from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)
    courses = db.relationship("Course", secondary = "enrollments")
class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    course_code = db.Column(db.String, unique = True, nullable = False)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)
    #students = db.relationship("Student", secondary = "enrollments")
class Enrollments(db.Model):
    __tablename__ = "enrollments"
    enrollment_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable = False)

    @app.route('/')
def index():
    if request.method == "GET":
        students = Student.query.all()
        if len(students) ==0:
            return render_template("nostudent.html")
        return render_template("index.html",students = students)
@app.route('/student/create',methods = ['GET','POST'])
def addstu():
    if request.method=="GET":
        return render_template("addstu.html")
    else:
        temp = Student.query.filter_by(roll_number = request.form["roll"]).first()
        if temp is None:
            stu = Student(roll_number = request.form["roll"],first_name = request.form["f_name"],last_name = request.form["l_name"])
            courses_taken = request.form.getlist("courses")
            for cour in courses_taken:
                if cour=='course_1':
                    stu.courses.append(Course.query.filter_by(course_id = 1).one())
                elif cour=='course_2':
                    stu.courses.append(Course.query.filter_by(course_id = 2).one())
                elif cour == 'course_3':
                    stu.courses.append(Course.query.filter_by(course_id = 3).one())
                elif cour == 'course_4':
                    stu.courses.append(Course.query.filter_by(course_id = 4).one())
            db.session.add(stu)
            db.session.commit()
            return redirect("/")
        else:
            return render_template("rollexists.html")

@app.route('/student/<int:studentid>/update',methods = ["GET","POST"])
def upda(studentid):
    if request.method == "GET":
        stud = Student.query.filter_by(student_id = studentid).one()
        return render_template("update.html",stud = stud)
    else:
        temp = Enrollments.query.filter_by(estudent_id = studentid).first()
        if temp is not None:            
            enroll = Enrollments.query.filter_by(estudent_id = studentid).all()
            for enrollment in enroll:
                db.session.delete(enrollment)
        studa = Student.query.filter_by(student_id = studentid).one()
        studa.first_name = request.form["f_name"]
        studa.last_name = request.form["l_name"]
        courses_taken = request.form.getlist("courses")
        for cour in courses_taken:
            if cour=='course_1':
                studa.courses.append(Course.query.filter_by(course_id = 1).one())
            elif cour=='course_2':
                studa.courses.append(Course.query.filter_by(course_id = 2).one())
            elif cour == 'course_3':
                studa.courses.append(Course.query.filter_by(course_id = 3).one())
            elif cour == 'course_4':
                studa.courses.append(Course.query.filter_by(course_id = 4).one())
        db.session.commit()
        return redirect("/")
@app.route('/student/<int:studentid>/delete')
def dele(studentid):
    temp = Enrollments.query.filter_by(estudent_id = studentid).first()
    if temp is not None:            
        enroll = Enrollments.query.filter_by(estudent_id = studentid).all()
        for enrollment in enroll:
            db.session.delete(enrollment)
    studa = Student.query.filter_by(student_id = studentid).one()
    db.session.delete(studa)
    db.session.commit()
    return redirect("/")
@app.route('/student/<int:studentid>')
def show(studentid):
    stud = Student.query.filter_by(student_id = studentid).one()
    return render_template("show.html",stud = stud)
if __name__ == "__main__":
    app.run()
