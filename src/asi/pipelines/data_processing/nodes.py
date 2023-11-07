import pandas as pd


def preprocess_universities(universities: pd.DataFrame) -> pd.DataFrame:
    return universities


def create_model_input_table(
        companies: pd.DataFrame
) -> pd.DataFrame:
    companies = companies.drop_duplicates()
    # TODO: Do some more preprocessing
    # TODO: maybe remove broad_impact column? (seems to be empty in most records)
    return companies
