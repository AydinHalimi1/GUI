import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('100x200')
        self.main_window.title('Label Demo')

        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.output_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.test1_frame = tkinter.IntVar()
        self.test2_frame = tkinter.IntVar()
        self.test3_frame = tkinter.IntVar()
        self.output_frame = tkinter.IntVar()
        self.bottom_frame = tkinter.IntVar()


        self.Label1 = tkinter.Label(self.test1_frame,text='Enter the score for test 1:',variable=self.test1_frame)
        self.Label2 = tkinter.Label2(self.test2_frame,text='Enter the score for test 2:',variable=self.test2_frame)
        self.Label3 = tkinter.Label3(self.test3_frame,text='Enter the score for test 3:',variable=self.test3_frame)

        self.avg_entry = tkinter.Entry(self.main_window,width=10)


        self.Label4 = tkinter.Label4(self.ouput_frame,text='Average',variable=self.output_frame)

        self.Label5 = tkinter.Label5(self.bottom_frame,text='Option 3',variable=self. bottom_frame)

        self.avg_button = tkinter.Button(self.main_window,text='Average',command=self.convert)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)


        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

 