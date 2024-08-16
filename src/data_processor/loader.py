
from pathlib import Path
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame
from data_processor.schema import SalesDataSchema


@pa.check_types
def load_sales_data(filepath: Path) -> DataFrame[SalesDataSchema]:
    df = pd.read_csv(filepath)
    return df
