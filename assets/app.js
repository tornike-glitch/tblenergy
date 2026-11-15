(function(){
  var root=document.documentElement;

  // language
  function setLang(l){
    root.setAttribute('data-lang',l);root.lang=l;
    document.querySelectorAll('[data-set]').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-set')===l?'true':'false')});
    try{localStorage.setItem('btl-lang',l)}catch(e){}
  }
  document.querySelectorAll('[data-set]').forEach(function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-set'))})});
  setLang(root.getAttribute('data-lang')||'ka');

  // mobile menu
  var burger=document.getElementById('burger');
  if(burger){
    burger.addEventListener('click',function(){
      var open=document.body.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded',open?'true':'false');
    });
    document.querySelectorAll('.mnav a').forEach(function(a){a.addEventListener('click',function(){document.body.classList.remove('menu-open');burger.setAttribute('aria-expanded','false')})});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&document.body.classList.contains('menu-open')){document.body.classList.remove('menu-open');burger.setAttribute('aria-expanded','false');burger.focus()}});
  }

  // project filters
  var filterBtns=document.querySelectorAll('[data-filter]');
  var items=[].slice.call(document.querySelectorAll('.grid-works button'));
  filterBtns.forEach(function(b){
    b.addEventListener('click',function(){
      var f=b.getAttribute('data-filter');
      filterBtns.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
      items.forEach(function(it){it.hidden=!(f==='all'||it.getAttribute('data-cat')===f)});
    });
  });

  // lightbox
  var lb=document.getElementById('lb');
  if(lb){
    var img=lb.querySelector('img'),count=lb.querySelector('.count'),cur=0,last=null;
    function visible(){return items.filter(function(it){return !it.hidden})}
    function show(i){
      var v=visible();if(!v.length)return;
      cur=(i+v.length)%v.length;var it=v[cur];
      img.src=it.getAttribute('data-full');img.alt=it.querySelector('img').alt;
      count.textContent=(cur+1)+' / '+v.length;
    }
    items.forEach(function(it){it.addEventListener('click',function(){last=it;show(visible().indexOf(it));lb.classList.add('open');document.body.style.overflow='hidden';lb.querySelector('.x').focus()})});
    function close(){lb.classList.remove('open');document.body.style.overflow='';if(last)last.focus()}
    lb.querySelector('.x').addEventListener('click',close);
    lb.querySelector('.prev').addEventListener('click',function(){show(cur-1)});
    lb.querySelector('.next').addEventListener('click',function(){show(cur+1)});
    lb.addEventListener('click',function(e){if(e.target===lb)close()});
    document.addEventListener('keydown',function(e){
      if(!lb.classList.contains('open'))return;
      if(e.key==='Escape')close();
      if(e.key==='ArrowLeft')show(cur-1);
      if(e.key==='ArrowRight')show(cur+1);
    });
  }
})();

