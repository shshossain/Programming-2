import time
import json
import linecache
import pandas as pd
import matplotlib.pyplot as plt
class CsvConverter:
    def __init__(self, header):
        self.header = header.split(',')
    
    def csv_to_json(self, lines):
        json_data = [
            dict(zip(self.header, line.strip().split(',')))
            for line in lines
            if len(line.strip().split(',')) == len(self.header)
        ]
        return json.dumps(json_data)



class CsvConverter:
    def __init__(self, header):
        self.header = header.split(',')
    
    def csv_to_json(self, lines):
        json_data = [
            dict(zip(self.header, line.strip().split(',')))
            for line in lines
            if len(line.strip().split(',')) == len(self.header)
        ]
        assert all(len(line.strip().split(',')) == len(self.header) for line in lines), "Number of items in line doesn't match header"
        return json.dumps(json_data)
class Reader:
    def __init__(self, csv_file='dSST.csv'):
        self.csv_file = csv_file
        self.stride = 5
        self.converter = CsvConverter(linecache.getline(csv_file, 1))
        self.current_line = 2
        self.observers = set()
    
    def add_observer(self, observer):
        self.observers.add(observer)
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update()
    
    def get_lines(self):
        lines = [
            linecache.getline(self.csv_file, self.current_line + i)
            for i in range(self.stride)
        ]
        if not all(lines):
            return ""
        self.current_line += self.stride
        self.notify_observers()  # Notify observers when new data is read
        return self.converter.csv_to_json(lines)

class AverageYear:
    def __init__(self, reader):
        self.reader = reader
        self.averages = []
        self.years = []
        self.figure, self.ax = plt.subplots()
    
    def update(self):
        self.calculate_year_average()
        self.visualize()
    
    def calculate_year_average(self):
        self.averages.clear()
        self.years.clear()
        while True:
            data = self.reader.get_lines()
            if not data:
                break
            df = pd.read_json(data)
            average_anomaly = df['J-D'].mean() 
            self.averages.append(average_anomaly)
            self.years.append(df['Year'].iloc[-1])  # Assuming 'Year' column exists
    
    def visualize(self):
        self.ax.clear()
        self.ax.plot(self.years, self.averages, 'go--')
        self.ax.set_xlabel('Year')
        self.ax.set_ylabel('Yearly Average Temperature')
        self.ax.set_title('Yearly Average Temperature')
        self.ax.grid(True)
        plt.pause(0.05)
        plt.show()


class AverageMonth:
    def __init__(self, reader):
        self.reader = reader
        self.averages = []
        self.month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.monthly_averages = {month: [] for month in self.month_names}
        self.monthly_figure, self.monthly_ax = plt.subplots()
    
    def update(self):
        self.calculate_month_average()
        self.visualize()
    
    def calculate_month_average(self):
        self.monthly_averages = {month: [] for month in self.month_names}  # Clear previous data
        while True:
            data = self.reader.get_lines()
            if not data:
                break
            df = pd.read_json(data)
            for month in self.month_names:
                monthly_average = df[month].mean()
                self.monthly_averages[month].append(monthly_average)
    
    def visualize(self):
        self.monthly_ax.clear()
        for month, temps in self.monthly_averages.items():
            self.monthly_ax.plot(range(1, len(temps) + 1), temps, label=month)

        self.monthly_ax.set_xlabel('Data Point')
        self.monthly_ax.set_ylabel('Monthly Average Temperature')
        self.monthly_ax.set_title('Monthly Average Temperatures')
        self.monthly_ax.legend()
        self.monthly_ax.grid(True)
        plt.pause(0.05)
        plt.show()


