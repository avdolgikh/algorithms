# python3

test_cases = [
                { "jobs": [1, 2, 3, 4, 5],
                  "n_workers": 2,
                  "output": [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)] },
                  
                { "jobs": [1, 2, 2, 1, 2, 4],
                  "n_workers": 2,
                  "output": [(0, 0), (1, 0), (0, 1), (1, 2), (0, 3), (1, 3)] },
                  
                { "jobs": [1] * 20,
                  "n_workers": 4,
                  "output": [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4)] },
                
                { "jobs": [0, 6, 10, 12, 7],
                  "n_workers": 2, 
                   "output": [(0, 0), (0, 0), (1, 0), (0, 6), (1, 10)] },
                
                { "jobs": [2, 14, 0, 12, 12, 10, 2, 7, 5],
                  "n_workers": 4,
                  "output": [(0, 0), (1, 0), (2, 0), (2, 0), (3, 0), (0, 2), (0, 12), (2, 12), (3, 12)] },

                { "jobs": [10, 8, 14, 0, 7, 10, 0],
                  "n_workers": 2,
                  "output": [(0, 0), (1, 0), (1, 8), (0, 10), (0, 10), (0, 17), (1, 22)] },
             ]

class Queue:
    def __init__(self, **kwargs):
        self.storage = []

    def get_size(self):
        return len(self.storage)

    def insert(self, worker_id, stop_time):
        self.storage.append((worker_id, stop_time))
        self.sift_up(len(self.storage) - 1)

    def extract(self):
        result = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        del self.storage[len(self.storage) - 1]
        self.sift_down(0)
        return result

    def sift_up(self, index):
        while index > 0:
            parent_index = self.parent(index)
            if self.storage[index][1] < self.storage[parent_index][1] or (self.storage[index][1] == self.storage[parent_index][1] and self.storage[index][0] < self.storage[parent_index][0]):
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
                index = parent_index
            else:
                break

    def sift_down(self, index):
        size = len(self.storage)
        min_index = index
        left = self.left_child(index)
        if left < size and ( self.storage[left][1] < self.storage[min_index][1] or (self.storage[left][1] == self.storage[min_index][1] and self.storage[left][0] < self.storage[min_index][0])):
            min_index = left
        right = self.right_child(index)
        if right < size and ( self.storage[right][1] < self.storage[min_index][1] or (self.storage[right][1] == self.storage[min_index][1] and self.storage[right][0] < self.storage[min_index][0])):
            min_index = right
        if index != min_index:
            self.storage[index], self.storage[min_index] = self.storage[min_index], self.storage[index]
            self.sift_down(min_index)

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

def process(jobs, n_workers):
    assigned_workers = [None] * len(jobs)
    start_times = [None] * len(jobs)
    next_free_time = [0] * n_workers

    for i in range(len(jobs)):
        available_worker = get_available_worker(n_workers, next_free_time)
        assigned_workers[i] = available_worker
        start_times[i] = next_free_time[available_worker]
        next_free_time[available_worker] += jobs[i]

    return assigned_workers, start_times

def get_available_worker(n_workers, next_free_time):
    next_worker = 0
    for j in range(n_workers):
        if next_free_time[j] < next_free_time[next_worker]:
            next_worker = j
    return next_worker

def process_queue(job_lengths, n_workers):
    assigned_workers = [None] * len(job_lengths)
    start_times = [None] * len(job_lengths)

    queue = Queue()

    worker_id = 0
    job_id = 0
    while worker_id < n_workers and job_id < len(job_lengths):
        stop_time = job_lengths[job_id]
        assigned_workers[job_id] = worker_id
        start_times[job_id] = 0
        if job_lengths[job_id] > 0:
            queue.insert(worker_id, stop_time)
            worker_id += 1
        job_id += 1
    
    while job_id < len(job_lengths):
        if queue.get_size() == n_workers:
            worker_id, start_time = queue.extract()

        stop_time = start_time + job_lengths[job_id]

        if job_lengths[job_id] > 0:
            queue.insert(worker_id, stop_time)

        assigned_workers[job_id] = worker_id
        start_times[job_id] = start_time

        job_id += 1

    return assigned_workers, start_times

def build_response(assigned_workers, start_times):
    response = []
    for i in range(len(assigned_workers)):
        response.append((assigned_workers[i], start_times[i]))
    return response

def test():
    for case in test_cases:
        assigned_workers, start_times = process_queue(case["jobs"], case["n_workers"])
        output = build_response(assigned_workers, start_times)
        if not are_outputs_equal(output, case["output"]):
            print("jobs: {}, n_workers: {}, expected output: {}, actual output: {}".format(case["jobs"], case["n_workers"], case["output"], output))

def stress_test():
    import numpy as np
    for _ in range(10000):
        n = np.random.randint(1, 5, 1, dtype=int)[0] # 10**5
        m = np.random.randint(1, 10, 1, dtype=int)[0] # 10**5
        t = np.random.randint(0, 15, m, dtype=int) # 10**9

        assigned_workers, start_times = process(t, n)
        output1 = build_response(assigned_workers, start_times)

        assigned_workers, start_times = process_queue(t, n)
        output2 = build_response(assigned_workers, start_times)

        if not are_outputs_equal(output1, output2):
            print("jobs: {}, n_workers: {}, expected output: {}, actual output: {}".format(t, n, output1, output2))
            break

def load_test():
    import numpy as np
    from time import perf_counter

    for _ in range(1000):
        n = np.random.randint(1, 10**5, 1, dtype=int)[0]
        m = np.random.randint(1, 10**5, 1, dtype=int)[0]
        t = np.random.randint(0, 10**9, m, dtype=int)

        time = perf_counter()
        assigned_workers, start_times = process_queue(t, n)
        print(perf_counter() - time)

def are_outputs_equal(output1, output2):
    if len(output1) != len(output2):
        return False
    for i in range(len(output1)):
        if output1[i][0] != output2[i][0] or output1[i][1] != output2[i][1]:
            return False    
    return True

if __name__ == '__main__':
    test()
    #stress_test()
    #load_test()

    #n, m = map(int, input().split()) #  n independent threads to process the given list of m jobs
    #t = [int(x) for x in input().split()]  #  the times in seconds it takes any thread to process i-th job. 
    
    #assigned_workers, start_times = process_queue(t, n)
    
    #for i in range(len(t)):
    #    print(assigned_workers[i], start_times[i])