/* ---------- circuit background: traces with travelling current pulses ---------- */
(function(){
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function rnd(a,b){return a+Math.random()*(b-a)}
  function Circuit(cv){
    var ctx=cv.getContext('2d'),dpr=Math.min(window.devicePixelRatio||1,2),W=0,H=0,paths=[],pulses=[],nodes=[],base=null,raf=0,visible=true,last=0;
    var density=parseFloat(cv.getAttribute('data-density')||'1');
    function build(){
      var r=cv.getBoundingClientRect();W=Math.max(1,r.width);H=Math.max(1,r.height);
      cv.width=W*dpr;cv.height=H*dpr;
      var step=W<700?22:28,cols=Math.floor(W/step),rows=Math.floor(H/step);
      paths=[];nodes=[];
      var count=Math.round((W*H)/(step*step*7)*density);
      for(var n=0;n<count;n++){
        var x=Math.round(cols*(0.25+0.75*Math.pow(Math.random(),0.6))),y=Math.floor(Math.random()*rows);
        var pts=[[x*step,y*step]],dir=Math.random()<.7?0:1,len=Math.floor(rnd(4,14));
        for(var k=0;k<len;k++){
          var seg=Math.floor(rnd(1,5));
          if(dir===0){x+=Math.random()<.65?-seg:seg}else{y+=Math.random()<.5?-seg:seg}
          x=Math.max(0,Math.min(cols,x));y=Math.max(0,Math.min(rows,y));
          var p=pts[pts.length-1];
          if(p[0]!==x*step||p[1]!==y*step)pts.push([x*step,y*step]);
          dir=1-dir;
        }
        if(pts.length<2)continue;
        var L=0,segs=[];
        for(var s=1;s<pts.length;s++){var d=Math.abs(pts[s][0]-pts[s-1][0])+Math.abs(pts[s][1]-pts[s-1][1]);segs.push(d);L+=d}
        paths.push({pts:pts,segs:segs,len:L});
        nodes.push({x:pts[pts.length-1][0],y:pts[pts.length-1][1],f:0,path:paths.length-1});
      }
      // static layer
      base=document.createElement('canvas');base.width=cv.width;base.height=cv.height;
      var b=base.getContext('2d');b.scale(dpr,dpr);
      b.strokeStyle='rgba(160,180,200,.10)';b.lineWidth=1;
      paths.forEach(function(p){b.beginPath();b.moveTo(p.pts[0][0]+.5,p.pts[0][1]+.5);for(var i=1;i<p.pts.length;i++)b.lineTo(p.pts[i][0]+.5,p.pts[i][1]+.5);b.stroke()});
      b.fillStyle='rgba(160,180,200,.18)';
      paths.forEach(function(p){var a=p.pts[0];b.fillRect(a[0]-1.5,a[1]-1.5,3,3)});
      b.strokeStyle='rgba(240,180,0,.35)';
      nodes.forEach(function(nd){b.strokeRect(nd.x-3,nd.y-3,6,6)});
      pulses=[];var pc=Math.max(6,Math.round(paths.length*.22));
      for(var q=0;q<pc;q++)pulses.push(newPulse(true));
      draw(0);
    }
    function newPulse(init){var pi=Math.floor(Math.random()*paths.length);return{p:pi,t:init?Math.random()*paths[pi].len:0,v:rnd(90,220),tail:rnd(40,90)}}
    function at(path,d){
      d=Math.max(0,Math.min(path.len,d));var acc=0;
      for(var i=0;i<path.segs.length;i++){
        if(acc+path.segs[i]>=d){var a=path.pts[i],b=path.pts[i+1],r=(d-acc)/path.segs[i];return[a[0]+(b[0]-a[0])*r,a[1]+(b[1]-a[1])*r]}
        acc+=path.segs[i];
      }
      return path.pts[path.pts.length-1];
    }
    function draw(dt){
      ctx.setTransform(1,0,0,1,0,0);ctx.clearRect(0,0,cv.width,cv.height);
      if(base)ctx.drawImage(base,0,0);
      ctx.setTransform(dpr,0,0,dpr,0,0);
      ctx.lineCap='round';
      pulses.forEach(function(pl,idx){
        var path=paths[pl.p];if(!path)return;
        pl.t+=pl.v*dt;
        if(pl.t-pl.tail>path.len){nodes[pl.p].f=1;pulses[idx]=newPulse(false);return}
        var head=at(path,pl.t),N=8;
        for(var k=0;k<N;k++){
          var a=at(path,pl.t-pl.tail*k/N),b=at(path,pl.t-pl.tail*(k+1)/N);
          ctx.strokeStyle='rgba(255,200,40,'+(0.9*(1-k/N))+')';ctx.lineWidth=1.6;
          ctx.beginPath();ctx.moveTo(a[0]+.5,a[1]+.5);ctx.lineTo(b[0]+.5,b[1]+.5);ctx.stroke();
        }
        var g=ctx.createRadialGradient(head[0],head[1],0,head[0],head[1],10);
        g.addColorStop(0,'rgba(255,225,120,.95)');g.addColorStop(1,'rgba(255,190,0,0)');
        ctx.fillStyle=g;ctx.beginPath();ctx.arc(head[0],head[1],10,0,6.283);ctx.fill();
      });
      nodes.forEach(function(nd){
        if(nd.f>0){
          var g=ctx.createRadialGradient(nd.x,nd.y,0,nd.x,nd.y,22*nd.f+4);
          g.addColorStop(0,'rgba(255,210,80,'+(.8*nd.f)+')');g.addColorStop(1,'rgba(255,190,0,0)');
          ctx.fillStyle=g;ctx.beginPath();ctx.arc(nd.x,nd.y,22*nd.f+4,0,6.283);ctx.fill();
          ctx.fillStyle='rgba(255,215,90,'+nd.f+')';ctx.fillRect(nd.x-3,nd.y-3,6,6);
          nd.f=Math.max(0,nd.f-dt*1.4);
        }
      });
    }
    function loop(ts){
      var dt=last?Math.min(.05,(ts-last)/1000):0;last=ts;
      draw(dt);raf=requestAnimationFrame(loop);
    }
    function start(){if(reduce||raf||!visible||document.hidden)return;last=0;raf=requestAnimationFrame(loop)}
    function stop(){if(raf){cancelAnimationFrame(raf);raf=0}}
    build();
    if(reduce){draw(0)}
    if('IntersectionObserver' in window){new IntersectionObserver(function(e){visible=e[0].isIntersecting;visible?start():stop()}).observe(cv)}
    document.addEventListener('visibilitychange',function(){document.hidden?stop():start()});
    var to;window.addEventListener('resize',function(){clearTimeout(to);to=setTimeout(function(){stop();build();start()},180)});
    start();
  }
  document.querySelectorAll('canvas.circuit').forEach(function(cv){try{Circuit(cv)}catch(e){}});

  /* ---------- 3-phase scope ---------- */
  var sc=document.getElementById('scope-cv');
  if(sc){
    var c=sc.getContext('2d'),dpr=Math.min(window.devicePixelRatio||1,2),w=0,h=0,t0=performance.now(),raf2=0;
    var cols=['#f0b400','#e8edf2','#4da3ff'];
    function size(){var r=sc.getBoundingClientRect();w=r.width;h=r.height;sc.width=w*dpr;sc.height=h*dpr}
    function frame(now){
      var t=(now-t0)/1000;
      c.setTransform(dpr,0,0,dpr,0,0);c.clearRect(0,0,w,h);
      c.strokeStyle='rgba(255,255,255,.05)';c.lineWidth=1;
      for(var gx=0;gx<=10;gx++){var x=Math.round(w*gx/10)+.5;c.beginPath();c.moveTo(x,0);c.lineTo(x,h);c.stroke()}
      for(var gy=0;gy<=6;gy++){var y=Math.round(h*gy/6)+.5;c.beginPath();c.moveTo(0,y);c.lineTo(w,y);c.stroke()}
      c.strokeStyle='rgba(255,255,255,.12)';c.beginPath();c.moveTo(0,h/2+.5);c.lineTo(w,h/2+.5);c.stroke();
      var amp=h*.36,cyc=2.5;
      for(var ph=0;ph<3;ph++){
        c.strokeStyle=cols[ph];c.lineWidth=1.8;c.shadowColor=cols[ph];c.shadowBlur=8;
        c.beginPath();
        for(var px=0;px<=w;px+=2){
          var v=Math.sin((px/w)*cyc*6.283 - t*2.2 - ph*2.0944);
          v+=0.025*Math.sin((px/w)*cyc*6.283*5 - t*11);
          var yy=h/2-v*amp;px?c.lineTo(px,yy):c.moveTo(px,yy);
        }
        c.stroke();
      }
      c.shadowBlur=0;
      // sweep line
      var sx=((t*0.18)%1)*w;
      var g=c.createLinearGradient(sx-60,0,sx,0);g.addColorStop(0,'rgba(240,180,0,0)');g.addColorStop(1,'rgba(240,180,0,.18)');
      c.fillStyle=g;c.fillRect(sx-60,0,60,h);
      if(!reduce)raf2=requestAnimationFrame(frame);
    }
    size();frame(performance.now());
    window.addEventListener('resize',function(){size();if(reduce)frame(performance.now())});
    // jitter readings
    var els=[document.getElementById('v1'),document.getElementById('v2'),document.getElementById('v3'),document.getElementById('hz')];
    var basev=[230.6,229.8,231.2];
    if(!reduce)setInterval(function(){
      for(var i=0;i<3;i++)if(els[i])els[i].firstChild.nodeValue=(basev[i]+ (Math.random()-.5)*1.2).toFixed(1);
      if(els[3])els[3].textContent=(50+(Math.random()-.5)*.04).toFixed(2)+' Hz';
    },900);
  }
})();

