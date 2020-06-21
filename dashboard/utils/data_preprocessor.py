import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from .country_decision_maker import Country


def load_data(csv_file: str):
    countries = []
    try:
        data = pd.read_csv(csv_file)

        for index, row in data.iterrows():
            countries.append(Country(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                     row[7]))
        alternatives = data['name'].values
        criteria = ['Control of corruption', 'Political Stability', 'Inflation Rate', 'Gdp Growth',
                    'Ease of Doing Business', 'Unemployment Rate',
                    'Individuals using the Internet']
    except:
        raise Exception('Error')
    return countries, alternatives, criteria


def normalize_data(self):
    dataset = self.dataset.drop(columns=['name'])
    imp = SimpleImputer(missing_values=pd.np.nan, strategy="mean")
    X = dataset[:].values
    X = imp.fit_transform(X)
    # dataset.head(5)
    data_normalizer = MinMaxScaler(feature_range=[0, 1])
    features = dataset.columns
    normalized_data = data_normalizer.fit_transform(dataset[features])
    return normalized_data
