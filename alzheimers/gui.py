import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pickle
from PIL import Image, ImageTk
import os

# ================= LOAD MODEL =================
with open("alzheimer_model.pkl", "rb") as f:
    model = pickle.load(f)

USERS_FILE = "users.txt"

# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("Alzheimer System Login")
root.geometry("500x500")
root.config(bg="#0D47A1")

# ================= TITLE =================
title = tk.Label(root,
                 text="ALZHEIMER DETECTION SYSTEM",
                 font=("Arial", 18, "bold"),
                 bg="#0D47A1",
                 fg="white")
title.pack(pady=20)

# ================= MAIN FRAME =================
main_frame = tk.Frame(root, bg="white", bd=3, relief="solid")
main_frame.pack(pady=20, ipadx=20, ipady=20)

# ================= BUTTONS =================
btn_frame = tk.Frame(main_frame, bg="white",bd=3, relief="solid")
btn_frame.pack(pady=10)

def show_register():
    login_frame.pack_forget()
    reset_frame.pack_forget()
    register_frame.pack()

def show_login():
    register_frame.pack_forget()
    reset_frame.pack_forget()
    login_frame.pack()

def show_reset():
    login_frame.pack_forget()
    register_frame.pack_forget()
    reset_frame.pack()

tk.Button(btn_frame, text="Register", width=15, command=show_register,bd=3, relief="solid",font=("arial",20),bg="green",fg="white").grid(row=0,column=0,padx=5)
tk.Button(btn_frame, text="Login", width=15, command=show_login,bd=3, relief="solid",font=("arial",20),bg="blue",fg="white").grid(row=0,column=1,padx=5)
tk.Button(btn_frame, text="Reset", width=15, command=show_reset,bd=3, relief="solid",font=("arial",20),bg="orange",fg="white").grid(row=0,column=2,padx=5)

# ================= REGISTER =================
register_frame = tk.Frame(main_frame, bg="white",relief="solid",bd=3)

tk.Label(register_frame,text="Username",bg="white",font=("arial",20,"bold")).pack()
reg_user = tk.Entry(register_frame,relief="solid",bd=3,bg="yellow",font=("arial",20,"bold"),width=15)
reg_user.pack()

tk.Label(register_frame,text="Password",bg="white",font=("arial",20,"bold")).pack()
reg_pass = tk.Entry(register_frame, show="*",relief="solid",bd=3,bg="yellow",width=15,font=("arial",20,"bold"))
reg_pass.pack()

def register():
    u = reg_user.get()
    p = reg_pass.get()

    if u == "" or p == "":
        messagebox.showerror("Error","Fill all fields")
        return

    with open(USERS_FILE,"a") as f:
        f.write(u+","+p+"\n")

    messagebox.showinfo("Success","Registered Successfully")

tk.Button(register_frame,text="Register",bg="green",fg="white",command=register).pack(pady=10)

register_frame.pack()

# ================= LOGIN =================
login_frame = tk.Frame(main_frame, bg="white",relief="solid",bd=3)

tk.Label(login_frame,text="Username",bg="white",font=("arial",20,"bold")).pack()
log_user = tk.Entry(login_frame,width=15,relief="solid",bd=3,bg="green",fg="white",font=("arial",20,"bold"))
log_user.pack()

tk.Label(login_frame,text="Password",bg="white",font=("arial",20,"bold")).pack()
log_pass = tk.Entry(login_frame, width=15,show="*",relief="solid",bd=3,bg="green",fg="white",font=("arial",20,"bold"))
log_pass.pack()

# ================= RESET =================
reset_frame = tk.Frame(main_frame, bg="white",relief="solid",bd=3)

tk.Label(reset_frame,text="Username",bg="white",font=("arial",20,"bold")).pack()
reset_user = tk.Entry(reset_frame,width=15,relief="solid",bd=3,bg="red",fg="white",font=("arial",20,"bold"))
reset_user.pack()

tk.Label(reset_frame,text="New Password",bg="white").pack()
reset_pass1 = tk.Entry(reset_frame, show="*",relief="solid",bd=3,bg="red",fg="white",font=("arial",20,"bold"),width=15)
reset_pass1.pack()

