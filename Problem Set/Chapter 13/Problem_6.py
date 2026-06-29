# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

r'''
# Export packages from system Python
pip freeze > requirements.txt

# Create virtual environment
python -m venv myenv

# Activate virtual environment
myenv\Scripts\activate

# Install all packages
pip install -r requirements.txt

'''