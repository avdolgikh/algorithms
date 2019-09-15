# Uses python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

test_cases = [
              { "buffer_size": 1,
               "requests": [],
               "output": [] },

              { "buffer_size": 1,
               "requests": [Request(0, 0)],
               "output": [0] },
    
              { "buffer_size": 1,
               "requests": [Request(0, 1), Request(0, 1)],
               "output": [0, -1] },

               { "buffer_size": 1,
               "requests": [Request(0, 1), Request(1, 1)],
               "output": [0, 1] },
               
               { "buffer_size": 2,
               "requests": [Request(0, 2), Request(1, 2), Request(3, 1)],
               "output": [0, 2, 4] },
               
               { "buffer_size": 1,
               "requests": [Request(0, 2), Request(1, 2), Request(3, 1)],
               "output": [0, -1, 3] },
               
                { "buffer_size": 1,
               "requests": [Request(0, 2), Request(1, 2), Request(2, 1)],
               "output": [0, -1, 2] },
               
                { "buffer_size": 4,
               "requests": [Request(0, 2), Request(1, 1), Request(2, 1), Request(2, 2), Request(3, 1), Request(3, 2)],
               "output": [0, 2, 3, 4, 6, 7] },
               
               { "buffer_size": 2,
               "requests": [Request(0, 2), Request(1, 4), Request(5, 3)],
               "output": [0, 2, 6] },

               { "buffer_size": 2,
               "requests": [Request(0, 2), Request(1, 1), Request(1, 1), Request(2, 2), Request(2, 1), Request(3, 1)],
               "output": [0, 2, -1, 3, -1, 5] },
            ]

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = [] # ~queue
        self.prev_arrived_at = -1        

    def process(self, request):
        now = request[0]

        if self.prev_arrived_at < now:
            # clean buffer from all finished items
            self.finish_time = [time for time in self.finish_time if time > now]

        self.prev_arrived_at = now

        time_to_process = request[1]
        
        prev_finish_time = 0
        if any(self.finish_time):
            prev_finish_time = self.finish_time[ len(self.finish_time) - 1 ]

        if now >= prev_finish_time:
            started_at = now
            finish_time = started_at + time_to_process
            self.finish_time.append(finish_time)
            return Response(False, started_at)

        elif len(self.finish_time) < self.size:
            started_at = prev_finish_time
            finish_time = started_at + time_to_process
            self.finish_time.append(finish_time)
            return Response(False, started_at)

        else:
            return Response(True, -1)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

def simulation(buffer_size, requests):
    buffer = Buffer(buffer_size)

    responses = process_requests(requests, buffer)

    output = []
    for response in responses:
        output.append(response.started_at if not response.was_dropped else -1)

    return output

def are_outputs_equal(output1, output2):
    if len(output1) != len(output2):
        return False

    for i in range(len(output1)):
        if output1[i] != output2[i]:
            return False
    
    return True

def test():
    for case in test_cases:
        output = simulation(case["buffer_size"], case["requests"])
        if not are_outputs_equal(output, case["output"]):
            print("buffer_size: {}, requests: {}, expected output: {}, actual output: {}".format(case["buffer_size"], case["requests"], case["output"], output))


if __name__ == '__main__':
    #test()

    requests = []
    buffer_size, n_requests = map(int, input().split())    
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    
    output = simulation(buffer_size, requests)
    
    for line in output:
        print(line)

