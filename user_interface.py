import tkinter as tk
from tkinter import *
import tkinter
from tkinter import filedialog
from tkinter import ttk, StringVar, IntVar
from PIL import ImageTk, Image
from tkinter import messagebox
from PIL import Image
import final_sotware
import xlwt
from xlwt import Workbook


def s_exit():
    exit(0)

def show():
    window2 = Tk()
    window2.title("Attendance System")
    window2.geometry("600x350")
    tkinter.Label(window2, text = "WELCOME TO FACE RECOGNITION ATTENDANCE SOFTWARE", fg="black", bg="snow4").pack(fill="x")
    
    tkinter.Label(window2, text = "\n").pack(fill = 'y')

    tkinter.Label(window2, text = "TRAIN - to train a classifer on the facenet model.\n\n"
                                  "TEST - to test a facenet classification model on previously created dataset.\n\n"
                                  "CREATE - to create dataset.\n\n"
                                  "RUN - to test using webcam or mark attendance.\n",fg = 'snow4', bg = 'snow2').pack(fill = 'y')

    bottom_frame = tkinter.Frame(window2).pack(side = "bottom")

    def train():
        print('train')
        window2.destroy()
        show_train()

    def test():
        print('test')
        window2.destroy()
        show_test()

    def create():
        print('create')
        window2.destroy()
        show_create()

    def run():
        print('run')
        window2.destroy()
        show_run()

    btn1 = tkinter.Button(bottom_frame, text = "TRAIN", fg = "black", bg = 'snow3', command = train)
    btn1.place(x=130, y=200, width=50)

    btn2 = tkinter.Button(bottom_frame, text = "TEST", fg = "black", bg = 'snow3', command = test)
    btn2.place(x=230, y=200, width=50)

    btn3 = tkinter.Button(bottom_frame, text = "CREATE", fg = "black", bg = 'snow3', command = create)
    btn3.place(x=330, y=200, width=50)

    btn3 = tkinter.Button(bottom_frame, text = "RUN", fg = "black", bg = 'snow3', command = run)
    btn3.place(x=430, y=200, width=50)

    btn4 = tkinter.Button(bottom_frame, text = "EXIT", fg = "black", bg = 'tomato', command = s_exit)
    btn4.place(x=270, y=270, width=60)

    window2.mainloop()

