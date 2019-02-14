import pandas as pd
from utils import convert_to_date, convert_to_hour
import warnings
warnings.filterwarnings('ignore')

df1 = pd.read_csv('locations.csv')
df2 = pd.read_csv('pickup_times.csv')
df2.columns=[ 'Location','Time', 'Pickup Time']



df2['Date'] = [convert_to_date(each) for each in df2['Time']]
df2['Hour'] = [convert_to_hour(each) for each in df2['Time']]

date_selection = df2['Date'].unique().tolist()
hour_selection = df2['Hour'].unique()
location = df1['location_id']

print("Select the date that you want below: ")

index = 1
for each in sorted(date_selection):
    print("{}. {}".format(index, each))
    index += 1
date = int(input("Choose a number: "))

start = input("Selec the STARTING HOUR between {} - {}: ".format(hour_selection.min(), hour_selection.max()))

end = input("Selec the STARTING HOUR between {} - {}: ".format(hour_selection.min(), hour_selection.max()))


date_result = df2[df2['Date'] == date_selection[date-1]]

final_result = date_result[(date_result['Hour']== int(start))|(date_result['Hour']==int(end))]

final_locations = final_result['Location'].unique().tolist()

for each in sorted(final_locations):
    avg = final_result[final_result['Location'] == each]['Pickup Time'].mean()
    print("location {} - mean: {}".format(each, avg))


#TODO:
# 1. Write input checks
# 2. Write to csv
