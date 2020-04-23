import re

from django.template import loader

from common.markdown.club_renderer import YOUTUBE_RE

IMAGE_RE = re.compile(r"(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|jpeg|gif|png|ico)")

CUSTOM_ICONS = {
    "www.youtube.com": """<i class="fab fa-youtube"></i>""",
    "youtube.com": """<i class="fab fa-youtube"></i>""",
    "youtu.be": """<i class="fab fa-youtube"></i>""",
    "github.com": """<i class="fab fa-github"></i>""",
    "twitter.com": """<i class="fab fa-twitter"></i>""",
    "facebook.com": """<i class="fab fa-facebook"></i>""",
    "www.patreon.com": """<i class="fab fa-patreon"></i>""",
    "apple.com": """<i class="fab fa-apple"></i>""",
    "vk.com": """<i class="fab fa-vk"></i>""",
    "medium.com": """<i class="fab fa-medium"></i>""",
}

CUSTOM_PARSERS = {
    "www.youtube.com": {
        "template": loader.get_template("posts/embeds/youtube.html"),
        "data": lambda post: {
            "src": YOUTUBE_RE.match(post.url).group(1)
        }
    },
    "github.com": {
        "template": loader.get_template("posts/embeds/github.html"),
        "data": lambda post: {
            "metadata": post.metadata
        }
    },
    "www.patreon.com": {
        "do_not_parse": True
    },
}
