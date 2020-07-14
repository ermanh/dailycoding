'''
2020-07-14
[from dailycodingproblems.com #41]

Given an unordered list of flights taken by someone, each represented as 
(origin, destination) pairs, and a starting airport, compute the person's 
itinerary. If no such itinerary exists, return null. If there are multiple 
possible itineraries, return the lexicographically smallest one. All flights 
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), 
('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return 
the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting 
airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 
and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] 
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the 
first one is lexicographically smaller.
'''

def get_itinerary(flights, itinerary):
    if not flights:
        return itinerary

    last_arrival = itinerary[-1]
    for i, (departure, arrival) in enumerate(flights):
        remaining_flights = flights[:i] + flights[i + 1:]
        itinerary.append(arrival)
        if departure == last_arrival:
            return get_itinerary(remaining_flights, itinerary)
        itinerary.pop()

    return None        

def get_first_itinerary(flights):
    itineraries = []
    for _ in range(len(flights)):
        flights = [flights.pop()] + flights
        for (departure, _) in flights:
            itinerary = get_itinerary(flights, [departure])
            if itinerary is not None:
                itineraries.append(itinerary)
    
    if len(itineraries) > 0:
        itineraries.sort()
        return itineraries[0]
    return []


'''
# TESTS
get_first_itinerary([]) == []
get_first_itinerary([('A', 'B')]) == ['A', 'B']
get_first_itinerary([('B', 'A'), ('A', 'B')]) == ['A', 'B', 'A']
get_first_itinerary([('B', 'A'), ('A', 'C')]) == ['B', 'A', 'C']

get_first_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
get_first_itinerary([('SFO', 'HKO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]) == []

get_first_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]) == ['A', 'B', 'C', 'A', 'C']
get_first_itinerary([('A', 'C'), ('B', 'C'), ('C', 'A'), ('A', 'B')]) == ['A', 'B', 'C', 'A', 'C']

'''
