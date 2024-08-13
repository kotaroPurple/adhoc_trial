
from pathlib import Path

import pandas as pd
import pandera as pa
from pandera.typing import DataFrame
from data_processor.schema import SalesDataSchema

REPO_ROOT = Path("../../")


@pa.check_types
def process_sales_data(df_raw: pd.DataFrame) -> DataFrame[SalesDataSchema]:
    df_processed = df_raw.copy()
    df_processed = df_processed.loc[:, df_processed.columns != 'value']
    return df_processed


def main():
    df_raw = pd.read_csv(REPO_ROOT / "data" / "raw" / "example.csv")
    print(df_raw)
    df_processed = process_sales_data(df_raw)
    print(df_processed)
    df_processed.to_csv(REPO_ROOT / "data" / "processed" / "sales_data.csv", index=False)


if __name__ == "__main__":
    main()
