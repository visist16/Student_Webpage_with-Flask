# Student_Webpage_with-Flask
Student Name, Roll Number, with Student details and Enrollment details.
Using a standard flask template, create an application that:
1. On the home page (URI = ‘/’), (when we open it via the browser) displays an index page. The index
page must display a table with the list of students currently enrolled. The HTML table should be the
same as given below (Its id must be “all-students”). It should display an appropriate message if no
student is enrolled. It should also have a button labeled “Add student”, as shown in the Figure 1.
<table id = "all-students">
<tr>
<th>SNo</th>
<th>Roll Number</th>
<th>First Name</th>
<th>Last Name</th>
<th>Actions</th>
</tr>
<tr>
<td>s_no_1</td>
<td><a href="/student/<int:student_id>">roll_number_1</a></td>
<td>first_name_1</td>
<td>last_name_1</td>
<td>
<a href="/student/<int:student_id>/update" type="button">Update</a>
<a href="/student/<int:student_id>/delete" type="button">Delete</a>
</td>
</tr>
......
......
......
<tr>
<td>s_no_n</td>
<td><a href="/student/<int:student_id>">roll_number_n</a></td>
<td>first_name_n</td>
<td>last_name_n</td>
<td>
<a href="/student/<int:student_id>/update" type="button">Update</a>
<a href="/student/<int:student_id>/delete" type="button">Delete</a>
</td>
</tr>
</table>
Note: s no 1, roll number 1, first name 1, last name 1 .......... s no n, roll number n,
first name n, last name n, < int : student id > should be populated accordingly.

2. If the user clicks the “Add student”, your flask application should send a GET request to an endpoint
“/student/create”, which should display an HTML form as shown in the Figure 2. The HTML form
should be the same as given below. Its id must be “create-form”.
<form action="/student/create" method="POST" id="create-form">
<div>
<label>Roll Number:</label>
<input type="text" name="roll" required />
</div>
<div>
<label>First Name:</label>
<input type="text" name="f_name" required />
</div>
<div>
<label>Last Name:</label>
<input type="text" name="l_name" />
</div>
<div>
<label>Select Courses: </label>
<input type="checkbox" name="courses" value="course_1" />
<label>MAD I</label>
<input type="checkbox" name="courses" value="course_2" />
<label>DBMS</label>
<input type="checkbox" name="courses" value="course_3" />
<label>PDSA</label>
<input type="checkbox" name="courses" value="course_4" />
<label>BDM</label>
</div>
<div>
<input type="submit" value = "Submit">
</div>
</form>
• The HTML form should not have any other input elements.
• If the user clicks the submit button, the browser should send a POST request to your flask
application’s “/student/create” URI. The flask application should then create a student object
(with attributes roll number, first name and last name) and enrollments objects(s) (depending on
the number of courses user selects) and add them into the database and, it should redirect to the
home page (URI = ‘/’) and the student should be added into the table as shown in the Figure 3.
Note that each row of the table should be clickable
• If the roll number already exists, then, the user should be redirected to an HTML page, which
should display an appropriate message and have a button to navigate back to the home page (URI
= ‘/’), as shown in the Figure 4.
3. If the user clicks the “Update” button, your flask application should send a GET request to an endpoint
“/student/<int:student id>/update”, which should display an HTML form as shown in the Figure 5.
The HTML form should be the same as given below. Its id must be “update-form”.
<form action="/student/<int:student_id>/update" method="POST" id="update-form">

Page 3

<div>
<label>Roll Number:</label>
<input type="text" name="roll" value="current_roll" disabled />
</div>
<div>
<label>First Name:</label>
<input type="text" name="f_name" value="current_f_name" required />
</div>
<div>
<label>Last Name:</label>
<input type="text" name="l_name" value="current_l_name"/>
</div>
<div>
<label>Select Courses: </label>
<input type="checkbox" name="courses" value="course_1" />
<label>MAD I</label>
<input type="checkbox" name="courses" value="course_2" />
<label>DBMS</label>
<input type="checkbox" name="courses" value="course_3" />
<label>PDSA</label>
<input type="checkbox" name="courses" value="course_4" />
<label>BDM</label>
</div>
<div>
<input type="submit" value = "Submit">
</div>
</form>
Note: < int : student id >, current f name, current l name and current roll should be
populated accordingly.
• The HTML form should not have any other input elements.
• If the user clicks the submit button, the browser should send a POST request to your flask
application’s “/student/<int:student id/update>” URI.
• The flask application should then update the student and corresponding enrollments into the
database and redirect to the home page (URI = ‘/’).

4. If the user clicks the “Delete” button, your flask application should send a GET request to an end-
point “/student/<int:student id>/delete”, which should delete the student and all the corresponding

enrollments from the database and redirect to the home page (URI = ‘/’).
5. If the user clicks on the roll number of any row in the table in the home page of the flask application,
the application should send a GET request to an endpoint “/student/<int:student id>”, which should
show all the information (student details and enrollment details) in an HTML page. The HTML page
should also have a button labelled “Go Back” to navigate back to the home page (URI = ‘/’), as shown
in the Figure 6. There must be 2 HTML tables in this page, one for showing the personal details and
the other for displaying the enrollment details. The HTML for showing personal details should be the
same as given below. Its id must be “personal-detail”.

Page 4

<table id = "personal-details">
<tr>
<th>Roll Number</th>
<th>First Name</th>
<th>Last Name</th>
</tr>
<tr>
<td>roll-no-of-student</td>
<td>first-name-of-student</td>
<td>last-name-of-student</td>
</tr>
</table>
Note: All the <td> should be populated accordingly.
The HTML for displaying the enrollment details should be the same as given below. Its id should be
“enroll-table”.
<table id = "enroll-table">
<tr>
<th>S. No.</th>
<th>Course Code</th>
<th>Course Name</th>
<th>Course Description</th>
</tr>
<tr>
<td>1</td>
<td>course-code-for-course_1</td>
<td>course-name-for-course_1</td>
<td>course-description-for-course_1</td>
</tr>
......
......
......
<tr>
<td>2</td>
<td>course-code-for-course_n</td>
<td>course-name-for-course_n</td>
<td>course-description-for-course_n</td>
</tr>
</table>
Note: All the <td> should be populated accordingly.
