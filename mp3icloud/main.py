import glob
from argparse import Namespace
from pathlib import Path
from typing import List

from mutagen.easyid3 import EasyID3
from natsort import natsorted
from tqdm import tqdm


def get_files_in_directory(path='.', ext='mp3') -> List[str]:
    file_mask_to_search = f'{path}/*.{ext}'
    files = glob.glob(file_mask_to_search)
    return natsorted(files, key=lambda y: y.lower())


def update_meta(filepath, index, args) -> None:
    audio: EasyID3 = EasyID3(filepath)

    audio['title'] = Path(filepath).stem if args.use_filenames else index
    audio['album'] = args.album
    audio['artist'] = args.artist
    audio['genre'] = args.genre

    audio.save()


def main(args: Namespace):
    files = get_files_in_directory(path=args.directory)
    for index, file in enumerate(tqdm(files)):
        update_meta(file, index, args)
