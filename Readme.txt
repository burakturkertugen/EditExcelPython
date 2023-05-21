You have to install the package "openpyxl"

In Pycharm
File / Settings / Python Interpreter
"+" click the icon and add "openpyxl"

Instruction
You may get the top company in your country from ChatGPT. ChatGPT will give you both the name and the website of the company. It might be a thousand. You might need to organize this information in Excel whether the website is Linkedin or others. 
###SplittingStringFromWebsite
You see "websites_string = JTI: https://www.linkedin.com/company/jti/"
Type as many company names and sites as you want. But only the website will be separated and will be printed.

###WriteWebsitesWithoutName
It is the same function as "SplittingStringFromWebsite", but Python gets the websites and inserts them into a cell as HYPERLINK in the excel File.

###InsertBothNameWebsites
Inserting both the string and the website into the cell. 

WARNING! 
1) You have to create an Excel file before using this. 
2) Change the directory in the Python -> filepath = "C:/Users/burak/Desktop/Excel_SQL/PROJE/LifeQuality/CompanyList.xlsx"
3) Change the name of the Excel file -> filepath = "C:/Users/burak/Desktop/Excel_SQL/PROJE/LifeQuality/CompanyList.xlsx"
Mine is "CompanyList.xlsx"
4) The Excel file should never be ".xlsm" which supports Macro. This will definitely corrupt your file. It should be ".xlsx"
5) Don't forget to change the ROW & COLUMN number
for row, website in enumerate(websites, start=1):
    worksheet.cell(row=row, column=1).hyperlink = website.strip()
6) Work always on a copy file. 
7) Don't forget to change the content in the list named "companies_websites"
Python will split the content WITHIN the list.
