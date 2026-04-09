# QA API Automation Project

## 📌 Overview

This project demonstrates automated API testing using Python and pytest.
The tests validate endpoints from JSONPlaceholder public API.

## 🛠 Technologies Used

- Python
- pytest
- requests
- Git

## 📂 Project Structure

qa-api-automation/
│
├── api/
│ ├── users_api.py
│ ├── posts_api.py
│
├── tests/
│ ├── test_users.py
│ ├── test_posts.py
│
├── requirements.txt
├── README.md


## ✅ What Is Being Tested

### Users Endpoint
- Get all users
- Get user by ID
- Invalid user
- Create user
- Parameterized user validation

### Posts Endpoint
- Get all posts
- Get post by ID

## ▶️ How to Run

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
pip install -r requirements.txt

4. Run tests:
pytest -v


## 📊 Example Output
12 passed in 0.85s

## 🎯 Purpose

This project demonstrates:
- API automation testing
- Test parametrization
- Modular test architecture
- Fixture usage
- Clean separation of API logic and test logic
## "🚀 También puedes ver mi framework de automatización Web con Playwright en la rama feature/web-automation de este repositorio."
