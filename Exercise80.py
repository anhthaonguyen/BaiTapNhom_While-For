import random
def simulate_coin_flips():
    flips = []
    count = 0
    while True:
        flip = random.choice(['H', 'T'])
        flips.append(flip)
        count += 1
        if len(flips) < 3:
            continue
        if flips[-3] == flips[-2] == flips[-1]:
            return count

def main():
    num_simulations = 10
    total_flips = 0
    for i in range(num_simulations):
        flips = simulate_coin_flips()
        total_flips += flips
        print(''.join(flips), f'({flips} flips)')
    print(f'On average, {total_flips / num_simulations} flips were needed.')

if __name__ == '__main__':
    main()
