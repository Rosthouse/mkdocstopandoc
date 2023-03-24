#!/usr/bin/env python3
import panflute as pf

to_remove = []


def prepare(doc: pf.Doc):
    doc.icon_folder = str(doc.get_metadata('icons-folder', './'))
    doc.content_tabs = doc.get_metadata('content-tabs', [])

    doc.admonitions = doc.get_metadata('admonitions', False)
    doc.keys = doc.get_metadata('keys', False)

    pf.debug(doc.content_tabs)


def remove(elem: pf.Element, doc: pf.Doc):
    if elem in to_remove:
        return []
    return elem


def shortcuts(elem: pf.Element, doc: pf.Doc) -> pf.Element:

    if not doc.keys:
        return elem

    if isinstance(elem, pf.Str):
        if elem.text.startswith("++") and elem.text.endswith("++"):
            txt = elem.text
            txt = txt.removeprefix("++")
            txt = txt.removesuffix("++")
            txt = txt.upper()
            elem.text = txt
    return elem


def content_tabs(elem: pf.Element, doc: pf.Doc) -> pf.Element:

    if not hasattr(doc, 'content_tabs'):
        return elem

    if isinstance(elem, pf.Para) and pf.stringify(elem).startswith("==="):
        # pf.debug(elem)
        type = elem.content[2].content[0].text
        if type in doc.content_tabs and isinstance(elem.next, pf.CodeBlock):
            conv = pf.convert_text(elem.next.text)

            new_elem = pf.BlockQuote(
                *conv
            )
            to_remove.append(elem.next)
            return new_elem
        else:
            to_remove.append(elem.next)
            return []

    return elem


def icons(elem: pf.Element, doc: pf.Doc) -> pf.Element:
    if isinstance(elem, pf.Str):
        if elem.text.startswith(":") and elem.text.endswith(":"):
            txt = elem.text
            txt = txt.removeprefix(":")
            txt = txt.removesuffix(":")
            txt = txt.replace("-", "/") + ".svg"
            pf.debug("Exchanging {} for {}".format(elem.text, txt))
            return pf.Image(url=txt, title="ICON {} NOT FOUND".format(txt))

    return elem


def admonitions(elem: pf.Element, doc: pf.Doc) -> pf.Element:

    if doc.admonitions == False:
        return elem

    if isinstance(elem, pf.Para) and pf.stringify(elem).startswith("!!!"):
        if isinstance(elem.next, pf.CodeBlock):
            conv = pf.convert_text(elem.next.text)
            new_elem = pf.BlockQuote(
                pf.Para(
                    pf.Strong(pf.Str(elem.content[2].text.capitalize()))
                ),
                *conv
            )
            to_remove.append(elem.next)
            return new_elem
    return elem


def main(doc: pf.Doc = None):
    return pf.run_filters([shortcuts, icons, admonitions, content_tabs, remove], prepare=prepare)


if __name__ == "__main__":
    main()
