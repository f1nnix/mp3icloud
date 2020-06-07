import argparse

from mp3icloud.main import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tiny script for audio ID3v2 metatag normalization, which allows imported to Apple Music Library files preserve sort order.')

    parser.add_argument('directory', type=str, help='Directory with mp3 files. E.g. "/home/f1nnix/alice_audiobook"')
    parser.add_argument('artist', type=str, help='Artist set for all tracks. E.g. "Lewis Carroll"')
    parser.add_argument('album', type=str, help='Album to set for all books, e.g. "Alice in Wonderland"')
    parser.add_argument('genre', type=str, help='Genre to set for all books, e.g. "Audiobook"')
    parser.add_argument('--use-filenames', dest='use_filenames', action='store_true', default=False,
                        help="Preserve original filename as title tag")

    args = parser.parse_args()

    main(args)
