import pandas as pd
import json

class DataProvider:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def get_weather_data(self, parameter='all'):
        if parameter is None or parameter == 'all':
            return self.data.T.to_json()
        elif isinstance(parameter, int):
            data = self.data[self.data['Year'] == parameter]
            if data.empty:
                raise ValueError(f"No data available for year {parameter}")
            return data.T.to_json()
        elif isinstance(parameter, tuple) and len(parameter) == 2 and all(isinstance(year, int) for year in parameter):
            from_year, to_year = parameter
            data = self.data[(self.data['Year'] >= from_year) & (self.data['Year'] <= to_year)]
            if data.empty:
                raise ValueError(f"No data available for the range {from_year}-{to_year}")
            return data.T.to_json()
        else:
            raise ValueError("Invalid parameter: must be 'all', an integer year, or a tuple of two integer years")

# Example usage
provider = DataProvider('C:/Users/HP Pavilion Gaming/Desktop/Programming_2/2.1/dSST.csv')

#print(provider.get_weather_data())
#print(provider.get_weather_data(1998))
#print(provider.get_weather_data((1991, 2000)))
