%python
# Define the path to the file in the local file storage
#file_path = "file:/Workspace/Users/email@email.com/Political Analysis/Political Regimes by Country.csv"
file_path =    "file:/Workspace/Users/admin@analysis.ie/Political Analysis/Political Regimes by Country.csv"
# Read the CSV file into a DataFrame
df = spark.read.format("csv").option("header", "true").load(file_path)
# Display the DataFrame
display(df)
