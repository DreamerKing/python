mouths = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

endings = ['st', 'nd', 'rd'] + 17*['th'] \
  + ['st', 'nd', 'rd'] + ['th']*7 \
  + ['st']

print(endings)

year = input("Year: ")
mouth = input("Mouth (1-12): ")
day = input("Day(1-31): " )

mouth_number = int(mouth)
day_number = int(day)

mouth_name = mouths[mouth_number - 1]
day_name = day + endings[day_number - 1]

print(mouth_name, day_name + ',', year)