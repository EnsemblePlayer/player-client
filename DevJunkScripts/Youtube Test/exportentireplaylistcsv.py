import youtube_dl
import pandas as pd
import os
import traceback


options = {
    'format': 'bestaudio', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': '%(id)s',        # name the file the ID of the video
    'noplaylist' : True,}       # only download single song, not playlist
ydl = youtube_dl.YoutubeDL(options)

with ydl:

    # read in videos CSV with pandas
    df = pd.read_csv(CSV, sep=";", skipinitialspace=True)
    df.Link = df.Link.map(str.strip)  # strip space from URLs

    # for each row, download
    for _, row in df.iterrows():
        print "Downloading: %s from %s..." % (row.Title, row.Link)

        # download location, check for progress
        savepath = make_savepath(row.Title, row.Artist)
        try:
            os.stat(savepath)
            print "%s already downloaded, continuing..." % savepath
            continue

        except OSError:
            # download video
            try:
                result = ydl.extract_info(row.Link, download=True)
                os.rename(result['id'], savepath)
                print "Downloaded and converted %s successfully!" % savepath

            except Exception as e:
                print "Can't download audio! %s\n" % traceback.format_exc()