# Video Tools

Tools to converts videos to mp4 with codec H.265 with 28 fixed frames per second

This app deprends of ffmpeg on your path to proper execute.
To install ffmpeg please refer to it's website
It's possible to compress a single video or all videos recursively from a folder

## Install
```
python setup.py install
```

## Compress
```
video_tools compress <path of videos>
```

If you want to delete the original video after the compression
```
video_tools compress --delete <path of videos>
```

## Cleanup
Remove Windows and macOS meta files

```
video_tools cleanup <PATH>
```

## Counter
Show total of files per extension

Has the option to show the files with `--verbose`
```
video_tools count <PATH>
```

```
video_tools count <PATH> .mp4 .mov
```
