import Tkinter, time

root = Tkinter.Tk()
root.geometry("1100x700") #tkinter sucks
root.resizable(False,False)

file_text = open("README.md", 'r').read()

sections = []
for line in file_text.split("\n"):
    if line[:2] == "##":
        sections.append(line)

text = Tkinter.Text(root)
text.pack(fill='both', side='left')
text.insert('1.0', file_text)

last_cb_data = ""
last_cb_url = ""
last_cb_text = ""

def format_entry(text, url):
    proj_name = url.split('/')[-1]
    return "- ["+proj_name+"]("+url+") - "+text.strip()

def insert_entry(section):
    lines = text.get("1.0", "end").split("\n")
    section_start = 0
    for line in lines:
        if section in line:
            break
        section_start+=1
    section_end = section_start+1
    for i in range(section_start+1, len(lines)):
        if lines[i][:2] == "##":
            section_end = i-1
            break
    lines.insert(section_end, format_entry(last_cb_text, last_cb_url))
    text.delete(1.0,'end')
    text.insert('1.0', '\n'.join(lines))

entry_label = Tkinter.Label(root, text="waiting clipboard data... ")
entry_label.pack()

for section in sections:
    button = Tkinter.Button(root, text="Add to"+section[2:], command= lambda s=section: insert_entry(s))
    button.pack()

Tkinter.Button(root, text="SAVE CHANGES", command=lambda: open("README.md", 'w').write(text.get("1.0", "end"))).pack()

def is_url(text):
    if ("github.com" in text):
        return True
    return False

while True:
    try:
        cur_cb_data = root.clipboard_get()
        if cur_cb_data != last_cb_data:
            if is_url(cur_cb_data):
                last_cb_url = cur_cb_data
            else:
                last_cb_text = cur_cb_data
            last_cb_data = cur_cb_data

        cur_entry = format_entry(last_cb_text, last_cb_url)

        entry_label["text"] = "Current Text:\n" + last_cb_text +\
                              "\nCurrent URL:\n" + last_cb_url +\
                              "\nCurrent Entry:\n" + cur_entry
    except:
        pass
    
    root.update_idletasks()
    root.update()
    time.sleep(0.05)
