from django.shortcuts import render, HttpResponse, redirect

from .MyFiles.change_pass import *
from .MyFiles.edit_database import *
from .MyFiles.event_register import *
from .MyFiles.insert_database import *
from .MyFiles.insrert_marks import *
from .MyFiles.remove_database import *


from application.models import Student
from application.models import Faculty


# username = admin
# password = admin


# Create your views here.
login_done = False

student_data = {}
faculty_data = {}
admin_data = {}
sem_data = {
    "sem1": ["Maths 1", "Physics", "Java 1", "Software Engineering"],
    "sem2": [
        "Maths 2",
        "Fundamental Of Electrical Engineering",
        "Java 2",
        "Data Structure",
        "Database Management System",
    ],
    "sem3": [
        "Full Stack Development",
        "Python 1",
        "Digital Electronics",
        "Probability & Statistics",
        "Effective Technical Communication",
    ],
    "sem4": [
        "Full Stack Development 2",
        "Python 2",
        "Theory Of Computation",
        "Discrete Maths",
    ],
    "sem5": [
        "Algorithm",
        "Operating System",
        "Computer Network",
        "Computer Organization and Architecture",
    ],
}


# main page
def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        button = request.POST.get("button")

        obj = CheckInDatabase(email, password, button)
        answer = obj.check()
        print(answer)  # [()] form
        if answer:
            data = answer[0]
            print(data)  # () form
            global login_done
            login_done = True

            # student login
            if button == "student":
                global student_data
                student_data = {
                    "enrollment": data[1],
                    "name": data[2],
                    "email": data[3],
                    "maths1": data[5],
                    "physics": data[6],
                    "java1": data[7],
                    "software": data[8],
                    "maths2": data[9],
                    "fee": data[10],
                    "java2": data[11],
                    "ds": data[12],
                    "dbms": data[13],
                    "department": data[14],
                    "sem1_spi": data[15],
                    "sem2_spi": data[16],
                    "fees": data[17],
                    "phone": data[18],
                    "address": data[19],
                    "fsd": data[20],
                    "python1": data[21],
                    "de": data[22],
                    "ps": data[23],
                    "etc": data[24],
                    "sem3_spi": data[25],
                    "fsd2": data[26],
                    "python2": data[27],
                    "toc": data[28],
                    "dm": data[29],
                    "sem4_spi": data[30],
                    "algo": data[31],
                    "os": data[32],
                    "cn": data[33],
                    "coa": data[34],
                    "sem5_spi": data[35],
                }
                return render(request, "student.html", student_data)

            # faculty login
            elif button == "faculty":
                global faculty_data
                faculty_data = {
                    "f_id": data[0],
                    "name": data[1],
                    "email": data[2],
                    "phone": data[4],
                    "address": data[5],
                    "department": data[6],
                    "designation": data[7],
                    "course": data[8],
                    "atteched_year": data[9],
                }
                return render(request, "faculty.html", faculty_data)

            # admin login
            elif button == "admin":
                global admin_data
                admin_data = {
                    "email": data[2],
                    "name": data[1],
                }
                return render(request, "adminfile.html", {**admin_data, **sem_data})

        # if answer is false
        else:
            return render(
                request, "index.html", {"error_message": "Invalid Email or Password..."}
            )
    return render(request, "index.html")


# about page
def about(request):
    return render(request, "about.html")


