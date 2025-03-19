📝 Task Management API
A Django REST Framework-based Task Management API that allows users to create, update, retrieve, and delete tasks with advanced filtering, pagination, and custom permissions.

🚀 Project Overview
This Task Management API is designed to help users manage their tasks efficiently. Key features include:

✅ CRUD Operations — Create, Read, Update, Delete tasks.
✅ Custom Permissions — Admins can view all tasks; regular users can only view and manage their own tasks.
✅ Token Authentication — Ensures secure access to the API.
✅ Filtering — Filter tasks by completion status and date ranges.
✅ Pagination — Efficient data handling with paginated results.
✅ Admin Panel — Full control over users and tasks for admin users.

📂 Project Structure
markdown
Copy
Edit
/TaskManager
├── /tasks
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── /TaskManager
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
### 📄 **README.md - Task Management API**

---

# 📝 **Task Management API**
A Django REST Framework-based Task Management API that allows users to create, update, retrieve, and delete tasks with advanced filtering, pagination, and custom permissions.

---

## 🚀 **Project Overview**
This Task Management API is designed to help users manage their tasks efficiently. Key features include:  

✅ **CRUD Operations** — Create, Read, Update, Delete tasks.  
✅ **Custom Permissions** — Admins can view all tasks; regular users can only view and manage their own tasks.  
✅ **Token Authentication** — Ensures secure access to the API.  
✅ **Filtering** — Filter tasks by completion status and date ranges.  
✅ **Pagination** — Efficient data handling with paginated results.  
✅ **Admin Panel** — Full control over users and tasks for admin users.

---

## 📂 **Project Structure**
```
/TaskManager
├── /tasks
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── /TaskManager
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ **Setup Instructions**

### 🔹 **1. Clone the Repository**
```bash
git clone <repository-url>
cd TaskManager
```

---

### 🔹 **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate       # (Linux/Mac)
venv\Scripts\activate          # (Windows)
```

---

### 🔹 **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### 🔹 **4. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🔹 **5. Create a Superuser**
```bash
python manage.py createsuperuser
```

---

### 🔹 **6. Run the Server**
```bash
python manage.py runserver
```

---

### 🔹 **7. Generate Tokens for Users**
In Django shell:

```bash
python manage.py shell
```

```python
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Generate a token for a specific user
user = User.objects.get(username='admin')
token, created = Token.objects.get_or_create(user=user)
print(f'Admin Token: {token.key}')
```

✅ Use this token in your requests for authentication.

---

## 🌐 **API Endpoints Documentation**

### 🔐 **Authentication Endpoints**
| **Method** | **Endpoint**               | **Description** |
|:------------|:---------------------------|:-----------------|
| **POST**     | `/api/token/`              | Generate token for authentication |

✅ **Request Body:**
```json
{
    "username": "admin",
    "password": "password123"
}
```

✅ **Response:**
```json
{
    "token": "your_generated_token"
}
```

---

### 📋 **Task Management Endpoints**
| **Method** | **Endpoint**                   | **Description** |
|:------------|:---------------------------------|:-----------------|
| **GET**      | `/api/tasks/`                   | List tasks (Admin: All, Users: Their own tasks) |
| **POST**     | `/api/tasks/`                   | Create a new task (Authenticated users only) |
| **GET**      | `/api/tasks/{id}/`              | Retrieve details of a specific task |
| **PUT/PATCH**| `/api/tasks/{id}/`              | Update a task (Only task creator) |
| **DELETE**   | `/api/tasks/{id}/`              | Delete a task (Only task creator) |

---

### 🔎 **Task Filtering Endpoints**
| **Filter Type** | **Example Endpoint**                        | **Description** |
|:----------------|:--------------------------------------------|:-----------------|
| **Completed**    | `/api/tasks/?completed=true`                | Filter completed tasks |
| **Created Date** | `/api/tasks/?created_after=2024-01-01`      | Filter tasks created after Jan 1, 2024 |
| **Updated Date** | `/api/tasks/?updated_after=2024-01-01`      | Filter tasks updated after Jan 1, 2024 |

✅ **Combine Filters Example:**  
```
/api/tasks/?completed=true&created_after=2024-01-01
```

---

### 📄 **Pagination**
| **Page Navigation** | **Example Endpoint**          | **Description** |
|:--------------------|:------------------------------|:-----------------|
| **Page 1**           | `/api/tasks/?page=1`           | Displays the first 10 tasks |
| **Page 2**           | `/api/tasks/?page=2`           | Displays the next 10 tasks |

✅ **Custom Page Size:**  
```
/api/tasks/?page=1&page_size=5
```

---

### 🔐 **Admin Access**
- Admin users can log in via the **Django Admin Panel**.  
➡️ **URL:** `/admin/`  
➡️ Use your **superuser** credentials.  

---

## 🔎 **Testing Your API**
You can test the endpoints using:  
✅ **Postman**  
✅ **cURL**  
✅ **Django Browsable API**  

### 🔹 **Sample POST Request Using Postman**
**URL:** `/api/tasks/`  
**Headers:**
```
Authorization: Token <your_token>
Content-Type: application/json
```

**Body:**
```json
{
    "title": "Complete API Documentation",
    "description": "Write clear documentation for endpoints.",
    "completed": false
}
```

✅ **Expected Response:**
```json
{
    "id": 1,
    "title": "Complete API Documentation",
    "description": "Write clear documentation for endpoints.",
    "completed": false,
    "created_by": 1
}
```

---

## 🔎 **Testing Admin vs Regular User Access**
| **Action**         | **Admin** | **Regular User** |
|:-------------------|:---------:|:-----------------:|
| **View All Tasks**  | ✅ Allowed | ❌ Only their own |
| **Update Tasks**    | ✅ Allowed | ❌ Only their own |
| **Delete Tasks**    | ✅ Allowed | ❌ Only their own |

---

## 📜 **Key Features**
✅ Admins can view **all tasks**.  
✅ Regular users can only view **their own tasks**.  
✅ Users can filter tasks by **completed status** or **date range**.  
✅ Pagination ensures efficient data handling.  
✅ Token Authentication ensures secure access.  



## 🚀 **Final Checklist**
✅ Clear project structure.  
✅ Detailed `README.md`.  
✅ Fully working endpoints.  
✅ Added test cases for robustness.  
✅ Project deployed or ready for submission.  

