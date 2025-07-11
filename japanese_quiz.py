import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random

normal_font = ("Comic Sans MS", 45, "bold")

class app(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("kanji_quiz")
    self.geometry("1920x1000")
    self.state("zoomed")
    self.main_frame = main_frame(self, bg="red", width=1920, height=1000)
    self.main_frame.pack()

class main_frame(tk.Frame):
  def __init__(self, master=None, *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self.start_btn = tk.Button(self, text="start", command=self.start, width=20, height=3, bg="grey22",
                              font=normal_font)
    self.start_btn.place(x=600, y=200)
    
    self.quit_btn = tk.Button(self, width=20, height=3, command=self.master.quit, bg="grey12", 
                              font=normal_font, text="quit")
    self.quit_btn.place(x=600, y=700)
  def start(self):
    self.master.game_frame = game_frame(self, width=1920, height=1000, bg="blue")
    self.master.game_frame.pack()
    game_frame.set_choices(self.master.game_frame)

class game_frame(tk.Canvas):
  def __init__(self, master, *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    diction_copy = diction.copy()
    random_kanji = random.choice(diction_copy)
    diction_copy.remove(random_kanji)
    
    self.count = 0
    self.question_number = 0
    
    self.pause_btn = tk.Button(self, text="||", width=5, height=2, bg="grey12", command=self.destroy,
                              font=("Ariel", 30, "bold"))
    self.pause_btn.place(x=50, y=50)
    
    self.score = tk.Label(self, width=10, height=2, bg="snow", font=normal_font,
                          text=f"{self.count}/{self.question_number}")
    self.score.place(x=800, y=100)
    
    self.quest_lbl = tk.Label(self, bg="grey12", width=3, height=1, font=("Comic Sans MS", 60, "bold"),
                              fg="white")
    self.quest_lbl.place(x=900, y=450)
    
    self.a_frame = tk.Frame(self, width=960, height=500)
    self.a_frame.pack_propagate(False)
    self.a_button = ctk.CTkButton(self.a_frame, bg_color="grey12", width=15, height=3, font=normal_font,
            text=None, corner_radius=200)
    self.a_lbl = tk.Label(self.a_frame, width=400, height=50, font=normal_font)
    self.a_frame.place(x=0, y=0)
    self.a_button.pack()
    self.a_lbl.pack()
    
    self.b_frame = tk.Frame(self, width=960, height=500)
    self.b_frame.pack_propagate(False)
    self.b_button = ctk.CTkButton(self.b_frame, bg_color="grey12", width=15, height=3, font=normal_font,
            text=None, corner_radius=200)
    self.b_lbl = tk.Label(self.b_frame, width=400, height=50, font=normal_font)
    self.b_frame.place(x=960, y=0)
    self.b_button.pack()
    self.b_lbl.pack()
    
    self.c_frame = tk.Frame(self, width=960, height=500)
    self.c_frame.pack_propagate(False)
    self.c_button = ctk.CTkButton(self.c_frame, bg_color="grey12", width=15, height=3, font=normal_font,
            text=None, corner_radius=200)
    self.c_lbl = tk.Label(self.c_frame, width=400, height=50, font=normal_font)
    self.c_frame.place(x=0, y=500)
    self.c_button.pack()
    self.c_lbl.pack()
    
    self.d_frame = tk.Frame(self, width=960, height=500)
    self.d_frame.pack_propagate(False)
    self.d_button = ctk.CTkButton(self.d_frame, bg_color="grey12", width=15, height=3, font=normal_font,
            text=None, corner_radius=200)
    self.d_lbl = tk.Label(self.d_frame, width=400, height=50, font=normal_font)
    self.d_frame.place(x=960, y=500)
    self.d_button.pack()
    self.d_lbl.pack()
  
  def answer_effect(self):
    self.question_number += 1
    self.score.configure(text=f"{self.count}/{self.question_number}")
    for i in [self.a_lbl, self.b_lbl, self.c_lbl, self.d_lbl]:
      if i.cget("text") == f"{self.the_right_answer.get()}":
        i.configure(bg="green")
        self.master.master.update()
      else:
        i.configure(bg="red")
        self.master.master.update()
    self.after(1000, self.set_choices())
  
  def set_choices(self):
      diction_copy = diction.copy()
      random_kanji = random.choice(diction_copy)
      self.quest_lbl.configure(text=f"{random_kanji["name"]}")
      diction_copy.remove(random_kanji)
      buttons_list = [self.a_frame, self.b_frame, self.c_frame, self.d_frame]
      for i in buttons_list:
        i.winfo_children()[1].configure(background="white")
      self.true_answer = random.choice(buttons_list)
      self.true_answer.winfo_children()[0].configure(command=self.true_answer_command,
            image=f"{random_kanji["meaning"][random.choice(list(random_kanji["meaning"].keys()))]}",
            width=960, height=400)
      self.true_answer.winfo_children()[1].configure(text=f"{random.choice(list(random_kanji["meaning"].keys()))}")
      buttons_list.remove(self.true_answer)
      self.the_right_answer = tk.StringVar(self,
            f"{self.true_answer.winfo_children()[1].cget("text")}")
      decoys_list = buttons_list
      for i in decoys_list:
        random_kanji2 = random.choice(diction_copy)
        i.winfo_children()[0].configure(command=self.answer_effect,
                    image=f"{random_kanji2["meaning"][random.choice(list(random_kanji2["meaning"].keys()))]}",
                    width=960, height=400)
        i.winfo_children()[1].configure(text=f"{random.choice(list(random_kanji2["meaning"].keys()))}")
        diction_copy.remove(random_kanji2)
      self.quest_lbl.lift()
      self.score.lift()
      self.pause_btn.lift()
  def true_answer_command(self):
    self.count += 1
    self.answer_effect()


if __name__ == "__main__":
    myapp = app()
    from kanji_list import diction
    myapp.bind("<q>", quit)
    myapp.mainloop()
