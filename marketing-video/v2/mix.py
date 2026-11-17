"""Builds out/audio.wav: music bed + timed sound design."""
import subprocess
S = 'audio/sfx/'
cues = [  # (file, time, volume)
 ('stamp', .5, .7), ('stamp', 1.5, .7), ('stamp', 2.5, .8), ('riser', 2.0, .55), ('impact', 4.0, 1.0), ('shimmer', 4.05, .5),
 ('whoosh2', 5.5, .8), ('counter', 7.1, .3), ('whoosh', 9.75, .8), ('whoosh', 11.8, .7), ('counter', 12.2, .25), ('whoosh', 13.8, .7),
 ('ding', 14.15, .45), ('ding', 14.45, .4), ('ding', 14.75, .4), ('ding', 15.05, .4), ('ding', 15.35, .4),
 ('whoosh2', 15.6, .8), ('tap', 16.05, .9), ('whoosh', 17.75, .5), ('tap', 18.05, .9), ('whoosh', 19.75, .5), ('tap', 20.05, .9), ('whoosh', 21.75, .5), ('tap', 22.05, .9),
 ('whoosh2', 23.6, .9), ('counter', 24.25, .35), ('whoosh', 25.95, .5), ('ding', 28.0, .6), ('ding', 29.0, .6), ('ding', 30.0, .6),
 ('whoosh2', 31.5, .9), ('whoosh', 37.5, .8), ('stamp', 38.98, 1.0), ('impact', 39.0, .5), ('success', 39.1, .7), ('tap', 40.0, .8), ('tap', 40.5, .8), ('tap', 41.0, .8),
 ('whoosh2', 43.5, .9), ('shimmer', 44.1, .6), ('whoosh', 45.7, .8), ('ding', 46.5, .5), ('ding', 47.0, .5), ('riser', 46.0, .6),
 ('glitch', 47.95, .9), ('impact', 48.0, 1.0), ('alarm', 48.2, .7), ('glitch', 48.5, .3), ('glitch', 49.0, .3), ('whoosh', 49.65, .8),
 ('typing', 50.25, .7), ('error', 50.97, .8), ('typing', 51.3, .7), ('error', 52.02, .8), ('typing', 52.35, .7), ('error', 53.07, .8), ('typing', 53.35, .7), ('success', 54.0, .9),
 ('whoosh2', 54.65, .8), ('stamp', 55.15, .7), ('whoosh2', 56.15, .8), ('stamp', 56.65, .7), ('whoosh2', 57.65, .8), ('impact', 58.0, .7),
 ('riser', 62.0, .6), ('impact', 64.0, 1.0), ('shimmer', 64.1, .6), ('whoosh', 65.0, .5), ('tap', 66.5, .9), ('ding', 66.55, .5),
]
inputs = ['-i', 'audio/music.mp3']
fc = ['[0:a]atrim=start=0.05,asetpts=PTS-STARTPTS,volume=0.80,afade=t=in:d=0.15,afade=t=out:st=71.2:d=0.8[m]']
labels = ['[m]']
for i, (f, t, v) in enumerate(cues, 1):
    inputs += ['-i', f'{S}{f}.mp3']
    fc.append(f'[{i}:a]aformat=channel_layouts=stereo,volume={v},adelay={int(t*1000)}:all=1[s{i}]')
    labels.append(f'[s{i}]')
fc.append(''.join(labels) + f'amix=inputs={len(labels)}:normalize=0:duration=first,alimiter=limit=0.9,loudnorm=I=-14:TP=-1.5:LRA=11[a]')
cmd = ['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[a]', '-t', '72', '-ar', '48000', 'out/audio.wav']
subprocess.run(cmd, check=True)
print('ok')
