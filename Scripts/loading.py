import pandas as pd
import gzip
import json
import random
import sqlite3


def load_from_db(db_path, db_name):  # '../Data/phonereviews.db', 'phonereviews'
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * from " + str(db_name), conn)
    df = df.drop(['RATING'], axis=1)
    df.columns = ['NODE', 'URL', 'text', 'REVIEWRATING', 'BESTRATING', 'WORSTRATING']
    return df


def load_schema_full(input_link):
    df = pd.read_csv(input_link)
    df = df[['REVIEWBODY', 'REVIEWRATING_adj']]
    df.columns = ['text', 'label']
    return df


def load_amazon_full(input_link):
    data = []
    with gzip.open(input_link) as file:
        for line in file:
            data.append(json.loads(line.strip()))

    df = pd.DataFrame.from_dict(data)
    df = df[['reviewText', 'overall']]
    df.columns = ['text', 'label']
    return df


def load_merged_data(schema_link, amazon_link, schema_per_class, amazon_per_class):
    if schema_per_class != 0:
        schema_df = pd.read_pickle(schema_link)
        schema_df_1 = schema_df[schema_df['label'] == 1.0].values.tolist()
        schema_df_2 = schema_df[schema_df['label'] == 2.0].values.tolist()
        schema_df_3 = schema_df[schema_df['label'] == 3.0].values.tolist()
        schema_df_4 = schema_df[schema_df['label'] == 4.0].values.tolist()
        schema_df_5 = schema_df[schema_df['label'] == 5.0].values.tolist()

        try:
            random.seed(123)
            df1 = random.sample(schema_df_1, schema_per_class)
        except ValueError:
            random.seed(123)
            df1 = random.choices(schema_df_1, k=schema_per_class)
        try:
            random.seed(123)
            df2 = random.sample(schema_df_2, schema_per_class)
        except ValueError:
            random.seed(123)
            df2 = random.choices(schema_df_2, k=schema_per_class)
        try:
            random.seed(123)
            df3 = random.sample(schema_df_3, schema_per_class)
        except ValueError:
            random.seed(123)
            df3 = random.choices(schema_df_3, k=schema_per_class)
        try:
            random.seed(123)
            df4 = random.sample(schema_df_4, schema_per_class)
        except ValueError:
            random.seed(123)
            df4 = random.choices(schema_df_4, k=schema_per_class)
        try:
            random.seed(123)
            df5 = random.sample(schema_df_5, schema_per_class)
        except ValueError:
            random.seed(123)
            df5 = random.choices(schema_df_5, k=schema_per_class)
        df11 = pd.DataFrame(df1)
        df12 = pd.DataFrame(df2)
        df13 = pd.DataFrame(df3)
        df14 = pd.DataFrame(df4)
        df15 = pd.DataFrame(df5)
        schema = pd.concat([df11, df12, df13, df14, df15])
        schema['origin'] = 'schema'
        schema = schema[[4, 3, 'origin']]
        schema.columns = ['text_prep', 'label', 'origin']
    else:
        schema = pd.DataFrame(columns=['text_prep', 'label', 'origin'])

    if amazon_per_class != 0:
        ama_df = pd.read_pickle(amazon_link)
        ama_df_1 = ama_df[ama_df['label'] == 1.0].values.tolist()
        ama_df_2 = ama_df[ama_df['label'] == 2.0].values.tolist()
        ama_df_3 = ama_df[ama_df['label'] == 3.0].values.tolist()
        ama_df_4 = ama_df[ama_df['label'] == 4.0].values.tolist()
        ama_df_5 = ama_df[ama_df['label'] == 5.0].values.tolist()

        try:
            random.seed(123)
            adf1 = random.sample(ama_df_1, amazon_per_class)
        except ValueError:
            random.seed(123)
            adf1 = random.choices(ama_df_1, k=amazon_per_class)
        try:
            random.seed(123)
            adf2 = random.sample(ama_df_2, amazon_per_class)
        except ValueError:
            random.seed(123)
            adf2 = random.choices(ama_df_2, k=amazon_per_class)
        try:
            random.seed(123)
            adf3 = random.sample(ama_df_3, amazon_per_class)
        except ValueError:
            random.seed(123)
            adf3 = random.choices(ama_df_3, k=amazon_per_class)
        try:
            random.seed(123)
            adf4 = random.sample(ama_df_4, amazon_per_class)
        except ValueError:
            random.seed(123)
            adf4 = random.choices(ama_df_4, k=amazon_per_class)
        try:
            random.seed(123)
            adf5 = random.sample(ama_df_5, amazon_per_class)
        except ValueError:
            random.seed(123)
            adf5 = random.choices(ama_df_5, k=amazon_per_class)
        adf11 = pd.DataFrame(adf1)
        adf12 = pd.DataFrame(adf2)
        adf13 = pd.DataFrame(adf3)
        adf14 = pd.DataFrame(adf4)
        adf15 = pd.DataFrame(adf5)
        amazon = pd.concat([adf11, adf12, adf13, adf14, adf15])
        amazon['origin'] = 'amazon'
        amazon = amazon[[2, 1, 'origin']]
        amazon.columns = ['text_prep', 'label', 'origin']
    else:
        amazon = pd.DataFrame(columns=['text_prep', 'label', 'origin'])
    df_all = pd.concat([schema, amazon], ignore_index=True)
    df_all = df_all[['text_prep', 'label', 'origin']]
    return df_all


def load_sampled(link, per_class):
    df = pd.read_pickle(link)
    df_1 = df[df['label'] == 1.0].values.tolist()
    df_2 = df[df['label'] == 2.0].values.tolist()
    df_3 = df[df['label'] == 3.0].values.tolist()
    df_4 = df[df['label'] == 4.0].values.tolist()
    df_5 = df[df['label'] == 5.0].values.tolist()

    try:
        random.seed(123)
        adf1 = random.sample(df_1, per_class)
    except ValueError:
        random.seed(123)
        adf1 = random.choices(df_1, k=per_class)
    try:
        random.seed(123)
        adf2 = random.sample(df_2, per_class)
    except ValueError:
        random.seed(123)
        adf2 = random.choices(df_2, k=per_class)
    try:
        random.seed(123)
        adf3 = random.sample(df_3, per_class)
    except ValueError:
        random.seed(123)
        adf3 = random.choices(df_3, k=per_class)
    try:
        random.seed(123)
        adf4 = random.sample(df_4, per_class)
    except ValueError:
        random.seed(123)
        adf4 = random.choices(df_4, k=per_class)
    try:
        random.seed(123)
        adf5 = random.sample(df_5, per_class)
    except ValueError:
        random.seed(123)
        adf5 = random.choices(df_5, k=per_class)
    adf11 = pd.DataFrame(adf1)
    adf12 = pd.DataFrame(adf2)
    adf13 = pd.DataFrame(adf3)
    adf14 = pd.DataFrame(adf4)
    adf15 = pd.DataFrame(adf5)
    df_all = pd.concat([adf11, adf12, adf13, adf14, adf15], ignore_index=True)
    df_all = df_all[[2, 1]]
    df_all.columns = ['text_prep', 'label']
    print(f'{per_class} reviews per class from {link} loaded')
    return df_all


