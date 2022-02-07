with open("data.txf") as fin:
    version = fin.readline().strip()[1:]
    company = fin.readline().strip()[1:].split(" ")[0]
    report_date = fin.readline().strip().split(" ")[1]
    with open(f"{company}.csv", "w") as fout:
        # write the header
        data = [
            "Reporting Category", "Long/Short", "Description", "Date Acquired", "Date Sold",
            "Cost or Other basis", "Sales Proceeds"
        ]
        fout.write(",".join(data) + "\n")
        # this is a new line of record
        while fin.readline().strip() == "^":
            data = []
            fin.readline() # skip a unknown column
            # 8949 code
            code = fin.readline().strip()
            if len(code) == 0:
                break
            if code in ["N321", "N323"]:
                data.append("A")
            elif code in ["N711", "N713"]:
                data.append("B")
            elif code in ["N712", "N714"]:
                data.append("C")
            else:
                data.append("unknown")
            # short term or long term
            if code in ["N321", "N682", "N711", "N712"]:
                data.append("short")
            elif code in ["N323", "N713", "N714"]:
                data.append("long")
            else:
                data.append("unknown")
            for i in range(2):
                fin.readline()  # skip unknown columns
            for i in range(5):
                data.append(fin.readline().strip()[1:])
            fin.readline().strip() # might be a sale wash indicator
            # export to CSV
            fout.write(",".join(data) + "\n")
