# generate Brownian motion stock data
# min price = 1, max price = 500
# number of days = 1000
# maximum movement = 10%
# minimum movement = 0%
# output file = stock_data.csv

import random
import csv
min_price = 1
max_price = 9000
num_days = 1000
max_movement = 0.1
min_movement = 0.0
output_file = 'stock_data.csv'

def next_price(current_price):
    movement = random.uniform(min_movement, max_movement)
    delta = -5 + random.randint(0, 10)
    if random.random() < 0.45:
        movement = -movement
    return int(current_price * (1 + movement) + delta)

def clamp_price(price):
    return max(min(price, max_price), min_price)

def gen_data(num_days, start_price, output_file):
    # current_price = random.randint(min_price, max_price)
    current_price = start_price
    with open(output_file, 'w', encoding="utf-8") as f:
        # writer = csv.writer(f)
        for i in range(num_days):
            current_price = clamp_price(next_price(current_price))
            # writer.writerow([current_price])
            f.write(str(current_price) + '\n')

# main guard
if __name__ == '__main__':
    gen_data(1_000_000, 50,'stock_data.csv')