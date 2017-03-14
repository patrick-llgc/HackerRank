#!/bin/python3

import sys

class Solution(object):
    def flatland_space_station(self):
        """Find the maximum of the shortest distance to a station for each city."""
        n,m = input().strip().split(' ')
        n,m = [int(n),int(m)]
        c = [int(c_temp) for c_temp in input().strip().split(' ')]
        max_value = -1
        for i_city in range(n):
            # iterate through all cities
            min_distance = min([abs(station - i_city) for station in c])
            if min_distance > max_value:
                max_value = min_distance
        return max_value
    def flatland_space_station2(self):
        """Alternative, faster way"""
        n,m = input().strip().split(' ')
        n,m = [int(n),int(m)]
        c = [int(c_temp) for c_temp in input().strip().split(' ')]
        max_value = -1
        # iterate through all stations, thus much faster if n >> m
        c = sorted(c)
        diffs = [(abs(c[i-1] - c[i]))//2 for i in range(1, len(c))]
        diffs.append(c[0])
        diffs.append(n - 1 - c[m-1])
        return max(diffs)

if __name__ == "__main__":
    max_value = Solution().flatland_space_station2()
    print(max_value)

