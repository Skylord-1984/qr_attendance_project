# SmartAttend – QR Code Based Smart Attendance System

SmartAttend is a Django-based attendance management system designed to simplify classroom attendance using dynamically generated QR codes.

The project aims to reduce manual attendance work and make attendance recording faster and more reliable.

## 🎯 Project Objectives

- Simplify classroom attendance.
- Reduce manual attendance management.
- Generate time-limited QR codes.
- Allow students to mark attendance using smartphones.
- Prevent duplicate attendance submissions.

## 🛠️ Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** To be finalized
- **QR Code:** Python QR Code Library
- **Version Control:** Git & GitHub

## ✨ Planned Features

- Teacher and student authentication.
- Teacher dashboard.
- Dynamic QR code generation.
- QR code expiration and validation.
- Student attendance submission.
- Duplicate attendance prevention.
- Attendance records and reports.

## 📂 Project Structure

```text
qr_attendance_project/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── decorators.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── dashboard.html
│   └── registration/
│       └── login.html
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## 🚀 Project Status

Currently under development.

This repository contains the initial Django project setup. Features will be implemented incrementally.

## 🔒 Security

- Environment variables are used for sensitive configuration.
- `.env` files are excluded from Git tracking.
- Authentication and attendance validation will be implemented with security in mind.

## 👨‍💻 Developer

**Sachin Bharti**

GitHub: [@Skylord-1984](https://github.com/Skylord-1984)

---

*SmartAttend – Making classroom attendance smarter.*
