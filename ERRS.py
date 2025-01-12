from collections import deque

class Process:
    def __init__(self, id, burst_time, arrival_time):
        self.id = id
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_median(processes, ready_queue):
    """
    Calculates the median burst time of processes in the ready queue.

    Args:
        processes: A list of Process objects.
        ready_queue: A queue containing process indices.

    Returns:
        The median burst time.
    """
    burst_times = []
    temp_queue = deque(ready_queue)

    while temp_queue:
        burst_times.append(processes[temp_queue.popleft()].remaining_time)

    burst_times.sort()
    size = len(burst_times)
    if size % 2 == 0:
        return burst_times[size // 2]  # Higher middle for even-sized list
    else:
        return burst_times[size // 2]  # Middle for odd-sized list

def enhanced_round_robin(processes):
    """
    Simulates the Enhanced Round Robin Scheduling algorithm.

    Args:
        processes: A list of Process objects.
    """
    time = 0
    ready_queue = deque()

    # Add all processes to the ready queue initially
    for i, process in enumerate(processes):
        ready_queue.append(i)

    while ready_queue:
        median_quantum = calculate_median(processes, ready_queue)  # Calculate median time quantum

        process_index = ready_queue.popleft()
        current_process = processes[process_index]

        if current_process.remaining_time <= median_quantum:
            # Process can finish within the current time quantum
            time += current_process.remaining_time
            current_process.remaining_time = 0
            current_process.completion_time = time
            current_process.turnaround_time = time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        else:
            # Process needs to be preempted
            time += median_quantum
            current_process.remaining_time -= median_quantum
            ready_queue.append(process_index)  # Place process back in the ready queue

def display_results(processes):
    """
    Displays the results of the scheduling algorithm.
    """
    total_turnaround_time = 0
    total_waiting_time = 0

    print("PID\t\tBT\t\tAT\t\tCT\t\tTA\t\tWT")
    for process in processes:
        print(f"{process.id}\t\t{process.burst_time}\t\t{process.arrival_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    print(f"\nAverage Turnaround Time: {total_turnaround_time / len(processes)}")
    print(f"Average Waiting Time: {total_waiting_time / len(processes)}")

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        processes.append(Process(i+1, burst_time, arrival_time))

    enhanced_round_robin(processes)
    display_results(processes)