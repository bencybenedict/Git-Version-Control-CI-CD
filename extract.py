import csv
def extract():
    with open("Sales.csv", "r") as file:
        data = list(csv.DictReader(file))

    print("Number of rows:", len(data))
if __name__ == "__main__":
    extract()