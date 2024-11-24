%python
# Correct the storage account name according to the connection string
storage_account_name = "stgpolitics"
container_name = "container2"
file_path = "Political Regmies by Country.csv"

# Define the full path to the file using the appropriate protocol for Azure Data Lake Storage Gen2
data_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/{file_path}"

# Correct the storage account key according to the connection string
storage_account_key = dbutils.secrets.get(scope="scope_rg_databricks_pipelines", key="storage_account_key")

# Configure the Spark session with the correct storage account key for Data Lake Storage Gen2
spark.conf.set(f"fs.azure.account.key.{storage_account_name}.dfs.core.windows.net", storage_account_key)

# Read the CSV file into a DataFrame
df = spark.read.format("csv").option("header", "true").load(data_path)

# Display the DataFrame
display(df)
