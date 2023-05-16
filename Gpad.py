import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("Gpad text editer")
main_application.wm_iconbitmap("icon.ico")


#--1--########################################## main menu ########################################
# ---------------------------------&&&&&&& End main menu &&&&&&&---------------------------
main_menu = tk.Menu(main_application)
# file icons
new_icon = tk.PhotoImage(file="ICONS/new icon1.png")
open_icon = tk.PhotoImage(file="ICONS/open icon1.png")
save_icon = tk.PhotoImage(file="ICONS/save icon1.png")
save_as_icon = tk.PhotoImage(file="ICONS/save as icon1.png")
exit_icon = tk.PhotoImage(file="ICONS/exit icon1.png")

file =tk.Menu(main_menu,tearoff=False)


# edit icons
cut_icon = tk.PhotoImage(file="ICONS/cut icon1.png")
copy_icon = tk.PhotoImage(file="ICONS/copy icon1.png")
paste_icon = tk.PhotoImage(file="ICONS/paste icon1.png")
clear_all_icon = tk.PhotoImage(file="ICONS/clear icon1.png")
find_icon = tk.PhotoImage(file="ICONS/find icon1.png")

edit =tk.Menu(main_menu,tearoff=False)


# view icon 
tool_bar_icon = tk.PhotoImage(file="ICONS/tool bar icon1.png")
status_bar_icon = tk.PhotoImage(file="ICONS/status bar icon1.png")

view =tk.Menu(main_menu,tearoff=False)



# colour icon
light_default_icon = tk.PhotoImage(file="ICONS/light default icon1.png")
light_plus_icon = tk.PhotoImage(file="ICONS/light plus icon1.png")
dark_icon = tk.PhotoImage(file="ICONS/dark icon1.png")
red_icon = tk.PhotoImage(file="ICONS/red icon1.png")
monokai_icon = tk.PhotoImage(file="ICONS/monokai icon1.png")
night_blue_icon = tk.PhotoImage(file="ICONS/night blue icon1.png")

colour_theme =tk.Menu(main_menu,tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict = {
  "Light Default" :("#000000","#ffffff"), #textcolor #background color
  "Light Plus" : ("#474747","#e0e0e0"),
  "Dark" : ("#c4c4c4","#2d2d2d"), 
  "Red" : ("#2d2d2d","#ffe8e8"),
  "Monokai" : ("#d3b774","#474747"),
  "Night Blue" : ("#ededed","#6b9dc2")
}



# casade
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Colour theme",menu=colour_theme)


#--2--########################################## Tool bar ########################################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_box["values"]= font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5)

# size box 
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=16,textvariable=size_var,state="readonly")
font_size["values"] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

# bold button
bold_icon = tk.PhotoImage(file="ICONS/bold icon1.png")
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

# underline button
underlined_icon = tk.PhotoImage(file="ICONS/underlined icon1.png")
underlined_btn = ttk.Button(tool_bar,image=underlined_icon)
underlined_btn.grid(row=0,column=3,padx=5)

# italic button
italic_icon = tk.PhotoImage(file="ICONS/italic icon1.png")
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=4,padx=5)

# font color button
font_color_icon = tk.PhotoImage(file="ICONS/font color icon1.png")
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)  

# left para button
left_para_icon = tk.PhotoImage(file="ICONS/left para icon1.png")
left_para_btn = ttk.Button(tool_bar,image=left_para_icon)
left_para_btn.grid(row=0,column=6,padx=5) 

# mid para button
mid_para_icon = tk.PhotoImage(file="ICONS/mid para icon1.png")
mid_para_btn = ttk.Button(tool_bar,image=mid_para_icon)
mid_para_btn.grid(row=0,column=7,padx=5)

# right para button
right_para_icon = tk.PhotoImage(file="ICONS/right para icon1.png")
right_para_btn = ttk.Button(tool_bar,image=right_para_icon)
right_para_btn.grid(row=0,column=8,padx=5)

# ---------------------------------&&&&&&& End Tool bar &&&&&&&---------------------------

#--3--########################################## text editor ########################################

text_editor = tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
current_font_family = "Arial"
current_font_size = 12

