import gspread

sa = gspread.service_account(filename="creds.json")

sh = sa.open("NA/EMEA GGST/SF6 Online Tourney Times")

wks = sh.worksheet("Sheet1")

print("Rows: ", wks.row_count)
print("Columns, ", wks.col_count)


search = "NA" # filter value

values = [r for r in wks.get_all_values() if r[5] == search] # get all the rows where column 5 (region) contains NA itll store the rows in a list

print(values) # print everything in the list
