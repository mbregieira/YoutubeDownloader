# YouTube Downloader Script

A simple Python script to download YouTube videos or extract audio in
MP3 format using `yt-dlp`.

## Requirements

-   Python 3.x
-   yt-dlp
-   ffmpeg (required for audio extraction)

### Install dependencies

``` bash
pip install yt-dlp
```

Install ffmpeg:

-   Linux:

``` bash
sudo apt install ffmpeg
```

-   Windows: Download from https://ffmpeg.org and add it to your PATH.

------------------------------------------------------------------------

## Usage

### Download video (default)

``` bash
python youtubedownloader.py <url>
```

### Download audio only (MP3)

``` bash
python youtubedownloader.py <url> --audio
```

### Specify custom filename

``` bash
python youtubedownloader.py <url> --name video123
```

### Specify quality

``` bash
python youtubedownloader.py <url> --quality 720p
```

### Specify format

``` bash
python youtubedownloader.py <url> --format mp4
```

### Specify output directory

``` bash
python youtubedownloader.py <url> --output /path/to/directory
```

------------------------------------------------------------------------

## Arguments

  ------------- -----------------------------------------
  `url`         YouTube video or playlist URL
  `--audio`     Download audio only (MP3 format)
  `--name`      Custom filename (without extension)
  `--format`    Force specific format (e.g., mp4, webm)
  `--quality`   Limit video quality (e.g., 720p, 1080p)
  `--output`    Output directory

------------------------------------------------------------------------

## How it works

-   Uses `yt-dlp` to download video/audio streams
-   Selects best available quality by default
-   Uses `ffmpeg` to extract and convert audio to MP3
-   Supports playlists automatically

------------------------------------------------------------------------

## Notes

-   Quality values like `720p` are internally converted to a height
    filter
-   If both `--format` and `--quality` are provided, `--format` takes
    priority
-   Filenames are restricted to safe characters using
    `restrictfilenames=True`

------------------------------------------------------------------------

## Legal Disclaimer

Downloading content from YouTube may violate its Terms of Service. Use
this tool only for content you own or have permission to download.
