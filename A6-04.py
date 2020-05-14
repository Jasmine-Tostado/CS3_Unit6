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
                us_death_list.append(us_daily_deaths)
                china_death_list.append(china_daily_deaths)
                date_list.append(us_history['date'].strip("T00:00:00"))

            if china_daily_deaths > china_peak_rate:
                china_peak_rate = china_daily_deaths
                china_peak_date = china_history["date"]

    peak_year, peak_month, peak_day = date_helper(china_peak_date)
    days_until_peak = date_to_days("2020-01-22T00:00:00", china_peak_date)
    print(f"\nChina's max rate: {china_peak_rate}, Peak date: "
          f"{f'{peak_day}/{peak_month}/{peak_year}'}, "
          f"Days it took: {days_until_peak} \nThe US is expected to peak in"
          f" {days_until_peak} days from 08/03/2020 \n(when the US had similar"
          f" values to China's first values [548]). \nPeak date for the US: "
          f"{days_to_date('2020-03-08T00:00:00', days_until_peak)}.")

    plt.plot(date_list, us_death_list)
    plt.xticks(rotation=90)
    plt.xlabel("Date")
    plt.ylabel("US Daily Deaths")
    plt.title("US's daily deaths due to Covid-19")
    plt.show()
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
        while days_apart > 0:
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

