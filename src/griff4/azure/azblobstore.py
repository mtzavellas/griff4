#%% [markdown]

# Run experiments to store data in azure storage blob.

#%%

from io import BytesIO
from azure.storage.blob import BlobClient
import os

#%% [markdown]

# Get a BlobClient with the specified blob name
#%%

bc = BlobClient.from_connection_string(
    conn_str = os.environ['BLOB_CONNECTION_STR'],
    container_name = os.environ['CONTAINER_NAME'],
    blob_name = 'my.parquet'
)
bc

#%% [markdown]

# Create a pandas data frame for storage

#%%

import pyarrow as pa
import pandas as pd

data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
df = pd.DataFrame(data, index = ('i1', 'i2', 'i3', 'i4'))

#%% [markdown]

# Create a pyarrow table from pandas data frame

#%%

output_table = pa.Table.from_pandas(df)
output_table.schema

#%% [markdown]

# Write the pyarrow table as parquet and store it in azure

#%%

import pyarrow.parquet as pq

try:
    outputstream = BytesIO()
    pq.write_table(output_table, outputstream)
    bc.upload_blob(outputstream.getvalue())
finally:
    outputstream.close()

#%% [markdown]

# Read the schema back from the blob store

#%%
try:
    input_blob = bc.download_blob()
    inputstream = BytesIO()
    input_blob.download_to_stream(inputstream)
    input_table = pq.read_table(source=inputstream)
finally:
    inputstream.close()

#%% [markdown]

# Assert that the schema are the same
#%%

assert output_table.schema == input_table.schema

# Print out the table content as pandas data frame

#%%

pdf = input_table.to_pandas()
pdf

#%%
