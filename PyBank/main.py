import csv
import os


#despite of the fact that this function is executed only once, 
#I decided to move the main logic of the task into the function, because functions were in scope of this module
def budget_analysis(budget_data_path):
    #define lists for main calculations
    months = []
    profits_and_losses =[]

    #reading from a source CSV file
    with open(budget_data_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader) #skip the headers in the first row

        #reading each row in the CSV file and store the first column to months list and the second column to profit_and_losses list
        for row in csvreader:
            months.append(row[0])
            profits_and_losses.append(int(row[1]))

    #calculate total months as a length of the dates list
    total_num_of_months = len(months)

    #calculate total profit/losses as a sum of all elements in the profit_losses list 
    total_amount_of_prof_loss = sum(profits_and_losses)

    #calculate changes list using the following logic: (<profit/losses for the current month> - <profit/losses for the previous month>)
    #leverage List comprehensions for such calculation
    #changes are calculated started from the 2nd month (Feb-10), because there no previous month for Jan-10 and therefore the change cannot be defined
    changes_for_period = [profits_and_losses[i]- profits_and_losses[i-1] for i in range(1, len(profits_and_losses))]

    #calculate average change
    average_changes_for_period = sum(changes_for_period)/len(changes_for_period)

    #calculate the greatest increase in profits as a max value in changes_for_period list
    greatest_increase = max(changes_for_period)
    #get a month that is corresponded the max change
    #because both lists are aligned, using index from changes_for_period list to retrive a value from months list
    #apply + 1, because changes list is shorter than dates list by 1 item (there is no data for the very first month (Jan-10))
    greatest_increase_index = changes_for_period.index(greatest_increase) + 1
    greatest_increase_date = months[greatest_increase_index]

    #the similar calculation for the greatest decrease
    greatest_decrease = min(changes_for_period)
    greatest_decrease_index = changes_for_period.index(greatest_decrease) + 1
    greatest_decrease_date = months[greatest_decrease_index]

    #generate analysis summary
    #using tuple here, because it produces more compact code when I print or save it to a file, w/o using a for loop
    results = (
            "Financial Analysis\n"
            "----------------------------\n"
            f"Total Months: {total_num_of_months}\n"
            f"Total: ${total_amount_of_prof_loss}\n"
            f"Average Change: ${average_changes_for_period:.2f}\n"
            f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
            f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
    )

    #print the analysis to the terminal
    print(results)

    #export a text file with the results
    output_file_path = os.path.join(".", "analysis", "analysis_summary.txt")
    with open(output_file_path, 'w') as file:
        file.write(results)

#set a path to a source file to pass it to the function
budget_data_path = os.path.join(".", "Resources", "budget_data.csv")

#execute the function that performs the main logic of the task
budget_analysis(budget_data_path)