/Users/jasminetostado/Documents/CS3_Unit6/A6-04.py
*** KEY: [TCC: Total Confirmed, DD: Daily Deaths Date,  TR: Total Recovered] *** 
Date:         |  US TCC:  |   US DD:  |  US TR :   | China TCC:| China DD: | China TR: |
23/01/2020    |         1 |+         0|         0 |       643 |+         1|        30  |
24/01/2020    |         2 |+         0|         0 |       920 |+         8|        36  |
25/01/2020    |         2 |+         0|         0 |      1406 |+        16|        39  |
26/01/2020    |         5 |+         0|         0 |      2075 |+        14|        49  |
27/01/2020    |         5 |+         0|         0 |      2877 |+        26|        58  |
28/01/2020    |         5 |+         0|         0 |      5509 |+        49|       101  |
29/01/2020    |         5 |+         0|         0 |      6087 |+         2|       120  |
03/01/2020    |         5 |+         0|         0 |      8141 |+        38|       135  |
31/01/2020    |         7 |+         0|         0 |      9802 |+        42|       214  |
01/02/2020    |         8 |+         0|         0 |     11891 |+        46|       275  |
02/02/2020    |         8 |+         0|         0 |     16630 |+       102|       462  |
03/02/2020    |        11 |+         0|         0 |     19716 |+        64|       614  |
04/02/2020    |        11 |+         0|         0 |     23707 |+        66|       843  |
05/02/2020    |        11 |+         0|         0 |     27440 |+        72|      1112  |
06/02/2020    |        11 |+         0|         0 |     30587 |+        70|      1477  |
07/02/2020    |        11 |+         0|         0 |     34110 |+        85|      1999  |
08/02/2020    |        11 |+         0|         0 |     36814 |+        87|      2594  |
09/02/2020    |        11 |+         0|         3 |     39829 |+       100|      3219  |
01/02/2020    |        11 |+         0|         3 |     42354 |+       107|      3916  |
11/02/2020    |        12 |+         0|         3 |     44386 |+       100|      4636  |
12/02/2020    |        12 |+         0|         3 |     44759 |+         5|      5083  |
13/02/2020    |        13 |+         0|         3 |     59895 |+       252|      6217  |
14/02/2020    |        13 |+         0|         3 |     66358 |+       152|      7973  |
15/02/2020    |        13 |+         0|         3 |     68413 |+       142|      9298  |
16/02/2020    |        13 |+         0|         3 |     70513 |+       103|     10755  |
17/02/2020    |        13 |+         0|         3 |     72434 |+        98|     12462  |
18/02/2020    |        13 |+         0|         3 |     74211 |+       139|     14206  |
19/02/2020    |        13 |+         0|         3 |     74619 |+       113|     15962  |
02/02/2020    |        13 |+         0|         3 |     75077 |+       122|     18013  |
21/02/2020    |        15 |+         0|         5 |     75550 |+         0|     18704  |
22/02/2020    |        15 |+         0|         5 |     77001 |+       205|     22699  |
23/02/2020    |        15 |+         0|         5 |     77022 |+         2|     23187  |
24/02/2020    |        51 |+         0|         5 |     77241 |+       150|     25015  |
25/02/2020    |        51 |+         0|         6 |     77754 |+        70|     27676  |
26/02/2020    |        57 |+         0|         6 |     78166 |+        52|     30084  |
27/02/2020    |        58 |+         0|         6 |     78600 |+        29|     32930  |
28/02/2020    |        60 |+         0|         7 |     78928 |+        44|     36329  |
29/02/2020    |        68 |+         1|         7 |     79356 |+        47|     39320  |
01/03/2020    |        74 |+         0|         7 |     79932 |+        35|     42162  |
02/03/2020    |        98 |+         5|         7 |     80136 |+        42|     44854  |
03/03/2020    |       118 |+         1|         7 |     80261 |+        33|     47450  |
04/03/2020    |       149 |+         4|         7 |     80386 |+        36|     50001  |
05/03/2020    |       217 |+         1|         7 |     80537 |+        32|     52292  |
06/03/2020    |       262 |+         2|         7 |     80690 |+        29|     53944  |
07/03/2020    |       402 |+         3|         7 |     80770 |+        28|     55539  |
08/03/2020    |       518 |+         4|         7 |     80823 |+        28|     57388  |
09/03/2020    |       583 |+         1|         7 |     80860 |+        23|     58804  |
01/03/2020    |       768 |+         6|         7 |     80887 |+        16|     60181  |
11/03/2020    |      1165 |+         4|        11 |     80921 |+        22|     61644  |
12/03/2020    |      1758 |+         9|        12 |     80935 |+        12|     62911  |
13/03/2020    |      2354 |+         9|        13 |     80972 |+        20|     65634  |
14/03/2020    |      3068 |+        10|        16 |     80996 |+        10|     67004  |
15/03/2020    |      3773 |+         9|        17 |     81020 |+        14|     67843  |
16/03/2020    |      4760 |+        23|        17 |     81051 |+        13|     68777  |
17/03/2020    |      6579 |+        22|        18 |     81088 |+        11|     69717  |
18/03/2020    |      9385 |+        33|       108 |     81140 |+         8|     70529  |
19/03/2020    |     14298 |+        61|       108 |     81200 |+         3|     71262  |
02/03/2020    |     19853 |+        62|       147 |     81287 |+         7|     71854  |
21/03/2020    |     26880 |+        75|       147 |     81349 |+         6|     72360  |
22/03/2020    |     35171 |+       125|       178 |     81440 |+         9|     72815  |
23/03/2020    |     46343 |+       113|       179 |     81515 |+         0|     72822  |
24/03/2020    |     55095 |+       215|       181 |     81596 |+         7|     73275  |
25/03/2020    |     69007 |+       252|       303 |     81728 |+        10|     74167  |
26/03/2020    |     85947 |+       247|       303 |     81785 |+         0|     74175  |
27/03/2020    |    104518 |+       415|       302 |     81947 |+         8|     75092  |
28/03/2020    |    124285 |+       474|       302 |     82057 |+         5|     75570  |
29/03/2020    |    156449 |+       840|       809 |     82153 |+         4|     75898  |
03/03/2020    |    175674 |+       590|      1182 |     82241 |+         1|     76188  |
31/03/2020    |    198298 |+       830|      1182 |     82295 |+         1|     76200  |
01/04/2020    |    231159 |+      1209|      9163 |     82395 |+         6|     76420  |
02/04/2020    |    260025 |+       910|      9639 |     82431 |+         0|     76427  |
03/04/2020    |    291998 |+      1093|     10231 |     82475 |+         0|     76446  |
04/04/2020    |    326023 |+      1332|     15461 |     82494 |+         0|     76446  |
05/04/2020    |    351842 |+      1154|     17991 |     82523 |+         0|     76479  |
06/04/2020    |    382157 |+      1337|     20269 |     82547 |+         0|     76489  |
07/04/2020    |    413259 |+      1899|     22699 |     82568 |+         0|     76509  |
08/04/2020    |    445523 |+      1900|     24247 |     82594 |+         0|     76537  |
09/04/2020    |    479633 |+      1864|     26270 |     82607 |+         0|     76566  |
01/04/2020    |    515558 |+      2114|     28820 |     83004 |+        27|     77844  |
11/04/2020    |    543839 |+      1825|     31305 |     83097 |+         0|     77921  |
12/04/2020    |    571269 |+      1496|     40755 |     83136 |+         0|     77956  |
13/04/2020    |    596325 |+      1526|     42597 |     83303 |+         2|     78148  |
14/04/2020    |    625192 |+      2432|     48186 |     83352 |+         1|     78265  |
15/04/2020    |    654411 |+      2413|     50605 |     83402 |+         0|     78370  |
16/04/2020    |    686640 |+      2256|     53452 |     83754 |+      1290|     78472  |
17/04/2020    |    722123 |+      6387|     56444 |     83785 |+         0|     78540  |
18/04/2020    |    750284 |+      2010|     62973 |     83804 |+         0|     78594  |
19/04/2020    |    774985 |+      1570|     68179 |     83818 |+         0|     78647  |
02/04/2020    |    802871 |+      1755|     70051 |     83850 |+         0|     78715  |
21/04/2020    |    829231 |+      2562|     73056 |     83865 |+         0|     78758  |
22/04/2020    |    857382 |+      2576|     75521 |     83877 |+         0|     78818  |
23/04/2020    |    891855 |+      2403|     79419 |     83885 |+         0|     78869  |
24/04/2020    |    922630 |+      2157|     95892 |     83886 |+         0|     78909  |
25/04/2020    |    960905 |+      1923|    120798 |     83910 |+         0|     79023  |
26/04/2020    |    987385 |+      1062|    121414 |     83913 |+         1|     79113  |
27/04/2020    |   1008886 |+      1163|    140954 |     83919 |+         0|     79220  |

China's max rate: 1290, Peak date: 16/04/2020, Days it took: 83 
The US is expected to peak in 83 days from 08/03/2020 
(when the US had similar values to China's first values [548]). 
Peak date for the US: 31/5/2020.

Process finished with exit code 0

"""
