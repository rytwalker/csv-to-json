# Redirect Script for Prismic

1. Add a CSV file to parse in the csv folder
2. On Line 13 update the file name and save
3. Check the page_types_dictonary on line 5. The key is the slug and the value is the corresponding page type in prismic. If the one you are working with isn't there, add it to the dictonary.
4. Run `python3 csv_parser.py` in the terminal
