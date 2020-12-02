import markdown

from pathlib import Path

paths = Path("posts").glob('**/*.md')
for path in paths:
    markdown.markdownFromFile(
        input=str(path),
        output=str(path.with_suffix(".html")),
    )
