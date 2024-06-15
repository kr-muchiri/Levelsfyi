import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Salary Transparency Insights", layout="wide", initial_sidebar_state="expanded")

# Load the generated salary data
df = pd.read_csv('/Users/muchirikahwai/Downloads/Levelsfyi/salary_data.csv')

# Sidebar
st.sidebar.header("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Salary Insights", "Content Hub", "User Engagement"])

# Home Section
if navigation == "Home":
    st.title("Welcome to Salary Transparency Insights")
    st.write("""
    **About This App**

    Welcome to the Salary Transparency Insights Generator! This application was developed as part of my application for the Content Marketing Internship Opportunity at levels.fyi. It showcases my technical skills in data analysis, interactive visualization, and my understanding of salary transparency analytics. This app provides a comprehensive analysis of salary data across different industries, roles, and locations. Each section below contains insights and recommendations based on the visualizations.

    **Key Points**
    - **Metrics Selection**: The key metrics chosen to evaluate salary transparency include average salary by role, location, and trends over time.
    - **Weighted Analysis**: The insights are computed using a comprehensive analysis of these metrics. The weights can be adjusted dynamically to explore different scenarios.
    - **Interactive Visualizations**: The app features interactive bar charts, line charts, and box plots to help visualize salary data across different dimensions.

    **Skills Demonstrated**
    - **Technical Proficiency**: Expertise in Python, data analysis with pandas, and creating interactive visualizations with Seaborn and Matplotlib.
    - **Clear Communication**: Ability to explain complex concepts in a clear and concise manner.
    - **Passion for Technology**: A strong interest in how data analytics and technology are reshaping salary transparency and driving business growth.
             
    **App Sections Explained**
    
    - **Home**: This section provides an introduction to the app, its purpose, and the skills demonstrated.
    - **Salary Insights**: Explore detailed salary data visualizations. This section includes charts and graphs that show average salaries by role and location, salary distribution, and trends over time.
    - **Content Hub**: Find engaging blog posts, social media feeds, and a content calendar. This section provides resources and updates related to salary transparency.
    - **User Engagement**: Use tools like the Salary Calculator to get personalized salary estimates based on your role, experience, and location. Participate in polls and provide feedback to help us improve.

    **Note**: The data used in this application was randomized and generated for the purpose of demonstrating my data analysis skills.

    **Date Built**: June 14, 2024
    """)
    st.image("/Users/muchirikahwai/Downloads/Levelsfyi/image.webp", caption="Salary Insights", use_column_width=True)
    
# Salary Insights Section
if navigation == "Salary Insights":
    st.title("Salary Insights")

    # Data Visualization
    st.header("Salary Data Visualization")
    st.write("Interactive charts and graphs to explore salary data:")

    # Salary by Role
    st.subheader("Average Salary by Role")
    fig, ax = plt.subplots()
    role_avg_salary = df.groupby('Role')['Average Salary'].mean().sort_values()
    sns.barplot(x=role_avg_salary.values, y=role_avg_salary.index, palette="viridis", ax=ax)
    ax.set_xlabel('Average Salary ($)')
    ax.set_ylabel('Role')
    st.pyplot(fig)

    # Salary by Location
    st.subheader("Average Salary by Location")
    fig, ax = plt.subplots()
    location_avg_salary = df.groupby('Location')['Average Salary'].mean().sort_values()
    sns.barplot(x=location_avg_salary.values, y=location_avg_salary.index, palette="magma", ax=ax)
    ax.set_xlabel('Average Salary ($)')
    ax.set_ylabel('Location')
    st.pyplot(fig)

    # Salary Distribution by Role
    st.subheader("Salary Distribution by Role")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Average Salary', y='Role', data=df, palette="Set2", ax=ax)
    ax.set_xlabel('Average Salary ($)')
    ax.set_ylabel('Role')
    st.pyplot(fig)

    # Salary Distribution by Location
    st.subheader("Salary Distribution by Location")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Average Salary', y='Location', data=df, palette="coolwarm", ax=ax)
    ax.set_xlabel('Average Salary ($)')
    ax.set_ylabel('Location')
    st.pyplot(fig)



    # Filter Data by Location
    st.subheader("Filter Data by Location")
    location = st.selectbox("Select Location", df['Location'].unique(), key="filter_location")
    filtered_data = df[df['Location'] == location]
    st.write(filtered_data)

# Content Hub Section
if navigation == "Content Hub":
    st.title("Content Hub")

    # Blog Posts Section
    st.header("Blog Posts")
    st.write("Engaging and informative blog posts about salary transparency:")

    blog_posts = [
        {"title": "Understanding Salary Trends in Tech", "link": "#"},
        {"title": "How to Negotiate Your Salary", "link": "#"},
        {"title": "Salary Transparency: Why It Matters", "link": "#"},
    ]

    for post in blog_posts:
        st.write(f"[{post['title']}]({post['link']})")

    # Social Media Feed (Placeholder)
    st.header("Social Media Feed")
    st.write("Recent posts from our social media channels:")

    # Placeholder for social media posts
    social_media_posts = [
        {"platform": "Twitter", "content": "Latest insights on salary transparency..."},
        {"platform": "Instagram", "content": "Check out our new infographic on salary trends..."},
    ]

    for post in social_media_posts:
        st.write(f"**{post['platform']}**: {post['content']}")

    # Content Calendar
    st.header("Content Calendar")
    st.write("Upcoming blog posts and social media campaigns:")
    content_calendar = [
        {"date": "2024-07-01", "content": "Blog post on salary negotiation tips"},
        {"date": "2024-07-05", "content": "Instagram live session on industry salary trends"},
    ]

    for item in content_calendar:
        st.write(f"**{item['date']}**: {item['content']}")

# User Engagement Section
if navigation == "User Engagement":
    st.title("User Engagement")

    # Salary Calculator
    st.header("Salary Calculator")
    st.write("Get a personalized salary estimate based on your role, experience, and location:")

    role = st.selectbox("Select Role", df['Role'].unique(), key="calculator_role")
    experience = st.slider("Years of Experience", 0, 20, 1, key="calculator_experience")
    location = st.selectbox("Select Location", df['Location'].unique(), key="calculator_location")

    # Salary calculation logic
    base_salary = df[(df['Role'] == role) & (df['Location'] == location)]['Average Salary'].mean()
    estimated_salary = base_salary * (1 + (experience * 0.02))  # Simple estimation logic

    st.write(f"Estimated Salary for a {role} with {experience} years of experience in {location}: ${estimated_salary:,.2f}")

    # Newsletter Subscription
    st.header("Newsletter Subscription")
    st.write("Sign up for our newsletter to get the latest updates on salary transparency.")
    email = st.text_input("Enter your email address:", key="newsletter_email")
    if st.button("Subscribe"):
        st.write("Thank you for subscribing!")

    # User Engagement Section
    st.header("User Engagement")
    st.write("Participate in our latest polls and provide feedback:")

    # Example Poll
    poll_question = "What is the most important factor in job satisfaction for you?"
    poll_options = ["Salary", "Work-life balance", "Career growth", "Company culture"]
    poll_selection = st.radio(poll_question, poll_options)

    if st.button("Submit Poll Response"):
        st.write("Thank you for participating!")

    # Feedback Form
    st.subheader("Feedback Form")
    feedback = st.text_area("We value your feedback. Please share your thoughts with us.")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")