def show_run():

    window3 = Tk()
    window3.title("Attendance System")
    window3.geometry("800x400")
    tkinter.Label(window3, text = "WELCOME TO FACE DETECTION AND RECOGNITION SOFTWARE", fg="black", bg="snow4").pack(fill="x")
    tkinter.Label(window3, text="\n ").pack(fill='y')
    
    #tkinter.Label(window3, text = "Enter the path to classifier.pkl").place(x=50, y=50, width=250)
    path1 = tkinter.Entry(window3)
    #path1.place(x=60, y=70, width=400)

    #tkinter.Label(window3, text = "Enter the path to 20180402-114759 FOLDER").place(x=50, y=100, width=300)
    path2 = tkinter.Entry(window3)
    #path2.place(x=60, y=120, width=400)

    #tkinter.Label(window3, text = "Enter desired face width and height for face aligner (WidthxHeight format)").place(x=50, y=150, width=530)
    face_dim = tkinter.Entry(window3)
    #face_dim.place(x=60, y=170, width=400)
    
    tkinter.Label(window3, text = "gpu memory fraction out of 1").place(x=60, y=50, width=200)
    gpu = tkinter.Entry(window3)
    gpu.place(x=60, y=70, width=200)

    tkinter.Label(window3, text = "threshold for MTCNN detection").place(x=300, y=50, width=200)
    thresh1 = tkinter.Entry(window3)
    thresh1.place(x=300, y=70, width=200)

    tkinter.Label(window3, text = "threshold for face recognition").place(x=540, y=50, width=200)
    thresh2 = tkinter.Entry(window3)
    thresh2.place(x=540, y=70, width=200)

    tkinter.Label(window3, text="Default values would be assigned to empyt fields", fg="navy", bg="lightblue").place(x=200, y=120, width=400)

    rdbtn1 = IntVar()
    rdbtn2 = IntVar()
    rdbtn3 = IntVar()

    rdbi = tkinter.Checkbutton(window3, text="Input: Image", variable = rdbtn3, fg="navy", bg="lightblue")
    rdbi.place(x=60, y=170, width=200)

    tkinter.Label(window3, text = "path to input images folder").place(x=300, y=150, width=200)
    img_path = tkinter.Entry(window3)
    img_path.place(x=300, y=170, width=200)

    tkinter.Label(window3, text = "path to output images folder").place(x=540, y=150, width=200)
    out_img_path = tkinter.Entry(window3)
    out_img_path.place(x=540, y=170, width=200)

    rdbv = tkinter.Checkbutton(window3, text="Input: Video", variable = rdbtn2, fg="navy", bg="lightblue")
    rdbv.place(x=60, y=220, width=200)

    tkinter.Label(window3, text = "path to input video file").place(x=300, y=200, width=200)
    vid_path = tkinter.Entry(window3)
    vid_path.place(x=300, y=220, width=200)

    tkinter.Label(window3, text = "Save o/p 'y'").place(x=540, y=200, width=80)
    vid_save = tkinter.Entry(window3)
    vid_save.place(x=540, y=220, width=80)

    tkinter.Label(window3, text = "See o/p 'y'").place(x=660, y=200, width=80)
    vid_see = tkinter.Entry(window3)
    vid_see.place(x=660, y=220, width=80)

    rdbw = tkinter.Checkbutton(window3, text="Input: Webcam", variable = rdbtn1, fg="navy", bg="lightblue")
    rdbw.place(x=60, y=270, width=200)
    tkinter.Label(window3, text = "Supported webcam resolution (eg 640x480)").place(x=300, y=250, width=380)
    resolution = tkinter.Entry(window3)
    resolution.place(x=300, y=270, width=400)

    def mark_attend():
        if rdbtn1.get():
            print('Webcam')
            mode = 'w'
        elif rdbtn2.get():
            print('Video')
            mode = 'v'
        elif rdbtn3.get():
            print('Image')
            mode = 'i'
        else:
            print('default')
            mode = 'w'

        print(mode)
        parameters = path1.get(), path2.get(), face_dim.get(), gpu.get(), thresh1.get(), thresh2.get(), resolution.get(), \
                     img_path.get(), out_img_path.get(), vid_path.get(), vid_save.get(), vid_see.get()
        print(parameters)
        st_name = final_sotware.recognize(mode, parameters)
        print('students recognised', st_name)

    btn11 = tkinter.Button(window3, text = "Mark Attendance", fg = "black", bg = 'lawn green', command = mark_attend)
    btn11.place(x=350, y=320, width=120)

    btn10 = tkinter.Button(window3, text = "EXIT", fg = "black", bg = 'tomato', command = s_exit)
    btn10.place(x=480, y=320, width=60)

    def home():
        window3.destroy()
        gotohome()

    btn12 = tkinter.Button(window3, text = "HOME", fg = "black", bg = 'turquoise1', command = home)
    btn12.place(x=250, y=320, width=90)

    window3.mainloop()

