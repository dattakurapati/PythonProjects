from tkinter import *

def raise_frame(frame):
    frame.tkraise()

# creates tkinter window called root
root = Tk()
root.geometry("600x600") # can be changed if needed
root.title("Grade Checker - Kaushik Kurapati")

# creates an overall button and calls the raise_frame method to switch between frames
overall_button = Button(root, text="Overall",
                        width=10, command=lambda: raise_frame(overall_frame))
overall_button.place(x=10, y=5)
# creates an class button and calls the raise_frame method to switch between frames
class_button = Button(root, text="Class", width=10,
                      command=lambda: raise_frame(class_frame))
class_button.place(x=100, y=5)

overall_frame = Frame(root, width=600, height=565, bg="Coral")    # need to change color when complete
class_frame = Frame(root, width=600, height=565, bg="Deep Sky Blue")    # need to change color when complete

# ------------------------ your code goes here ------------------------ 
c1_var = StringVar()
c2_var = StringVar()
c3_var = StringVar()
c4_var = StringVar()
c5_var = StringVar()
c6_var = StringVar()
average_sem1 = IntVar()
average_sem2 = IntVar()
average = IntVar()
needed = IntVar()


instructions = Label(overall_frame, text="Enter your cycle average in the input boxes below (? if unknown): ", font = ('Times New Roman', 15), bg = "coral", foreground="white")
instructions.place(x = 10, y = 10)

c1_label = Label(overall_frame, text="Cycle 1: ", font = ('Times New Roman', 15), bg = "coral", foreground="white")
c1_label.place(x = 50, y = 55)

c1_entry = Entry(overall_frame, font=('Times New Roman', 15), width = 15, textvariable=c1_var)
c1_entry.place(x = 125, y = 55)

c2_label = Label(overall_frame, text="Cycle 2: ", font = ('Times New Roman', 15), bg = "coral", foreground="white")
c2_label.place(x = 50, y = 95)

c2_entry = Entry(overall_frame, font=('Times New Roman', 15), width = 15, textvariable=c2_var)
c2_entry.place(x = 125, y = 95)

c3_label = Label(overall_frame, text="Cycle 3: ", font = ('Times New Roman', 15), bg = "coral", foreground="white")
c3_label.place(x = 50, y = 135)

c3_entry = Entry(overall_frame, font=('Times New Roman', 15), width = 15, textvariable=c3_var)
c3_entry.place(x = 125, y = 135)

c4_label = Label(overall_frame, text="Cycle 4: ", font = ('Times New Roman', 15), bg = "coral", foreground="white")
c4_label.place(x = 285, y = 55)

c4_entry = Entry(overall_frame, font=('Times New Roman', 15), width = 15, textvariable=c4_var)
c4_entry.place(x = 360, y = 55)

c5_label = Label(overall_frame, text="Cycle 5: ", font = ('Times New Roman', 15), bg = "coral", foreground="white")
c5_label.place(x = 285, y = 95)

c5_entry = Entry(overall_frame, font=('Times New Roman', 15), width = 15, textvariable=c5_var)
c5_entry.place(x = 360, y = 95)

c6_label = Label(overall_frame, text="Cycle 6: ", font = ('Times New Roman', 15), bg = "coral", foreground="white")
c6_label.place(x = 285, y = 135)

c6_entry = Entry(overall_frame, font=('Times New Roman', 15), width = 15, textvariable=c6_var)
c6_entry.place(x = 360, y = 135)

