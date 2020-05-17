""" Assignment A6-04 - Jasmine Tostado """
import requests
import json
import matplotlib.pyplot as plt


def stats_helper(us_stats, us_location, china_stats, china_location):
    """ Runs trough the data dictionaries and calls helper functions
     to help analyze the data. """
    date_list = []
    us_death_list = []
    china_death_list = []
    china_peak_rate = 0
    china_peak_date = ""
    line_count = 0
    date_count = 0
    for i in range(len(us_stats["history"])):
        date_count += 1
        us_history = us_stats["history"][i]
        china_history = china_stats["history"][i]
        if i > 0:
            us_prev_day = us_stats["history"][i - 1]
            us_daily_deaths = us_history['deaths'] - us_prev_day['deaths']
            china_prev_day = china_stats["history"][i - 1]
            china_daily_deaths = china_history['deaths'] - \
                                 china_prev_day['deaths']
            line_count = table_format(us_history, us_location, us_daily_deaths,
                                      line_count)
            line_count = table_format(china_history, china_location,
                                      china_daily_deaths, line_count)
            if i > 10:
                if us_history['date'] != "2020-04-17T00:00:00":
                    us_death_list.append(us_daily_deaths)
                if china_history['date'] != "2020-04-16T00:00:00":
                    china_death_list.append(china_daily_deaths)
                    date = us_history['date'].strip("T00:00:00")
                    date_list.append(date)

            if china_daily_deaths > china_peak_rate and china_history['date'] !=\
                    "2020-04-16T00:00:00":
                china_peak_rate = china_daily_deaths
                china_peak_date = china_history["date"]

    peak_year, peak_month, peak_day = date_helper(china_peak_date)
    days_until_peak = date_to_days("2020-01-24T00:00:00", china_peak_date)
    print(f"\nChina's max rate: {china_peak_rate}, Peak date: "
          f"{f'{peak_day}/{peak_month}/{peak_year}'}, "
          f"Days it took: {days_until_peak} \nThe US is expected to peak in"
          f" {days_until_peak} days from 12/03/2020 \n(when the US had similar"
          f" values to China's first values [8]). \nPeak date for the US: "
          f"{days_to_date('2020-03-12T00:00:00', days_until_peak)}.")

    fig, ax = plt.subplots()
    text = f"US is expected to peak on: " \
           f"{days_to_date('2020-03-12T00:00:00', days_until_peak)}"
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)
    plt.plot(date_list, us_death_list)
    plt.xticks(rotation=90)
    plt.xlabel("Date")
    plt.ylabel("US Daily Deaths")
    plt.title("US's daily deaths due to Covid-19")
    plt.show()
    fig, ax = plt.subplots()
    ch_text = f"China's peak reached on: {peak_day}/{peak_month}/{peak_year}" \
              f", rate = {china_peak_rate}"
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, ch_text, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)
    plt.plot(date_list, china_death_list)
    plt.xlabel("Date")
    plt.ylabel("China Daily Deaths")
    plt.title("China's daily deaths due to Covid-19")
    plt.xticks(rotation=90)
    plt.show()


def table_format(data_dict, location, daily_deaths, line_count):
    """ Prints the data for China and the US in a table. I don't print the
     table directly in stats_helper because I can only go trough one dict.
     at a time. """
    date = data_dict['date']
    if date == "2020-01-23T00:00:00" and location == "United States":
        # Printing header once
        print(f"*** KEY: [TCC: Total Confirmed, DD: Daily Deaths Date,  "
              f"TR: Total Recovered] *** "
              f"\nDate:         |  US TCC:  |   US DD:  |  US TR :   | "
              f"China TCC:| China DD: | China TR: |")
    for key, value in data_dict.items():
        line_count += 1
        if key == "date":
            year, month, day = date_helper(value)
            if location == "United States":
                # Making sure the date is not printed twice
                print(f"{day}/{month}/{year}    |", end="")
        elif key == "deaths" and date != "2020-01-22T00:00:00":
            print(f"+{daily_deaths:10}|", end="")
        else:
            if line_count <= 7:
                print(f"{value:10} |", end="")
            else:
                print(f"{value:10}  |")
                line_count = 0
    return line_count