def show_create():

    window4 = Tk()
    window4.title("Attendance System")
    window4.geometry("800x400")
    tkinter.Label(window4, text = "WELCOME TO FACE RECOGNITION ATTENDANCE SOFTWARE", fg="black", bg="snow4").pack(fill="x")
    tkinter.Label(window4, text="\n ").pack(fill='y')

    tkinter.Label(window4, text = "path to output folder").place(x=60, y=50, width=200)
    path1 = tkinter.Entry(window4)
    path1.place(x=60, y=70, width=200)

    tkinter.Label(window4, text = "Supported webcam resolution (eg 640x480)").place(x=320, y=50, width=400)
    webcam = tkinter.Entry(window4)
    webcam.place(x=320, y=70, width=400)

    tkinter.Label(window4, text = "gpu memory fraction out of 1").place(x=320, y=100, width=400)
    gpu = tkinter.Entry(window4)
    gpu.place(x=320, y=120, width=400)

    #tkinter.Label(window4, text = "Enter desired face width and height (WidthxHeight format)").place(x=50, y=200, width=430)
    face_dim = tkinter.Entry(window4)
    #face_dim.place(x=60, y=220, width=400)

    tkinter.Label(window4, text = "Enter user name (default: person)").place(x=60, y=100, width=200)
    username = tkinter.Entry(window4)
    username.place(x=60, y=120, width=200)

    tkinter.Label(window4, text="Default values would be assigned to empyt fields", fg="navy", bg="lightblue").place(x=180, y=170, width=400)

    tkinter.Label(window4, text = "Create dataset using:").place(x=60, y=240, width=110)

    rdbtn1 = IntVar()
    rdbtn2 = IntVar()

    rdbv = tkinter.Checkbutton(window4, text="Video", variable = rdbtn1, fg="black", bg="skyblue1")
    rdbv.place(x=280, y=240, width=80)

    rdbw = tkinter.Checkbutton(window4, text="Webcam", variable = rdbtn2, fg="black", bg="skyblue1")
    rdbw.place(x=180, y=240, width=80)

    tkinter.Label(window4, text = "path to input video file").place(x=380, y=220, width=300)
    vid_path = tkinter.Entry(window4)
    vid_path.place(x=380, y=240, width=340)

    get_f = 0

    def submit():
        print('submit')
        parameters = path1.get(), webcam.get(), face_dim.get(), gpu.get(), username.get(), vid_path.get()
        print(parameters)
        get_f = final_sotware.dataset_creation(parameters)

        if get_f == 1:
            tkinter.messagebox.showinfo("Attendance", "Dataset Created")

    btn9 = tkinter.Button(window4, text = "Create Dataset", fg = "black", bg = 'lawn green', command = submit)
    btn9.place(x=350, y=320, width=120)

    btn9 = tkinter.Button(window4, text = "EXIT", fg = "black", bg = 'tomato', command = s_exit)
    btn9.place(x=480, y=320, width=60)

    def home():
        window4.destroy()
        gotohome()

    btn10 = tkinter.Button(window4, text = "HOME", fg = "black", bg = 'turquoise1', command = home)
    btn10.place(x=250, y=320, width=90)

    window4.mainloop()

def show_train():

    window5 = Tk()
    window5.title("Attendance System")
    window5.geometry("800x400")
    tkinter.Label(window5, text = "WELCOME TO FACE RECOGNITION ATTENDANCE SOFTWARE", fg="black", bg="snow4").pack(fill="x")
    tkinter.Label(window5, text="\n ").pack(fill='y')

    tkinter.Label(window5, text = "path to dataset folder").place(x=60, y=50, width=300)
    path1 = tkinter.Entry(window5)
    path1.place(x=60, y=70, width=300)

    tkinter.Label(window5, text = "path to 20180402-114759 folder").place(x=420, y=50, width=300)
    path2 = tkinter.Entry(window5)
    path2.place(x=420, y=70, width=300)

    tkinter.Label(window5, text = "gpu memory fraction out of 1").place(x=60, y=100, width=300)
    gpu = tkinter.Entry(window5)
    gpu.place(x=60, y=120, width=300)

    tkinter.Label(window5, text = "batch size of images to process at once").place(x=420, y=100, width=300)
    batch = tkinter.Entry(window5)
    batch.place(x=420, y=120, width=300)

    tkinter.Label(window5, text = "input image dimension (eg. 160)").place(x=60, y=150, width=300)
    img_dim = tkinter.Entry(window5)
    img_dim.place(x=60, y=170, width=300)

    tkinter.Label(window5, text = "filename of output SVM classifier").place(x=420, y=150, width=300)
    svm_name = tkinter.Entry(window5)
    svm_name.place(x=420, y=170, width=300)

    tkinter.Label(window5, text="Default values would be assigned to empyt fields", fg="navy", bg="lightblue").place(x=180, y=220, width=400)

    tkinter.Label(window5, text = "Split dataset into training and testing:").place(x=60, y=270, width=200)

    chkbtn1 = IntVar()
    chkbtn2 = IntVar()

    ckbt1 = tkinter.Checkbutton(window5, text="Yes", variable = chkbtn1, fg="black", bg="skyblue1")
    ckbt1.place(x=330, y=270, width=50)

    ckbt2 = tkinter.Checkbutton(window5, text="No", variable = chkbtn2, fg="black", bg="skyblue1")
    ckbt2.place(x=270, y=270, width=50)

    tkinter.Label(window5, text = "Enter split percentage").place(x=400, y=255, width=320)
    split_percent = tkinter.Entry(window5)
    split_percent.place(x=400, y=275, width=320)

    def submit():
        print('submit')
        if chkbtn1.get():
            print('Yes')
            split_data = 'y'

        elif chkbtn2.get():
            print('No')
            split_data = ''
        else:
            print('default')
            split_data = 'y'

        parameters = path1.get(), path2.get(), batch.get(), img_dim.get(), gpu.get(), svm_name.get(), split_percent.get(), split_data
        print(parameters)
        # mode = 'w'
        get_f = final_sotware.train(parameters)

        if get_f == 1:
            tkinter.messagebox.showinfo("Title", "Training Completed")

    btn9 = tkinter.Button(window5, text = "Train Model", fg = "black", bg = 'lawn green', command = submit)
    btn9.place(x=350, y=320, width=120)

    btn9 = tkinter.Button(window5, text = "EXIT", fg = "black", bg = 'tomato', command = s_exit)
    btn9.place(x=480, y=320, width=60)

    def home():
        window5.destroy()
        gotohome()

    btn10 = tkinter.Button(window5, text = "HOME", fg = "black", bg = 'turquoise1', command = home)
    btn10.place(x=250, y=320, width=90)

    window5.mainloop()

