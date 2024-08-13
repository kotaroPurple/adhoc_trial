
# import numpy as np
import pandera as pa
from pandera import DataFrameModel
from pandera.typing import Series


class SalesDataSchema(DataFrameModel):
    # value: Series[np.float64]
    user: Series[int]
    item: Series[int]
    quantity: Series[int] = pa.Field(ge=0)