def date_helper(date):
    """Returns the year, month, and day (other functions format the string)."""
    date_str = date.strip("T00:00:00")
    date_list = date_str.split("-")
    if len(date_list[2]) < 2:
        date_list[2] = f"0{date_list[2]}"
    return date_list[0], date_list[1], date_list[2]


def date_to_days(date, peak_date):
    """ Determines how many days apart two dates are.  """
    months = {1: 30, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 30, 8: 28, 9: 31, 10: 30, 11: 31, 12: 30,
              }
    year1, month1, day1 = date_helper(date)
    year2, month2, day2 = date_helper(peak_date)
    month2 = int(month2)
    month1 = int(month1)
    day2 = int(day2)
    day1 = int(day1)
    if month1 == month2:
        days_apart = day2 - day1
    else:
        months_apart_list = [i for i in range(month1 + 1, month2)]
        days_apart = months[month1] - day1
        for month in months_apart_list:
            days_apart += months[month]
        days_apart += day2
    return days_apart


def days_to_date(date, days_apart):
    """ Returns the date after adding days_apart to given date. """
    months = {1: 30, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 30, 8: 28, 9: 31, 10: 30, 11: 31, 12: 30,
              }
    year, month, day = date_helper(date)
    month = int(month)
    day = int(day)
    if days_apart - (months[month] - day) < 0:
        # If new date is in the same month
        return f"{day + days_apart}/{month}/{year}"
    else:
        days_apart -= (months[month] - day)
        while days_apart >= 0:
            month += 1
            day = 1
            if days_apart - months[month] > 0:
                # Have to check since the months have a diff. amount days
                days_apart -= months[month]
            else:
                break
        day += days_apart
    return f"{day}/{month}/{year}"


def main():

    api_url = 'https://api.smartable.ai/coronavirus/stats/US'
    api_params = {
        'Cache-Control': 'no-cache',
        'Subscription-Key': 'eed0071037774749a48da14d2356627d'
    }
    response = requests.get(url=api_url, params=api_params)
    json_data = response.text
    us_data = json.loads(json_data)
    us_location_dict = us_data["location"]
    us_location = us_location_dict["countryOrRegion"]
    us_stats = us_data["stats"]

    api_url2 = 'https://api.smartable.ai/coronavirus/stats/CN'
    api_params2 = {
        'Cache-Control': 'no-cache',
        'Subscription-Key': 'eed0071037774749a48da14d2356627d'
    }
    response2 = requests.get(url=api_url2, params=api_params2)
    json_data2 = response2.text
    china_data = json.loads(json_data2)
    ch_location_dict = china_data["location"]
    china_location = ch_location_dict["countryOrRegion"]
    china_stats = china_data["stats"]
    stats_helper(us_stats, us_location, china_stats, china_location)
    #print(days_to_date("2020-3-12T00:00:00", 19))

main()

r"""
Sources used:
https://docs.python.org/3/installing/index.html
https://www.sitepoint.com/plot-charts-python-matplotlib/
https://www.datasciencelearner.com/matplotlib-tutorial-complete-guide-to-use-
matplotlib-with-python/
https://muddoo.com/tutorials/matplotlib-plot-multiple-lines-on-same-graph-using
-python/

Question:
Using China's peak for the number daily deaths, when can we predict the US's number 
of deaths will peak? The peak is determined by the biggest increase in daily 
deaths.

In order to answer this question I had to calculate the rate of increasing 
deaths in China and find the biggest rate increase. I saved the date (4/16)
for the peak and called a function to find the days it took China to get there. 
I noticed that the US had a close number of cases to China's cases at the 
beginning (1/22, cases: 548) on 3/8. The US had 518 cases on 3/8 so I added the
days that it took China to get to their peak to 3/18 in order to get the US peak.
I wanted to print US values only after 3/18 so that the pattern could be more
obvious but the formatting of my table did not allow me to do that. I would
either have a lot of blank space on the table or China's values from
1/22 - 3/8 would be removed. 

The plot shows how China had a jump in the number of deaths on 4/16
and slow/no increase in the number of deaths after that. The US's graph
looks like it will continue to increase but the different circumstances
in each country make the peak different.
"""