# NYU-Class-File-Downloader

## Description
Python scripts that helps download all the files under the resources tab of a class.

## Dependencies
 - BS4
 - Selenium
 - Chrome
 - Chrome Driver
 
## Setup
Please make sure the two Chromedriver executable files are placed under the same folder with Python.exe and the chrome.exe. Replace the nyu_class.html with the actual html file of NYU Classes where the files are located and rename it as nyu_class.html before running the chrome_downloader.py script; fill in your NetId and Password inside chrome_downloader.py. After dependencies are installed, correct credentials are filled, and html file is supplied, run the chrome_downloader.py and it will automate the downloading process where you will be asked to approve the DUO MFA Verification. The project may add the feature to automatically bypass the Duo Verification in the future. Files will be at the downloads folder under the project folder.

## Notice
It does not download any file inside a subfolder of the folder that you provided.

## Contact
Reach me at [hncswpy@gmail.com](mailto:hncswpy@gmail.com)

