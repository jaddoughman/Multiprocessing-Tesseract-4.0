import time
from subprocess import Popen, PIPE
from pathlib import Path
from job import Job

class TesseractOCRJob(Job):

    class TesseractNotFoundException(Job.ToolNotFoundException):
        pass

    TOOL_PATH_KEY = "tesseract_path"
    DEFAULT_TESSERACT_PATH = "/usr/bin/tesseract"

    @staticmethod
    def tool_path_key():
        return TesseractOCRJob.TOOL_PATH_KEY

    @staticmethod
    def tool_path(path=None):
        try:
            if path is None:
                tesseract_path_obj = Path(TesseractOCRJob.DEFAULT_TESSERACT_PATH)
            else:
                tesseract_path_obj = Path(path)
            assert tesseract_path_obj.exists()

            try:
                assert tesseract_path_obj.is_file()
            except AssertionError:
                tesseract_path = str(tesseract_path_obj) + "/tesseract"
                tesseract_path_obj = Path(tesseract_path)
                assert tesseract_path_obj.exists()

            tesseract_path = str(tesseract_path_obj)
            return tesseract_path
        except AssertionError:
            raise TesseractOCRJob.TesseractNotFoundException

    def __init__(self, image_filepath, output_filepath, languages):
        language_arg = "+".join(languages)
        self.__args = [None, str(image_filepath), str(output_filepath), "-l", language_arg]

    def process(self, tool_path, job_queue_idx, queue_task_done_callback, job_callback):
        self.__args[0] = tool_path
        start_time = time.time()
        process = Popen(self.__args, stdout=PIPE, stderr=PIPE)
        process.wait()
        duration = time.time() - start_time
        return_code = process.returncode
        stdout = process.stdout.read()
        stderr = process.stderr.read()

        stdout_text = stdout.decode('utf-8')
        stderr_text = stderr.decode('utf-8')

        queue_task_done_callback(job_queue_idx)
        job_callback(job_queue_idx, return_code, stdout_text, stderr_text, duration)