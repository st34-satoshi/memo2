import csv
import matplotlib.pyplot as plt


def read_csv(file_name):
    '''
    return {country_name: gdp}
    '''
    data = {}
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        for row in reader:
            if row[7] in ['n/a', '']:
                continue
            data[row[0]] = float(row[7].replace(',', ''))
    return data


def graph(gdp_data):
    '''
    draw a pie chart
    gdp_data: {country: gdp}
    '''
    numb_display_country = 15
    sorted_gdp = sorted(gdp_data.items(), key=lambda x:x[1], reverse=True)  # [(country, gdp)]

    # Some data
    labels = []
    gdp_values = []
    others_sum = 0
    for i, (country, gdp) in enumerate(sorted_gdp):
        if i < numb_display_country:
            labels.append(country)
            gdp_values.append(gdp)
        else:
            others_sum += gdp
    labels.append('Others')
    gdp_values.append(others_sum)

    # A standard pie plot
    plt.pie(gdp_values, labels=labels, autopct='%1.1f%%', shadow=True)

    # plt.show()
    plt.savefig('gdp.png')


if __name__ == '__main__':
    file_name = "WEO_Data.csv"
    gdp = read_csv(file_name)
    graph(gdp)