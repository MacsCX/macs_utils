import csv

with open("mock_data/EN-animals.txt", "r") as file:
    spamreader = csv.reader(file, delimiter=" ")

