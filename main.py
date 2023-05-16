# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from pathlib import Path
import shutil
os.chdir('C:/Users/sumit1234/Downloads')

if not os.path.exists('Documents'):
    os.mkdir('Documents')
if not os.path.exists('Webpages'):
    os.mkdir('Webpages')
if not os.path.exists('Subtitles'):
    os.mkdir('Subtitles')
if not os.path.exists('Executables and Installers'):
    os.mkdir('Executables and Installers')
if not os.path.exists('Zip'):
    os.mkdir('Zip')
if not os.path.exists('Images'):
    os.mkdir('Images')
if not os.path.exists('Videos'):
    os.mkdir('Videos')
if not os.path.exists('Other'):
    os.mkdir('Other')
for file in os.listdir():
    if file=="Document_files" or file=="My portfolio_files":
        continue
    name,ext=os.path.splitext(file)
    ext=ext.strip()
    if ext=='.png'or ext==".jpg" or ext==".jpeg":
        shutil.move(file,"Images")

    elif(ext=='.zip'):
        shutil.move(file,"ZIP")
    elif(ext=='.pdf') or ext=='.docx':
        shutil.move(file,"Documents")
    elif(ext=='.html'):
        shutil.move(file,"Webpages")
    elif(ext=='.exe') or ext=='.msi':
        shutil.move(file,"Executables and Installers")
    elif(ext=='.mp4'):
        shutil.move(file,"Videos")
    elif ext=='.srt':
        shutil.move(file,"Subtitles")
    else:
        shutil.move(file,'Other')