def show_test():

    window6 = Tk()
    window6.title("Attendance System")
    window6.geometry("800x400")
    tkinter.Label(window6, text = "WELCOME TO FACE RECOGNITION ATTENDANCE SOFTWARE", fg="black", bg="snow4").pack(fill="x")
    tkinter.Label(window6, text="\n").pack(fill='y')

    tkinter.Label(window6, text = "path to classifier.pkl").place(x=60, y=50, width=300)
    path1 = tkinter.Entry(window6)
    path1.place(x=60, y=70, width=300)

    tkinter.Label(window6, text = "path to 20180402-114759 Folder").place(x=60, y=100, width=300)
    path2 = tkinter.Entry(window6)
    path2.place(x=60, y=120, width=300)

    tkinter.Label(window6, text="path to dataset folder").place(x=60, y=150, width=300)
    path3 = tkinter.Entry(window6)
    path3.place(x=60, y=170, width=300)

    tkinter.Label(window6, text="batch size of images to process at once").place(x=420, y=50, width=300)
    batch = tkinter.Entry(window6)
    batch.place(x=420, y=70, width=300)

    tkinter.Label(window6, text="input image dimension (eg. 160)").place(x=420, y=100, width=300)
    img_dim = tkinter.Entry(window6)
    img_dim.place(x=420, y=120, width=300)

    tkinter.Label(window6, text="Default values would be assigned to empyt fields", fg="navy", bg="lightblue").place(x=180, y=240, width=400)

    def submit():
        gpu = 0.8
        parameters = path1.get(), path2.get(), path3.get(), batch.get(), img_dim.get(), gpu
        print(parameters)
        get_f = final_sotware.test(parameters = parameters)

        if get_f == 1:
            tkinter.messagebox.showinfo("Title", "Training Completed")

    btn9 = tkinter.Button(window6, text = "Test Model", fg = "black", bg = 'turquoise1', command = submit)
    btn9.place(x=350, y=320, width=120)

    btn9 = tkinter.Button(window6, text = "EXIT", fg = "black", bg = 'tomato', command = s_exit)
    btn9.place(x=480, y=320, width=90)

    def home():
        window6.destroy()
        gotohome()

    btn10 = tkinter.Button(window6, text = "HOME", fg = "black", bg = 'turquoise1', command = home)
    btn10.place(x=250, y=320, width=90)

    window6.mainloop()

def gotohome():
  show()

if __name__ == '__main__':
    show()
