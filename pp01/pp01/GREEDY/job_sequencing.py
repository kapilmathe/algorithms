# https://www.geeksforgeeks.org/job-sequencing-using-disjoint-set-union/
def sorting_key(job):
    return job[2]

def job_sequencing(d, p):
    n = len(d)
    jobs = zip(list(range(n)), d, p)
    jobs = sorted(jobs, key=sorting_key)
    buckets = [None]*n
    print(jobs)
    for job in jobs:
        bucket = job[1]-1
        if buckets[bucket] is None:
            buckets[bucket] = job[0]
        else:
            while bucket > 0:
                bucket -= 1
                if buckets[bucket] is None:
                    buckets[bucket] = job[0]
                    break
    return buckets



