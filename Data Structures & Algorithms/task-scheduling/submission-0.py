import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = dict()
        for task in tasks:
            freq[task] = freq.get(task,0) + 1
        
        max_h = []
        # store a max heap of #appears: task

        for task, freq in freq.items():
            heapq.heappush(max_h, freq*-1)
            # values don't matter

        cycles = 0

        while max_h:
            remaining_tasks = []
            tasks_done = 0

            for _ in range(n+1):
                if max_h:
                    task_freq = heapq.heappop(max_h) * -1
                    task_freq -= 1
                    tasks_done += 1

                    if task_freq > 0:
                        remaining_tasks.append(task_freq)

            for task in remaining_tasks:
                heapq.heappush(max_h, task*-1)

            if max_h:
                # heap still has tasks
                cycles += n + 1
            else:
                cycles += tasks_done

        return cycles

        

                