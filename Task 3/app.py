def unsafe_function(user_input):
    query = f"SELECT * FROM users WHERE name='{user_input}'"
    execute_query(query)

#review code with bandit
bandit -r app.py
