import re


def subsctract_statis_js_files(content: str):
    # Helper function that remove files like src="/static/js(css)/11.1081b612.chunk.js(css)"
    # Because for each build they will be different. That makes impossible to compare hashes
    # Example: </style><link href="/static/css/main.d60c75f7.chunk.css"
    # Example: rel="stylesheet"><script charset="utf-8" src="/static/js/52.0625a25d.chunk.js">
    return re.sub(r"(?:src|href)=\"/static/(?:js|css)/\S+\.\S+.chunk\.(?:js|css)\"", "", content)
