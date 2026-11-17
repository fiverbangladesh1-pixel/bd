p = 'video.html'
s = open(p).read()
subs = [
 # hidden-at-start elements
 ("window.prep=async()=>{", "gsap.set(['.slam','#streak'],{autoAlpha:0});gsap.set(['#flash','.act em','#ring1','#ring2','#e_rip i'],{opacity:0});\nwindow.prep=async()=>{"),
 # scrim
 ("#scrim{position:absolute;left:0;right:0;top:0;height:760px;background:linear-gradient(#06050b 0%,rgba(6,5,11,.94) 42%,rgba(6,5,11,0) 100%);opacity:0}",
  "#scrim{position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(#06050b 0%,#06050b 66%,rgba(6,5,11,0) 100%);opacity:0}"),
 ("tl.to(P,{y:-500,scale:Z,duration:.7,ease:'expo.inOut'},13.65);", "tl.to(P,{y:-330,scale:Z,duration:.7,ease:'expo.inOut'},13.65);"),
 ("tl.to(P,{y:-540,scale:Z+.05,duration:1.4,ease:'none'},14.35);", "tl.to(P,{y:-365,scale:Z+.05,duration:1.4,ease:'none'},14.35);"),
 # features phone bigger / higher
 ("tl.to(P,{scale:.86,y:560,rotationX:48,", "tl.to(P,{scale:1.02,y:430,rotationX:48,"),
 (".tok{position:absolute;left:400px;top:700px;", ".tok{position:absolute;left:400px;top:720px;"),
 # HUD counter
 ("forEach(([t,n,s])=>tl.call(()=>{},null,t)&&tl.set('#hn',{textContent:n},t)&&tl.set('#hs',{textContent:s},t));",
  "forEach(([t,n,s])=>tl.call(()=>{$('#hn').textContent=n;$('#hs').textContent=s},null,t));"),
 # commission layout
 ("#c_panel{position:absolute;left:64px;right:64px;top:760px;height:640px;", "#c_panel{position:absolute;left:64px;right:64px;top:760px;height:530px;"),
 ("#c_bars{position:absolute;left:0;right:0;bottom:60px;height:360px;", "#c_bars{position:absolute;left:0;right:0;bottom:60px;height:270px;"),
 (".toast{position:absolute;right:64px;width:650px;height:124px;", ".toast{position:absolute;right:64px;left:64px;height:124px;"),
 ('class="toast" style="top:1010px"', 'class="toast" style="top:1340px"'),
 ('class="toast" style="top:1150px"', 'class="toast" style="top:1484px"'),
 ('class="toast" style="top:1290px"', 'class="toast" style="top:1628px"'),
 ("ft(t,{x:760,rotation:4},", "ft(t,{x:1100,rotation:4},"),
 # history bigger
 ("tl.set(P,{y:1900,rotationX:62,rotationY:0,rotationZ:-60,scale:.9},31.9);", "tl.set(P,{y:1900,rotationX:60,rotationY:0,rotationZ:-60,scale:1.06},31.9);"),
 ("tl.to(P,{y:430,rotationZ:-34,duration:1.2,ease:'expo.out'},31.95);", "tl.to(P,{y:330,rotationZ:-34,duration:1.2,ease:'expo.out'},31.95);"),
 ("tl.to(P,{rotationZ:-22,y:400,duration:4.9,ease:'none'},33.1);", "tl.to(P,{rotationZ:-22,y:300,duration:4.9,ease:'none'},33.1);"),
 ("z:70+i*46,", "z:90+i*60,"), ("z:110+i*74,", "z:140+i*95,"),
 ("#k_chips div{background:rgba(10,30,24,.86);", "#k_chips div{background:#0b2019;box-shadow:0 30px 60px rgba(0,0,0,.5);"),
 # vip
 (".med{position:absolute;left:300px;top:520px;", ".med{position:absolute;left:300px;top:600px;"),
 (".vt{position:absolute;left:0;right:0;top:1090px;", ".vt{position:absolute;left:0;right:0;top:1180px;"),
 ("#b1{left:90px;top:500px;", "#b1{left:90px;top:570px;"), ("#b2{right:80px;top:940px;", "#b2{right:80px;top:1010px;"),
 # warning
 ("font-stretch:80%;font-size:310px;line-height:1.25;white-space:nowrap}", "font-stretch:80%;font-size:250px;line-height:1.25;white-space:nowrap}"),
 ("font-family:Inter;font-weight:700;font-size:56px;letter-spacing:-.015em;position:relative}", "font-family:Inter;font-weight:700;font-size:50px;letter-spacing:-.02em;position:relative}"),
 ("#verdict{position:absolute;right:26px;top:22px;height:88px;padding:0 30px;border-radius:44px;display:flex;align-items:center;gap:12px;font-family:Mono;font-weight:500;font-size:30px;letter-spacing:.1em;",
  "#verdict{position:absolute;right:24px;top:28px;height:76px;padding:0 24px;border-radius:38px;display:flex;align-items:center;gap:12px;font-family:Mono;font-weight:500;font-size:24px;letter-spacing:.08em;"),
 (".rule{position:absolute;left:64px;right:64px;top:520px;", ".rule{position:absolute;left:64px;right:64px;top:600px;"),
 ("#notice{position:absolute;left:64px;right:64px;top:330px;", "#notice{position:absolute;left:64px;right:64px;top:280px;"),
 ("#notice h2{font-weight:800;font-stretch:84%;font-size:104px;", "#notice h2{font-weight:800;font-stretch:84%;font-size:124px;"),
 ("#notice h2 span{color:#ff5d70}", ".red{color:#ff5d70}"),
 ('গুরুত্বপূর্ণ <span>ঘোষণা</span>', 'গুরুত্বপূর্ণ <span class="red">ঘোষণা</span>'),
 ("#notice p{font-size:53px;font-weight:500;font-stretch:92%;line-height:1.5;", "#notice p{font-size:62px;font-weight:500;font-stretch:90%;line-height:1.52;"),
 ("#notice p mark{background:#ff2d46;color:#fff;padding:0 12px;border-radius:6px;font-weight:800}", "#notice p mark{background:#ff2d46;color:#fff;padding:2px 12px;border-radius:6px;font-weight:800;-webkit-box-decoration-break:clone;box-decoration-break:clone}"),
 ("তার জন্য E-Wallet <mark>", 'তার জন্য <span style="white-space:nowrap">E-Wallet</span> <mark>'),
]
for a, b in subs:
    assert a in s, a
    s = s.replace(a, b)
open(p, 'w').write(s)
