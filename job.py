from abc import ABCMeta, abstractmethod

class Job(metaclass=ABCMeta):
    class ToolNotFoundException(Exception):
        pass

    @abstractmethod
    def tool_path_key():
        pass

    @abstractmethod
    def tool_path(path):
        pass

    @abstractmethod
    def process(self, tool_path, job_queue_idx, queue_task_done_callback, job_callback):
        pass