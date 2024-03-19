class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-c for c in counter.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        print(maxHeap)
        while maxHeap or q:
            # increate time by one unit for one letter
            time += 1
            if maxHeap:
                # one occurance is processed, hence decrease count by 1
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: # check if cnt is not zero, if so, that means all occurances are done
                    # after competing one occurance, block that later for next n time unit
                    q.append([cnt, time + n])
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
