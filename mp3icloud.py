#!/usr/bin/env python3
import sys, glob, os
from subprocess import call
import errno
import os
from natsort import natsorted, ns

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

try:
  workdir = sys.argv[1]
  author = sys.argv[2]
  album = sys.argv[3]
  genre = sys.argv[4]
except Exception as e:
  print("""[ERROR] At least 4 positional params should be provided:

* workdir
* author
* album
* genre
* rename song names based on album? - optional, 'yes'/<empty>

Example:

  ./update_tags3.py 'Стивен Кинг/После выпускного' 'Стивен Кинг' 'После выпускного' 'Audiobook' yes""")
  print('\nExiting...')
  sys.exit()

try:
  reorder_songs = True if sys.argv[5] else False
except Exception as e:
  reorder_songs = False


print("""
workdir\t%s
author\t%s
album\t%s
genre\t%s
rename\t%s
  """ % (workdir, author, album, genre, reorder_songs))

files = glob.glob(workdir + '/*.mp3')
files = natsorted(files, key=lambda y: y.lower())
# files = sorted( os.listdir(workdir) )
# print(files)
for index, file in enumerate(files):
  basedir = os.path.dirname(file)
  basename = os.path.basename(file)
  filename, file_extension = os.path.splitext(basename)
  output_dir = "%s/output" % basedir

  # print(filename, file_extension)

  mkdir_p(output_dir)

  if len(files) > 99:
    _index = "%03d" % (index + 1,)
  elif len(files) > 9:
    _index = "%02d" % (index + 1,)
  else:
    _index = "%01d" % (index + 1,)

  output_filename = "%s - %s" % (_index, album) if reorder_songs == True else basename

  call([
    'lame -b 192 "%s" "%s/%s"' % (file, output_dir, output_filename + ".mp3")
  ], shell=True)


  call([
    'mid3v2 --artist="%s" --album="%s" --song="%s" --genre="%s" "%s"' % (author, album, output_filename, genre, "%s/%s" % (output_dir, output_filename + ".mp3") )
    ], shell=True)
