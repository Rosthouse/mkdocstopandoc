#!/usr/bin/env python3
import panflute as pf

to_remove = []


def prepare(doc: pf.Doc):
    doc.icon_folder = str(doc.get_metadata('icons-folder', './'))
    doc.scripting_language = str(
        doc.get_metadata('scripting-language', 'GDScript')
    )


def remove(elem: pf.Element, doc: pf.Doc):
    if elem in to_remove:
        return []
    return elem


def shortcuts(elem: pf.Element, doc: pf.Doc) -> pf.Element:
    if isinstance(elem, pf.Str):
        if elem.text.startswith("++") and elem.text.endswith("++"):
            txt = elem.text
            txt = txt.removeprefix("++")
            txt = txt.removesuffix("++")
            txt = txt.upper()
            elem.text = txt
    return elem


def code_tabs(elem: pf.Element, doc: pf.Doc) -> pf.Element:
    if isinstance(elem, pf.Para) and pf.stringify(elem).startswith("==="):
        # pf.debug(elem)
        type = elem.content[2].content[0].text
        if type == doc.scripting_language and isinstance(elem.next, pf.CodeBlock):
            conv = pf.convert_text(elem.next.text)

            new_elem = pf.BlockQuote(
                *conv
            )
            to_remove.append(elem.next)
            return new_elem
        else:
            to_remove.append(elem.next)
            return []
        # txt: str = elem.content[2].text
        # if txt == "C#":
        #     # if isinstance(elem.next, pf.CodeBlock):
        #     conv = pf.convert_text(elem.next.text)
        #     new_elem = pf.BlockQuote(
        #         pf.Para(
        #             pf.Strong(pf.Str(elem.content[2].text.capitalize()))
        #         ),
        #         *conv
        #     )
        #     to_remove.append(elem.next)
        #     return new_elem
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


def admonition(elem: pf.Element, doc: pf.Doc) -> pf.Element:
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


def main(doc=None):
    return pf.run_filters([shortcuts, icons, admonition, code_tabs, remove], prepare=prepare)


if __name__ == "__main__":
    main()
