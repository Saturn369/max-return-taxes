// Max Return Taxes — inner page behavior
(function(){
  var sp=document.getElementById('sp'),nav=document.getElementById('nav');
  function onScroll(){
    var max=document.body.scrollHeight-window.innerHeight;
    if(sp)sp.style.transform='scaleX('+(max>0?Math.min(window.scrollY/max,1):0)+')';
    if(nav)nav.classList.toggle('scrolled',window.scrollY>60);
  }
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  var hbg=document.getElementById('hbg'),nl=document.getElementById('navLinks');
  if(hbg&&nl){
    function setOpen(o){
      nl.classList.toggle('open',o);hbg.setAttribute('aria-expanded',o);
      hbg.children[0].style.transform=o?'rotate(45deg) translate(4.5px,4.5px)':'';
      hbg.children[1].style.opacity=o?'0':'';
      hbg.children[2].style.transform=o?'rotate(-45deg) translate(4.5px,-4.5px)':'';
    }
    hbg.addEventListener('click',function(){setOpen(!nl.classList.contains('open'))});
    nl.addEventListener('click',function(e){if(e.target.closest('a'))setOpen(false)});
  }
})();
