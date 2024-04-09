import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset.
    race = df['race'].value_counts()
    race_count = race.values

    # Average age of men.
    average_age_men = round(df[df['sex']=='Male']['age'].mean(),1)

    # Percentage of people who have a Bachelor's degree.
    count_bachelors = df[df['education']=='Bachelors']['education'].count()
    total_count = df['education'].count()
    percentage_bachelors = round((count_bachelors/total_count)*100,1)

    # Percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) who make more than 50K.
    # Percentage of people without advanced education who make more than 50K.

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    rich_higher = higher_education[higher_education['salary'] == '>50K']['education']
    higher_education_rich = round((rich_higher.count() / higher_education['education'].count())*100,1)
    rich_lower = lower_education[lower_education['salary'] == '>50K']['education']
    lower_education_rich = round((rich_lower.count() / lower_education['education'].count())*100,1)

    # Minimum number of hours a person works per week (hours-per-week feature).
    min_work_hours = df['hours-per-week'].min()

    # Percentage of the people who work the minimum number of hours per week who have a salary of >50K.
    num_min_workers = df[df['hours-per-week']==min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = round((rich_min_workers['hours-per-week'].count()/num_min_workers['hours-per-week'].count())*100,1)

    # Country that has the highest percentage of people that earn >50K.
    rich_people = df[df['salary'] == '>50K']
    rich_per_country = rich_people.groupby('native-country').size()
    size_per_country = df.groupby('native-country').size()
    percentage_per_country = round((rich_per_country/size_per_country)*100,1)
    highest_earning_country = percentage_per_country.idxmax()
    highest_earning_country_percentage = percentage_per_country.max()

    # Most popular occupation for those who earn >50K in India.
    rich_in_india = rich_people[rich_people['native-country'] == 'India']
    top_IN_occupation = rich_in_india['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
