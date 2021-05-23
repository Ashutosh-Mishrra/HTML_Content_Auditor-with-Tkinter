#!/usr/bin/env python
__author__ = "Ashutosh Mishra"
__credits__ = ["Ashutosh Mishra"]
__code_name__ = "HTML_Content_Auditor"
__version__ = "1.0"
__maintainer__ = "Ashutosh Mishra"
__status__ = "Production"

import os
from datetime import datetime
import time
import difflib
from tkinter import *
from tkinter import filedialog
from tkinter import font as f
from pil import Image, ImageTk
from tkinter import ttk

t1 = time.time()

dir_path = os.path.dirname(os.path.realpath(__file__))

class content_auditor():

    def file_location(self):

        htmlfile1 = filedialog.askopenfilename()

        htmlfile2 = filedialog.askopenfilename()

        obj.main_function(htmlfile1,htmlfile2)

        obj.difference_output(htmlfile1, htmlfile2)


    def main_function(self,loc1,loc2):

        htmlfile1 = loc1

        htmlfile2 = loc2

        with open(htmlfile1) as we, open(htmlfile2) as woe:

            count = 0

            line_error = 0

            error_no_list = []

            for file1Line, file2Line in zip(we, woe):

                line_error += 1

                if file1Line != file2Line:

                    self.flagg = True

                    count += 1

                    #print(f'Difference:{count}')

                    #print(f'Error in Line: {line_error}')

                    #print(file1Line.strip('\n'))

                    #print(file2Line.strip('\n'))

                    error_no_list.append(line_error)

            self.label1 = Label(window, text=f'Error in Lines : {error_no_list}', relief=RAISED, font=font_style)

            self.label1.place(relx=0.5, rely=0.5, anchor='center')

            self.label1.config(fg='Crimson',bg='PeachPuff')

            print(f'Total Differences: {count}')

            self.label3 = Label(window, text=f'Total Differences: {count}', relief=RAISED, font=font_style2)

            self.label3.place(relx=0.5, rely=0.4, anchor='center')

            self.label3.config(fg='RoyalBlue',bg = 'PeachPuff')

            if count == 0:

                self.flagg = False

                self.label2 = Label(window, text="100% Match", relief=RAISED,font=font_style3)

                self.label2.place(relx =0.5,rely =0.5,anchor='center')

                self.label2.config(fg='SeaGreen',bg = 'PeachPuff')

                print('100% Match')

        final = (time.time() - t1) / 60

        print(f"Total Execution Time: {final} mins")

        self.label4 = Label(window, text=f"Total Execution Time: {final} mins", relief=RAISED, font=font_style1)

        self.label4.config(fg='Maroon',bg = 'PeachPuff')

        self.label4.place(relx=0.5, rely=0.9, anchor='s')

    def clear_label(self):

        if self.flagg == True:

            self.label1.destroy()

            self.label3.destroy()

            self.label4.destroy()

        else:

            self.label1.destroy()

            self.label2.destroy()

            self.label3.destroy()

            self.label4.destroy()

    def difference_output(self,loc1,loc2):

        htmlfile1 = loc1

        htmlfile2 = loc2

        file1 = open(htmlfile1, 'r').readlines()

        file2 = open(htmlfile2, 'r').readlines()

        htmlDiffer = difflib.HtmlDiff()

        htmldiffs = htmlDiffer.make_file(file1, file2)

        with open(f'{dir_path}\\Output\\difference.html', 'w') as outfile:

            outfile.write(htmldiffs)

if __name__ == '__main__':

    start = datetime.now()

    obj = content_auditor()

    window = Tk()

    window.geometry("1366x768")

    window.iconbitmap(f'{dir_path}\\icon_files\\browse.ico')

    window['bg'] = 'LightCoral'

    window.title('HTML_Content_Auditor')

    window.resizable(0,0)

    image1 = Image.open(f'{dir_path}\\icon_files\\u.jpg')

    img = image1.resize((1366,768), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(img)

    image_label = ttk.Label(window, image=image2)

    image_label.place(x=0, y=0)

    font_style = f.Font(family="Impact", size=25)

    font_style1 = f.Font(family="Courier New", size=15)

    font_style2 = f.Font(family="Arial", size=25)

    font_style3 = f.Font(family="Arial", size=30)

    font_style4 = f.Font(family="Arial", size=22)

    click_button = Button(window,text="BROWSE FILES",command=obj.file_location,font=font_style4)

    click_button.config(fg='Black',bg = 'PeachPuff')

    click_button.place(relx =0.5,rely =0.1,anchor='n')

    click_button2 = Button(window, text="CLEAR", command=obj.clear_label,font=font_style4)

    click_button2.place(relx=0.5, rely=0.2, anchor='n')

    click_button2.config(fg='Black', bg='PeachPuff')

    #obj.file_location()

    window.mainloop()