tk.Label(reset_frame,text="Confirm Password",bg="white",font=("arial",20,"bold")).pack()
reset_pass2 = tk.Entry(reset_frame, show="*",relief="solid",bd=3,bg="red",fg="white",font=("arial",20,"bold"),width=15)
reset_pass2.pack()

def reset_password():
    u = reset_user.get()
    p1 = reset_pass1.get()
    p2 = reset_pass2.get()

    if p1 != p2:
        messagebox.showerror("Error","Passwords do not match")
        return

    if not os.path.exists(USERS_FILE):
        return

    lines = open(USERS_FILE).readlines()
    with open(USERS_FILE,"w") as f:
        for line in lines:
            user,passw = line.strip().split(",")
            if user == u:
                f.write(u+","+p1+"\n")
            else:
                f.write(line)

    messagebox.showinfo("Success","Password Reset Successful")

tk.Button(reset_frame,text="Reset Password",bg="orange",fg="white",command=reset_password).pack(pady=10)

# ================= SECOND WINDOW =================
def open_main_system():

    root.withdraw()

    top = tk.Toplevel()
    top.title("Alzheimer Detection System")
    top.geometry("1100x600")
    top.config(bg="#E3F2FD")
    tk.Label(top,text="Early Alzheimer Disease Detection System",
                 font=("Arial",22,"bold"),
                 bg="#E3F2FD",
                 fg="#0D47A1").pack(pady=10)

    def on_close():
        top.destroy()
        root.deiconify()

    top.protocol("WM_DELETE_WINDOW", on_close)

    # ================= MAIN CONTAINER =================
    main_container = tk.Frame(top, bg="#E3F2FD")
    main_container.pack(pady=10)

    # ================= LEFT FRAME =================
    left = tk.Frame(main_container,
                    bg="#BBDEFB",
                    width=300,
                    height=450,
                    bd=3,
                    relief="solid")
    left.grid(row=0, column=0, padx=10)
    left.pack_propagate(False)

    tk.Label(left,text="Patient Details",
             bg="#BBDEFB",
             font=("Arial",14,"bold")).pack(pady=10)

    tk.Label(left,text="Age",bg="#BBDEFB",font=("arial",15)).pack()
    age_entry = tk.Entry(left,width=12,font=("arial",15),bg="yellow",fg="black",bd=3,relief="solid")
    age_entry.pack()

    tk.Label(left,text="Memory",bg="#BBDEFB",font=("arial",15)).pack()
    memory_entry = tk.Entry(left,width=12,font=("arial",15),bg="yellow",fg="black",bd=3,relief="solid")
    memory_entry.pack()

    tk.Label(left,text="Thinking",bg="#BBDEFB",font=("arial",15)).pack()
    thinking_entry = tk.Entry(left,width=12,font=("arial",15),bg="yellow",fg="black",bd=3,relief="solid")
    thinking_entry.pack()

    tk.Label(left,text="Decision",bg="#BBDEFB",font=("arial",15)).pack()
    decision_entry = tk.Entry(left,width=12,font=("arial",15),bg="yellow",fg="black",bd=3,relief="solid")
    decision_entry.pack()

    # ================= MIDDLE FRAME =================
    middle = tk.Frame(main_container,
                      bg="#E1BEE7",
                      width=300,
                      height=450,
                      bd=3,
                      relief="solid")
    middle.grid(row=0, column=1, padx=10)
    middle.pack_propagate(False)

    tk.Label(middle,text="MRI Scan",
             bg="#E1BEE7",
             font=("Arial",14,"bold")).pack(pady=10)

    image_label = tk.Label(middle,bg="#E1BEE7")
    image_label.pack(pady=20)

    # ================= RIGHT FRAME =================
    right = tk.Frame(main_container,
                     bg="white",
                     width=300,
                     height=450,
                     bd=3,
                     relief="solid")
    right.grid(row=0, column=2, padx=10)
    right.pack_propagate(False)

    tk.Label(right,text="Report",
             font=("Arial",14,"bold"),
             bg="white").pack()

    report_text = tk.Text(right)
    report_text.pack(expand=True, fill="both")

    # ================= FUNCTIONS =================
    mri_holder = {"path":""}

    def upload_mri():
        file = filedialog.askopenfilename(filetypes=[("Image","*.jpg *.png")])
        if file:
            mri_holder["path"] = file
            img = Image.open(file).resize((200,200))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img
            messagebox.showinfo("Success","MRI Uploaded")

    def predict_patient():
        age = float(age_entry.get())
        memory = float(memory_entry.get())
        thinking = float(thinking_entry.get())
        decision = float(decision_entry.get())

        data = [[age,memory,thinking,decision]]
        pred = model.predict(data)[0]

        if pred==1:
            result="Alzheimer Detected"
            risk="HIGH"
            advice="Consult Neurologist"
        else:
            result="Normal"
            risk="LOW"
            advice="Healthy Lifestyle"

        report=f"""
================================
        PATIENT REPORT
================================

Age           : {age}
Memory Score  : {memory}
Thinking      : {thinking}
Decision      : {decision}

Risk Level    : {risk}
Prediction    : {result}

Recommendation:
{advice}

================================
"""
        report_text.delete(1.0,tk.END)
        report_text.insert(tk.END,report)
        messagebox.showinfo("Success","Prediction Done")

    def predict_mri():
        if mri_holder["path"]=="":
            messagebox.showerror("Error","Upload MRI First")
            return

        img=Image.open(mri_holder["path"]).convert("L")
        pixels=list(img.getdata())
        avg=sum(pixels)/len(pixels)

        if avg<120:
            result="Alzheimer Detected"
            risk="HIGH"
        else:
            result="Normal"
            risk="LOW"

        report=f"""
================================
        MRI REPORT
================================

MRI Status : {result}
Risk Level : {risk}

================================
"""
        report_text.delete(1.0,tk.END)
        report_text.insert(tk.END,report)
        messagebox.showinfo("Success","MRI Predicted")

    def predict_dataset():
        file=filedialog.askopenfilename(filetypes=[("CSV","*.csv")])
        if file:
            df=pd.read_csv(file)
            X=df[['Age','Memory','Thinking','Decision']]
            preds=model.predict(X)

            total=len(preds)
            alz=sum(preds)
            normal=total-alz

            report=f"""
================================
        DATASET REPORT
================================

Total Patients : {total}
Alzheimer      : {alz}
Normal         : {normal}

================================
"""
            report_text.delete(1.0,tk.END)
            report_text.insert(tk.END,report)
            messagebox.showinfo("Success","Dataset Predicted")

    # ================= BUTTONS =================
    bottom = tk.Frame(top, bg="#E3F2FD")
    bottom.pack(pady=10)

    tk.Button(bottom,text="Upload MRI",bg="purple",fg="white",
              command=upload_mri,width=15,font=("arial",20)).grid(row=0,column=0,padx=5)

    tk.Button(bottom,text="Predict Patient",bg="green",fg="white",
              command=predict_patient,width=15,font=("arial",20)).grid(row=0,column=1,padx=5)

    tk.Button(bottom,text="Predict MRI",bg="blue",fg="white",
              command=predict_mri,width=15,font=("arial",20)).grid(row=0,column=2,padx=5)

    tk.Button(bottom,text="Dataset",bg="orange",fg="white",
              command=predict_dataset,width=15,font=("arial",20)).grid(row=0,column=3,padx=5)

    tk.Button(bottom,text="Exit",bg="red",fg="white",
              command=on_close,width=15,font=("arial",20)).grid(row=0,column=4,padx=5)

# ================= LOGIN =================
def login():
    u=log_user.get()
    p=log_pass.get()

    if not os.path.exists(USERS_FILE):
        return

    lines=open(USERS_FILE).readlines()
    for line in lines:
        user,passw=line.strip().split(",")
        if user==u and passw==p:
            messagebox.showinfo("Success","Login Success")
            open_main_system()
            return

    messagebox.showerror("Error","Invalid Login")

tk.Button(login_frame,text="Login",bg="blue",fg="white",
          command=login,font=("arial",20),width=12).pack(pady=10)

root.mainloop()