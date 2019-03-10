import os
import multiprocessing
from pathlib import Path
from tesseract import TesseractOCRJob
from manager import JobQueueManager

IMAGE_ROOT_DIR = "0001w1"
LANGUAGES = ["ara"]
TESSERACT_OUTPUT_ROOT_DIR = "out"
TESSERACT_STATUS_ROOT_DIR = "status"

os.environ["TESSDATA_PREFIX"] = str(Path("tessdata").absolute())
os.environ["OMP_THREAD_LIMIT"] = "1"

job_types = [
    TesseractOCRJob
]

tool_paths = {
    "tesseract_path": str(Path("tesseract-bin/bin/tesseract"))
}

def save_tesseract_output(job_queue_idx, return_code, stdout, stderr, duration):
    image_id = image_filepaths_absolute[job_queue_idx].stem
    print("Finished job - image_id={}, job_idx={}, returncode={}, duration={:.02f}s".format(image_id, job_queue_idx, return_code, duration))
    status_filepath = Path(TESSERACT_STATUS_ROOT_DIR, "{}.txt".format(image_id))
    with open(status_filepath, 'w') as status_file:
        status_text = "Return code: {}\n\nstdout:\n{}\n\nstderr:\n{}".format(return_code, stdout, stderr)
        status_file.write(status_text)

image_filepaths = list(Path(IMAGE_ROOT_DIR).iterdir())
image_filepaths_absolute = sorted([image_filepath.absolute() for image_filepath in image_filepaths])
output_filepaths_absolute = [Path(TESSERACT_OUTPUT_ROOT_DIR, image_filepath.stem).absolute() for image_filepath in image_filepaths_absolute]
num_of_images = len(image_filepaths)
jobs = [TesseractOCRJob(image_filepaths_absolute[i], output_filepaths_absolute[i], LANGUAGES) for i in range(num_of_images)]

num_of_worker_threads = multiprocessing.cpu_count()
jq_manager = JobQueueManager(num_of_worker_threads=num_of_worker_threads)
jq_manager.register_job_types(job_types, tool_paths)
job_queue_indices = [None] * len(jobs)
for i in range(len(jobs)):
    job_queue_indices[i] = jq_manager.add_job(jobs[i], save_tesseract_output)
jq_manager.process_queue()