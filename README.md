# Shop Parser

Shop Parser is a simple web application built with Flask that aggregates product information from multiple online clothing stores. Instead of switching between different websites, users can search for items in one place, saving time and improving convenience.

## Features

- User registration and authentication system
- Search interface for querying items
- Aggregates and displays results from various online shops
- Organized structure with Flask Blueprints
- HTML templates for login, registration, search, and results

## Project Structure

```
project_root/
├── application/
│   ├── database/
│   │   ├── functions.py
│   │   ├── models.py
│   ├── parser/
│   │   └── extractors.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── main.py
│   │   ├── shop.py
│   ├── static/
│   │   └── background.png
│   ├── templates/
│   │   ├── login.html
│   │   ├── registration.html
│   │   ├── shop.html
│   │   ├── search.html
│   │   ├── success.html
│   │   └── error.html
│   ├── config.py
│   ├── logger.py
│   └── utils.py
├── data/
├── tests/
│   ├── test_auth.py
├── database.db
├── logs.log
├── main.py
└── README.md
```

## How to Run

1. Make sure you have Python installed (preferably version 3.8 or higher).
2. Install Flask:
   ```bash
   pip install Flask
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/`.

## Future Plans

- Add support for more websites and marketplaces
- Improve search accuracy and filtering options
- Implement a product comparison feature
- Add user preferences and favorites

## Notes

- No external dependencies required other than Flask
- No license applied yet — feel free to use for learning or testing purposes