/* ---------- process showcase ---------- */
(function(){
  var stage=document.getElementById('stage');if(!stage)return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var sec=stage.closest('.process-sec'),steps=[].slice.call(document.querySelectorAll('.pstep')),scenes=[].slice.call(stage.querySelectorAll('.scene')),titles=[].slice.call(stage.querySelectorAll('.stt')),segs=[].slice.call(stage.querySelectorAll('.seg i')),num=document.getElementById('stage-n'),pp=document.getElementById('pp');
  var cur=0,paused=reduce,visible=true;
  if(reduce)sec.classList.add('paused');
  function go(i){
    cur=(i+scenes.length)%scenes.length;
    scenes.forEach(function(s,k){s.classList.remove('on');if(k===cur){void s.getBoundingClientRect();s.classList.add('on')}});
    steps.forEach(function(b,k){b.classList.toggle('on',k===cur);b.setAttribute('aria-pressed',k===cur?'true':'false');var bar=b.querySelector('.pbar i');if(bar){bar.style.animation='none';void bar.offsetWidth;bar.style.animation=''}});
    titles.forEach(function(tl,k){tl.classList.toggle('on',k===cur)});
    segs.forEach(function(sg,k){sg.classList.toggle('on',k===cur);sg.classList.toggle('done',k<cur)});
    if(num)num.textContent='0'+(cur+1);
  }
  steps.forEach(function(b,k){
    b.addEventListener('click',function(){go(k)});
    var bar=b.querySelector('.pbar i');
    if(bar)bar.addEventListener('animationend',function(){if(!paused&&visible&&k===cur)go(cur+1)});
  });
  function setPaused(p){paused=p;sec.classList.toggle('paused',p);pp.setAttribute('aria-label',p?'Play':'Pause')}
  pp.addEventListener('click',function(){setPaused(!paused)});
  if('IntersectionObserver' in window){new IntersectionObserver(function(e){visible=e[0].isIntersecting;sec.classList.toggle('paused',paused||!visible);if(visible&&!paused)go(cur)}).observe(stage)}
  go(0);
})();

