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


def load(data):
    for row in data:
        print(row)


def validate(data):
    valid_data = []

    for row in data:
        if row["product"] and row["quantity"] and row["price"]:
            valid_data.append(row)

    return valid_data


if __name__ == "__main__":
    data = extract()
    data = transform(data)
    print("ETL processing completed")
    load(data)