# if student query form is submit or change password then execute this
def student(request):
    if login_done:
        if request.method == "POST":
            enrollment = request.POST.get("enrollment")
            button = request.POST.get("button")

            if button == "change_password":
                current_password = request.POST.get("current_password")
                new_password = request.POST.get("new_password")
                confirm_password = request.POST.get("confirm_password")

                if new_password != confirm_password:
                    return render(
                        request,
                        "student.html",
                        {"error_message": "Confirm password is different..."},
                    )
                else:
                    obj = Change_pass(
                        enrollment=enrollment,
                        current_pass=current_password,
                        new_pass=new_password,
                        table="student",
                    )
                    answer = obj.check()
                    if answer:
                        obj.change()
                        return render(
                            request,
                            "student.html",
                            {
                                "success_message": "Password Change Successfully...",
                                **student_data,
                            },
                        )
                    else:
                        return render(
                            request,
                            "student.html",
                            {
                                "success_message": "Current Password Is Wrong...",
                                **student_data,
                            },
                        )

            elif button == "query_button":
                name = request.POST.get("name")
                email = request.POST.get("email")
                description = request.POST.get("description")

                s = Student(
                    name=name,
                    email=email,
                    enrollment=enrollment,
                    description=description,
                )
                s.save()
                return render(
                    request,
                    "student.html",
                    {"success_message": "Form Submit...", **student_data},
                )

        return render(request, "student.html", student_data)
    else:
        return render(request, "unauthorized.html")


# if faculty submit form or want to change password the
def faculty(request):
    if login_done:
        # using post method
        if request.method == "POST":
            button = request.POST.get("button")

            # change_password
            if button == "change_password":
                id = request.POST.get("id")
                current_password = request.POST.get("current_password")
                new_password = request.POST.get("new_password")
                confirm_password = request.POST.get("confirm_password")

                if new_password != confirm_password:
                    return render(
                        request,
                        "faculty.html",
                        {"error_message": "Confirm password is different..."},
                    )
                else:
                    obj = Change_pass(
                        enrollment=id,
                        current_pass=current_password,
                        new_pass=new_password,
                        table="faculty",
                    )
                    answer = obj.check()

                    # if dta is exist or not
                    if answer:
                        obj.change()
                        return render(
                            request,
                            "faculty.html",
                            {
                                "success_message": "Password Change Successfully...",
                                **faculty_data,
                            },
                        )
                    else:
                        return render(
                            request,
                            "faculty.html",
                            {"error_message": "Something Is Wrong...", **faculty_data},
                        )

        # using get method
        if request.method == "GET":
            button = request.GET.get("button")

            # faculty
            if button == "faculty_query":
                name = request.GET.get("name")
                email = request.GET.get("email")
                description = request.GET.get("description")

                print(name, email, description)

                f = Faculty(name=name, email=email, description=description)
                f.save()

                return render(
                    request,
                    "faculty.html",
                    {"success_message": "Form Submit...", **faculty_data},
                )

        return render(request, "faculty.html", faculty_data)
    else:
        return render(request, "unauthorized.html")


