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
            if code == "N321":
                data.append("A") # Short term: Received a Form 1099-B showing basis was reported to the IRS
            elif code == "N711":
                data.append("B") # Short term: Received a Form 1099-B showing basis was NOT reported to the IRS
            elif code == "N712":
                data.append("C") # Short term: Did not receive a Form 1099-B
            elif code == "N323":
                data.append("D") # Long term: Received a Form 1099-B showing basis was reported to the IRS
            elif code == "N713":
                data.append("E") # Long term: Received a Form 1099-B showing basis was NOT reported to the IRS
            elif code == "N714":
                data.append("F") # Long term: Did not receive a Form 1099-B
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
