from pathlib import Path
from queue import Queue
from threading import Thread, Lock

class JobQueue(Queue):
    def __init__(self, threads, process_callback):
        super(JobQueue, self).__init__()
        self.__threads = threads
        self.__process_callback = process_callback

    def task_done(self, job_queue_idx):
        super(JobQueue, self).task_done()
        del self.__threads[job_queue_idx]
        self.__process_callback()


class JobQueueManager:

    def __init__(self, num_of_worker_threads=1):

        self.__num_of_worker_threads = num_of_worker_threads
        self.__threads = {}
        self.__queue = JobQueue(self.__threads, self.__process)
        self.__process_queue = False
        self.__job_queue_idx = 0
        self.__lock = Lock()
        self.__tool_paths = {}

    def register_job_types(self, job_classes, tool_paths):
        for job_class in job_classes:
            tool_path_key = job_class.tool_path_key()
            self.__tool_paths[tool_path_key] = job_class.tool_path(tool_paths[tool_path_key])

    def add_job(self, job, callback):
        job_queue_idx = self.__job_queue_idx
        self.__queue.put((job, callback, job_queue_idx))
        self.__job_queue_idx += 1
        self.__process()
        return job_queue_idx

    def process_queue(self):
        self.__process_queue = True
        self.__process()

    def __process(self):
        if not self.__process_queue:
            return
        while (not self.__queue.empty()) and (len(self.__threads) < self.__num_of_worker_threads):
            job, callback, job_queue_idx = self.__queue.get_nowait()
            tool_path_key = job.tool_path_key()
            tool_path = self.__tool_paths[tool_path_key]
            with self.__lock:
                thread = self.__threads[job_queue_idx] = Thread(target=job.process, args=
                [tool_path, job_queue_idx, self.__queue.task_done, callback])
            thread.start()

    def pause_queue(self):
        self.__process_queue = False

    def clear_queue(self):
        while not self.__queue.empty():
            self.__queue.get_nowait()
