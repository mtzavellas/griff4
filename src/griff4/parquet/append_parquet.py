import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def generate_and_random_ticks():
    ts_col_name = 'ts'
    start = pd.to_datetime('2019-10-1')
    end = pd.to_datetime('2019-10-30')
    writer = None
    filepath = 'tick_testdata.parquet'
    try:
        for i in range(31):
            ts_index = random_dates(start, end, 100)
            ts_index.name = ts_col_name
            ticks = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'), index=ts_index)
            writer = append_to_parquet(ticks, writer, filepath)
    finally:
        writer.close()

    pq.read_table(filepath).to_pandas()


def append_to_parquet(df: pd.DataFrame, writer: pq.ParquetWriter, filepath: str) -> pq.ParquetWriter:
    table = pa.Table.from_pandas(str)
    if writer is None:
        writer = pq.ParquetWriter(filepath, table.schema)
    writer.write_table(table=table)
    return writer


def random_dates(start, end, n):
    start_u = start.value // 10 ** 9
    end_u = end.value // 10 ** 9
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')


if __name__ == "__main__":
    generate_and_random_ticks()
