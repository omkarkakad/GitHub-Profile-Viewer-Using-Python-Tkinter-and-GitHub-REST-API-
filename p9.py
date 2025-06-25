from tkinter import *
from tkinter.messagebox import *
import requests
from PIL import Image, ImageTk
import io
import webbrowser


theme_mode="light"

root=Tk()
root.geometry("800x800+300+20")
root.title("👤 GitHub Profile Viewer")
root.configure(bg="linen")
f=("Arial",30,"bold")

# title
lab_title=Label(root,text="👤 GitHub Profile Viewer",font=f,bg="black",fg="white")
lab_title.pack(fill=X)

#Search Frame
frame=Frame(root,bg="white",bd=2,relief=SOLID)
frame.pack(padx=30,pady=15,fill=X)
lab_search=Label(frame,text="Enter GitHub Username:",font=("Arial",22,"bold"),bg="white")
lab_search.grid(row=0,column=0,padx=10,pady=15)
ent_search=Entry(frame,font=("Arial",22,"bold"),relief=SOLID)
ent_search.grid(row=0,column=1,padx=10,pady=15)


#Defining theme or toggle button
def toggle_theme():
	global theme_mode
	theme_mode="dark" if theme_mode=="light" else "light"

	if theme_mode=="dark":
		root.config(bg="#1e1e1e")
		frame.config(bg="#2d2d2d")
		lab_title.config(bg="#111", fg="white")
		lab_search.config(bg="#2d2d2d", fg="white")
		ent_search.config(bg="#3c3c3c", fg="white", insertbackground="white")
		info_label.config(bg="#1e1e1e", fg="white")
		img_label.config(bg="#1e1e1e")
		btn_frame.config(bg="#1e1e1e")
		btn2_frame.config(bg="#1e1e1e")
	else:
		root.config(bg="linen")
		frame.config(bg="white")
		lab_title.config(bg="black", fg="white")
		lab_search.config(bg="white", fg="black")
		ent_search.config(bg="white", fg="black", insertbackground="black")
		info_label.config(bg="linen", fg="black")
		img_label.config(bg="linen")
		btn_frame.config(bg="linen")
		btn2_frame.config(bg="linen")

#Defining Profile infrmation
def fetch_profile():
	username=ent_search.get().strip()
	if not username:
		showerror("Input error","Please ener a GitHub Username")
	url= f"https://api.github.com/users/{username}"	
	try:

		res=requests.get(url)	
		if res.status_code != 200:
			raise Exception("User not Found")
		data=res.json()

		name=data.get("name","N/A")
		bio=data.get("bio","N/A")
		location=data.get("location","N/A")
		public_repos=data.get("public_repos",0)
		followers=data.get("followers",0)
		following=data.get("following",0)
		info_var.set(f"👤 Name: {name}\n📝 Bio: {bio}\n📍 Location: {location}\n📦 Repos: {public_repos}\n👥 Followers: {followers} | Following: {following}")

		avatar_url=data.get("avatar_url")
		img_data=requests.get(avatar_url).content
		img = Image.open(io.BytesIO(img_data))
		img = img.resize((140, 160))
		photo = ImageTk.PhotoImage(img)
		img_label.config(image=photo)
		img_label.image = photo

	except Exception as e:
		showerror("Error",str(e))
		info_var.set("")
		img_label.config(image="")
		
#Button1Frame
btn_frame=Frame(root,bg="linen",bd=2)
btn_frame.pack(pady=10,fill=X)
theme_btn = Button(btn_frame, text="Toggle", bg="purple", fg="white", width=8, font=("Arial", 20, "bold"),command=toggle_theme)
theme_btn.pack(side=LEFT, padx=150)
search_btn = Button(btn_frame, text="Search", bg="green", fg="black", width=8, font=("Arial", 20, "bold"),command=fetch_profile)
search_btn.pack(side=LEFT, padx=30)

#Profile image
img_label=Label(root,bg="linen",relief=SOLID)
img_label.pack(pady=25)


#Profile information
info_var=StringVar()
info_label=Label(root,textvariable=info_var,font=("Arial",15),bg="linen",fg="black",justify=LEFT)
info_label.pack(pady=10)

#fetching repositories
def fetch_repositories():
	username=ent_search.get().strip()
	if not username:
		showerror("Input error","Please ener a GitHub Username first")
		return

	try:
		url= f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"	
		res=requests.get(url)	
		if res.status_code != 200:
			raise Exception("Fail to fetch repositories")
		repos=res.json()

		#Creating new window
		repo_win=Toplevel(root)
		repo_win.title(f"{username}'s Repositories")
		repo_win.geometry("700x500+250+100")
		repo_win.configure(bg="linen")

		canvas = Canvas(repo_win, bg="white")
		scrollbar = Scrollbar(repo_win, orient=VERTICAL, command=canvas.yview)
		inner_frame = Frame(canvas, bg="white")

		inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
		canvas.create_window((0, 0), window=inner_frame, anchor="nw")
		canvas.configure(yscrollcommand=scrollbar.set)

		canvas.pack(side=LEFT, fill=BOTH, expand=True)
		scrollbar.pack(side=RIGHT, fill=Y)

		for repo in repos:
			name=repo.get("name")
			stars=repo.get("stargazers_count",0)
			forks = repo.get("forks_count", 0)
			repo_url = repo.get("html_url")
			f = Frame(inner_frame, bg="white", bd=1, relief=SOLID)
			f.pack(fill=X, padx=10, pady=5)

			Label(f, text=f"🔹 {name}", font=("Arial", 14, "bold"), bg="white").pack(anchor="w")
			Label(f, text=f"⭐ Stars: {stars}   🍴 Forks: {forks}", font=("Arial", 10), bg="white").pack(anchor="w")
			Button(f, text="View Repo", bg="#0366d6", fg="white", font=("Arial", 10, "bold"),command=lambda url=repo_url: webbrowser.open(url)).pack(anchor="e", padx=5, pady=5)

	except Exception as e:
		showerror("Error", f"Failed to fetch repositories.\n{e}")

def open_profile():
	username = ent_search.get().strip()
	if username:
		webbrowser.open(f"https://github.com/{username}")
	else:
		showerror("Input error", "Please enter a GitHub username first.")	


#Button2Frame
btn2_frame=Frame(root,bg="linen",bd=2)
btn2_frame.pack(side=BOTTOM,fill=X,pady=70)
repo_btn = Button(btn2_frame, text="Visit Repositories", bg="black", fg="red", width=15, font=("Arial", 20, "bold"),command=fetch_repositories)
repo_btn.pack(side=LEFT, padx=90)
git_btn = Button(btn2_frame, text="Visit GitHub Profile", bg="black", fg="red", width=16, font=("Arial", 20, "bold"), command=open_profile)
git_btn.pack(side=LEFT, padx=10)
root.mainloop()


