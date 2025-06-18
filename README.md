
# Women Support NGO Website 🌸
A Django-powered platform for supporting and empowering women through resources, programs, and community engagement.

## 🚀 Features
- Informational homepage with mission and goals
- Programs page (legal aid, education, healthcare)
- Volunteer and donation forms
- Contact form with email support
- Admin dashboard for easy content management

## 📦 Tech Stack
- Django
- HTML/CSS
- MYSQL 
- Python Decouple for secret management

## 🛠️ Setup Instructions

```bash
# Clone the repo


# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Setup environment variables
cp .env.sample .env
# Then edit .env with your secret key

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
