import os
import re
from datetime import datetime, date
import pandas as pd
import csv
from csv import reader

date_list = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']


def create_dataframe():
    df = pd.DataFrame()
    return df

if __name__ == '__main__':
    df = pd.DataFrame()
    dates = []
    days = []
    names = []
    count = []
    path_to_files = 'Registratie 2022-2023 deel 1/'
    for tr_f in os.listdir(path_to_files):
        spitted = re.split('\.|-', tr_f)
        y, m, d = spitted[0], spitted[1], spitted[2]
        curr_date = date(int(y), int(m), int(d))
        with open(path_to_files + tr_f, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            header = next(csv_reader)
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                date_ = curr_date
                day_t = date_list[curr_date.weekday()]
                name = row[1].strip().replace('Ã«', 'ë')
                dates.append(date_)
                days.append(day_t)
                names.append(name)
                count.append(1)
                # print(date_, day_t, name)

    df['Datum'] = dates
    df['Trainingsdag'] = days
    df['Naam lid'] = names
    df['aantal'] = count

    aantal_per_lid = df['Naam lid'].value_counts()
    print(aantal_per_lid)

    aantal_leden = df['Naam lid'].unique().size
    print(aantal_leden)

    aantal_dagen = df['Datum'].unique().size
    print(aantal_dagen)

    import plotly.express as px

    fig = px.bar(df, x="aantal", y="Naam lid", color='Trainingsdag', orientation='h',
                hover_data=["Datum"],
                height=2000,
                title='Trainingsaanwezigheden')
    fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total ascending'})
    # fig.write_html("output_trainingsaanwezigheden.html")
    fig.show()

    fig = px.bar(df, x="aantal", y="Trainingsdag", orientation='h',
                hover_data=["Datum", "Naam lid"],
                height=500,
                title='Succes per dag')
    # fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total ascending'})
    fig.show()