def calculate():
    c1 = c1_var.get()
    c2 = c2_var.get()
    c3 = c3_var.get()
    c4 = c4_var.get()
    c5 = c5_var.get()
    c6 = c6_var.get()
    sem1 = average_sem1.get()
    sem2 = average_sem2.get()
    need = needed.get()
    output = " "
    if_pass = ""
    credit = 0
    credit_string = ""

    if c1 == "?":
        output += "Average of first semester currently: 0. \n Average of second semester currently: 0. \n You have not passed either semester, thus not earning any credit for the class. \n Overall course average currently: 0. \n   The cycle grades you need to receive for all 3 cycles and to pass your \n first semester is a 70. \n   The cycle grades you need to receive for all 3 cycles and to pass your \n second semester is a 70."
    elif c2 == "?":
        need = "{0:.0f}".format((210 - float(c1)) / 2)
        output += "Average of first semester currently: " + "{0:.0f}".format((float(c1))) + ". \n You have not passed either semester yet, thus not earning any credit for the class. \n Overall course average is currently: "+ "{0:.0f}".format(float(c1)) +". \n   The lowest cycle grades you can receive or average for both cycles 2 and 3 in order \n to pass the first semester is a "+ str(need) +". \n   The cycle grades you need to receive for all 3 cycles and to pass your \n second semester is a 70."
    elif c3 == "?":
        need = "{0:.0f}".format(210 - float(c1)-float(c2))
        output += "Average of first semester currently: " + "{0:.0f}".format((float(c1)+float(c2))/2) + ". \n You have not passed either semester yet, thus not earning any credit for the class. \n Overall course average is currently: "+ "{0:.0f}".format((float(c1)+float(c2))/2) +". \n   The lowest cycle grade you can receive for cycle 3 in order \n to pass the first semester is a "+ str(need) +". \n   The cycle grades you need to receive for all 3 cycles and to pass your \n second semester is a 70."
    elif c4 == "?":
        sem1 = "{0:.0f}".format((float(c1) + float(c2) + float(c3)) / 3)
        if float(sem1) >= 70.00:
            if_pass = " You have passed the first semester."
            credit += 0.5
        elif float(sem1) < 70.00:
            if_pass = " You have NOT passed the first semester. You need a " + "{0:.0f}".format((420-float(c1)-float(c2)-float(c3))/3) + " \n in the remaining cycles to semester average."
        
        if credit == 0.5:
            credit_string = "earned partial (0.5) credit for the class."
        elif credit == 0:
            credit_string = "have not earned any credit for the class so far. "

        output += "Average of first semester is: " + sem1 + ".\n " + if_pass + " \n You " + credit_string +" \n Overall course average is currently: "+ "{0:.0f}".format((float(c1)+float(c2)+float(c3))/3) +". \n  The cycle grades you need to receive for all 3 cycles and to pass your \n second semester is a 70."
    elif c5 == "?":
        sem1 = "{0:.0f}".format((float(c1) + float(c2) + float(c3)) / 3)

        if float(sem1) >= 70.00:
            if_pass = "You have passed the first semester."
            credit += 0.5
        elif float(sem1) < 70.00:
            if_pass = "You have NOT passed the first semester. You need a " + "{0:.0f}".format((420-float(c1)-float(c2)-float(c3)-float(c4))/2) + " \n in the remaining cycles to semester average."
        
        if credit == 0.5:
            credit_string = "earned partial (0.5) credit for the class. "
        elif credit == 0:
            credit_string = "have not earned any credit for the class. "

        need = "{0:.0f}".format((210 - float(c4)) / 2)

        output += "Average of first semester is: " + sem1 + ". \n Average of second semester is currently: " + "{0:.0f}".format((int(c4))) + ". \n " + if_pass + " \n You " + credit_string +" \n Overall course average is currently: "+ "{0:.0f}".format((float(c1)+float(c2)+float(c3)+float(c4))/4) +". \n  The lowest cycle grades you can receive or average for both cycles 2 and 3 in order \n to pass the second semester is a " + str(need) +" to average a 70."        
    elif c6 == "?":
        sem1 = "{0:.0f}".format((float(c1) + float(c2) + float(c3)) / 3)

        if float(sem1) >= 70.00:
            if_pass = "You have passed the first semester."
            credit += 0.5
        elif float(sem1) < 70.00:
            if_pass = "You have NOT passed the first semester. You need a " + "{0:.0f}".format((420-float(c1)-float(c2)-float(c3)-float(c4)-float(c5))) + " \n in the remaining cycles to semester average."
        
        if credit == 0.5:
            credit_string = "earned partial (0.5) credit for the class. "
        elif credit == 0:
            credit_string = "have not earned any credit for the class. "

        need = "{0:.0f}".format((210 - float(c4)-float(c5)))

        output += "Average of first semester is: " + sem1 + ". \n Average of second semester is currently: " + "{0:.0f}".format((float(c4)+float(c5))/2) + ". \n " + if_pass + " \n You " + credit_string +" \n Overall course average is currently: "+ "{0:.0f}".format((float(c1)+float(c2)+float(c3)+float(c4)+float(c5))/5) +". \n  The lowest cycle grades you can receive for cycle 3 in order \n to pass the second semester is a " + str(need) +" to average a 70."
    else:
        sem1 = "{0:.0f}".format((float(c1) + float(c2) + float(c3)) / 3)
        sem2 = "{0:.0f}".format((float(c4) + float(c5) + float(c6)) / 3)

        if float(sem1) >= 70.00:
           if_pass += "You passed the first semester. "
           credit += 0.5
        elif float(sem1) < 70.00:
            if_pass += "You have NOT passed the first semester. "

        if int(sem1) < 70 and ((int(sem1) + int(sem2))/2) >= 70 and int(sem2) >= 70:
            if_pass += "You passed the second semester."
            credit += 1.0
        elif ((int(sem1) + int(sem2))/2) >= 70 and int(sem1) >= 70 and int(sem2) < 70:
            if_pass += "You have NOT passed the second semester."
            credit += 1.0
        elif float(sem2) >= 70.00:
           if_pass += "You passed the second semester."
           credit += 0.5
        elif float(sem2) < 70.00:
            if_pass += "You have NOT passed the second semester."
        
        if credit == 0.5:
            credit_string = "earned partial (0.5) credit for the class. "
        elif credit == 0:
            credit_string = "have not earned any credit for the class. "
        elif credit == 1 and (int(sem1) < 70 and ((int(sem1) + int(sem2))/2) >= 70) or (((int(sem1) + int(sem2))/2) >= 70 and int(sem1) >= 70 and int(sem2) < 70):
            credit_string = "have passed the course earning 1.0 credit due to semester average. "
        elif credit == 1:
            credit_string = "have passed the course earning 1.0 credit. "

        output += "Average of first semester is: " + sem1 + ". \n Average of second semester is: " + sem2 + ". \n " + if_pass + " \n You " + credit_string +" \n Overall course average is: "+ "{0:.0f}".format((float(sem1)+float(sem2))/2) +"."

    display_grade.configure(text = output)

