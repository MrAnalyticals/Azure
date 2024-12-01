
#Connecting to Azure SQL database from Azure Databricks

# Retrieve the username and password from the secret scope
username = dbutils.secrets.get(scope="scope_rg_databricks_pipelines", key="politics_sql_username")
password = dbutils.secrets.get(scope="scope_rg_databricks_pipelines", key="politics_sql_password")

# Define the connection string
server = "sqlserverpoltics.database.windows.net"  # Fixed typo in server name
database = "sqldbpolitics"
url = f"jdbc:sqlserver://{server}:1433;database={database};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;"

# Define the query
query = "SELECT * FROM dbo.CountryData"

# Combine all options in one line
try:
    df = (spark.read.format("jdbc")
          .option("url", url)
          .option("dbtable", f"({query}) as temp_table")
          .option("user", username)
          .option("password", password)
          .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver")
          .load())
    print("DataFrame loaded successfully")
    # Create a temporary view
    df.createOrReplaceTempView("politicalregimes_view")  # Corrected the view name
    # Display the DataFrame
    display(df)
except Exception as e:
    print("DataFrame loading failed:", e)