def change_font(event=None):
  global current_font_family
  current_font_family = font_family.get()
  text_editor.configure(font=(current_font_family,current_font_size))


def change_fontsize(event=None):
  global current_font_size
  current_font_size = size_var.get()
  text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_fontsize)

# buttons functionality
# bold bottun functionality
def change_bold():
  text_property = tk.font.Font(font=text_editor["font"])
  if text_property.actual()["weight"]=="normal":
    text_editor.configure(font=(current_font_family,current_font_size,"bold"))
  if text_property.actual()["weight"]=="bold":
    text_editor.configure(font=(current_font_family,current_font_size,"normal"))

bold_btn.configure(command=change_bold)

# italic bottun functionality
def change_italic():
  text_property = tk.font.Font(font=text_editor["font"])
  if text_property.actual()["slant"]=="roman":
    text_editor.configure(font=(current_font_family,current_font_size,"italic"))
  if text_property.actual()["slant"]=="italic":
    text_editor.configure(font=(current_font_family,current_font_size,"normal"))

italic_btn.configure(command=change_italic)

# underline bottun functionality
def change_underline():
  text_property = tk.font.Font(font=text_editor["font"])
  if text_property.actual()["underline"]==0:
    text_editor.configure(font=(current_font_family,current_font_size,"underline"))
  if text_property.actual()["underline"]==1:
    text_editor.configure(font=(current_font_family,current_font_size,"normal"))

underlined_btn.configure(command=change_underline)

# font color functionality
def change_fontcolor():
  color_var = tk.colorchooser.askcolor()
  text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_fontcolor)

# left para functionality
def left_para():
  text_content = text_editor.get(1.0,"end")
  text_editor.tag_config("left",justify=tk.LEFT)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,text_content,"left")

left_para_btn.configure(command=left_para)

# mid para functionality
def mid_para():
  text_content = text_editor.get(1.0,"end")
  text_editor.tag_config("center",justify=tk.CENTER)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,text_content,"center")

mid_para_btn.configure(command=mid_para)

# right para functionality
def right_para():
  text_content = text_editor.get(1.0,"end")
  text_editor.tag_config("right",justify=tk.RIGHT)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,text_content,"right")

right_para_btn.configure(command=right_para)



text_editor.configure(font=("Arial",12))


# ---------------------------------&&&&&&& End text editor &&&&&&&---------------------------


#--4--########################################## status bar ########################################

status_bar = ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(even=None):
  global text_changed
  if text_editor.edit_modified():
    text_changed = True
    words = len(text_editor.get(1.0,"end-1c").split())
    characters = len(text_editor.get(1.0,"end-1c"))           #.replace(" ","")
    status_bar.config(text=f"characters : {characters} words : {words}")
  text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",changed)


# ---------------------------------&&&&&&& End status bar &&&&&&&---------------------------


#--5--########################################## main menu functionality ##############################

# variable
url = ""
# new functinality
def new_file(event=None):
  global url
  url = ""
  text_editor.delete(1.0,tk.END)

# file command
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)

# open functinality 

def open_file(even=None):
  global url
  url = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("Text File","*.txt"),("All Files","*.*")))
  try:
    with open(url,"r") as fr:
      text_editor.delete(1.0,tk.END)
      text_editor.insert(1.0,fr.read())
  except FileNotFoundError:
    return
  else:
    return
  main_application.title(os.path.basename(url))

file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)

# save file functinality
def save_file(event=None):
  global url 
  try:
    if url:
      content = str(text_editor.get(1.0,tk.END))
      with open(url,"w",encoding="utf-8") as fw:
        fw.write(content)
    else:
      url = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("Text File","*.txt"),("All Files","*.*")))
      content2 = text_editor.get(1.0,tk.END)
      url.write(content2)
      url.close()
  except:
    return

file.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)

# save as functionality 
def save_as_file(event=None):
  global url
  try:
    content = text_editor.get(1.0,tk.END)
    url = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("Text File","*.txt"),("All Files","*.*")))
    url.write(content)
    url.close()
  except:
    return