/* ---------- services sub-navigation ---------- */
(function(){
  var secs=[].slice.call(document.querySelectorAll('[data-sd]'));if(!secs.length)return;
  var links=[].slice.call(document.querySelectorAll('[data-sub]')),fill=document.getElementById('subnav-fill'),ticking=false;
  function update(){
    ticking=false;
    var mid=window.innerHeight*0.4,active=secs[0].id;
    secs.forEach(function(s){if(s.getBoundingClientRect().top<mid)active=s.id});
    links.forEach(function(a){a.classList.toggle('on',a.getAttribute('data-sub')===active)});
    var first=secs[0].getBoundingClientRect().top+window.scrollY,last=secs[secs.length-1],end=last.getBoundingClientRect().bottom+window.scrollY-window.innerHeight;
    var p=Math.max(0,Math.min(1,(window.scrollY-first+200)/Math.max(1,end-first+200)));
    if(fill)fill.style.width=(p*100)+'%';
  }
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(update)}},{passive:true});
  window.addEventListener('resize',update);update();
})();

/* ---------- project galleries ---------- */
(function(){
  var lb=document.getElementById('plb');if(!lb)return;
  var img=document.getElementById('plb-img'),title=document.getElementById('plb-title'),count=document.getElementById('plb-count'),thumbs=document.getElementById('plb-thumbs');
  var list=[],cur=0,opener=null;
  function show(i){
    cur=(i+list.length)%list.length;img.src=list[cur];img.alt=title.textContent+' '+(cur+1);
    img.style.animation='none';void img.offsetWidth;img.style.animation='';
    count.textContent=(cur+1)+' / '+list.length;
    [].forEach.call(thumbs.children,function(b,k){b.classList.toggle('on',k===cur);if(k===cur&&b.scrollIntoView)b.scrollIntoView({block:'nearest',inline:'center'})});
  }
  function open(btn){
    opener=btn;list=btn.getAttribute('data-imgs').split(',');
    var en=document.documentElement.getAttribute('data-lang')==='en';
    title.textContent=en?btn.getAttribute('data-title-en'):btn.getAttribute('data-title');
    thumbs.innerHTML='';
    list.forEach(function(src,k){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Photo '+(k+1));b.innerHTML='<img src="'+src+'" alt="">';b.addEventListener('click',function(){show(k)});thumbs.appendChild(b)});
    lb.hidden=false;document.body.style.overflow='hidden';show(0);document.getElementById('plb-x').focus();
  }
  function close(){lb.hidden=true;document.body.style.overflow='';if(opener)opener.focus()}
  document.querySelectorAll('.pj').forEach(function(b){b.addEventListener('click',function(){open(b)})});
  document.getElementById('plb-x').addEventListener('click',close);
  document.getElementById('plb-prev').addEventListener('click',function(){show(cur-1)});
  document.getElementById('plb-next').addEventListener('click',function(){show(cur+1)});
  document.addEventListener('keydown',function(e){if(lb.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(cur-1);if(e.key==='ArrowRight')show(cur+1)});
  var sx=null;lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  lb.addEventListener('touchend',function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)show(cur+(dx<0?1:-1));sx=null});
})();

/* ---------- light / dark theme ---------- */
(function(){
  var b=document.getElementById('theme-t');if(!b)return;
  b.addEventListener('click',function(){
    var r=document.documentElement,light=r.getAttribute('data-theme')!=='light';
    if(light)r.setAttribute('data-theme','light');else r.removeAttribute('data-theme');
    try{localStorage.setItem('tbl-theme',light?'light':'dark')}catch(e){}
  });
})();

/* mobile services dropdown */
(function(){
  var b=document.getElementById('msub-t');if(!b)return;
  b.addEventListener('click',function(){
    var w=b.parentNode,open=!w.classList.contains('open');
    w.classList.toggle('open',open);b.setAttribute('aria-expanded',open?'true':'false');
  });
})();
