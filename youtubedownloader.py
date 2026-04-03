# Youtube Downloader Script
# Usage examples:
# Video: python youtubedownloader.py <url>
# Audio: python youtubedownloader.py <url> --audio
# Custom name: python youtubedownloader.py <url> --name video123
# Quality: python youtubedownloader.py <url> --quality 720p
# Output dir: python youtubedownloader.py <url> --output /path/to/dir

import argparse
import yt_dlp
import os

def build_output_template(name=None, output_dir=None):
    """
    Build the final output template for the file.
    """
    filename = '%(title)s.%(ext)s'

    if name:
        filename = f'{name}.%(ext)s'

    if output_dir:
        return os.path.join(output_dir, filename)

    return filename


def download_video(url, name=None, output=None, fmt=None, quality=None):
    """
    Download video with audio.
    """
    outtmpl = build_output_template(name, output)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': outtmpl,
        'restrictfilenames': True,
        'noplaylist': False,
    }

    # If specific format is provided (ex: mp4, webm)
    if fmt:
        ydl_opts['format'] = fmt

    # If specific quality is provided (ex: 720p, 1080p)
    elif quality:
        try:
            height = int(quality.replace('p', ''))
            ydl_opts['format'] = f'bestvideo[height<={height}]+bestaudio/best'
        except ValueError:
            print("Invalid quality. Use format like 720p, 1080p")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_mp3(url, name=None, output=None):
    """
    Download audio only in MP3 format.
    """
    outtmpl = build_output_template(name, output)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'restrictfilenames': True,
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    parser = argparse.ArgumentParser(
        description='Download YouTube videos or extract audio (MP3).'
    )

    parser.add_argument('url', help='Video URL from YouTube')
    parser.add_argument('--audio', action='store_true',
                        help='Download audio only (MP3)')
    parser.add_argument('--name',
                        help='Custom filename (without extension)')
    parser.add_argument('--format',
                        help='Specific format (e.g., mp4, webm)')
    parser.add_argument('--quality',
                        help='Quality (e.g., 720p, 1080p)')
    parser.add_argument('--output',
                        help='Output directory (default: current directory)')

    args = parser.parse_args()

    if args.audio:
        download_mp3(
            args.url,
            name=args.name,
            output=args.output
        )
    else:
        download_video(
            args.url,
            name=args.name,
            output=args.output,
            fmt=args.format,
            quality=args.quality
        )


if __name__ == "__main__":
    main()