import csv


def extract():
    with open("sales.csv", "r") as file:
        data = list(csv.DictReader(file))

    return data


def transform(data):
    for row in data:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])

    return data


if __name__ == "__main__":
    data = extract()
    data = transform(data)

    print("Number of rows:", len(data))