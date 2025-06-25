# 👤 GitHub Profile Viewer using Python-Tkinter & GitHub API

A feature-rich GUI application built in **Python Tkinter** that fetches and displays GitHub profile data and repositories in real-time using the **GitHub REST API**. Designed with both functionality and aesthetics in mind – this tool brings GitHub insights directly to your desktop.

---

## 🚀 Features

- 🔍 **Live GitHub Profile Lookup**
  - Enter a GitHub username to retrieve profile details like:
    - Name, Bio, Location
    - Number of Repositories, Followers, Following

- 🖼️ **Profile Picture Fetching**
  - Fetches and displays the user’s GitHub avatar using `PIL`

- 🌐 **View Repositories**
  - Opens a scrollable window listing all public repositories
  - Shows star & fork count with links to visit repositories

- 🌓 **Dark/Light Theme Toggle**
  - Toggle between professional light and dark UI modes

- 🔗 **Visit GitHub in Browser**
  - Buttons to directly visit the user’s GitHub profile or repos

- 🛡️ **Exception Handling**
  - Handles invalid usernames, API failures, and user errors smoothly

---

## 🛠 Tech Stack

- Python  
- Tkinter  
- GitHub REST API  
- Pillow (PIL)  
- Requests  
- Webbrowser

---

## 💡 Learning Highlights

- Working with RESTful APIs in Python  
- Image handling using `Pillow`  
- GUI theming (dark/light toggle)  
- Real-time data fetching and dynamic layout rendering  
- Scrollable secondary windows and nested UI design

## ✅ Note
> 📌 No authentication or token needed for basic GitHub API usage. However, GitHub imposes rate limits on unauthenticated requests. For larger-scale usage, consider using a GitHub Personal Access Token.
