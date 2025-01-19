import argparse
import json


class CalcAvg():
    def __init__(self, fname=None):
        self.marks = {}
        self.fname = fname

        if fname:
            self.load_file()
        else:
            self.create_new()

        
    def load_file(self):
        with open(self.fname, "r") as f:
            self.marks = json.load(f)


    def save_marks(self):
        with open(self.fname, "w") as f:
            json.dump(self.marks, f, indent=4, sort_keys=True)
    

    def del_unit(self):
        try:
            keys = self.marks.keys()
            for idx, key in enumerate(keys):
                print (f'{idx + 1}. {key}')
            resp = int(input('Enter the subjects corresponding number(or 0 to quit):'))
            if resp == 0:
                self.main_menu()
            subject = (list(keys)[resp - 1])
            sdict = self.marks[subject]
            for idx, key in enumerate(sdict.keys()):
                print(f'{idx + 1}. {key}')
            unit_int = int(input("\nWhich unit do you want to delete(or 0 to quit): "))
            unit = (list(sdict)[unit_int - 1])
            sunit = self.marks[subject][unit]
            if unit_int == 0:
                self.main_menu()
            print(unit)
            yes_or_no = input('Are you sure you want to delete this unit (y or n): ')
            if yes_or_no == 'y':
                del self.marks[subject][unit]
                print(sdict)
            if yes_or_no == 'n':
                self.main_menu()    
        except:
            self.main_menu()


        

    def del_subject(self):
        try:
            keys = self.marks.keys()
            resp = input('do you want to delete something (y or n): ')
            if resp.lower() == 'y':
                s_or_u = input('Do you want to delete a subject or a unit(s or u or q to quit): ')
                if s_or_u.lower() == 'u':
                    self.del_unit()
                elif s_or_u.lower() == 's':
                    for idx, key in enumerate(keys):
                        print(f'{idx + 1}. {key}')
                    what_subject = int(input('What subject do you want to delete(enter the number):'))
                    subject = (list(keys)[what_subject - 1])
                    are_u_sure = input('Are you sure you whant to delete this subject(y or n): ')
                    if are_u_sure.lower() == 'y':
                        del self.marks[subject]
                        print(self.marks)
                    if are_u_sure.lower() == 'n':
                        self.main_menu()
                    elif s_or_u.lower() != 's' or 'u':
                        self.main_menu()
                elif resp.lower() == 'n':
                    self.main_menu()
                elif resp.lower() != 'n' or 'y':
                    self.main_menu()
        except:
            self.main_menu()

    def update_mark(self):
        try:
            keys = self.marks.keys()
            for idx, key in enumerate(keys):
                print (f'{idx + 1}. {key}')
            subj_int = int(input("\nEnter subject number(or 0 to quit): "))
            subject = (list(keys)[subj_int - 1])
            sdict = self.marks[subject]
            # print(sdict)
            for idx, key in enumerate(sdict.keys()):
                if sdict[key]['mark'] >= 0.0:
                    print(f'{idx + 1}. {key} {sdict[key]["mark"]}')
                else:
                    print(f'{idx + 1}. {key}')
            unit_int = int(input("\nWhich units mark do you want to change(or 0 to quit): "))
            unit = (list(sdict)[unit_int - 1])
            sunit = self.marks[subject][unit]
            print(sunit['mark'])
            new_grade = int(input('\nWhat is your new grade: '))
            sunit['mark'] = new_grade
            print(f"\nYour new grade is: {sunit['mark']}")
        except:
            self.main_menu()

    def update_weight(self):
        try:
            keys = self.marks.keys()
            for idx, key in enumerate(keys):
                print (f'{idx + 1}. {key}')
            subj_int = int(input("\nEnter subject number: "))
            subject = (list(keys)[subj_int - 1])
            sdict = self.marks[subject]
            for idx, key in enumerate(sdict.keys()):
                print(f'\n{idx + 1}. {key} {sdict[key]["weight"]}')
            unit_int = int(input("\nWhich units weight do you want to change: "))
            unit = (list(sdict)[unit_int - 1])
            sunit = self.marks[subject][unit]
            print(sunit['weight'])
            new_weight = int(input('\nWhat is your new weight: '))
            sunit['weight'] = new_weight
            print(f"\nYour new weight is: {sunit['weight']}")
        except:
            self.main_menu()
    

    def calculate_current_mark(self):
        # university mark
        univ_avg = 0
        total_weight = 0

        # traverse subjects
        for subject in self.marks:
            subject_avg = 0
            weight = 0
            

            # traverse each unit in subject
            for unit in self.marks[subject]:
                if self.marks[subject][unit]["mark"] < 0.0:
                    continue
                unit_avg = self.marks[subject][unit]["mark"] * self.marks[subject][unit]["weight"] / 100
                subject_avg = subject_avg + unit_avg
                weight = weight + self.marks[subject][unit]["weight"]
                print(f'{subject} {unit} {unit_avg} out of weight {self.marks[subject][unit]["weight"]}')
            print(f'{subject} {subject_avg} out of {weight} out of 100')
            univ_avg = (univ_avg + subject_avg)
            total_weight = total_weight + weight
        print(f'Univ: {univ_avg / len(self.marks)} out of {total_weight / len(self.marks)} out of 100')


    def new_unit(self):
        try:
            keys = self.marks.keys()
            for idx, key in enumerate(keys):
                print (f'{idx + 1}. {key}')
            subj_int = int(input("\nWhich subject do you want to add a unit to (enter number): "))
            subject = (list(keys)[subj_int - 1])
            sdict = self.marks[subject]
            resp = input('\nEnter units with a space in between each one(no spaces between units and their numbers): ')
            units = resp.split(' ')
            for unit in units:
                self.marks[subject][unit] = {
                    "mark" : -1.0,
                    "weight" : 0
                }
            print(self.marks)
        except:
            self.main_menu()




    def create_new(self):
        try:
            s_or_u = input('\nDo you want to add a new subject or a new unit (s or u): ')
            if s_or_u.lower() == 's':
                sub_input = input("\nEnter subjects separated by space: ")
                subjects = sub_input.split(' ')
                for s in subjects:
                    self.marks[s] = {
                    'midterm' : {
                    'weight': 0.0,
                    'mark': -1.0
                    },
                    'final' : {
                    'weight': 0.0,
                    'mark': -1.0
                    }
                                }
                    print(self.marks)
            elif s_or_u.lower() == 'u':
                self.new_unit()
        except:
            self.main_menu()

    def subject_menu(self):
        try:
            subjectchange = input("\nDo you want to change a subject's units weights or marks(y or n): ")
            if subjectchange.lower() == 'y':
                weight_mark = input("\nupdate weight or marks(w or m):")
                if weight_mark.lower() == 'w':
                    self.update_weight()
                elif weight_mark.lower() == 'm':
                    self.update_mark()
                elif weight_mark != 'w' or 'm':
                    self.subject_menu
            if subjectchange.lower() == 'n':
                self.main_menu
            elif subjectchange != 'y' or 'n':
                self.main_menu()
        except:
            self.main_menu()


    def final_calc(self):
        keys = self.marks.keys()
        for subject in keys:
            keys2 = self.marks[subject].keys()
            print(keys2)
            print(subject)
            for unit in keys2:
                keys3 = self.marks[subject][unit].keys()
                print(keys3)
                for mark in keys2:
                    print(self.marks[subject][unit][mark].keys())


    def main_menu(self):
        while True:
            print('\n1. Create a new subject or unit')
            print('2. Update subjects grades or weights')
            print('3. Delete subject or unit')
            print('4. Calculate grade')
            print('5. Save changes')
            print('6. final calculator')
            print('7. Quit')
            resp = input('Enter your option(number): ')
            if resp == '1':
                self.create_new()
            elif resp == '2':
                self.subject_menu()

            elif resp == '3':
                self.del_subject()
            elif resp == '4':
                self.calculate_current_mark()
            elif resp == '5':
                self.save_marks()
            elif resp == '6':
                self.final_calc()
            elif resp.lower() == 'q' or 'exit' or 'quit' or 'leave' or '7':
                break
            else:
                self.main_menu()



avg = CalcAvg("/home/chrisbuczy/src/python/gradeavg/christian.json")
avg.main_menu()