# all functionality of admin file
def adminfile(request):
    global login_done  
    global admin_data

    if login_done:
        if request.method == "POST":
            button = request.POST.get("button")
            print("Clicked button is", button)

            # button for add student
            if button == "student":
                email = request.POST.get("email")
                name = request.POST.get("name")
                phone = request.POST.get("phone")
                enrollment = request.POST.get("enrollment")
                address = request.POST.get("address")
                department = request.POST.get("department")

                obj = StudentInsert(
                    email=email,
                    name=name,
                    phone=phone,
                    enrollment=enrollment,
                    address=address,
                    department=department,
                )
                answer = obj.check()
                if answer == []:
                    obj.insert_into_database()
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Student Add in Database...",
                            **admin_data,
                            **sem_data,
                        },
                    )
                else:
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "error_message": "This Student Already Exists...",
                            **admin_data,
                            **sem_data,
                        },
                    )

            # button for add faculty
            elif button == "faculty":
                email = request.POST.get("email")
                name = request.POST.get("name")
                phone = request.POST.get("phone")
                department = request.POST.get("department")
                address = request.POST.get("address")
                designation = request.POST.get("designation")
                course = request.POST.get("course")
                attached_year = request.POST.get("attached_year")

                obj = FacultyInsert(
                    email=email,
                    name=name,
                    phone=phone,
                    department=department,
                    address=address,
                    designation=designation,
                    course=course,
                    attached_year=attached_year,
                )
                answer = obj.check()

                if not answer:
                    obj.insert_into_database()
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Faculty Add in Database...",
                            **admin_data,
                            **sem_data,
                        },
                    )
                else:
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "error_message": "This Faculty Member Already Exists...",
                            **admin_data,
                            **sem_data,
                        },
                    )

            # button for remove student
            elif button == "remove_student":
                email = request.POST.get("email")
                enrollment = request.POST.get("enrollment")

                obj = Remove_student(email=email, enrollment=enrollment)
                answer = obj.check()
                if answer:
                    obj.remove_student()
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Student Remove Successfully...",
                            **admin_data,
                            **sem_data,
                        },
                    )
                else:
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "error_message": "Student Not Found...",
                            **admin_data,
                            **sem_data,
                        },
                    )

            # button for remove faculty
            elif button == "remove_faculty":
                email = request.POST.get("email")
                id = request.POST.get("f_id")

                obj = Remove_faculty(email=email, id=id)
                answer = obj.check()
                if not answer:
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "error_message": "Faculty Not Found...",
                            **admin_data,
                            **sem_data,
                        },
                    )
                else:
                    obj.remove_faculty()
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Faculty Remove Successfully...",
                            **admin_data,
                            **sem_data,
                        },
                    )

            # button for edit student
            elif button == "edit_student":
                enrollment = request.POST.get("enrollment")
                attribute = request.POST.get("attribute")
                new_value = request.POST.get("new_value")
                print(enrollment, attribute, new_value)

                obj = Edit_student(
                    enrollment=enrollment, attribute=attribute, new_value=new_value
                )
                answer = obj.check()
                if not answer:
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "error_message": "Student Not Found...",
                            **admin_data,
                            **sem_data,
                        },
                    )
                else:
                    obj.change()
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Student Detail Edit Successfully...",
                            **admin_data,
                            **sem_data,
                        },
                    )

            # button for edit faculty
            elif button == "edit_faculty":
                id = request.POST.get("f_id")
                attribute = request.POST.get("attribute")
                new_value = request.POST.get("new_value")

                obj = Edit_faculty(id=id, attribute=attribute, new_value=new_value)
                answer = obj.check()
                if not answer:
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "error_message": "Faculty Not Found...",
                            **admin_data,
                            **sem_data,
                        },
                    )
                else:
                    obj.change()
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Faculty Detail Edit Successfully...",
                            **admin_data,
                            **sem_data,
                        },
                    )

            # button for marks enter
            elif button == "sem_select":
                # code for enter marks
                enrollment = request.POST.get("enrollment")
                subject_name = request.POST.get("subject")
                marks = request.POST.get("marks")

                obj = InsertMarks(
                    enrollment=enrollment, subject=subject_name, marks=marks
                )
                answer = obj.check()
                if answer:
                    obj.enter_marks()
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Marks Enter Successfully...",
                            **sem_data,
                            **admin_data,
                        },
                    )
                elif not answer:
                    return render(
                        request,
                        "adminfile.html",
                        {
                            "success_message": "Student Not Found...",
                            **sem_data,
                            **admin_data,
                        },
                    )

            else:
                return render(request, "adminfile.html", admin_data, sem_data)

        return render(request, "adminfile.html", sem_data)
    else:
        return render(request, "unauthorized.html")


# event registration
def event(request):
    if request.method == "POST":
        enrollment = request.POST.get("enrollment")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        name = request.POST.get("name")

        print(enrollment, email, phone, name)

        obj = Event(enrollment=enrollment, name=name, email=email, phone=phone)
        data = obj.check_student()
        if data:
            data2 = obj.check_event()
            if not data2:
                obj.enter_data()
                print(enrollment, email, phone, name)
                return render(
                    request,
                    "event.html",
                    {"success_message": "Registration is Done..."},
                )
            else:
                return render(
                    request,
                    "event.html",
                    {"success_message": "Registration is Already Done..."},
                )

        else:
            return render(
                request,
                "event.html",
                {"error_message": "Other Students Are Not Allowed..."},
            )
    return render(request, "event.html")
