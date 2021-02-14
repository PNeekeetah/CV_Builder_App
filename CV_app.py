# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:50:46 2021

@author: Nikita
"""

import tkinter as tk
#from tkinter import colorchooser
from tkinter import ttk
from jinja2 import Template

#All frames that the GUI has
root = tk.Tk()
mainframe = ttk.Frame(root)
secondframe = ttk.Frame(root)
thirdframe = ttk.Frame(root)
fourthframe = ttk.Frame(root)
fifthframe = ttk.Frame(root)
sixthframe = ttk.Frame(root)
seventhframe = ttk.Frame(root)

mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
secondframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
thirdframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
fourthframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
fifthframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
sixthframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
seventhframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# global variables
current_frame = 0
displayed_frame = mainframe
frames = [mainframe, secondframe, thirdframe, fourthframe, fifthframe, 
          sixthframe,seventhframe]
total_frames =  len(frames)
last_buttons = [ttk.Button(), ttk.Button()]

root.title("CV Builder")




def click():
    print("Click")



def nextFrame( number : int):
    global current_frame
    global total_frames
    global frames
    global displayed_frame
    global last_buttons
    global label_skills
    global label_languages
    
    # Get rid of arrow
    if (displayed_frame == mainframe):
        menu_employment.entryconfigure(1,label = "Personal Details")
    elif(displayed_frame == secondframe):
        menu_employment.entryconfigure(2,label = "Summary")
    elif(displayed_frame == thirdframe):
        menu_employment.entryconfigure(3,label = "Academic History")
    elif(displayed_frame == fourthframe):
        menu_employment.entryconfigure(4,label = "Employment History")
    elif(displayed_frame == fifthframe):
        menu_employment.entryconfigure(5,label = "Skills")
    elif(displayed_frame == sixthframe):
        menu_employment.entryconfigure(6,label = "Languages")
    elif(displayed_frame == seventhframe):
        menu_employment.entryconfigure(7,label = "Wrap Up")
        
    # Add arrow    
    current_frame += number
    current_frame %= total_frames
    frames[current_frame].tkraise()
    displayed_frame = frames[current_frame]
    last_buttons[0].destroy()
    last_buttons[1].destroy()
    total = 0
    
    if (displayed_frame == fifthframe):
        total = 2*len(label_skills) + 4
    elif (displayed_frame == sixthframe):
        total = 2*len(label_languages) + 4
    else:
        total = 6
    
    # Add arrow
    if (displayed_frame == mainframe):
        menu_employment.entryconfigure(1,label = "->Personal Details")
    elif(displayed_frame == secondframe):
        menu_employment.entryconfigure(2,label = "->Summary")
    elif(displayed_frame == thirdframe):
        menu_employment.entryconfigure(3,label = "->Academic History")
    elif(displayed_frame == fourthframe):
        menu_employment.entryconfigure(4,label = "->Employment History")
    elif(displayed_frame == fifthframe):
        menu_employment.entryconfigure(5,label = "->Skills")
    elif(displayed_frame == sixthframe):
        menu_employment.entryconfigure(6,label = "->Languages")
    elif(displayed_frame == seventhframe):
        menu_employment.entryconfigure(7,label = "->Wrap Up")

    
    
    button_next = ttk.Button(displayed_frame, text = "Next >",command = lambda:nextFrame(1))
    button_next.grid(column = 1, row = total, sticky = tk.E, padx = (0,20))
    button_previous = ttk.Button(displayed_frame, text = "< Previous", command = lambda:nextFrame(-1))
    button_previous.grid(column = 0, row = total, sticky = tk.W , padx = (20,0))
    
    last_buttons[0] = button_next
    last_buttons[1] = button_previous

def addLanguage():
    global label_languages 
    global languages 
    global label_languages_level 
    global languages_level 
    global last_buttons_language
    global last_buttons
    
    label_languages.append(ttk.Label(sixthframe, text = 'Language '+str(len(label_languages)+1)))
    languages.append(ttk.Entry(sixthframe, font = ('Helvetica',16)))
    label_languages_level.append(ttk.Label(sixthframe, text = 'Language level ' + str(len(label_languages_level)+1)))
    languages_level.append(ttk.Entry(sixthframe, font = ('Helvetica',16)))
    total = 2*len(label_languages)
    
    label_languages[-1].grid(column = 0, row = total+1, sticky = (tk.W), padx = (20,0),pady = 10)
    languages[-1].grid(column = 1, row = total+1, sticky = (tk.E), padx = (0,20),pady = 10)
    label_languages_level[-1].grid(column = 0, row = total+2, sticky = tk.W , padx = (20,0),pady = 10)
    languages_level[-1].grid(column = 1, row = total+2, sticky = tk.E , padx = (0,20),pady = 10)
    
    
    last_buttons_language[0].destroy()
    last_buttons_language[1].destroy()
    
    last_buttons_language.append(ttk.Button())
    last_buttons_language.append(ttk.Button())
    
    last_buttons_language[0] = ttk.Button(sixthframe, text = "+ Add Language",command = addLanguage)
    last_buttons_language[0].grid(column = 1, row = total + 3, sticky = tk.E, padx = (0,20))
    last_buttons_language[1] = ttk.Button(sixthframe, text = "- Remove Language", command = removeLanguage)
    last_buttons_language[1].grid(column = 0, row = total + 3, sticky = tk.W , padx = (20,0))

    last_buttons[0].destroy()
    last_buttons[1].destroy()

    button_next = ttk.Button(displayed_frame, text = "Next >",command = lambda:nextFrame(1))
    button_next.grid(column = 1, row = total+4, sticky = tk.E, padx = (0,20))
    button_previous = ttk.Button(displayed_frame, text = "< Previous", command = lambda:nextFrame(-1))
    button_previous.grid(column = 0, row = total+4, sticky = tk.W , padx = (20,0))
    
    last_buttons[0] = button_next
    last_buttons[1] = button_previous

def removeLanguage():
    global label_languages 
    global languages 
    global label_languages_level 
    global languages_level 
    global last_buttons_language
    global last_buttons
    
    total = 2*len(label_languages)
    if (total > 0):
            
        label_languages[-1].destroy()
        languages[-1].destroy()
        label_languages_level[-1].destroy()
        languages_level[-1].destroy()
        
        label_languages.pop()
        languages.pop()
        label_languages_level.pop()
        languages_level.pop()
    
        total = 2*len(label_languages)
    
        last_buttons_language[0].destroy()
        last_buttons_language[1].destroy()
        
        last_buttons_language.append(ttk.Button())
        last_buttons_language.append(ttk.Button())
        
        last_buttons_language[0] = ttk.Button(sixthframe, text = "+ Add Entry",command = addLanguage)
        last_buttons_language[0].grid(column = 1, row = total + 3, sticky = tk.E, padx = (0,20))
        last_buttons_language[1] = ttk.Button(sixthframe, text = "- Remove Entry", command = removeLanguage)
        last_buttons_language[1].grid(column = 0, row = total + 3, sticky = tk.W , padx = (20,0))
    
        last_buttons[0].destroy()
        last_buttons[1].destroy()
    
        button_next = ttk.Button(displayed_frame, text = "Next >",command = lambda:nextFrame(1))
        button_next.grid(column = 1, row = total+4, sticky = tk.E, padx = (0,20))
        button_previous = ttk.Button(displayed_frame, text = "< Previous", command = lambda:nextFrame(-1))
        button_previous.grid(column = 0, row = total+4, sticky = tk.W , padx = (20,0))
        
        last_buttons[0] = button_next
        last_buttons[1] = button_previous

def addSkill():
    global label_skills 
    global skills 
    global label_skills_level 
    global skills_level 
    global last_buttons_skill
    global last_buttons
    
    label_skills.append(ttk.Label(fifthframe,  text = 'Skill ' + str(len(label_skills) + 1)))
    skills.append(ttk.Entry(fifthframe, font = ('Helvetica',16)))
    label_skills_level.append(ttk.Label(fifthframe,  text = 'Skill level ' + str(len(label_skills_level) + 1)))
    skills_level.append(ttk.Entry(fifthframe, font = ('Helvetica',16)))
    total = 2*len(label_skills)
    
    label_skills[-1].grid(column = 0, row = total+1, sticky = (tk.W), padx = (20,0),pady = 10)
    skills[-1].grid(column = 1, row = total+1, sticky = (tk.E), padx = (0,20),pady = 10)
    label_skills_level[-1].grid(column = 0, row = total+2, sticky = tk.W , padx = (20,0),pady = 10)
    skills_level[-1].grid(column = 1, row = total+2, sticky = tk.E , padx = (0,20),pady = 10)
    
    
    last_buttons_skill[0].destroy()
    last_buttons_skill[1].destroy()
    
    last_buttons_skill.append(ttk.Button())
    last_buttons_skill.append(ttk.Button())
    
    last_buttons_skill[0] = ttk.Button(fifthframe, text = "+ Add Entry",command = addSkill)
    last_buttons_skill[0].grid(column = 1, row = total + 3, sticky = tk.E, padx = (0,20))
    last_buttons_skill[1] = ttk.Button(fifthframe, text = "- Remove Entry", command = removeSkill)
    last_buttons_skill[1].grid(column = 0, row = total + 3, sticky = tk.W , padx = (20,0))

    last_buttons[0].destroy()
    last_buttons[1].destroy()

    button_next = ttk.Button(displayed_frame, text = "Next >",command = lambda:nextFrame(1))
    button_next.grid(column = 1, row = total+4, sticky = tk.E, padx = (0,20))
    button_previous = ttk.Button(displayed_frame, text = "< Previous", command = lambda:nextFrame(-1))
    button_previous.grid(column = 0, row = total+4, sticky = tk.W , padx = (20,0))
    
    last_buttons[0] = button_next
    last_buttons[1] = button_previous
    
def removeSkill():

    global label_skills 
    global skills 
    global label_skills_level 
    global skills_level 
    global last_buttons_skill
    global last_buttons
    
    total = 2*len(label_skills)
    if (total > 0):
            
        label_skills[-1].destroy()
        skills[-1].destroy()
        label_skills_level[-1].destroy()
        skills_level[-1].destroy()
        
        label_skills.pop()
        skills.pop()
        label_skills_level.pop()
        skills_level.pop()
    
        total = 2*len(label_skills)
    
        last_buttons_skill[0].destroy()
        last_buttons_skill[1].destroy()
        
        last_buttons_skill.append(ttk.Button())
        last_buttons_skill.append(ttk.Button())
        
        last_buttons_skill[0] = ttk.Button(fifthframe, text = "+ Add Entry",command = addSkill)
        last_buttons_skill[0].grid(column = 1, row = total + 3, sticky = tk.E, padx = (0,20))
        last_buttons_skill[1] = ttk.Button(fifthframe, text = "- Remove Entry", command = removeSkill)
        last_buttons_skill[1].grid(column = 0, row = total + 3, sticky = tk.W , padx = (20,0))
    
        last_buttons[0].destroy()
        last_buttons[1].destroy()
    
        button_next = ttk.Button(displayed_frame, text = "Next >",command = lambda:nextFrame(1))
        button_next.grid(column = 1, row = total+4, sticky = tk.E, padx = (0,20))
        button_previous = ttk.Button(displayed_frame, text = "< Previous", command = lambda:nextFrame(-1))
        button_previous.grid(column = 0, row = total+4, sticky = tk.W , padx = (20,0))
        
        last_buttons[0] = button_next
        last_buttons[1] = button_previous

def navigate(page : int):
    global displayed_frame

    # Get rid of arrow
    if (displayed_frame == mainframe):
        nextFrame(page-0)   
        menu_employment.entryconfigure(1,label = "Personal Details")
    elif(displayed_frame == secondframe):
        nextFrame(page-1)   
        menu_employment.entryconfigure(2,label = "Summary")
    elif(displayed_frame == thirdframe):
        nextFrame(page-2)   
        menu_employment.entryconfigure(3,label = "Academic History")        
    elif(displayed_frame == fourthframe):
        nextFrame(page-3)   
        menu_employment.entryconfigure(4,label = "Employment History")        
    elif(displayed_frame == fifthframe):
        nextFrame(page-4)   
        menu_employment.entryconfigure(5,label = "Skills")
    elif(displayed_frame == sixthframe):
        nextFrame(page-5)   
        menu_employment.entryconfigure(6,label = "Languages")
    elif(displayed_frame == seventhframe):
        nextFrame(page-6)   
        menu_employment.entryconfigure(7,label = "Wrap Up")
        
    # Add arrow
    if (displayed_frame == mainframe):
        menu_employment.entryconfigure(1,label = "->Personal Details")
    elif(displayed_frame == secondframe):
        menu_employment.entryconfigure(2,label = "->Summary")
    elif(displayed_frame == thirdframe):
        menu_employment.entryconfigure(3,label = "->Academic History")        
    elif(displayed_frame == fourthframe):
        menu_employment.entryconfigure(4,label = "->Employment History")        
    elif(displayed_frame == fifthframe):
        menu_employment.entryconfigure(5,label = "->Skills")
    elif(displayed_frame == sixthframe):
        menu_employment.entryconfigure(6,label = "->Languages")
    elif(displayed_frame == seventhframe):
        menu_employment.entryconfigure(7,label = "->Wrap Up")
        
def printToTemplate():
    
    
    all_entries = {}
    for label,entry in zip(labels,entries):
        print (label['text'])
        if ( isinstance(entry , ttk.Entry)):
            all_entries[label['text'].replace(" ","")] = entry.get()
            print(label['text'])
        elif (isinstance( entry, tk.Text)):
            all_entries[label['text'].replace(" ","")] = entry.get("1.0","end")
    
    extracted_skills = []
    extracted_skill_levels = []
    extracted_languages = []
    extracted_language_levels = []
    for skill, skill_level in zip(skills,skills_level):
        extracted_skills.append(skill.get())
        extracted_skill_levels.append(skill_level.get())
        
    for language, language_level in zip(languages,languages_level):
        
        extracted_languages.append(language.get())
        extracted_language_levels.append(language_level.get())
        
    template = open("LaTeXTemplates\BlueBasicTexTemplate\BlueBasicTemplate.tex", "r")
    text = Template(template.read())
    template.close()
    write_to = open( "CreatedLatexFiles\CV.tex", "w")
    write_to.write(text.render(all_entries, languages = zip(extracted_languages,extracted_language_levels),  
                               skills = zip(extracted_skills,extracted_skill_levels)) )
    write_to.close()
    
def addAcademicEntry():
    global total_academic_history_entries
    total = total_academic_history_entries
    menu_academic_history.entryconfigure(total + 1,label = "Academic History " + str(total+1))
    menu_academic_history.entryconfigure(total + 1, command = lambda:navigate(2))
    if (total_academic_history_entries == 1):
        menu_academic_history.add_command(label = "+ Academic History Entry", command = addAcademicEntry)    
        menu_academic_history.add_command(label = "- Academic History Entry", command = deleteAcademicEntry)
    else:
        menu_academic_history.entryconfigure(total + 2,label = "+ Academic History Entry")
        menu_academic_history.entryconfigure(total + 2, command = addAcademicEntry)
        menu_academic_history.add_command(label = "- Academic History Entry", command = deleteAcademicEntry)

    total_academic_history_entries += 1
         
def deleteAcademicEntry():
    global total_academic_history_entries
    total = total_academic_history_entries
    menu_academic_history.delete(total,total+2)
    total -= 1
    total_academic_history_entries -= 1
    if (total == 1):
        menu_academic_history.add_command(label = "+ Academic History Entry", command = addAcademicEntry)
    else:
        menu_academic_history.add_command(label = "+ Academic History Entry", command = addAcademicEntry)
        menu_academic_history.add_command(label = "- Academic History Entry", command = deleteAcademicEntry)
        
    
# This is the menu that navigates through all the pages

menu_employment = tk.Menu(root)
menu_employment.add_command(label = "->Personal Details", command = lambda:navigate(0))

menu_employment.add_command(label = "Summary",command = lambda:navigate(1))

menu_academic_history = tk.Menu(menu_employment)
menu_employment.add_cascade(label = "Academic History", menu=menu_academic_history)
menu_academic_history.add_command(label = "Academic History 1", command = lambda:navigate(2))
total_academic_history_entries = 1
menu_academic_history.add_command(label = "+ Academic History Entry", command = addAcademicEntry)


menu_employment.add_command(label = "Employment History", command = lambda:navigate(3))

menu_employment.add_command(label = "Skills", command = lambda:navigate(4))

menu_employment.add_command(label = "Languages", command = lambda:navigate(5))

menu_employment.add_command(label = "Wrap Up", command = lambda:navigate(6))

root.config(menu = menu_employment)

entries = []
labels = []
    
# Everything here is related to the first frame

label_name = ttk.Label(mainframe, text = 'Name')
label_name.grid(column = 0, row = 0, sticky = (tk.W), padx = (20,0),pady = 10)
name = ttk.Entry(mainframe, font = ('Helvetica',16))
name.grid(column = 1, row = 0, sticky = (tk.E), padx = (0,20),pady = 10)

label_surname = ttk.Label(mainframe, text = 'Surname')
label_surname.grid(column = 0, row = 1, sticky = tk.W , padx = (20,0),pady = 10)
surname = ttk.Entry(mainframe, font = ('Helvetica',16))
surname.grid(column = 1, row = 1, sticky = tk.E , padx = (0,20),pady = 10)

label_telephone_number = ttk.Label(mainframe, text = 'Phone number')
label_telephone_number.grid(column = 0, row = 2, sticky = tk.W , padx = (20,0),pady = 10)
telephone_number = ttk.Entry(mainframe, font = ('Helvetica',16))
telephone_number.grid(column = 1, row = 2, sticky = tk.E , padx = (0,20),pady = 10)

label_mail = ttk.Label(mainframe, text = 'Email')
label_mail.grid(column = 0, row = 3, sticky = tk.W, padx = (20,0),pady = 10)
mail = ttk.Entry(mainframe, font = ('Helvetica',16))
mail.grid(column = 1, row = 3, sticky = tk.E, padx = (0,20),pady = 10)

label_Linkedin = ttk.Label(mainframe, text = 'Linkedin URL')
label_Linkedin.grid(column = 0, row = 4, sticky = tk.W, padx = (20,0),pady = 10)
Linkedin = ttk.Entry(mainframe, font = ('Helvetica',16))
Linkedin.grid(column = 1, row = 4, sticky =tk.E, padx = (0,20),pady = 10)

button_next = ttk.Button(displayed_frame, text = "Next >",command = lambda:nextFrame(1))
button_next.grid(column = 1, row = 5, sticky = tk.E, padx = (0,20))
button_previous = ttk.Button(displayed_frame, text = "< Previous", command = lambda:nextFrame(-1))
button_previous.grid(column = 0, row = 5, sticky = tk.W , padx = (20,0))
last_buttons[0] = button_next
last_buttons[1] = button_previous

entries.append(surname)
labels.append(label_surname)
entries.append(name)
labels.append(label_name)
entries.append(Linkedin)
labels.append(label_Linkedin)
entries.append(mail)
labels.append(label_mail)
entries.append(telephone_number)
labels.append(label_telephone_number)


for i in range(0,2):
    for j in range (0,5):
        mainframe.rowconfigure(i, weight = 1)
        mainframe.columnconfigure(j, weight = 3)

# Everything here is related to the second frame

label_summary = ttk.Label(secondframe, text = 'Profile')
label_summary.grid(column = 0, row = 0, sticky = (tk.W), padx = (20,20),pady = 10)
text_summary = tk.Text(secondframe, font = ('Helvetica',12),  height = 5, width = 40)
text_summary.grid(column = 1, row = 0, sticky = (tk.S,tk.N,tk.E,tk.W), padx = (20,20),pady = 10)
text_summary.insert("1.0","Give employers a summary of your life. \n")

entries.append(text_summary)
labels.append(label_summary)

# Everything here is related to the third frame

label_establishment = ttk.Label(thirdframe, text = 'Establishment')
label_establishment.grid(column = 0, row = 0, sticky = (tk.W), padx = (20,0),pady = 10)
establishment = ttk.Entry(thirdframe, font = ('Helvetica',16))
establishment.grid(column = 1, row = 0, sticky = (tk.E), padx = (0,20),pady = 10)

label_start_date = ttk.Label(thirdframe, text = 'Start date')
label_start_date.grid(column = 0, row = 1, sticky = (tk.W), padx = (20,0),pady = 10)
start_date = ttk.Entry(thirdframe, font = ('Helvetica',16))
start_date.grid(column = 1, row = 1, sticky = (tk.E), padx = (0,20),pady = 10)

label_end_date = ttk.Label(thirdframe, text = 'End date')
label_end_date.grid(column = 0, row = 2, sticky = (tk.W), padx = (20,0),pady = 10)
end_date = ttk.Entry(thirdframe, font = ('Helvetica',16))
end_date.grid(column = 1, row = 2, sticky = (tk.E), padx = (0,20),pady = 10)

label_specialization = ttk.Label(thirdframe, text = 'Specialization')
label_specialization.grid(column = 0, row = 3, sticky = (tk.W), padx = (20,0),pady = 10)
specialization = ttk.Entry(thirdframe, font = ('Helvetica',16))
specialization.grid(column = 1, row = 3, sticky = (tk.E), padx = (0,20),pady = 10)

label_description = ttk.Label(thirdframe, text = 'Description')
label_description.grid(column = 0, row = 4, sticky = (tk.W), padx = (20,0),pady = 10)
text_description = tk.Text(thirdframe, font = ('Helvetica',16), height = 5, width = 40)
text_description.grid(column = 1, row = 4, sticky = (tk.E), padx = (0,20),pady = 10)
text_description.insert("1.0", "List highlights of your time spent in said establishment. \n")

entries.append(establishment)
labels.append(label_establishment)
entries.append(start_date)
labels.append(label_start_date)
entries.append(end_date)
labels.append(label_end_date)
entries.append(specialization)
labels.append(label_specialization)
entries.append(text_description)
labels.append(label_description)

# Everything here is related to the fourth frame

label_company_name = ttk.Label(fourthframe, text = 'Company')
label_company_name.grid(column = 0, row = 0, sticky = (tk.W), padx = (20,0),pady = 10)
company_name = ttk.Entry(fourthframe, font = ('Helvetica',16))
company_name.grid(column = 1, row = 0, sticky = (tk.E), padx = (0,20),pady = 10)

label_start_date_job = ttk.Label(fourthframe, text = 'Job start date')
label_start_date_job.grid(column = 0, row = 1, sticky = (tk.W), padx = (20,0),pady = 10)
start_date_job = ttk.Entry(fourthframe, font = ('Helvetica',16))
start_date_job.grid(column = 1, row = 1, sticky = (tk.E), padx = (0,20),pady = 10)

label_end_date_job = ttk.Label(fourthframe, text = 'Job end date')
label_end_date_job.grid(column = 0, row = 2, sticky = (tk.W), padx = (20,0),pady = 10)
end_date_job = ttk.Entry(fourthframe, font = ('Helvetica',16))
end_date_job.grid(column = 1, row = 2, sticky = (tk.E), padx = (0,20),pady = 10)

label_position = ttk.Label(fourthframe, text = 'Position')
label_position.grid(column = 0, row = 3, sticky = (tk.W), padx = (20,0),pady = 10)
position = ttk.Entry(fourthframe, font = ('Helvetica',16))
position.grid(column = 1, row = 3, sticky = (tk.E), padx = (0,20),pady = 10)

label_description_job = ttk.Label(fourthframe, text = 'Job description')
label_description_job.grid(column = 0, row = 4, sticky = (tk.W), padx = (20,0),pady = 10)
text_description_job = tk.Text(fourthframe, font = ('Helvetica',16), height = 5, width = 40)
text_description_job.grid(column = 1, row = 4, sticky = (tk.E), padx = (0,20),pady = 10)
text_description_job.insert("1.0","Give employers an idea of what your job entitled. \n")


entries.append(company_name)
labels.append(label_company_name)
entries.append(start_date_job)
labels.append(label_start_date_job)
entries.append(end_date_job)
labels.append(label_end_date_job)
entries.append(position)
labels.append(label_position)
entries.append(text_description_job)
labels.append(label_description_job)

# Everything here is related to the fifth frame

label_skills = [ttk.Label()]
skills = [ttk.Entry()]
label_skills_level = [ttk.Label()]
skills_level = [ttk.Entry()]

label_skills[0] = ttk.Label(fifthframe, text = 'Skill 1')
label_skills[0].grid(column = 0, row = 0, sticky = (tk.W), padx = (20,0),pady = 10)
skills[0] = ttk.Entry(fifthframe, font = ('Helvetica',16))
skills[0].grid(column = 1, row = 0, sticky = (tk.E), padx = (0,20),pady = 10)

label_skills_level[0] = ttk.Label(fifthframe, text = 'Skill level 1')
label_skills_level[0].grid(column = 0, row = 1, sticky = tk.W , padx = (20,0),pady = 10)
skills_level[0] = ttk.Entry(fifthframe, font = ('Helvetica',16))
skills_level[0].grid(column = 1, row = 1, sticky = tk.E , padx = (0,20),pady = 10)
    
last_buttons_skill = []

last_buttons_skill.append(ttk.Button(fifthframe, text = "+ Add Entry",command = addSkill))
last_buttons_skill[0].grid(column = 1, row = 5, sticky = tk.E, padx = (0,20))
last_buttons_skill.append(ttk.Button(fifthframe, text = "- Remove Entry", command = removeSkill))
last_buttons_skill[1].grid(column = 0, row = 5, sticky = tk.W , padx = (20,0))

# Everything here is related to the sixth frame

label_languages = [ttk.Label()]
languages = [ttk.Entry()]
label_languages_level = [ttk.Label()]
languages_level = [ttk.Entry()]

label_languages[0] = ttk.Label(sixthframe, text = 'Language 1')
label_languages[0].grid(column = 0, row = 0, sticky = (tk.W), padx = (20,0),pady = 10)
languages[0] = ttk.Entry(sixthframe, font = ('Helvetica',16))
languages[0].grid(column = 1, row = 0, sticky = (tk.E), padx = (0,20),pady = 10)

label_languages_level[0] = ttk.Label(sixthframe, text = 'Language level 1')
label_languages_level[0].grid(column = 0, row = 1, sticky = tk.W , padx = (20,0),pady = 10)
languages_level[0] = ttk.Entry(sixthframe, font = ('Helvetica',16))
languages_level[0].grid(column = 1, row = 1, sticky = tk.E , padx = (0,20),pady = 10)
    
last_buttons_language = []

last_buttons_language.append(ttk.Button(sixthframe, text = "+ Add Language",command = addLanguage))
last_buttons_language[0].grid(column = 1, row = 5, sticky = tk.E, padx = (0,20))
last_buttons_language.append(ttk.Button(sixthframe, text = "- Remove Language", command = removeLanguage))
last_buttons_language[1].grid(column = 0, row = 5, sticky = tk.W , padx = (20,0))

# Everything here is related to the seventh frame

label_cv_name = ttk.Label(seventhframe, text = 'CV name')
label_cv_name.grid(column = 0, row = 0, sticky = (tk.W), padx = (20,0),pady = 10)
cv_name = ttk.Entry(seventhframe, font = ('Helvetica',16))
cv_name.grid(column = 1, row = 0, sticky = (tk.E), padx = (0,20),pady = 10)

button_finish = ttk.Button(seventhframe, text = "Print To Template",command = printToTemplate)
button_finish.grid(column = 0, row = 2, sticky = tk.W, padx = (20,0))


#template = Template(template)

#file = open("template.tex","r+")
#hello = file.read()
#doc = Document('basic')
#doc.append(hello)
#doc.generate_pdf('basic_maketitle2', clean_tex=False)
#file.close()


""" 
        might want to call pack last or set the 
        height last OR at least set it as a variable 
        and call all packs last
"""
""" 
        the next button ideally iterates through all entries 
        and registers everything in a dictionary of the form 
        dict(label : entry)

"""
#tk.colorchooser.askcolor(initialcolor='#ff0000') - might come in handy

mainframe.tkraise()
root.mainloop()