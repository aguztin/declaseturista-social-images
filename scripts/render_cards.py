#!/usr/bin/env python3
"""DeClaseTurista social card generator. No third-party Python packages needed.
Usage: python scripts/render_cards.py
All example values are DEMOS and must never be presented as verified deals.
"""
from pathlib import Path
from html import escape

OUT = Path("plantillas")
OUT.mkdir(exist_ok=True)
NAVY="#18385C"; AQUA="#9FE6DE"; CORAL="#FF786F"; YELLOW="#FFDB59"
def t(x,y,value,size=40,weight=700,color=NAVY,anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(str(value))}</text>'
def box(x,y,w,h,color="white",r=32):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{color}"/>'
def pill(x,y,w,label,color="white",text_color=NAVY):
    return box(x,y,w,70,color,32)+t(x+w/2,y+47,label,28,800,text_color)
def base(kind,destination,tagline):
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">',
       '<defs><linearGradient id="bg" x2="0" y2="1"><stop stop-color="#A5ECE3"/><stop offset="1" stop-color="#85D8D4"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#22536A" flood-opacity=".14"/></filter></defs>',
       '<rect width="1080" height="1350" fill="url(#bg)"/>',
       '<circle cx="1015" cy="390" r="165" fill="#C7F3E8" opacity=".8"/>',
       '<circle cx="45" cy="1120" r="200" fill="#C7F3E8" opacity=".55"/>',
       t(540,104,"✈  DeClaseTurista",55,900),
       t(540,148,"Ayudas, ofertas y oportunidades para viajar",22,500),
       box(155,180,770,76,YELLOW,38),t(540,232,"¡"+kind.upper()+"!",34,900),
       t(540,345,destination.upper(),92 if len(destination)<13 else 68,900),
       t(540,405,tagline,30,700),
       '<path d="M 860 380 l 110 -60 -28 54 20 40 -35 -12 -30 30 8 -42 z" fill="#FFFFFF" opacity=".75"/>']
    return s
def price(s,label,price):
    s += [f'<g filter="url(#shadow)">{box(90,455,900,240,CORAL,46)}</g>',
          t(540,520,label,30,800,"white"),t(540,637,price,95 if len(price)<12 else 76,900,"white")]
def footer(s,source):
    s += [box(90,1188,900,104,"white",34),t(540,1232,"CONSULTÁ DISPONIBILIDAD Y CONDICIONES",23,900),
          t(540,1267,source,23,700),'</svg>']
def save(name,s):
    (OUT/name).write_text("\n".join(s),encoding="utf-8")
def flight():
    s=base("Oferta de vuelos","Madrid","España · ida y vuelta")
    price(s,"TARIFA DE EJEMPLO · POR PERSONA","USD 650")
    s += [box(90,735,900,126),t(540,787,"BUENOS AIRES  →  MADRID",35,900),t(540,830,"EZE  →  MAD",30,700),
          box(90,887,900,126),t(540,940,"12/02–02/03 · 18 días",37,900),t(540,984,"Febrero–marzo 2027",28,600),
          pill(90,1038,900,"EJEMPLO VISUAL · PRECIO NO VERIFICADO",YELLOW)]
    footer(s,"Link de reserva en el texto del post");save("01-vuelos.svg",s)
def package():
    s=base("Paquete turístico","Cancún","México · vuelo + hotel")
    price(s,"PRECIO DE EJEMPLO · POR PERSONA","USD 1.250")
    s += [box(90,735,900,150),t(540,790,"✈  Vuelo ida y vuelta",36,900),t(540,850,"🏨  Hotel · 7 noches",35,800),
          box(90,908,900,115),t(540,957,"10/05–17/05 · 7 noches",35,900),t(540,997,"Mayo 2027",27,600),
          pill(90,1045,900,"EJEMPLO · SERVICIOS SIN VERIFICAR",YELLOW)]
    footer(s,"Aclarar régimen, traslados e impuestos");save("02-paquetes.svg",s)
def multi():
    s=base("Multidestino","Europa","Madrid + Roma + París")
    price(s,"PRECIO TOTAL DE EJEMPLO · POR PERSONA","USD 980")
    s += [box(90,725,900,225),t(540,781,"EZE → MAD → FCO → CDG → EZE",31,900),
          t(540,834,"Madrid  •  Roma  •  París",33,800),
          t(540,894,"3 ciudades · 21 días",32,700),
          box(90,972,900,110),t(540,1018,"03/04–24/04 · 21 días",35,900),t(540,1061,"Abril 2027",27,600),
          pill(90,1100,900,"EJEMPLO · TRAMOS SIN VERIFICAR",YELLOW)]
    footer(s,"Confirmar cada tramo antes de publicar");save("03-multivuelos.svg",s)
if __name__=="__main__":
    flight();package();multi()
    print("Generated 3 SVG templates in plantillas/")
