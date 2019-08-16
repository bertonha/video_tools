# Video Compressor

Converts MP4 videos to H.265 with 28 fixed frames per second

This app deprends of ffmpeg on your path to proper execute.
It's possible to compress a single video or all videos recursivile from a folder

## Install
```
python setup.py install
```

## Execute
```
video_compress <path of videos>
```

If you want to delete the original video after the compression
```
video_compress --delete <path of videos>
```
