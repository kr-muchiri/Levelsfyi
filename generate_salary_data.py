import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Define parameters
num_records = 1000
roles = ['Data Scientist', 'Software Engineer', 'Product Manager', 'UX Designer', 'QA Engineer', 'DevOps Engineer', 'Business Analyst', 'HR Specialist']
locations = ['San Francisco', 'New York', 'Austin', 'Seattle', 'Boston', 'Chicago', 'Denver', 'Los Angeles']
company_sizes = ['Small', 'Medium', 'Large']

# Base salaries by role
base_salaries = {
    'Data Scientist': 120000,
    'Software Engineer': 110000,
    'Product Manager': 105000,
    'UX Designer': 95000,
    'QA Engineer': 90000,
    'DevOps Engineer': 115000,
    'Business Analyst': 95000,
    'HR Specialist': 80000
}

# Location salary multipliers
location_multipliers = {
    'San Francisco': 1.3,
    'New York': 1.25,
    'Austin': 1.1,
    'Seattle': 1.2,
    'Boston': 1.15,
    'Chicago': 1.05,
    'Denver': 1.0,
    'Los Angeles': 1.1
}

# Generate data
data = []

for _ in range(num_records):
    role = np.random.choice(roles)
    location = np.random.choice(locations)
    company_size = np.random.choice(company_sizes)
    experience = np.random.randint(0, 21)  # Years of experience

    # Base salary
    base_salary = base_salaries[role]

    # Adjust salary based on location and company size
    location_factor = location_multipliers[location]
    company_size_factor = {'Small': 0.9, 'Medium': 1.0, 'Large': 1.1}[company_size]
    experience_factor = 1 + (experience * 0.02)  # 2% increase per year of experience

    # Final salary calculation
    salary = base_salary * location_factor * company_size_factor * experience_factor
    salary = max(30000, salary + np.random.normal(0, 10000))  # Adding some noise

    # Random timestamp within the last 5 years
    timestamp = pd.Timestamp('2023-01-01') - pd.Timedelta(days=np.random.randint(0, 365*5))

    data.append([role, location, company_size, experience, salary, timestamp])

# Create DataFrame
df = pd.DataFrame(data, columns=['Role', 'Location', 'Company Size', 'Experience', 'Average Salary', 'Timestamp'])

# Save to CSV
df.to_csv('salary_data.csv', index=False)

print("Data generation complete. Saved to 'salary_data.csv'")
