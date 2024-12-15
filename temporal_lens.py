# temporal_lens.py
# A mysterious utility for peering into the flow of time.

def distort_time(factor: float):
    if factor == 0:
        raise ValueError("Time cannot be stopped in this universe.")
    print(f"Time is distorted by a factor of {factor}. The flow bends to Pendulum's will.")

def reflect_time():
    print("Time reflects upon itself, casting shadows of the past into the future.")

# Placeholder for demonstration
if __name__ == "__main__":
    distort_time(1.5)
    reflect_time()
