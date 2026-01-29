## ⚙️ Setup Instructions

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
