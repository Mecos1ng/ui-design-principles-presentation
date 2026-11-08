# -*- coding: utf-8 -*-
"""Fill the YMH213 course template with presentation_content.py.

Usage: python build_presentation.py <template.pptx> <output.pptx>
Also writes Kaynak_Rehberi.md next to the output file.
"""
import copy
import os
import re
import sys

from pptx import Presentation
from pptx.util import Pt

import presentation_content as C

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
prs = Presentation(TEMPLATE)
slides = list(prs.slides)
cover, outline, proto_a, proto_b, questions, refs = slides
PROTO_TREE = copy.deepcopy(proto_a.shapes._spTree)
REFS_TREE = copy.deepcopy(refs.shapes._spTree)


def ph(slide, idx=None, kind=None):
    for s in slide.placeholders:
        f = s.placeholder_format
        if (idx is not None and f.idx == idx) or (kind and f.type is not None and str(f.type).startswith(kind)):
            return s
    raise KeyError((idx, kind))


def set_title(slide, text):
    tf = ph(slide, kind="TITLE").text_frame
    p = tf.paragraphs[0]
    for r in list(p.runs)[1:]:
        r._r.getparent().remove(r._r)
    p.runs[0].text = text


def set_body(slide, items, sizes=None, bullets=True, align=None):
    tf = ph(slide, idx=1).text_frame
    tf.word_wrap = True
    for p in list(tf.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    first = True
    for level, text in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.level = level
        r = p.add_run()
        r.text = text
        r._r.get_or_add_rPr().set("lang", "en-US")
        if sizes:  # otherwise keep the template's own sizes (26 / 23 pt)
            r.font.size = Pt(sizes[min(level, len(sizes) - 1)])
        if align:
            p._p.get_or_add_pPr().set("algn", align)
        if not bullets:
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", "457200")
            pPr.set("indent", "-457200")
            for tag in ("a:buNone",):
                el = pPr.makeelement("{http://schemas.openxmlformats.org/drawingml/2006/main}buNone", {})
                pPr.insert(0, el)


def set_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def clone_slide(tree):
    s = prs.slides.add_slide(proto_a.slide_layout)
    sp = s.shapes._spTree
    for child in list(sp):
        sp.remove(child)
    for child in copy.deepcopy(tree):
        sp.append(child)
    return s


def set_slide_number(slide, n):
    for t in slide.shapes._spTree.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}fld"):
        for el in t.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t"):
            el.text = str(n)


# ---- cover --------------------------------------------------------------
for shape in cover.shapes:
    if not shape.has_text_frame:
        continue
    for p in shape.text_frame.paragraphs:
        txt = "".join(r.text for r in p.runs)
        if txt.strip() == "Title of the Presentation":
            p.runs[0].text = C.TITLE
            for r in p.runs[1:]:
                r.text = ""
        if "4" in txt and "Presenter" in txt:
            runs = list(p.runs)
            # drop ", 4" "th" " Presenter"
            for i, r in enumerate(runs):
                if r.text.startswith(", 4"):
                    for rr in runs[i:i + 3]:
                        rr._r.getparent().remove(rr._r)
                    break

# ---- outline ------------------------------------------------------------
set_body(outline, C.OUTLINE)
set_notes(outline, "Presenter 1 shows this slide quickly: 'Here is the plan for today.'")

# ---- content slides -----------------------------------------------------
content_slides = []
for i, data in enumerate(C.SLIDES):
    s = proto_a if i == 0 else proto_b if i == 1 else clone_slide(PROTO_TREE)
    set_title(s, data["title"])
    set_body(s, data["bullets"])
    if data.get("kind") == "handover":
        # first line ("Presenter 1 ➜ Presenter 2") stands out in bold
        ph(s, idx=1).text_frame.paragraphs[0].runs[0].font.bold = True
        notes = (f"HANDOVER – PRESENTER {data['from_speaker']} ENDS HERE\n\n{data['script_from']}\n\n"
                 f"PRESENTER {data['speaker']} STARTS HERE\n\n{data['script']}\n\n"
                 "SOURCES FOR THIS SLIDE\n" + "\n".join("• " + x for x in data["sources"]))
    else:
        notes = f"PRESENTER {data['speaker']} – SCRIPT\n\n{data['script']}\n\nSOURCES FOR THIS SLIDE\n" + "\n".join("• " + x for x in data["sources"])
    set_notes(s, notes)
    content_slides.append(s)

