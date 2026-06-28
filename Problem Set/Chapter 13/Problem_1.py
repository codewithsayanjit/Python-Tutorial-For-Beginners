# Create two virtual environments, install few packages in the first one. How do you createa similar environment in the second one?

r'''
# Create first environment
python -m venv env1

# Activate env1
env1\Scripts\activate

# Install packages
pip install numpy pandas matplotlib

# Save package list
pip freeze > requirements.txt

# Deactivate
deactivate

# Create second environment
python -m venv env2

# Activate env2
env2\Scripts\activate

# Recreate same environment
pip install -r requirements.txt

'''