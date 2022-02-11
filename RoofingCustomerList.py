def merge_file(past_file_path, proposed_file_path, merged_file_path):
    past_file_contents = load_file(past_file_path)
    proposed_file_contents = load_file(proposed_file_path)

    proposed_customer_name = []
    for row in proposed_file_contents:
        proposed_customer_name.append(row[1])

    with open(merged_file_path, 'w'):
        outputf.write("Customer Number, Customer Name, Address\r\n")

        for row in proposed_file_contents:
            line = str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + "\r\n"
            outputf.write(line)

        for row in past_file_contents:
            if row[1] in proposed_customer_name:
                continue
            else:
                line = str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + "\r\n"
                outputf.write(line)

        print("Files merged successfully!")


# reads the file and returns the content as 2D lists
def load_file(path):
    file_contents = []
    with open(path, 'r') as past_file_path:
        for line in past_file_path:
            cells = line.split(",")
            row = []
            for cell in cells:
                if cell.lower().strip() == "customer number":
                    break
                else:
                    row.append(cell.strip())
            if len(row) > 0:
                file_contents.append(row)
    return file_contents


past_file_path = "F:\\Past Customer.txt"
proposed_file_path = "F:\\Proposed Customer.txt"
merged_file_path = "F:\\Merged File.txt"
merge_file(past_file_path, proposed_file_path, merged_file_path)
