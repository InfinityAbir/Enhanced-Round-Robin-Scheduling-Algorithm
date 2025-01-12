# Enhanced Round Robin Scheduling Algorithm (ERRS)

This repository contains a Python implementation of the **Enhanced Round Robin Scheduling Algorithm (ERRS)**. This version improves upon the traditional Round Robin algorithm by dynamically calculating a **variable time quantum** based on the **median of the burst times** of processes in the ready queue, leading to better CPU utilization and reduced waiting and turnaround times.

## Features

- Implements **Enhanced Round Robin Scheduling** with a variable time quantum.
- Dynamically adjusts the time quantum using the **median burst time** of processes in the ready queue.
- Computes key scheduling metrics:
  - Completion Time
  - Turnaround Time
  - Waiting Time
- Provides a detailed display of process statistics and averages.

## How It Works

1. **Input**:
   - Number of processes.
   - Burst time and arrival time for each process.

2. **Dynamic Quantum Calculation**:
   - For each scheduling cycle, the median of the burst times of processes in the ready queue is calculated.
   - This median is used as the time quantum for the current cycle.

3. **Process Execution**:
   - Processes are executed for the calculated median time quantum or until completion, whichever comes first.
   - Incomplete processes are returned to the queue.

4. **Output**:
   - Displays a summary of process statistics:
     - Burst Time (BT)
     - Arrival Time (AT)
     - Completion Time (CT)
     - Turnaround Time (TA)
     - Waiting Time (WT)
   - Computes and displays the **average turnaround time** and **average waiting time**.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Code
1. Clone the repository or download the `ERRS.py` file.
2. Run the script in your terminal:
   ```bash
   python ERRS.py
