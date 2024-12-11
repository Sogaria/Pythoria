from prettytable import PrettyTable #import class from package

table = PrettyTable() #create object from class
table.field_names = ["Country", "City", "Population"] #attribute
table.align = "l"
table.add_row(["Germany", "Berlin", "3,432,000"]) #method
table.add_row(["France", "Paris", "2,103,000"])
table.add_row(["Spain", "Madrid", "3,277,000"])
table.add_row(["Netherlands", "Amsterdam", "921,000"])

print(table)

