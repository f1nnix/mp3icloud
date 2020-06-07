# mp3icloud

Tiny script for audio ID3v2 metatag normalization, which allows imported to Apple Music Library files preserve sort order.

## Why

When you upload some audiobook to Apple Music Library, it's common all MP3 files have no porper ID3v2 tags. So, after improting all of them look like "Alice In Wonderland 000", and chapters order is ruined.

This script allows to bulk rename tags for all files in directory and set some name, which can preserve order:

1. name with file index, like `01`, `02`, `03`, ...
2. keep original filename if, for example, it has chapter title.

This script was written literally for 15 minutes to upload old MP3 audiobook to Apple Music Library, so do what you want. I'm happy, if someone also finds it useful.

# Install

Clone repo, then:

```
pipenv --three
pipenv shell
```

# Run

```
python -m mp3icloud -h
usage: __main__.py [-h] [--use-filenames] directory artist album genre

Tiny script for audio ID3v2 metatag normalization, which allows imported to
Apple Music Library files preserve sort order.

positional arguments:
  directory        Directory with mp3 files. E.g.
                   "/home/f1nnix/alice_audiobook"
  artist           Artist set for all tracks. E.g. "Lewis Carroll"
  album            Album to set for all books, e.g. "Alice in Wonderland"
  genre            Genre to set for all books, e.g. "Audiobook"

optional arguments:
  -h, --help       show this help message and exit
  --use-filenames  Preserve original filename as title tag
```

By default mp3icloud just renames all files in provided directory to numbers, e.g. 1,2,3,... `--use-filenames` options allows to use actual filenames as titles, if they have sortable title.

Example run:

```
python -m mp3icloud \
  '/home/f1nnix/alice_audiobook' \
  'Lewis Carroll' 'Alice\'s Adventures in Wonderland' 'Audiobook' \
  --use-filenames

100%|██████████████████████████████████████| 235/235 [00:16<00:00, 14.35it/s]
```