def reset_overall():
    c1 = c1_var.get()
    c2 = c2_var.get()
    c3 = c3_var.get()
    c4 = c4_var.get()
    c5 = c5_var.get()
    c6 = c6_var.get()
    output = " "
    c1 = ""
    c2 = ""
    c3 = ""
    c4 = ""
    c5 = ""
    c6 = ""
    c1_var.set(c1)
    c2_var.set(c2)
    c3_var.set(c3)
    c4_var.set(c4)
    c5_var.set(c5)
    c6_var.set(c6)
    display_grade.configure(text = output) 


submit = Button(overall_frame, text="Calculate", font=('Times New Roman', 13), width = 10, command = calculate)
submit.place(x = 245, y = 185)

display_grade = Label(overall_frame, text = " ", font = ('Times New Roman', 13), width = 64, height = 13)
display_grade.place(x = 10, y = 235)

reset_button = Button(overall_frame, text="Reset", font=('Times New Roman', 13), width = 10, command = reset_overall)
reset_button.place(x = 190, y = 510)

close_button = Button(overall_frame, text="Close", font=('Times New Roman', 13), width = 10, command = root.destroy)
close_button.place(x = 310, y = 510)

# --------------------------------------------- Cycle Grades---------------------------------------------------------

assignment1 = IntVar()
assignment2 = IntVar()
assignment3 = IntVar()
assignment4 = IntVar()
assignment5 = IntVar()
assignment6 = IntVar()
assignment7 = IntVar()
assignment8 = IntVar()

assessment1 = IntVar()
assessment2 = IntVar()
assessment3 = IntVar()
assessment4 = IntVar()

assignment_button_count = IntVar()
assessment_button_count = IntVar()

