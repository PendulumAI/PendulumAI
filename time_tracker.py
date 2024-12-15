# time_tracker.py
# Tracks the ever-shifting perception of time through AI.

import datetime

class TimeTracker:
    def __init__(self):
        self.timestamps = []

    def record_event(self, event_description: str):
        timestamp = datetime.datetime.now()
        self.timestamps.append((event_description, timestamp))
        print(f"Event recorded: '{event_description}' at {timestamp}")

    def show_timeline(self):
        print("Pendulum's Timeline:")
        for event, time in self.timestamps:
            print(f"- {time}: {event}")

# Example usage
if __name__ == "__main__":
    tracker = TimeTracker()
    tracker.record_event("Pendulum initialized.")
    tracker.show_timeline()
