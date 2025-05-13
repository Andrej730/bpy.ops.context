import markdown
import pystache
from typing import Union
from html2text import html2text
from lxml import html, etree
from pathlib import Path
from util import cprint

TAGS = {
    "TAG_CONTEXT_NOT_USED": "⬜ context is not used",
    "TAG_CONTEXT_OVERRIDE_SUPPORT_PARTIAL": "🧩 partial context override",
    "TAG_CONTEXT_OVERRIDE_SUPPORT": "✅ context override",
    "TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED": "❌ context override",
    "TAG_ACTIVE_OBJECT_NOT_AFFECTED": "active object is not affected",
}
SRC = Path(__file__).parent
OPS_MD = SRC / "ops.md"
INDEX_MUSTACHE = SRC / "index.mustache"
DOCS = SRC.parent / "docs"
DEBUG_HTML = DOCS / "debug.html"
INDEX_MD = DOCS / "index.md"


def main():
    html_text = markdown.markdown(OPS_MD.read_text(encoding="utf-8"))
    DEBUG_HTML.write_text(html_text, encoding="utf-8")
    tree: html.HtmlElement = html.fromstring(html_text)

    # Parse existing descriptions to `ops`.
    ops: dict[str, str] = {}
    op_headers: list[str] = tree.xpath("//h3/code/text()")
    op_lists: list[html.HtmlElement] = tree.xpath("//ul")
    assert len(op_headers) == len(op_lists)
    for op_header, op_list in zip(op_headers, op_lists, strict=True):
        op_description = ""
        list_item: html.HtmlElement
        for list_item in op_list.xpath("li"):
            text: Union[str, None] = list_item.text
            # Seems to be `None` when item starts with `<code>`.
            if text is not None and text.startswith("TAG_"):
                assert text in TAGS, f"Unknown tag: '{text}'."
                md_text = f"* {TAGS[text]}"
            else:
                html_text = etree.tostring(list_item, encoding="unicode")
                md_text = html2text(html_text).strip()
            op_description += f"{md_text}\n"
        ops[op_header] = op_description

    # Generate pystache context.
    context = {}
    context_ops = context.setdefault("ops", [])
    for op_name, op_description in ops.items():
        op_context = {
            "op_name": op_name,
            "op_description": op_description,
        }
        context_ops.append(op_context)

    # Render and save.
    rendered = pystache.render(INDEX_MUSTACHE.read_text(), context)
    rendered = rendered.rstrip() + "\n"
    INDEX_MD.write_text(rendered, encoding="utf-8")
    cprint(f"{{GREEN_CYAN}}index.md updated.")


if __name__ == "__main__":
    main()
