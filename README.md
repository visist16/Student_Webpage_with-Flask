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
