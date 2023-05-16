import logging
import random
import threading
import time

TOTAL_TICKETS = 10
TICKETS_LEFT = 50

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            if TICKETS_LEFT != 0 and TOTAL_TICKETS <= 4:
                continue
            else:
                with self.sem:
                    if TOTAL_TICKETS <= 0:
                        break
                    self.tickets_sold += 1
                    TOTAL_TICKETS -= 1
                    logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')

        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))

class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.max_tickets = TICKETS_LEFT
        self.tickets_added = 0
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        global TICKETS_LEFT
        is_running = True
        while is_running:
            if TOTAL_TICKETS <= 4:
                with self.sem:
                    tickets_to_print = min(TICKETS_LEFT, 10 - TOTAL_TICKETS)
                    TOTAL_TICKETS += tickets_to_print
                    TICKETS_LEFT -= tickets_to_print
                    self.tickets_added += tickets_to_print
                    logger.info(f'Director added {tickets_to_print} tickets; {TICKETS_LEFT} left')
                    if TICKETS_LEFT == 0:
                        is_running = False
        logger.info(f'Director printed {self.tickets_added} tickets')

def main():
    semaphore = threading.Semaphore()
    sellers = []

    director = Director(semaphore)
    director.start()

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()

if __name__ == '__main__':
    main()