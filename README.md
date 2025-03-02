---

# 📚 Online Kutubxona API 🚀

Welcome to the **Online Kutubxona API**! This project is a fully-featured REST API for managing an online library system. It allows you to manage authors, books, genres, book copies, and book lendings with ease. Built with **Django** and **Django REST Framework**, this API is designed to be simple, scalable, and developer-friendly.

---

## 🌟 Features

- **Authors Management** 📖
  - Create, read, update, and delete authors.
  - Get a list of all authors with pagination.
  - View the number of books written by each author.

- **Books Management** 📚
  - Add, update, and delete books.
  - Associate books with authors and genres.
  - View all copies of a specific book.

- **Book Copies Management** 📑
  - Track individual book copies.
  - Manage the condition and availability of each copy.

- **Book Lending Management** ⏳
  - Borrow and return books.
  - Track due dates and overdue books.

- **Pagination** 🔢
  - All list views support pagination for better performance.

---

## 🛠️ Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default), PostgreSQL (production-ready)
- **Tools**: Postman (for API testing), Git (version control)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework 3.14+

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/online-kutubxona-api.git
   cd online-kutubxona-api
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the API**:
   - Open your browser and go to `http://127.0.0.1:8000/api/`.

---

## 📄 API Documentation

### Endpoints

| Method | Endpoint                  | Description                          |
|--------|---------------------------|--------------------------------------|
| GET    | `/api/authors/`           | List all authors (paginated).        |
| POST   | `/api/authors/`           | Create a new author.                 |
| GET    | `/api/authors/<id>/`      | Retrieve a specific author.          |
| PUT    | `/api/authors/<id>/`      | Update a specific author.            |
| DELETE | `/api/authors/<id>/`      | Delete a specific author.            |
| GET    | `/api/books/`             | List all books (paginated).          |
| POST   | `/api/books/`             | Create a new book.                   |
| GET    | `/api/books/<id>/`        | Retrieve a specific book.            |
| PUT    | `/api/books/<id>/`        | Update a specific book.              |
| DELETE | `/api/books/<id>/`        | Delete a specific book.              |
| GET    | `/api/copies/`            | List all book copies (paginated).    |
| POST   | `/api/copies/`            | Create a new book copy.              |
| GET    | `/api/copies/<id>/`       | Retrieve a specific book copy.       |
| PUT    | `/api/copies/<id>/`       | Update a specific book copy.         |
| DELETE | `/api/copies/<id>/`       | Delete a specific book copy.         |
| GET    | `/api/lendings/`          | List all book lendings (paginated).  |
| POST   | `/api/lendings/`          | Create a new book lending.           |
| GET    | `/api/lendings/<id>/`     | Retrieve a specific book lending.    |
| PUT    | `/api/lendings/<id>/`     | Update a specific book lending.      |
| DELETE | `/api/lendings/<id>/`     | Delete a specific book lending.      |

---

## 🎨 Example Requests

### Create an Author
```bash
curl -X POST http://127.0.0.1:8000/api/authors/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Ernest",
  "last_name": "Hemingway",
  "bio": "American novelist...",
  "birth_date": "1899-07-21",
  "nationality": "American"
}'
```

### List All Authors
```bash
curl -X GET http://127.0.0.1:8000/api/authors/
```

---

## 🧑‍💻 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## 🙏 Acknowledgments

- Thanks to the Django and Django REST Framework teams for creating such amazing tools.
- Special thanks to all contributors and users of this project.

---

## 📞 Contact

If you have any questions or suggestions, feel free to reach out:

- **Email**: rinkusoft77@gmail.com
- **GitHub**: [Rinku](https://github.com/rinkuo)

---

Made with ❤️ by **Rinku**  
✨ Happy Coding! ✨

---

---
