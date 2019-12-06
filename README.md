# Multi-Processing Tesseract 4.0
In an effort to decrease the execution time of the OCR process, a multi-processing script was created using Python's multi-processing module. The script spawns several worker threads, each constantly processing the Tesseract 4.0 OCR jobs appeneded to the job queue by the JobQueueManager. 

## Brief history

Tesseract was originally developed at Hewlett-Packard Laboratories Bristol and
at Hewlett-Packard Co, Greeley Colorado between 1985 and 1994, with some
more changes made in 1996 to port to Windows, and some C++izing in 1998.
In 2005 Tesseract was open sourced by HP. Since 2006 it is developed by Google.

The latest (LSTM based) stable version is **[4.1.0](https://github.com/tesseract-ocr/tesseract/releases/tag/4.1.0)**, released on July 7, 2019. Latest source code is available from [master branch on GitHub](https://github.com/tesseract-ocr/tesseract/tree/master). Open issues can be found in [issue tracker](https://github.com/tesseract-ocr/tesseract/issues), and [Planning wiki](https://github.com/tesseract-ocr/tesseract/wiki/Planning).

The latest 3.5 version is **[3.05.02](https://github.com/tesseract-ocr/tesseract/releases/tag/3.05.02)**, released on June 19, 2018. Latest source code for 3.05 is available from [3.05 branch on GitHub](https://github.com/tesseract-ocr/tesseract/tree/3.05). There is no development for this version, but it can be used for special cases (e.g. see [Regression of features from 3.0x](https://github.com/tesseract-ocr/tesseract/wiki/Planning#regression-of-features-from-30x)).

See **[Release Notes](https://github.com/tesseract-ocr/tesseract/wiki/ReleaseNotes)** and **[Change Log](https://github.com/tesseract-ocr/tesseract/blob/master/ChangeLog)** for more details of the releases.

## Installing Tesseract

You can either [Install Tesseract via pre-built binary package](https://github.com/tesseract-ocr/tesseract/wiki) or [build it from source](https://github.com/tesseract-ocr/tesseract/wiki/Compiling).

Supported Compilers are:

* GCC 4.8 and above
* Clang 3.4 and above
* MSVC 2015, 2017, 2019

Other compilers might work, but are not officially supported.

## Usage

* Install [Tesseract 4.0](https://github.com/tesseract-ocr/)
* Add tessdata of your desired language to the *tessdata* directory
* Import your input images to the *input* directory
* Run main.py [python3 main.py]
   
