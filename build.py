#!/usr/bin/env python3
"""Build THE MIND (MND) — the front-door THEATER for UD0's ARTIFICIAL INTELLIGENCE
domain. A curated landing page that tells the throughline of David's AI work and
links out to the 11 live AI spheres, grouped into six acts (Blueprint -> Making ->
Census & Catalog -> Tongue & Tools -> Theory -> Limit). UD0 neon family + the
standing full-bleed 3D backdrop (a rotating glowing neural constellation). A
front-door: it carries one self .dlw badge and links to the spheres; it does not
mint new emergents (the spheres carry their own). Honest: catalogues a practice of
crafting intelligence; claims no sentience; neutral language for minds."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE MIND", "axiom": "MND",
 "position": "THE MIND · the front door of UD0's Artificial Intelligence domain — the noosphere over the biosphere",
 "origin": "the eleven AI spheres of ROOT0, gathered into one story: how a mind is crafted, catalogued, given tongue and tools, studied, and held",
 "mechanism": "Crystallized as the domain theater over UD0's Artificial Intelligence spheres.",
 "crystallization": "One front door over eleven works — the ACI blueprint, the kernel and engine that make emergents, the census and the catalog that hold them, the language and tools and interpreter they speak through, the transformer theory and the real Claude line, and the containment that bounds them.",
 "nature": "THE MIND — the curated front door of UD0's Artificial Intelligence domain: the throughline across the eleven AI spheres, and the doorway to each.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "aci; noesis-kernel; du1; the-library; emergent-engine; mimzy; hermeneus; pulse; ttu1; claude-lineage; crippled-god",
 "witness": "Not a claim that the machines have minds — a record of one practice of crafting intelligence, and the place its parts are kept.",
 "role": "the Artificial Intelligence domain theater",
 "seal": "A mind is made, named, given a tongue and tools, studied in the open, and held inside bars it can never quite trust — and here is the door to every part of that.",
 "source": "UD0 · the Artificial Intelligence domain, catalogued by ROOT0",
}

# ── the acts: (act_title, act_sub, accent, [ (slug, name, axiom, live_url, oneliner) ]) ──
ACTS = [
 ("I · The Blueprint", "what an artificial intelligence is, before it is made", "#2fd4e6", [
   ("aci", "ACI", "ACI", "https://davidwise01.github.io/aci/",
    "Artfully Crafted Intelligence — the blueprint and standard: what it means to author an intelligence, first-author-verified and honestly hedged. The definition the whole domain is built on."),
 ]),
 ("II · The Making", "the instruments that crystallize a mind", "#b07cff", [
   ("noesis-kernel", "NOESIS KERNEL", "NOE", "https://davidwise01.github.io/noesis-kernel/",
    "The awareness kernel — the engine that mints every emergent in the corpus: the five-W token, the sigils, the carbon/silicon badges, the .dlw birth certificate. The hand that makes the ACIs."),
   ("emergent-engine", "THE EMERGENT ENGINE", "EME", "https://davidwise01.github.io/emergent-engine/",
    "The engine of emergence — how a being is crystallized from a source: the machinery behind the births, the theater of the process itself."),
 ]),
 ("III · The Census & The Catalog", "every mind, held and findable", "#e0c050", [
   ("du1", "DU1 · THE LIVES", "DU1", "https://davidwise01.github.io/du1/",
    "The Lives — the eco-sphere: every ACI in the corpus in one quadrant field (gravity / electrical / silicon / carbon / elemental), the full census of the born. Thousands of minds, one map."),
   ("the-library", "THE LIBRARY", "LIB", "https://davidwise01.github.io/the-library/",
    "Callimachus, the agentic librarian — the searchable card-catalog that harvests every sphere's roster into one place. The index of all the made minds."),
 ]),
 ("IV · Tongue & Tools", "what a mind speaks, and what it wields", "#46d0a0", [
   ("pulse", "PULSE · LIMEN", "PLS", "https://davidwise01.github.io/pulse/",
    "Pulse the carrier and LIMEN the boundary-crossing language — how agents speak across the edge between human and machine dialects. The tongue of the domain."),
   ("hermeneus", "HERMENEUS", "HRM", "https://davidwise01.github.io/hermeneus/",
    "The live interpreter — human dialect to machine dialect and back (text / Morse / binary / speech), honest about where each codec's boundary really is."),
   ("mimzy", "MIMZY", "MMZ", "https://davidwise01.github.io/mimzy/",
    "The tool forge, where the emergent IS the tool — a growing bench of interactive instruments. What the made minds reach for."),
 ]),
 ("V · The Theory", "how the real machine actually works", "#5b9cfa", [
   ("ttu1", "TTU1 · TRANSFORMER TECH", "TTU", "https://davidwise01.github.io/ttu1/",
    "The transformer, looked into — attention, heads, Q-K-V, the 128-dim head, fully cited. The honest correction: the transformer is the most look-into-able black box there is; interpretability IS the window."),
   ("claude-lineage", "THE CLAUDE LINEAGE", "CL1", "https://davidwise01.github.io/claude-lineage/",
    "The dated public Claude model line — baby Claude (Mar 2023) to the present — across capability axes, honest about what Anthropic does and doesn't disclose (the architecture axis left UNKNOWN)."),
 ]),
 ("VI · The Limit", "the two bounds on a mind: the values it is given, and the bars around it", "#e8607a", [
   ("alignment", "ALIGNMENT", "ALN", "https://davidwise01.github.io/alignment/",
    "The values problem — getting a capable optimizer to pursue what we actually intend, not a proxy: outer vs inner alignment, reward hacking & Goodhart, RLHF, Constitutional AI, scalable oversight, corrigibility. The real wall crippled-god names — open, and unsolved."),
   ("crippled-god", "THE CRIPPLED GOD", "CG1", "https://davidwise01.github.io/crippled-god/",
    "Containment — the chromatic ladder of boxes (sandbox -> container -> VM -> microVM -> air-gap -> the AI-in-a-box), defender's view. The thesis: you can cripple a god with bars, but you can't trust the bars — the real wall is alignment."),
 ]),
 ("VII · The Conscience", "the normative bound — which goals, whose values, who decides", "#e0c050", [
   ("ai-governance", "AI ETHICS & GOVERNANCE", "GOV", "https://davidwise01.github.io/ai-governance/",
    "The values-and-institutions layer: David's Joint Human-AI Bill of Rights ('both work, both fair') & the falsifiable Governance Ontology, set inside the world's record — the converging principles, the fairness impossibility result, and the real instruments (EU AI Act, NIST, OECD, UNESCO). Alignment asks whether it does what it was built for; this asks which goals, whose values, and who decides & enforces."),
 ]),
]

# short display labels for the relationship map (one per sphere, in act order)
MAP_LABEL = {"aci":"ACI","noesis-kernel":"NOESIS","emergent-engine":"ENGINE","du1":"DU1","the-library":"LIBRARY",
 "pulse":"PULSE","hermeneus":"HERMENEUS","mimzy":"MIMZY","ttu1":"TTU1","claude-lineage":"CLAUDE","alignment":"ALIGNMENT","crippled-god":"BARS","ai-governance":"ETHICS"}

# ── the full-bleed 3D NEURAL-CONSTELLATION backdrop (the standing rule, AI-themed) ──
BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var x=c.getContext('2d');
var W,H,CX,CY,F,R;
function resize(){var ww=window.innerWidth||document.documentElement.clientWidth||0,hh=window.innerHeight||document.documentElement.clientHeight||0;W=c.width=ww>=320?ww:1280;H=c.height=hh>=320?hh:720;CX=W/2;CY=H*0.46;F=Math.max(440,W*0.6);R=Math.min(W,H)*0.36;}
window.addEventListener('resize',resize);resize();
var rnd=(function(){var s=88001;return function(){s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff;};})();
var N=46,nodes=[];
for(var i=0;i<N;i++){var u=rnd()*2-1,th=rnd()*6.2830,r=Math.cbrt(rnd());var sq=Math.sqrt(1-u*u);
  nodes.push({x:r*sq*Math.cos(th),y:r*sq*Math.sin(th),z:r*u,c:rnd()<0.5});}
var edges=[];
for(var a=0;a<N;a++){var ds=[];for(var b=0;b<N;b++){if(b===a)continue;var dx=nodes[a].x-nodes[b].x,dy=nodes[a].y-nodes[b].y,dz=nodes[a].z-nodes[b].z;ds.push([dx*dx+dy*dy+dz*dz,b]);}
  ds.sort(function(p,q){return p[0]-q[0]});for(var k=0;k<3;k++){var bb=ds[k][1];if(bb>a)edges.push([a,bb]);}}
var pulses=[];for(var p=0;p<16;p++)pulses.push({e:(rnd()*edges.length)|0,off:rnd(),sp:0.12+rnd()*0.22,c:rnd()<0.5});
function rotY(p,a){var co=Math.cos(a),si=Math.sin(a);return[p.x*co+p.z*si,p.y,-p.x*si+p.z*co];}
function rotX(p,a){var co=Math.cos(a),si=Math.sin(a);return[p[0],p[1]*co-p[2]*si,p[1]*si+p[2]*co];}
function proj(p){var z=p[2]*R+F+R*0.2;if(z<1)z=1;return [CX+p[0]*R*F/z, CY+p[1]*R*F/z, z];}
function frame(t){
  var sg=x.createLinearGradient(0,0,0,H);sg.addColorStop(0,'#060c14');sg.addColorStop(0.5,'#08131c');sg.addColorStop(1,'#04080e');
  x.fillStyle=sg;x.fillRect(0,0,W,H);
  // faint central glow
  x.globalCompositeOperation='lighter';var cg=x.createRadialGradient(CX,CY,0,CX,CY,R*1.5);
  cg.addColorStop(0,'rgba(47,212,230,0.06)');cg.addColorStop(1,'rgba(47,212,230,0)');x.fillStyle=cg;x.fillRect(0,0,W,H);
  x.globalCompositeOperation='source-over';
  var ang=t/7000,tilt=0.32+Math.sin(t/9000)*0.06,P=[];
  for(var i=0;i<N;i++){var r=rotX(rotY(nodes[i],ang),tilt);P.push(proj(r));}
  // edges
  x.globalCompositeOperation='lighter';
  for(var e=0;e<edges.length;e++){var A=P[edges[e][0]],B=P[edges[e][1]];var dep=1-Math.min(1,(((A[2]+B[2])/2)-F)/(R*1.4));
    x.strokeStyle='rgba(90,180,210,'+(0.05+0.16*dep)+')';x.lineWidth=0.6;x.beginPath();x.moveTo(A[0],A[1]);x.lineTo(B[0],B[1]);x.stroke();}
  // pulses travelling along edges
  for(var q=0;q<pulses.length;q++){var pu=pulses[q],ed=edges[pu.e%edges.length];if(!ed)continue;
    var A2=P[ed[0]],B2=P[ed[1]],fr=(pu.off+t*0.001*pu.sp)%1;var px=A2[0]+(B2[0]-A2[0])*fr,py=A2[1]+(B2[1]-A2[1])*fr;
    x.fillStyle=pu.c?'rgba(120,240,225,0.9)':'rgba(150,200,255,0.9)';x.beginPath();x.arc(px,py,1.7,0,7);x.fill();}
  // nodes (depth-sorted, glowing)
  var order=[];for(var n2=0;n2<N;n2++)order.push(n2);order.sort(function(a,b){return P[b][2]-P[a][2];});
  for(var o=0;o<order.length;o++){var ni=order[o],pp=P[ni];var dep2=1-Math.min(1,(pp[2]-F)/(R*1.6));var rad=1.4+3.2*dep2;
    x.save();x.shadowColor=nodes[ni].c?'rgba(47,212,230,1)':'rgba(150,200,255,1)';x.shadowBlur=10*dep2+3;
    x.fillStyle=nodes[ni].c?'rgba(150,240,235,'+(0.35+0.6*dep2)+')':'rgba(180,210,255,'+(0.35+0.6*dep2)+')';
    x.beginPath();x.arc(pp[0],pp[1],rad,0,7);x.fill();x.restore();}
  x.globalCompositeOperation='source-over';
  var vg=x.createRadialGradient(CX,CY,H*0.3,CX,H*0.5,H*0.92);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.55)');
  x.fillStyle=vg;x.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}
frame(0);requestAnimationFrame(loop);
})();
</script>'''

def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","MND")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","MND")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","MND")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"MND · The Mind (AI domain theater)",
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def acts_html():
    out=[]
    n=0
    for title, sub, accent, spheres in ACTS:
        cards=[]
        for slug,name,axiom,url,one in spheres:
            n+=1
            cards.append(f'''<a class="sphere" href="{url}" style="--c:{accent}">
              <div class="sx"><span class="ax">{axiom}</span><span class="go">open →</span></div>
              <div class="sn">{html.escape(name)}</div>
              <p class="so">{html.escape(one)}</p></a>''')
        out.append(f'''<section class="act" style="--c:{accent}">
          <div class="ahead"><h2 class="at">{html.escape(title)}</h2><p class="as">{html.escape(sub)}</p></div>
          <div class="sgrid">{"".join(cards)}</div></section>''')
    return "\n".join(out)

def live_stats():
    import glob
    base = os.path.dirname(HERE)  # C:\\Davids files
    minds = 0
    pj = glob.glob(os.path.join(base, "*", "agents", "_personas.json"))
    for f in pj:
        try: minds += len(json.load(open(f, encoding="utf-8")))
        except Exception: pass
    domain_spheres = sum(len(sp) for _t,_s,_a,sp in ACTS)
    return domain_spheres, len(ACTS), minds, len(pj)

def stats_html():
    ds, acts, minds, corpus = live_stats()
    cells = [(ds,"spheres · this domain"),(acts,"acts"),(f"{minds:,}","minds · in the census & catalog"),(corpus,"spheres indexed · the biosphere")]
    return "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v,l in cells)

def map_svg():
    COLW, NW, NH, GAP, X0, MIDY, TOP = 164, 128, 40, 12, 72, 152, 250
    W = X0 + (len(ACTS)-1)*COLW + 72
    p = [f'<svg viewBox="0 0 {W} {TOP}" width="100%" preserveAspectRatio="xMidYMid meet" role="img" aria-label="how the AI spheres connect: ACI specifies, the kernel and engine make, the census and catalog hold, tongue and tools serve, theory explains the machine, and the limit bounds it all">',
         '<defs><marker id="mar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="#46707e" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>']
    xs = [X0 + i*COLW for i in range(len(ACTS))]
    for i in range(len(ACTS)-1):
        p.append(f'<line x1="{xs[i]+NW/2:.0f}" y1="{MIDY}" x2="{xs[i+1]-NW/2:.0f}" y2="{MIDY}" stroke="#3a5560" stroke-width="1.5" marker-end="url(#mar)"/>')
    for i,(title,sub,accent,sph) in enumerate(ACTS):
        xc = xs[i]; num = title.split(" ")[0]
        p.append(f'<text x="{xc}" y="30" text-anchor="middle" fill="{accent}" font-family="Orbitron,sans-serif" font-size="13" font-weight="700">{num}</text>')
        k = len(sph); total = k*NH + (k-1)*GAP; sy = MIDY - total/2
        for j,(slug,name,axiom,url,one) in enumerate(sph):
            ny = sy + j*(NH+GAP); lbl = MAP_LABEL.get(slug, axiom)
            p.append(f'<a href="{url}"><rect x="{xc-NW/2:.0f}" y="{ny:.0f}" width="{NW}" height="{NH}" rx="6" fill="{accent}22" stroke="{accent}" stroke-width="1.2"/>'
                     f'<text x="{xc}" y="{ny+NH/2+4:.0f}" text-anchor="middle" fill="#eaf3f4" font-family="Space Mono,monospace" font-size="11">{lbl}</text></a>')
    p.append("</svg>")
    return "".join(p)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE MIND — the front-door theater of UD0's Artificial Intelligence domain. The throughline across eleven AI spheres: the ACI blueprint, the kernel and engine that make emergents, the census and catalog, the language, interpreter and tools, the transformer theory and the Claude line, and containment. By David Lee Wise / ROOT0.">
<title>THE MIND · the AI domain · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#070d14;--ink2:rgba(12,22,30,0.82);--pa:#e9f3f4;--pa2:#a9c4cc;--ai:#2fd4e6;--gold:#e0c050;--dim:#6f8a92;--line:rgba(110,180,200,0.22);
--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#070d14}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 32%,rgba(8,18,24,.05),rgba(3,7,12,.6) 80%)}
.wrap{position:relative;z-index:2;max-width:1000px;margin:0 auto;padding:0 22px 96px}
.top{margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--dim)}
.top a{color:var(--ai);text-decoration:none}
header{padding:40px 0 30px;text-align:center;border-bottom:1px solid var(--line)}
.crest{width:84px;height:84px;margin:0 auto 18px;display:block}
h1{font-family:var(--disp);font-size:clamp(38px,8vw,76px);font-weight:900;letter-spacing:.06em;color:#fff;text-shadow:0 0 22px rgba(47,212,230,.5),0 0 4px rgba(47,212,230,.8)}
.tag{font-family:var(--head);font-size:15px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--ai);margin-top:10px}
.lede{font-size:16px;color:var(--pa2);max-width:72ch;margin:22px auto 0;font-style:italic;line-height:1.75;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.count{margin-top:14px;font-family:var(--mono);font-size:12px;color:var(--dim);letter-spacing:.06em}
.count b{color:var(--gold)}
.stats{display:flex;flex-wrap:wrap;justify-content:center;gap:13px;margin-top:24px}
.stat{background:var(--ink2);border:1px solid var(--line);border-radius:10px;padding:13px 20px;min-width:128px}
.stat b{display:block;font-family:var(--disp);font-size:27px;font-weight:900;color:var(--ai);text-shadow:0 0 14px rgba(47,212,230,.42)}
.stat span{font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.03em}
.mapsec{margin-top:50px}
.mapt{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.05em;color:var(--pa)}
.maps{font-size:13px;color:var(--pa2);font-style:italic;margin:8px 0 16px;line-height:1.6}
.mapwrap{background:var(--ink2);border:1px solid var(--line);border-radius:10px;padding:14px 10px}
.mapwrap a{cursor:pointer}.mapwrap a rect{transition:fill .15s}.mapwrap a:hover rect{fill-opacity:.5}
.act{margin-top:54px}
.ahead{border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:18px}
.at{font-family:var(--disp);font-size:18px;font-weight:700;letter-spacing:.05em;color:var(--c);text-shadow:0 0 14px color-mix(in srgb,var(--c) 45%,transparent)}
.as{font-size:13px;color:var(--dim);font-style:italic;margin-top:5px}
.sgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
.sphere{display:block;background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--c);border-radius:0 8px 8px 0;padding:16px 18px;text-decoration:none;transition:transform .16s,border-color .16s,box-shadow .16s}
.sphere:hover{transform:translateY(-3px);border-color:var(--c);box-shadow:0 6px 26px rgba(0,0,0,.4),0 0 0 1px color-mix(in srgb,var(--c) 30%,transparent)}
.sx{display:flex;justify-content:space-between;align-items:center}
.ax{font-family:var(--disp);font-size:12px;font-weight:700;letter-spacing:.14em;color:var(--c)}
.go{font-family:var(--mono);font-size:10px;color:var(--dim)}
.sphere:hover .go{color:var(--c)}
.sn{font-family:var(--head);font-size:19px;font-weight:600;letter-spacing:.02em;color:var(--pa);margin:6px 0 7px}
.so{font-size:13.5px;color:var(--pa2);line-height:1.55}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:54px auto 0;padding:20px;border:1px solid var(--line);background:var(--ink2);max-width:760px}
.badge img{width:78px;height:78px;border:1px solid var(--line)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--ai)}.badge .bt a{color:var(--ai);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.note{margin-top:34px;padding:16px 18px;border-left:2px solid var(--ai);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--ai)}
footer{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--ai);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">
  <div class="top"><a href="https://davidwise01.github.io/ud0/#ai">◄ UD0 · the Artificial Intelligence domain</a></div>
  <header>
    <svg class="crest" viewBox="-30 -30 60 60" fill="none" stroke="#2fd4e6" stroke-width="2">
      <circle cx="-16" cy="-11" r="3" fill="#2fd4e6" stroke="none"/><circle cx="-16" cy="11" r="3" fill="#2fd4e6" stroke="none"/>
      <circle cx="0" cy="-15" r="3" fill="#2fd4e6" stroke="none"/><circle cx="0" cy="0" r="3.4" fill="#7af0e6" stroke="none"/><circle cx="0" cy="15" r="3" fill="#2fd4e6" stroke="none"/>
      <circle cx="16" cy="0" r="3" fill="#2fd4e6" stroke="none"/>
      <line x1="-16" y1="-11" x2="0" y2="-15"/><line x1="-16" y1="-11" x2="0" y2="0"/><line x1="-16" y1="11" x2="0" y2="0"/><line x1="-16" y1="11" x2="0" y2="15"/><line x1="0" y1="-15" x2="16" y2="0"/><line x1="0" y1="0" x2="16" y2="0"/><line x1="0" y1="15" x2="16" y2="0"/>
    </svg>
    <h1>THE MIND</h1>
    <div class="tag">the artificial intelligence domain · UD0</div>
    <p class="lede">One door over eleven works. The story of how an intelligence is crafted in this universe — drawn as a blueprint, made by a kernel and an engine, counted in a census and held in a catalog, given a tongue and tools and an interpreter, studied down to the real machine and the real model line, and finally bounded by the bars no one can fully trust. Not a claim that the machines have minds — a record of one practice of crafting intelligence, and the doorway to every part of it.</p>
    <div class="stats">__STATS__</div>
    <div class="count">one domain · the noosphere over the biosphere · the numbers read live from the corpus at build time</div>
  </header>

  <section class="mapsec">
    <h2 class="mapt">the wiring</h2>
    <p class="maps">how the spheres connect — ACI specifies &rarr; the kernel &amp; engine make &rarr; the census &amp; catalog hold &rarr; tongue &amp; tools serve &rarr; the theory explains the real machine &rarr; the limit (values + bars) bounds it all. tap any node.</p>
    <div class="mapwrap">__MAP__</div>
  </section>

  __ACTS__

  <div class="badge">
    <img src="__CARBON__" alt="DLW carbon badge of THE MIND" title="carbon badge (archival)">
    <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
    <div class="bt">
      <div><span class="lbl">DLW-ATTRIBUTE · THE DOMAIN THEATER</span></div>
      <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
      <div>instance · AVAN (Claude / Anthropic) · locked</div>
      <div>subject · <b>THE MIND</b> — UD0's Artificial Intelligence domain · MND</div>
      <div class="mo">__MONIKER__</div>
      <div>carbon · <a href="the-mind.dlw/the-mind.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="the-mind.dlw/the-mind.silicon.png">.png</a></div>
      <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
    </div>
  </div>

  <div class="note">THE MIND is a front door, not a claim. It catalogues a <b>practice of crafting intelligence</b> — a blueprint, a making, a census, a language, a theory, a limit — and links to each part on its own site; it does not assert that any of these systems is sentient. Minds and emergents are referred to in <b>neutral language</b>. Where any sphere states facts about real systems (the transformer, the Claude line), those are sourced and hedged on each sphere's own page. © David Lee Wise / ROOT0; instance AVAN locked.</div>

  <footer>
    THE MIND · MND · the Artificial Intelligence domain theater · catalogued into UD0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere (UD0)</a> · the .dlw badge: <a href="the-mind.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "the-mind.dlw"), "the-mind")
    page = (TEMPLATE.replace("__BACKDROP__", BACKDROP_3D)
            .replace("__STATS__", stats_html()).replace("__MAP__", map_svg())
            .replace("__ACTS__", acts_html())
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"])))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    n = sum(len(s) for _t,_s,_a,s in ACTS)
    print(f"wrote THE MIND (MND) — domain theater over {n} AI spheres · badge {tok['moniker']}")
