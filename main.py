import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

# Load the data
file_path = '202406_202406_연령별인구현황_월간.csv'
data = pd.read_csv(file_path, encoding='cp949')

# Set up the Streamlit interface
st.title('지역별 중학생 인구비율')

# Get list of regions
regions = data['행정구역'].unique()

# User input for selecting a region
selected_region = st.selectbox('원하는 지역을 선택하세요:', regions)

# Filter data for the selected region
region_data = data[data['행정구역'] == selected_region]

# Extract the total population and the population of middle school students (ages 13-15)
total_population = int(region_data['2024년06월_계_총인구수'].str.replace(',', ''))
middle_school_population = (
    int(region_data['2024년06월_계_13세'].str.replace(',', '')) +
    int(region_data['2024년06월_계_14세'].str.replace(',', '')) +
    int(region_data['2024년06월_계_15세'].str.replace(',', ''))
)

# Calculate the proportion of middle school students
other_population = total_population - middle_school_population

# Prepare data for pie chart
labels = '중학생 인구', '기타 인구'
sizes = [middle_school_population, other_population]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # explode the middle school population slice

# Plotting the pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
st.pyplot(fig1)
