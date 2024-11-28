import threading

class H2O:
    def __init__(self):
        self.hydrogen_semaphore = threading.Semaphore(2)
        self.oxygen_semaphore = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen) -> None:
        self.hydrogen_semaphore.acquire()
        
        self.barrier.wait()
        
        releaseHydrogen()
        
        self.hydrogen_semaphore.release()

    def oxygen(self, releaseOxygen) -> None:
        self.oxygen_semaphore.acquire()
        
        self.barrier.wait()
        
        releaseOxygen()
        
        self.oxygen_semaphore.release()

def releaseHydrogen():
    print("H", end="")

def releaseOxygen():
    print("O", end="")

h2o = H2O()

threads = []
for _ in range(6):
    threads.append(threading.Thread(target=h2o.hydrogen, args=(releaseHydrogen,)))
for _ in range(3):
    threads.append(threading.Thread(target=h2o.oxygen, args=(releaseOxygen,)))

for t in threads:
    t.start()


for t in threads:
    t.join()