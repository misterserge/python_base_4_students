import csv
from pathlib import Path

Path('csv').mkdir(exist_ok=True)
with open('csv/test.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['name', 'age', 'city'])
    csv_writer.writerow(['John', 30, 'New York'])
    csv_writer.writerow(['Jane', 25, 'Los Angeles'])
    csv_writer.writerow(['Jim', 35, 'Chicago'])

with open('csv/test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

# Path('csv/test.csv').unlink()
# Path('csv').rmdir()
        