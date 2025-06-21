from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(
    "🤓 [link=https://willmcgugan.github.io/]Will McGugan", guide_style="bold cyan"
)
python_tree = tree.add("🐍 Python expert", guide_style="green")
python_tree.add("⭐ [link=https://github.com/textualize/rich]Rich")
python_tree.add("⭐ [link=https://github.com/textualize/textual]Textual")
python_tree.add("⭐ [link=https://github.com/pyfilesystem/pyfilesystem2]PyFilesystem")
python_tree.add("⭐ [link=https://github.com/wildfoundry/dataplicity-lomond]Lomond")
full_stack_tree = tree.add("🔧 Full-stack developer")
tree.add(
    "📘 [link=https://www.amazon.co.uk/Beginning-Game-Development-Python-Pygame/dp/1590598725]Author"
)
tree.add("📷 [link=https://www.willmcgugan.com/blog/photography/]Photographer[/]")

about = """\
I'm a software engineer, living in [link=https://www.google.com/maps/place/Edinburgh/@55.9411289,-3.3454205,11z]Edinburgh[/], Scotland.

Probably best known for [link=https://github.com/textualize/rich]Rich[/] and [link=https://github.com/textualize/textual]Textual[/]. Two Python libraries that have been downloaded over 3 billion times between them!

I'm currently taking a sabbatical, although I am still maintaining my projects. I'm not currently looking for work, although I could be tempted by the right offer.

[green]Follow me on twitter [bold link=https://twitter.com/willmcgugan]@willmcgugan[/]"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
