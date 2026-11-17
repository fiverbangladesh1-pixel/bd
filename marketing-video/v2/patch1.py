p = 'video.html'
s = open(p).read()
subs = [
 ("const ft=(el,a,b,at)=>tl.fromTo(el,a,{immediateRender:false,...b},at);",
  "const seen=new Set();const ft=(el,a,b,at)=>{gsap.utils.toArray(el).forEach(e=>{if(!seen.has(e)){seen.add(e);gsap.set(e,a)}});return tl.fromTo(el,a,{immediateRender:false,...b},at)};"),
 ("$$('.rv').forEach(el=>{", "$$('.rv').forEach(el=>{const G=el.classList.contains('grad');if(G)el.className=el.className.replace('grad','');"),
 ("if(n!==el&&n.className)i.className+=' '+n.className;", "if(n!==el&&n.className)i.className+=' '+n.className;if(G)i.className+=' grad';"),
 ("font-stretch:78%;font-size:300px;line-height:1.25;white-space:nowrap}", "font-stretch:78%;font-size:250px;line-height:1.25;white-space:nowrap}"),
 ("{opacity:1,letterSpacing:'.16em',duration:1.2},.1);", "{opacity:1,letterSpacing:'.16em',duration:.3},.1);"),
 ("ft('#i_line',{scaleX:0},{scaleX:1,duration:1},.15);", "ft('#i_line',{scaleX:0},{scaleX:1,duration:.27},.15);"),
 ("{yPercent:0,opacity:1,duration:.7,stagger:.04},4.15);", "{yPercent:0,opacity:1,duration:.5,stagger:.03},4.1);"),
]
for a, b in subs:
    assert a in s, a
    s = s.replace(a, b)
open(p, 'w').write(s)
