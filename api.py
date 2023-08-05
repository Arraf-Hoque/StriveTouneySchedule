import gspread

sa = gspread.service_account(filename="creds.json")

sh = sa.open("NA/EMEA GGST/SF6 Online Tourney Times")

wks = sh.worksheet("Sheet1")

print("Rows: ", wks.row_count)
print("Columns, ", wks.col_count)


cell_list = [wks.col_values(6)]

for all in cell_list:
    if cell_list == "NA":
        print("NA SPOTTED")
    elif cell_list == "EMEA":
        print("EMEA SPOTTED")