def change_assignments():
    count = assignment_button_count.get()
    
    while True:
        if count < 8:
            count = count + 1
            break
        else:
            count += 0
            break

    as1 = assignment1.get()
    as2 = assignment2.get()
    as3 = assignment3.get()
    as4 = assignment4.get()
    as5 = assignment5.get()
    as6 = assignment6.get()
    as7 = assignment7.get()
    as8 = assignment8.get()


    for x in range(count):
        if count == 1:
            assignments_label_1 = Label(class_frame, text="#1", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_1.place(x=20, y=135)

            assignments_entry_1 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment1)
            assignments_entry_1.place(x = 50, y = 135)
        if count == 2:
            assignments_label_2 = Label(class_frame, text="#2", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_2.place(x=20, y=170)

            assignments_entry_2 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment2)
            assignments_entry_2.place(x = 50, y = 170)
        if count == 3:
            assignments_label_3 = Label(class_frame, text="#3", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_3.place(x=20, y=205)

            assignments_entry_3 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment3)
            assignments_entry_3.place(x = 50, y = 205)
        if count == 4:
            assignments_label_4 = Label(class_frame, text="#4", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_4.place(x=20, y=240)

            assignments_entry_4 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment4)
            assignments_entry_4.place(x = 50, y = 240)
        if count == 5:
            assignments_label_5 = Label(class_frame, text="#5", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_5.place(x=20, y=275)
            

            assignments_entry_5 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment5)
            assignments_entry_5.place(x = 50, y = 275)
        if count == 6:
            assignments_label_6 = Label(class_frame, text="#6", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_6.place(x=20, y=310)

            assignments_entry_6 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment6)
            assignments_entry_6.place(x = 50, y = 310)
        if count == 7:
            assignments_label_7 = Label(class_frame, text="#7", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_7.place(x=20, y=345)

            assignments_entry_7 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment7)
            assignments_entry_7.place(x = 50, y = 345)
        if count == 8:
            assignments_label_8 = Label(class_frame, text="#8", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assignments_label_8.place(x=20, y=380)

            assignments_entry_8 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assignment8)
            assignments_entry_8.place(x = 50, y = 380)

        assignment_button_count.set(count)

        assignment1.set(as1)
        assignment2.set(as2)
        assignment3.set(as3)
        assignment4.set(as4)
        assignment5.set(as5)
        assignment6.set(as6)
        assignment7.set(as7)
        assignment8.set(as8)

def change_assessments():
    count = assessment_button_count.get()

    while True:
        if count < 4:
            count = count + 1
            break
        else:
            count += 0
            break

    asm1 = assessment1.get()
    asm2 = assessment2.get()
    asm3 = assessment3.get()
    asm4 = assessment4.get()

    for x in range(count):
        if count == 1:
            assessment_label_1 = Label(class_frame, text="#1", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assessment_label_1.place(x=310, y=135)

            assessments_entry_1 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assessment1)
            assessments_entry_1.place(x = 340, y = 135)
        if count == 2:
            assessments_label_2 = Label(class_frame, text="#2", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assessments_label_2.place(x=310, y=170)

            assessments_entry_2 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assessment2)
            assessments_entry_2.place(x = 340, y = 170)
        if count == 3:
            assessments_label_3 = Label(class_frame, text="#3", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assessments_label_3.place(x=310, y=205)

            assessments_entry_3 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assessment3)
            assessments_entry_3.place(x = 340, y = 205)
        if count == 4:
            assessments_label_4 = Label(class_frame, text="#4", font = ('Times New Roman', 15), bg = "Deep Sky Blue", foreground="black")
            assessments_label_4.place(x=310, y=240)

            assessments_entry_4 = Entry(class_frame, font=('Times New Roman', 15), width = 20, textvariable=assessment4)
            assessments_entry_4.place(x = 340, y = 240)


        assessment_button_count.set(count)

        assessment1.set(asm1)
        assessment2.set(asm2)
        assessment3.set(asm3)
        assessment4.set(asm4)

