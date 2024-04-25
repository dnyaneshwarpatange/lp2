def printJobScheduling(arr, t):
    n = len(arr)
    # Sorting the jobs in descending order based on profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = [False] * t
    job = ['-1'] * t

    # Scheduling the jobs
    for i in range(len(arr)):
        # Finding the earliest available time slot for each job
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                # Assigning the job to the available time slot
                result[j] = True
                job[j] = arr[i][0]
                break

    print(job)

if __name__ == '__main__':
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print("Following is the maximum profit sequence of jobs")
    printJobScheduling(arr, 3)











































# The printJobScheduling function takes two arguments: arr, which represents an array of jobs with their respective durations and profits, and t, which represents the total number of time slots available.

# The function starts by sorting the arr array in descending order based on the profit of each job. It uses a bubble sort algorithm for this purpose. The inner loop compares adjacent jobs based on their profit (arr[j][2] and arr[j + 1][2]) and swaps them if the first job has a lower profit.

# Next, the function initializes two arrays: result and job. result is a boolean array of length t, representing the availability of each time slot. job is an array of length t, initially filled with '-1', which will store the scheduled jobs.

# The function iterates over each job in the sorted arr array. For each job, it starts from the minimum of t - 1 and the difference between the job's duration (arr[i][1]) and 1, and then goes down to 0. This loop helps find the earliest available time slot for each job.

# Inside the nested loop, it checks if the current time slot j is available (result[j] is False). If it is available, it marks the time slot as occupied (result[j] = True), assigns the job's identifier to the corresponding position in the job array (job[j] = arr[i][0]), and breaks out of the loop.

# After iterating through all the jobs, the function prints the job array, which represents the sequence of jobs scheduled in the available time slots.

# The code block at the end initializes an example arr array with job details and calls the printJobScheduling function with arr and the number of time slots t set to 3.