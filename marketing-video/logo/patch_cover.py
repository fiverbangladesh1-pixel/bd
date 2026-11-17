import re
p = 'cover.html'
s = open(p).read()
a = s.index('<div class="c">'); b = s.index('</div>\n  </div>\n</div>', a)
new = '''<div class="c">
      <div><span class="tgi"><svg viewBox="0 0 24 24" fill="#fff"><path d="M21.900 4.300 18.600 19.900c-.25 1.100-.9 1.370-1.820.85l-5.030-3.700-2.430 2.330c-.27.27-.5.5-1.010.5l.36-5.120 9.320-8.420c.4-.36-.09-.56-.63-.2L5.840 13.400.88 11.850c-1.080-.34-1.100-1.080.22-1.600L20.500 2.780c.9-.33 1.690.2 1.400 1.520z"/></svg></span>@ewalletbd247</div>
    '''
s = s[:a] + new + s[b:]
s = s.replace(".c{margin-top:40px;display:flex;gap:18px;font-family:Inter;font-weight:600;font-size:25px}",
              ".c{margin-top:36px;display:flex;gap:18px;font-family:Inter;font-weight:700;font-size:38px;letter-spacing:-.01em}")
s = s.replace(".c div{display:flex;align-items:center;gap:12px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.28)}",
              ".c div{display:flex;align-items:center;gap:18px;padding:10px 36px 10px 10px;border-radius:50px;background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.32)}\n.tgi{width:58px;height:58px;border-radius:50%;background:linear-gradient(#37aee2,#1e96c8);display:flex;align-items:center;justify-content:center}")
s = s.replace(".c svg{width:26px;height:26px}", ".c svg{width:34px;height:34px;margin-left:-4px}")
open(p, 'w').write(s)
