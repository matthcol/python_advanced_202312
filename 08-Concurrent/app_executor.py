from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from time import sleep
from typing import Sequence, List, Iterator, Tuple, Dict


def f():
    sleep(2)
    print('coucou')
    
def sum_part(data: Sequence[int], start: int, end: int) -> int:
    sleep(2)
    return sum(data[i] for i in range(start, end))

def play2_sum() -> None:
    data = list(range(10_000_000))
    with ThreadPoolExecutor(max_workers=5) as pool:
        parts = 20
        chunk = len(data) // parts
        jobs: List[Future[int]] = [
            pool.submit(sum_part, data, start=i*chunk, end=(i+1)*chunk)
            for i in range(parts)
        ]
        print("Jobs started:", jobs) # 5 running, other pending
        # wait for results
        sums = [ job.result() for job in jobs ]
        print("Results:", sums)
                
def play3_sum_map() -> None:
    data = list(range(10_000_000))
    with ThreadPoolExecutor(max_workers=5) as pool:
        parts = 20
        chunk = len(data) // parts
        resultsIt: Iterator[int] = pool.map(
            lambda args_dict: sum_part(**args_dict), 
            ({ 
                "data":data, 
                "start": i*chunk, 
                "end": (i+1)*chunk
            } for i in range(parts)))
        print("Jobs started") # 5 running, other pending
        # wait for results
        sums = [ s for s in resultsIt ]
        print("Results:", sums)

def play4_sum_as_completed() -> None:
    data = list(range(10_000_000))
    with ThreadPoolExecutor(max_workers=5) as pool:
        parts = 20
        chunk = len(data) // parts
        jobs_args: Dict[Future[int], Tuple[int,int,int]] = {
            pool.submit(sum_part, data, start=i*chunk, end=(i+1)*chunk): 
                (i, i*chunk, (i+1)*chunk) 
            for i in range(parts)
        }
        print("Jobs started")
        # wait for results
        for future_sum in as_completed(jobs_args):
            i, start, end = jobs_args[future_sum]
            sum_res = future_sum.result()
            print(i,start,end,sum_res)
            

def play1() -> None:
    # NB: without max_workers, adapt to OS/CPU
    with ThreadPoolExecutor(max_workers=5) as pool:
        # auto: call pool.__enter__()
        print(f"Pool started with pool._max_workers: {pool._max_workers}")
        for _ in range(7):
            pool.submit(f)
    # auto: call pool.__exit__() => pool.shutdown()
    
def run() -> None:
    # play1()
    # play2_sum()
    # play3_sum_map()
    play4_sum_as_completed()
    
if __name__ == '__main__':
    run()