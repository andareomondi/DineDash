# DineDash

DineDash is a comprehensive food delivery service application built using Django. It integrates multiple languages and libraries to offer a seamless experience for both users and administrators.

## Project Description

DineDash allows users to browse various food options, place orders, and have their meals delivered to their doorstep. The project is designed to be user-friendly and efficient, catering to the needs of both customers and service providers.

## Test Demo

You can explore the demo of the application [here](https://dine-dash-kappa.vercel.app/).

## Technologies Used

- **Languages**: Python, HTML, CSS, JavaScript
- **Frameworks and Libraries**: Django, Bootstrap, AOS

## Installation

### Prerequisites

- Python 3.12
- Django 5.1.1
- SQLite and PostgreSQL databases

### Clone the Repository

```bash
git clone https://github.com/andareomondi/DineDash.git
cd DineDash
```

### Setting Up the Environment

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. **Migrate Database**

   ```bash
   python manage.py migrate
   ```

2. **Configure PostgreSQL (If using PostgreSQL)**
   - Set up your PostgreSQL database and update the `DATABASES` setting in `settings.py`.

### Run the Development Server

```bash
python manage.py runserver
```

## Usage

1. **Running the Server**

   ```bash
   python manage.py runserver
   ```

2. **Accessing the Application**

   - Open your web browser and navigate to `http://127.0.0.1:8000/`.

3. **Creating a User Account**
   - Register as a new user through the signup page.
4. **Placing an Order**
   - Browse through the menu, select items, and place your order.

## Contributing

Currently, DineDash is a solo project with no associations. Contributions are welcome in the future. For now, any feedback can be directed to the repository owner.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or support, you can reach out to the repository owner through the GitHub repository.

---

Feel free to add more details or sections as needed. Let me know if there's anything else you'd like to include! 🚀📄
