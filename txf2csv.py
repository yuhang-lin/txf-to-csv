with open("data.txf") as fin:
    version = fin.readline().strip()[1:]
    company = fin.readline().strip()[1:].split(" ")[0]
    report_date = fin.readline().strip().split(" ")[1]
    with open(f"{company}.csv", "w") as fout:
        # write the header
        data = [
            "Description", "Date Acquired", "Date Sold",
            "Cost  or Other basis", "Sales Proceeds"
        ]
        fout.write(",".join(data) + "\n")
        # this is a new line of record
        while fin.readline().strip() == "^":
            data = []
            for i in range(4):
                fin.readline()  # skip unknown columns
            for i in range(5):
                data.append(fin.readline().strip()[1:])
            assert (fin.readline().strip() == "$")
            # export to CSV
            fout.write(",".join(data) + "\n")
