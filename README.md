# Multiprocessing-Tesseract-4.0
Multiprocessing Tesseract 4.0 for large number of images.

Performing OCR by running parallel instances of Tesseract 4.0. 

Steps: 
   1) Install Tesseract 4.0 from package manager [brew install tesseract-ocr]]
   2) Add tessdata of your desired language to tessdata directory
   3) Import your input images to "input" directory
   4) Optional: change num_of_worker_threads = the number of cores of your machine
   5) Run main.py [python3 main.py]
   
