import pandas

data = pandas.read_csv("lifestyle_data.csv")
print(data.columns.tolist())
# What data type is `data` as output from the `read_csv()` method?
print(type(data))
# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
print("Total number of students:", len(data))

# Find the mean average GPA of the students
print("Mean average GPA of the students:", data["GPA"].mean())

# Find the standard deviation of how much sleep students get per day
print("Standard deviation of sleep hours per day:", data["Sleep_Hours_Per_Day"].std())

# Find the maximum amount of study hours per day
print("Maximum amount of the study hours per day:", data["Study_Hours_Per_Day"].max())

# Sort the students by social hours per day ascending (lowest -> highest)
Sorted_social_hours = data.sort_values(by="Social_Hours_Per_Day")
print(Sorted_social_hours)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data["Total_hours"] = data["Sleep_Hours_Per_Day"] + data["Study_Hours_Per_Day"] + data["Social_Hours_Per_Day"] + data["Extracurricular_Hours_Per_Day"] + data["Physical_Activity_Hours_Per_Day"]
print(data)

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
high_stress_students = data[data["Stress_Level"].str.lower() == "high"]
low_stress_students = data[data["Stress_Level"].str.lower() == "low"]

print("High stress students:")
print(high_stress_students)
print("Low stress students:")
print(low_stress_students)
print("High stress mean GPA:", high_stress_students["GPA"].mean())
print("Low stress mean GPA:", low_stress_students["GPA"].mean())