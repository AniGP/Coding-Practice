class RecentCounter:

    def __init__(self):
        self.queue = deque() # Empty Queue to hold the timestamps

    def ping(self, t: int) -> int:

        # Append the current timesstamp to the deque
        self.queue.append(t)

        # Remove timestamps that are outside the [t-3000, t] range
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue) # The size of the queue is the number 
        # of pings in the last 3000 ms
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

recentCounter = RecentCounter()
print(recentCounter.ping(1))    # Should return 1
print(recentCounter.ping(100))  # Should return 2
print(recentCounter.ping(3001)) # Should return 3
print(recentCounter.ping(3002)) # Should return 3


'''

Credits(on explaining the logic, I did not understand the problem description at all): 
https://leetcode.com/problems/number-of-recent-calls/description/comments/1905405

Here's how it works:

When you create an instance of the RecentCounter class using RecentCounter(), it initializes the counter with zero recent requests.
The ping(int t) method is used to add a new request at time t and returns the number of requests that have occurred within the past 3000 milliseconds (including the new request).
Each time you call the ping method with a new time t, it adds the request to a list of requests and calculates the number of requests within the inclusive range of [t - 3000, t].
Let's go through the provided example to see how it works:

1.First, you create an instance of RecentCounter called recentCounter using RecentCounter().

2.Then, you call recentCounter.ping(1), which adds a new request at time 1 and returns the number of requests in the range [-2999, 1]. Since there's only one request (1) in that range, the return value is 1.

3.Next, you call recentCounter.ping(100), which adds another request at time 100 and returns the number of requests in the range [-2900, 100]. Now there are two requests (1 and 100) in that range, so the return value is 2.

4.Then, you call recentCounter.ping(3001), adding a request at time 3001 and calculating the number of requests in the range [1, 3001]. At this point, there are three requests (1, 100, and 3001) within that range, so the return value is 3.

5.Finally, you call recentCounter.ping(3002), adding a request at time 3002 and calculating the number of requests in the range [2, 3002]. Since all the requests fall within this range (1, 100, 3001, and 3002), the return value is still 3.
So, as you can see, the ping method keeps track of the requests made within the past 3000 milliseconds and returns the count of requests within the specified range.

Time Complexity: 

- O(1), on average for each call to ping, because while the while-loop may seem like it could take longer, each element is added and removed from the deque only once.

Space Complexity:

- O(N), where N is the number of elements in the queue at any given time. This is bounded by the number of pings that can occur in any 3000 millisecond period. In the worst case, this could be up to the maximum number of pings allowed within that window.

'''