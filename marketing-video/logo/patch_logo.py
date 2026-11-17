p = 'logo2.html'
s = open(p).read()
subs = [
 ('<linearGradient id="gW" x1="0" y1="0" x2="0" y2="1">', '<linearGradient id="gW" gradientUnits="userSpaceOnUse" x1="0" y1="176" x2="0" y2="436">'),
 ('<linearGradient id="gB" x1="0" y1="0" x2="1" y2="1">', '<linearGradient id="gB" gradientUnits="userSpaceOnUse" x1="116" y1="150" x2="396" y2="436">'),
 ('<linearGradient id="gD" x1="0" y1="0" x2="1" y2="1">', '<linearGradient id="gD" gradientUnits="userSpaceOnUse" x1="116" y1="150" x2="396" y2="436">'),
 ('''    <circle cx="312" cy="306" r="60" fill="none" stroke="#000" stroke-width="13"/>
    <circle cx="312" cy="306" r="20" fill="#000"/>''', '''    <circle cx="300" cy="306" r="13.500" fill="#000"/>'''),
 ('''    <rect x="190" y="273" width="120" height="66"/>
    <circle cx="312" cy="306" r="53.500"/>''', '''    <path d="M190 273 H300 a33 33 0 0 1 0 66 H190 Z"/>'''),
 ('.av svg.m{width:800px;height:800px;position:relative}', '.av svg.m{width:900px;height:900px;position:relative}'),
 ('.lk svg.m{width:420px;height:420px;flex:none;margin:-40px -50px -40px -60px}', '.lk svg.m{width:540px;height:540px;flex:none;margin:-90px -80px -90px -100px}'),
]
for a, b in subs:
    assert a in s, a
    s = s.replace(a, b)
open(p, 'w').write(s)
