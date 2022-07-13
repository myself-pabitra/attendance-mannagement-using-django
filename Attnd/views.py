from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from datetime import datetime
from datetime import timedelta
from .models import Student, StudentAttendence
from django.contrib import messages



                                                    # Home views starts here........
def home(request):
    if request.user.is_authenticated:
        now = datetime.now()
        if request.method == 'POST':
            a_dept = request.POST['department']
            a_roll = request.POST['roll']
            a_attendance = request.POST['attendance']
            try:
                Student.objects.get(stu_roll=a_roll, Stu_dept__icontains=a_dept)
                my_data = Student.objects.get(stu_roll=a_roll, Stu_dept__icontains=a_dept)
                print(my_data)
                a_roll = my_data.stu_roll
                student_name = my_data.Stu_name
                student_group = my_data.Stu_group
                student_department = my_data.Stu_dept
                d_attndance = StudentAttendence(student_roll=a_roll, student_present=a_attendance,
                                                student_name=student_name, student_group=student_group,
                                                student_department=student_department)
                messages.success(request, 'Attendance Recorded Successfully..!!')
                d_attndance.save()
            except Student.DoesNotExist:
                messages.warning(request, 'No student found for this Roll number Please ! Enter correct One')
                return redirect(home)

        today = StudentAttendence.objects.filter(attendance_date=datetime.now())
        yesterday = StudentAttendence.objects.filter(attendance_date=datetime.now() - timedelta(days=1))

        ytpresent = StudentAttendence.objects.filter(student_present='Present',
                                                     attendance_date=datetime.now() - timedelta(days=1)).count()

        ytabsent = StudentAttendence.objects.filter(student_present='Absent',
                                                    attendance_date=datetime.now() - timedelta(days=1)).count()

        ttpresent = StudentAttendence.objects.filter(student_present='Present', attendance_date=datetime.now()).count()

        ttabsent = StudentAttendence.objects.filter(student_present='Absent', attendance_date=datetime.now()).count()

        today_total = StudentAttendence.objects.all().filter(attendance_date=datetime.now()).count()
        yesterday_total = StudentAttendence.objects.all().filter(
            attendance_date=datetime.now() - timedelta(days=1)).count()
        context = {
            'today': today,
            'yesterday': yesterday,
            'ytpresent': ytpresent,
            'ytabsent': ytabsent,
            'ttpresent': ttpresent,
            'ttabsent': ttabsent,
            'tt': today_total,
            'yt': yesterday_total
        }
        return render(request, 'home.html', context)
    else:
        return redirect(user_login)

                                                        # Record Attendance view starts here.....
def record_attendance(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        dept = request.POST['dept']
        grp = request.POST['grp']

        try:
            Student.objects.get(stu_roll=roll)
            messages.error(request, 'Roll number is already taken')
            return redirect(record_attendance)
        except Student.DoesNotExist:
            if len(roll) != 4:
                messages.error(request, '**please Enter 4 digit roll number.')
                return redirect(record_attendance)
            elif len(name) <= 5:
                messages.error(request, '**please Enter Your valid name.')
                return redirect(record_attendance)
            elif len(grp) != 1:
                messages.error(request, '**Please enter your valid group')
                return redirect(record_attendance)
            else:
                present = Student(Stu_name=name, stu_roll=roll, Stu_dept=dept, Stu_group=grp)
                present.save()
                messages.info(request, 'Attendance Recorded Successfully..')
                return redirect(record_attendance)

    return render(request, 'record_attendance.html')


                                                  # Viewing Attendance View starts here.....
def view_attendance(request):
    students = Student.objects.all()
    return render(request, 'view_attendance.html', {'stud': students})

                                                # Search Attendance View Starts Here....
def search_attendance(request):
    if request.method == 'POST':
        s_name = request.POST['name']
        s_department = request.POST['Department']
        s_from_date = request.POST['from_date']
        if s_from_date:
            if StudentAttendence.objects.filter(student_name__icontains=s_name,
            student_department__icontains=s_department,student_present__contains='present',attendance_date=s_from_date):

                total_present = StudentAttendence.objects.filter(student_name__icontains=s_name,
                student_department__icontains=s_department,student_present__contains='present',attendance_date=s_from_date)
            
                total_number = StudentAttendence.objects.filter(student_name__icontains=s_name,
                student_department__icontains=s_department,student_present__contains='present',attendance_date=s_from_date).count()
            
                context = {
                'tp': total_present,
                'total_pr': total_number
            }
                return render(request, 'search_attendance.html', context)
            else:
                messages.error(request, 'No Attendence found with this search...')
        elif StudentAttendence.objects.filter(student_name__icontains=s_name,
            student_department__icontains=s_department,student_present__contains='present'):

            total_present = StudentAttendence.objects.filter(student_name__icontains=s_name,
            student_department__icontains=s_department,student_present__contains='present')
            print(total_present)
            total_number = StudentAttendence.objects.filter(student_name__icontains=s_name,
            student_department__icontains=s_department,student_present__contains='present').count()

            context = {
                'tp': total_present,
                'total_pr': total_number
            }
            
            return render(request, 'search_attendance.html', context)
        else:
            messages.warning(request, 'No Attendence found with this search...')

    return render(request, 'search_attendance.html')


        # try:
        #     StudentAttendence.objects.filter(student_name__icontains=s_name,
        #     student_department__icontains=s_department,student_present__contains='present',attendance_date=s_from_date)

        #     total_present = StudentAttendence.objects.filter(student_name__icontains=s_name,
        #     student_department__icontains=s_department,student_present__contains='present',attendance_date=s_from_date)
        #     print(total_present)
        #     total_number = StudentAttendence.objects.filter(student_name__icontains=s_name,
        #     student_department__icontains=s_department,student_present__contains='present',attendance_date=s_from_date).count()

        #     context = {
        #         'tp': total_present,
        #         'total_pr': total_number
        #     }
        #     return render(request, 'search_attendance.html', context)

        # except StudentAttendence.DoesNotExist:
        #     messages.error(request, 'No Attendence found with this search...')
        #     return render(request, 'search_attendance.html')

    # return render(request, 'search_attendance.html')

                        # User Sign up View Starts Here.......
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created Successfully !!')
            return redirect(user_login)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

                                   # User Login View Starts Here..........
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have logged in successfully..!')
                    return redirect(home)
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect(home)

                                                    # Logout View..............
def user_logout(request):
    logout(request)
    return redirect(home)