def calculate_average():
    c1 = c1_var.get()
    as1 = assignment1.get()
    as2 = assignment2.get()
    as3 = assignment3.get()
    as4 = assignment4.get()
    as5 = assignment5.get()
    as6 = assignment6.get()
    as7 = assignment7.get()
    as8 = assignment8.get()
    assignment_button_count.get()
    assessment_button_count.get()
    asm1 = assessment1.get()
    asm2 = assessment2.get()
    asm3 = assessment3.get()
    asm4 = assessment4.get()
    grade = 0

    if assignment_button_count.get() == 0:
        output_assignment = "No Assignments"
        assignments_average.configure(text=output_assignment)
    else:
        output_assignment = "Assignments Average: " +  "{0:.0f}".format((as1 + as2 + as3 + as4 + as5 + as6 + as7 + as8)/assignment_button_count.get())
        assignments_average.configure(text=output_assignment)

    if assessment_button_count.get() == 0:
        output_assessment = "No Assessments"
        assessments_average.configure(text=output_assessment)
    else:
        output_assessment = "Assessment Average: " +  "{0:.0f}".format((asm1 + asm2 + asm3 + asm4)/assessment_button_count.get())
        assessments_average.configure(text=output_assessment)

    if assessment_button_count.get() == 0 and assignment_button_count.get() > 0:
        grade = "{0:.0f}".format((as1 + as2 + as3 + as4 + as5 + as6 + as7 + as8)/assignment_button_count.get())
        cycle_average_label = Label(class_frame, text="Current Average:", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
        cycle_average_label.place(x = 400, y = 450)
        cycle_grade.configure(text=grade)
        c1_var.set(grade)

    elif assessment_button_count.get() > 0 and assignment_button_count.get() == 0:
        grade = "{0:.0f}".format((asm1 + asm2 + asm3 + asm4)/assessment_button_count.get())
        cycle_average_label = Label(class_frame, text="Current Average:", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
        cycle_average_label.place(x = 400, y = 450)
        cycle_grade.configure(text=grade)
        c1_var.set(grade)

    elif assessment_button_count.get() > 0 and assignment_button_count.get() > 0:
        grade = "{0:.0f}".format((((asm1 + asm2 + asm3 + asm4)/assessment_button_count.get()) * 0.6) + (((as1 + as2 + as3 + as4 + as5 + as6 + as7 + as8)/assignment_button_count.get()) * 0.4))
        cycle_average_label = Label(class_frame, text="Current Average:", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
        cycle_average_label.place(x = 400, y = 450)
        cycle_grade.configure(text=grade)
        c1_var.set(grade)

# cycle1_button = Button(class_frame, text="Cycle 1", font=('Times New Roman', 13), width = 7)
# cycle1_button.place(x = 10, y = 10)

# cycle2_button = Button(class_frame, text="Cycle 2", font=('Times New Roman', 13), width = 7 )
# cycle2_button.place(x = 85, y = 10)

# cycle3_button = Button(class_frame, text="Cycle 3", font=('Times New Roman', 13), width = 7)
# cycle3_button.place(x = 160, y = 10)

# cycle4_button = Button(class_frame, text="Cycle 4", font=('Times New Roman', 13), width = 7)
# cycle4_button.place(x = 235, y = 10)

# cycle5_button = Button(class_frame, text="Cycle 5", font=('Times New Roman', 13), width = 7)
# cycle5_button.place(x = 310, y = 10)

# cycle6_button = Button(class_frame, text="Cycle 6", font=('Times New Roman', 13), width = 7)
# cycle6_button.place(x = 385, y = 10)

cycle_label = Label(class_frame, text="Grades for Cycle 1", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
cycle_label.place(x = 230, y = 14)

assignments_label = Label(class_frame, text="Assignments", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
assignments_label.place(x = 113, y = 60)

assignments_button = Button(class_frame, text="Add Assignment", font=('Times New Roman', 13), width = 31 , command = change_assignments)
assignments_button.place(x = 10, y = 90)

assessments_label = Label(class_frame, text="Assessments", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
assessments_label.place(x = 403, y = 60)

assessments_button = Button(class_frame, text="Add Assessment", font=('Times New Roman', 13), width = 31 , command = change_assessments)
assessments_button.place(x = 300, y = 90)

assignments_average = Label(class_frame, text=" ", font = ('Times New Roman', 14), bg = "Deep Sky Blue", foreground="black")
assignments_average.place(x=60, y=415)

assessments_average = Label(class_frame, text=" ", font = ('Times New Roman', 14), bg = "Deep Sky Blue", foreground="black")
assessments_average.place(x=372, y=415)

calculate_average_button = Button(class_frame, text="Calculate Cycle Average", font=('Times New Roman', 13), width = 23 , command = calculate_average)
calculate_average_button.place(x = 10, y = 460)

assignments_weight_label = Label(class_frame, text="Assignment weight: 40%", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
assignments_weight_label.place(x=10, y=500)

assessment_weight_label = Label(class_frame, text="Assessment weight: 60%", font = ('Times New Roman', 13), bg = "Deep Sky Blue", foreground="black")
assessment_weight_label.place(x=10, y=525)

cycle_grade = Label(class_frame, text=" ", font = ('Times New Roman', 45), bg = "Deep Sky Blue", foreground="black")
cycle_grade.place(x = 420, y = 475)

# do not delete any of the code below
for frame in (overall_frame, class_frame):
    frame.place(x=0, y=35)

raise_frame(overall_frame)
root.mainloop()