# **GreatKart – Django-Based eCommerce Platform** 🛒

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-3.2-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## **Overview** 🌟

**GreatKart** is a comprehensive eCommerce platform developed using the **Django framework**. It offers a robust and scalable solution for online retail, featuring a user-friendly interface, secure payment integration, and a range of functionalities to manage products, orders, and customer interactions efficiently.

---

## **Features** 🚀

- **User Authentication**: Secure login and registration system.
- **Product Management**: Add, update, and categorize products.
- **Shopping Cart**: Add, remove, and update product quantities.
- **Order Management**: Process and track customer orders.
- **Payment Integration**: Secure payment gateway for transactions.
- **Admin Dashboard**: Manage products, orders, and users.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

## **Technologies Used** 🛠️

| Feature             | Technology       |
|---------------------|------------------|
| Backend             | Python, Django   |
| Frontend            | HTML, CSS, JavaScript |
| Database            | SQLite (default), PostgreSQL |
| Payment Gateway     | Paypal           |
| Deployment          | Heroku           |

---

## **Installation** 💾

### **Clone the Repository**

```bash
git clone https://github.com/Girishiam/GreatKart.git
cd GreatKart
Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Apply Migrations
bash
Copy
Edit
python manage.py migrate
Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
Run the Development Server
bash
Copy
Edit
python manage.py runserver
Access the application at http://127.0.0.1:8000/ in your web browser.

Project Structure 📂
php
Copy
Edit
GreatKart/
│
├── accounts/           # User authentication and profiles
├── cart/               # Shopping cart functionality
├── category/           # Product categories
├── orders/             # Order processing and management
├── static/             # Static files (CSS, JavaScript, images)
├── templates/          # HTML templates
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
