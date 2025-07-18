# leetcode 875
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Time Complexity:
# Space Complexity:

def kokoEatBananas(piles,h):
    low_speed = 1
    high_speed = max(piles)
    optimal_speed = high_speed
    max_hours = h

    while low_speed <= high_speed:
        current_speed = (low_speed + high_speed) // 2

        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + current_speed - 1) // current_speed

        if hours_needed <= max_hours:
            optimal_speed = current_speed
            high_speed = current_speed - 1
        else:
            low_speed = current_speed + 1

    return optimal_speed

print(kokoEatBananas([3,6,7,11],8))