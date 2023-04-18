import os
import csv

budget_csv = os.path.join("PyBank","Resources", "budget_data.csv")

#lists to store data
months = []
total_net = []
changes = []

#set previous row to equal 0 so we have a starting place
previous_row = 0

# open the csv file
with open(budget_csv) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=",")

    # skip and save the header
    csvheader = next(csvfile)

    for row in csvreader:
        # Add date
        months.append(row[0])

        # Add population
        total_net.append(int(row[1]))

        # calculate the current profit/loss
        changes.append(int(row[1]) - previous_row)
        previous_row = int(row[1])

    # print header
    print("Financial Analysis")
    print("----------------------------")
    # calculate the total number of dates
    print(len(months))

    #calculate the total amount of "Profit/Losses"
    print(f"${sum(total_net)}")

    # remove the first value from the changes list so we don't include it in the average changes
    changes.pop(0)

    # calculate the average changes
    average_changes = sum(changes) / (len(months)-1)
    average_changes = "{:.2f}".format(average_changes)
    print(f"${average_changes}")

    max_date = months[changes.index(max(changes)) + 1]
    min_date = months[changes.index(min(changes)) + 1]
    print(f"{max_date} (${max(changes)})")
    print(f"{min_date} (${min(changes)})")

output_file = os.path.join("PyBank","analysis","budget_data.txt")

with open(output_file, "w") as txtfile:
    writer = csv.writer(txtfile)

    #write the text file using the same code as before but using \n to move to the next line
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"{len(months)}\n")
    txtfile.write(f"${sum(total_net)}\n")
    txtfile.write(f"${average_changes}\n")
    txtfile.write(f"{max_date} (${max(changes)})\n")
    txtfile.write(f"{min_date} (${min(changes)})\n")