# ---- questions ----------------------------------------------------------
set_body(questions, [(0, "Thank you for listening!"), (0, "Do you have any questions?")], sizes=(28,), bullets=False, align="l")
set_notes(questions, "Possible questions and short answers:\n\n" + "\n\n".join(f"Q: {q}\nA: {a}" for q, a in C.QA))

# ---- references (two slides) ---------------------------------------------
half = (len(C.REFERENCES) + 1) // 2
ref_items = [(0, f"[{i}] {r}") for i, r in enumerate(C.REFERENCES, 1)]
set_body(refs, ref_items[:half], sizes=(16,), bullets=False, align="l")
refs2 = clone_slide(REFS_TREE)
set_title(refs2, "References (cont.)")
set_body(refs2, ref_items[half:], sizes=(16,), bullets=False, align="l")

# ---- order --------------------------------------------------------------
order = [cover, outline] + content_slides + [questions, refs, refs2]
lst = prs.slides._sldIdLst
id_by_part = {prs.slides.part.related_part(e.rId): e for e in lst}  # noqa
ids = list(lst)
rid_of = {}
for e in ids:
    rid_of[prs.part.related_part(e.rId)] = e
for e in ids:
    lst.remove(e)
for n, s in enumerate(order, 1):
    lst.append(rid_of[s.part])
    set_slide_number(s, n)

prs.save(OUT)
print("saved", OUT, "slides:", len(order))

# ---- Turkish source guide --------------------------------------------------
lines = [
    f"# Kaynak Rehberi – {C.TITLE}",
    "",
    "Bu dosya, hoca \"Bu cümleyi nereden aldınız?\" diye sorduğunda cevap verebilmeniz için hazırlandı.",
    "Ana kaynağımız Google Scholar'da bulup AIS eLibrary'den (aisel.aisnet.org) indirdiğimiz şu makale: **Adipat & Zhang (2005), \"Interface design for mobile applications\", AMCIS 2005** ([1]).",
    "Sayfa numaraları, konferans kitabındaki sayfa numaralarıdır (pp. 2281–2290). PDF'nin 1. sayfası AIS kapak sayfası, 2. sayfası ise s. 2281.",
    "Tüm metinler kaynaklardan **kendi cümlelerimizle** yazıldı; slaytlarda doğrudan alıntı yok (aşağıdaki 'Kaynak detayı' satırlarındaki tırnaklı ifadeler, kaynağın orijinal ifadeleridir; hoca sorarsa göstermek içindir). Köşeli parantezdeki numaralar (örn. [1]) References slaytındaki numaralardır.",
    "",
    "## Slayt slayt kaynaklar",
    "",
]
for i, d in enumerate(C.SLIDES, 3):
    who = (f"Geçiş: Konuşmacı {d['from_speaker']} ➜ Konuşmacı {d['speaker']}"
           if d.get("kind") == "handover" else f"Konuşmacı {d['speaker']}")
    lines += [f"### Slayt {i} – {d['title']} ({who})", "", d["tr"], "", "**Kaynak detayı:**", ""]
    lines += ["- " + x for x in d["sources"]]
    lines += ["", "**Slayttaki maddeler:**", ""]
    lines += [("  " * lvl) + "- " + t for lvl, t in d["bullets"]]
    lines += [""]
lines += ["## Olası sorular ve cevaplar", ""]
for q, a in C.QA:
    lines += [f"- **{q}**  ", f"  {a}"]
lines += ["", "## References (IEEE)", ""]
lines += [f"{i}. [{i}] {r}" for i, r in enumerate(C.REFERENCES, 1)]
lines += ["", "## Konuşma süreleri (kelime sayısı, ~120 kelime/dk)", ""]
for sp in (1, 2, 3):
    words = len(re.findall(r"\S+", C.speaker_script(sp)))
    lines.append(f"- Konuşmacı {sp}: {words} kelime ≈ {words / 120:.1f} dk")
guide = os.path.join(os.path.dirname(os.path.abspath(OUT)), "Kaynak_Rehberi.md")
with open(guide, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("wrote", guide)
