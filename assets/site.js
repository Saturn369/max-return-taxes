// Max Return Taxes — shared behavior for every page: nav, contact forms, analytics.
(function(){
  /* ---------- Analytics (GoatCounter: cookie-free, no personal data) ----------
     Set GOATCOUNTER_CODE to your GoatCounter site code (the "mycode" in
     https://mycode.goatcounter.com) to turn on page-view and click counting. */
  var GOATCOUNTER_CODE = 'maxreturntaxes';

  if (GOATCOUNTER_CODE) {
    var gc = document.createElement('script');
    gc.async = true; gc.src = 'https://gc.zgo.at/count.js';
    gc.setAttribute('data-goatcounter', 'https://' + GOATCOUNTER_CODE + '.goatcounter.com/count');
    document.head.appendChild(gc);
  }
  // Records a named event, e.g. "call-click" — shows up under Events in GoatCounter.
  function track(name, title){
    try {
      if (window.goatcounter && window.goatcounter.count)
        window.goatcounter.count({ path: name, title: title || name, event: true });
    } catch (e) {}
  }
  var here = location.pathname.replace(/^.*max-return-taxes/, '') || '/';
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href');
    if (h.indexOf('tel:') === 0) track('call-click ' + here, 'Phone click on ' + here);
    else if (h.indexOf('mailto:') === 0) track('email-click ' + here, 'Email click on ' + here);
  });

  /* ---------- Scroll progress + nav state ---------- */
  var sp = document.getElementById('sp'), nav = document.getElementById('nav');
  function onScroll(){
    var max = document.body.scrollHeight - window.innerHeight;
    if (sp) sp.style.transform = 'scaleX(' + (max > 0 ? Math.min(window.scrollY / max, 1) : 0) + ')';
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 60);
  }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- Mobile menu ---------- */
  var hbg = document.getElementById('hbg'), nl = document.getElementById('navLinks');
  if (hbg && nl) {
    var setOpen = function(o){
      nl.classList.toggle('open', o); hbg.setAttribute('aria-expanded', o);
      hbg.children[0].style.transform = o ? 'rotate(45deg) translate(4.5px,4.5px)' : '';
      hbg.children[1].style.opacity = o ? '0' : '';
      hbg.children[2].style.transform = o ? 'rotate(-45deg) translate(4.5px,-4.5px)' : '';
    };
    hbg.addEventListener('click', function(){ setOpen(!nl.classList.contains('open')); });
    nl.addEventListener('click', function(e){ if (e.target.closest('a')) setOpen(false); });
  }

  /* ---------- Contact forms (Web3Forms) ---------- */
  var CHECK = '<svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>';
  [].forEach.call(document.querySelectorAll('form.contact-form'), function(f){
    f.addEventListener('submit', function(e){
      e.preventDefault();
      var btn = f.querySelector('button[type=submit]'), orig = btn.innerHTML;
      btn.disabled = true; btn.innerHTML = 'Sending...';
      var show = function(html, bg){
        btn.innerHTML = html; btn.style.background = bg;
        setTimeout(function(){ btn.innerHTML = orig; btn.disabled = false; btn.style.background = ''; }, 5000);
      };
      var ctl = new AbortController(), t = setTimeout(function(){ ctl.abort(); }, 15000);
      fetch(f.action, { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(f), signal: ctl.signal })
        .then(function(r){ clearTimeout(t); return r.json().catch(function(){ return {}; }).then(function(d){
          if (!r.ok || d.success !== true) throw new Error(d.message || r.status);
        }); })
        .then(function(){
          f.reset();
          track('form-submit ' + here, 'Form sent: ' + (f.dataset.page || here));
          show(CHECK + ' Message Sent!', 'linear-gradient(135deg,#3D9A6E,#2A7A54)');
        })
        .catch(function(){
          clearTimeout(t);
          show('Could not send — please call (860) 993-9904', 'linear-gradient(135deg,#7a1a1a,#4a1010)');
        });
    });
  });
})();
