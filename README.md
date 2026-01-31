# Developers.FM 

## 1. Project Overview

**Developers.FM** is a simplified clone of the popular Ask.fm platform. The system allows users to ask and answer questions, either publicly or anonymously, with support for threaded discussions. The project was implemented using **Django + SQLite** 

---

## 2. Technologies Used

### Backend

* **Django**
* **SQLite** 
* Django Authentication System
* Django ORM

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Django Templates Engine**

---

## 3. System Features

### 3.1 Authentication & Authorization

* User **Sign Up** (name, username, email, password)
* User **Login / Logout**
* Each user can choose whether to **allow anonymous questions**

---

### 3.2 User Operations

* View questions:

  * Questions **sent by you**
  * Questions **sent to you**
  * **Feed questions** (answered questions from other users)
* Ask questions (anonymous or not)
* Answer questions
* Delete questions

---

### 3.3 Questions & Threads System

* Each question has a **system-generated unique ID**
* Questions can act as **parent questions (threads)**
* If a question is answered, other users can ask follow-up questions in the same thread
* Deleting a parent question deletes the entire thread

---

## 4. System Architecture

### 4.1 MVC Pattern (Django – MVT)

* **Models**: Define database structure (User, Question)
* **Views**: Handle business logic and request processing
* **Templates**: Render dynamic HTML pages using Django Templates

---

### 4.2 Database Design

<img width="851" height="376" alt="Untitled (6)" src="https://github.com/user-attachments/assets/b993a11c-90eb-4cfc-a09d-0efec5662e2e" />

---


# ⚙️ Setup Instructions

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Linux / macOS)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# install staticfiles folder
python manage.py collectstatic --noinput

# Run development server
python manage.py runserver
```
