p = 'blue.html'
s = open(p).read()
a = s.index('<!-- 1: squircle'); b = s.index('<!-- 4: motion E')
S = 'fill="none" stroke="currentColor" stroke-width="36" stroke-linecap="round" stroke-linejoin="round"'
new = f'''<!-- 1: squircle E with card slots -->
  <mask id="k1" maskUnits="userSpaceOnUse" x="0" y="0" width="240" height="240"><rect x="20" y="20" width="200" height="200" rx="56" fill="#fff"/>
    <path fill="#000" d="M103 72 a11 11 0 0 0 0 22 H240 V72 Z M103 146 a11 11 0 0 0 0 22 H240 V146 Z M172 90 a30 30 0 0 0 0 60 H240 V90 Z"/></mask>
  <symbol id="m1" viewBox="0 0 240 240"><rect width="240" height="240" fill="currentColor" mask="url(#k1)"/></symbol>
  <!-- 2: bracket + coin -->
  <symbol id="m2" viewBox="0 0 240 240"><path {S} d="M190 44 H84 a36 36 0 0 0 -36 36 V160 a36 36 0 0 0 36 36 H190"/><path {S} d="M48 120 H112"/><circle cx="172" cy="120" r="22" fill="currentColor"/></symbol>
  <!-- 3: bracket + arrow -->
  <symbol id="m3" viewBox="0 0 240 240"><path {S} d="M190 44 H84 a36 36 0 0 0 -36 36 V160 a36 36 0 0 0 36 36 H190"/><path {S.replace('36', '32')} d="M48 120 H184 M154 90 L184 120 L154 150"/></symbol>
  '''
s = s[:a] + new + s[b:]
s = s.replace('<symbol id="m4" viewBox="0 0 240 240"><g transform', '<symbol id="m4" viewBox="0 0 240 240"><g fill="currentColor" transform')
s = s.replace("svg{fill:currentColor;stroke:currentColor;stroke-width:0}\nsvg .s{fill:none;stroke-width:36;stroke-linecap:round;stroke-linejoin:round}\n", "")
open(p, 'w').write(s)