file.add_command(label="Save as",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Z",command=save_as_file)

# exit functionality
def exit_func(event=None):
  global url,text_changed
  try:
    if text_changed:
      mbox = messagebox.askyesnocancel("Warning","Do you want to save the file ?")
      if mbox is True:
        if url:
          content = text_editor.get(1.0,tk.END)
          with open(url,"w",encoding="utf-8") as fw:
            fw.write(content)
            main_application.destroy()
        else:
          content2 = str(text_editor.get(1.0,tk.END))
          url = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("Text File","*.txt"),("All Files","*.*")))
          url.write(content2)
          url.close()
          main_application.destroy()
      elif mbox is False:
        main_application.destroy()
    else:
      main_application.destroy()
  except:
    return


file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Q",command=exit_func)

# find functionality

def find_func(event=None):
  def find():
    word = find_input.get()
    text_editor.tag_remove("match","1.0", tk.END)
    matches = 0
    if word:
      start_pos = "1.0"
      while True:
        start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
        if not start_pos:
          break
        end_pos = f"{start_pos}+{len(word)}c"
        text_editor.tag_add("match",start_pos,end_pos)
        matches +=1
        start_pos = end_pos
        text_editor.tag_config("match",foreground="red",background="yellow")

  def replace():
    word = find_input.get()
    replace_text = replace_input.get()
    content = text_editor.get(1.0,tk.END)
    new_content = content.replace(word,replace_text)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(1.0,new_content)


  find_dialogue = tk.Toplevel()
  find_dialogue.geometry("450x250+500+200")
  find_dialogue.title("Find")
  find_dialogue.resizable(0,0)

  # frame
  find_frame = ttk.LabelFrame(find_dialogue,text="Find/Replace")
  find_frame.pack(pady=20)

  # labels
  text_find_label = ttk.Label(find_frame,text="Find : ")
  text_replace_label = ttk.Label(find_frame,text="Replace") 

  # entry
  find_input = ttk.Entry(find_frame,width=30)
  replace_input = ttk.Entry(find_frame,width=30)

  # button 
  find_button = ttk.Button(find_frame,text="Find", command=find)
  replace_button = ttk.Button(find_frame,text="Replace", command=replace)

  # label grid
  text_find_label.grid(row=0,column=0,padx=4,pady=4)
  text_replace_label.grid(row=1,column=0,padx=4,pady=4)

  # entry grid
  find_input.grid(row=0,column=1,padx=4,pady=4)
  replace_input.grid(row=1,column=1,padx=4,pady=4)

  # buuton grid
  find_button.grid(row=2,column=0,padx=8,pady=4)
  replace_button.grid(row=2,column=1,padx=8,pady=4)

  find_dialogue.mainloop()


# edit command
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+C",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find_func)

# view checkbutton

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
  global show_toolbar
  if show_toolbar:
    tool_bar.pack_forget()
    show_toolbar = False
  else:
    text_editor.pack_forget()
    status_bar.pack_forget()
    tool_bar.pack(side=tk.TOP,fill=tk.X)
    text_editor.pack(fill=tk.BOTH,expand=True)
    status_bar.pack(side=tk.BOTTOM)
    show_toolbar = True

def hide_statusbar():
  global show_statusbar
  if show_statusbar:
    status_bar.pack_forget()
    show_statusbar = False
  else:
    status_bar.pack(side=tk.BOTTOM)
    show_statusbar = True


view.add_checkbutton(label="Tool bar",onvalue=True,offvalue=0,variable= show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="Status bar",onvalue=True,offvalue=0,variable= show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

# color theme
def change_theme():
  chosen_theme = theme_choice.get()
  color_tuple = color_dict.get(chosen_theme)
  fg_color,bg_color = color_tuple[0],color_tuple[1]
  text_editor.config(background=bg_color,foreground=fg_color)

count = 0
for i in color_dict:
  colour_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
  count +=1


# ---------------------------------&&&&&&& End main menu functionality &&&&&&&-----------------------

main_application.config(menu=main_menu)
# Bind short cut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-z>",save_as_file)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)
main_application.mainloop()

# ----------- ended by gurucharan ------------------------------------------------------------------
