---
title: Requirement Analysis for an Assignment Submission System
---

Note: This requirements analysis provides one possible interpretation of
the requirements. It is a simple example that sticks very close to the
problem description. Items may possibly be missing, inconsistent, or
incorrect although overall it is very good.

Data in this particular analysis has been mostly limited to entities,
with few attributes specified and no primary keys or data constraints
given.

System constraints 
==================

1.  Web server software

2.  Database management system (DBMS)

3.  File server for submitted files

4.  Physical or virtual server(s) with compatible OS installed to host
    the web server, DBMS, and file server, with network and internet
    connectivity

5.  Backup and recovery system

6.  Client computers with web browser and Internet access

Users/ Activities / Relevant Data / Constraints
===============================================

Students
--------

1.  Login/Logout

    a.  relevant data: credential data (username & password)

    b.  constraints: Students can use the system and access their
        courses and only their courses when they input correct username
        and matched password.

2.  Student is able to read assignment instructions

    a.  relevant data: assignment data

    b.  constraints: Students can only access assignments of the courses
        that they are enrolled in.

3.  Student can select assignment they want to submit

    a.  relevant data: course data, assignment data

    b.  constraints: Students can only choose the assignment from the
        classes that they enrolled. Students can only submit assignments
        that are open.

4.  Student can upload files

    a.  relevant data: course data, assignment data, submission data

    b.  constraints: System should allow only correct file types for
        uploading.

5.  Student can provide a comment along with a file submission

    a.  relevant data: course data, assignment data, submission data

    b.  constraints: System should allow a maximum number of characters
        and not allow sql injection.

6.  Student can submit/re-submit uploaded file

    a.  relevant data: course data, assignment data, submission data

    b.  constraints: Students can only choose the assignment from the
        classes that they enrolled. Students can only submit assignments
        that are open.

Teacher Assistants (TA)
-----------------------

1.  Login/Logout

    a.  relevant data: credential data (username & password)

    b.  constraints: TAs can use the system and access their course
        sections and only their course sections when they input correct
        username and matched password.

1.  TA can view course assignments.

    a.  relevant data: assignment data

    b.  constraints: TAs can only access assignments of the course
        sections that they are assigned to.

2.  TA can view student submissions for an assignment.

    a.  relevant data: student data, assignment data, submission data

    b.  constraints: TAs can only access assignments of the course
        sections that they are assigned to.

3.  TA can search students in a course

    a.  relevant data: student data, course data

    b.  constraints: TAs can search only the students who are in the
        course sections that they are assigned to manage.

4.  TA can collect assignments by downloading students\' submission
    files

    a.  relevant data: course data, assignment data, submission data

    b.  constraints: The system will show only the assignments from the
        course sections for which they are listed as a TA.

Instructor
----------

1.  Login/Logout

    a.  relevant data: credential data (username & password)

    b.  constraints: Instructors can use the system functions except
        student and system administrator functions, when they input
        correct username and matched password.

1.  Instructors can perform all functions TAs can perform.

    a.  Constraints: instructors can only access courses they have
        created.

2.  Instructor can create/edit/remove courses and sections

    a.  relevant data: student data, course data (including start and
        end dates), section data

    b.  constraints: Instructors can only manage courses they have
        created, but cannot remove or access the other instructors\'
        courses.

2.  Instructor can add /remove TAs for the course sections

    a.  relevant data: TA data, course data

    b.  constraints: Instructors can only add or remove TAs from their
        own course sections.

3.  Instructor can add/remove students in the course sections

    a.  relevant data: course data, student data

    b.  constraints: Instructors can only manage their course.
        Instructors should be able to upload students in bulk from a
        file.

4.  Instructor can create/edit/remove assignments of each course

    a.  relevant data: course data, assignment data (including start
        dates, due dates, and availability-end dates)

    b.  constraints: Instructors can only manage in their course.
        Assignments cannot be deleted between when a submission has
        occurred and the course end date.

System Administrator
--------------------

1.  Admin can add/edit/remove/disable instructors

    a.  relevant data: instructor data

    b.  constraints: Admin can manage only instructors; the system
        should check the type of user to be added is instructors.
        Instructors cannot be deleted if they have courses. Instructors
        cannot be disabled (have privileges revoked) if they have an
        active course.
