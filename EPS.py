import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as 
import Request





class AnalyticsCalculator:
    def __init__(self, data):
        self.data = data
        self.price_data = []
        self.target_price = None

    def filter_data(self, condition):
        filtered_data = [x for x in self.data if condition(x)]
        return filtered_data

    def calculate_mean(self, data):
        if not data:
            return None
        return sum(data) / len(data)

    def set_price_data(self, price_data):
        self.price_data = price_data

    def set_target_price(self, target_price):
        self.target_price = target_price

    def calculate_profit(self):
        if not self.price_data or self.target_price is None:
            return None
        profit = (self.target_price - self.price_data[-1]) / self.price_data[-1]
        return profit

# Sample data
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Create an instance of AnalyticsCalculator
calculator = AnalyticsCalculator(data)

# Define a filter condition (e.g., filter even numbers)
condition = lambda x: x % 2 == 0

# Filter the data based on the condition
filtered_data = calculator.filter_data(condition)

# Calculate the mean of the filtered data
mean = calculator.calculate_mean(filtered_data)

# Set price data and target price
calculator.set_price_data([100, 110, 120, 130, 140])
calculator.set_target_price(150)

# Calculate profit based on price and target price
profit = calculator.calculate_profit()

# Display the results
print("Original data:", data)
print("Filtered data (even numbers):", filtered_data)
print("Mean of filtered data:", mean)
print("Price data:", calculator.price_data)
print("Target price:", calculator.target_price)
print("Profit:", profit)
