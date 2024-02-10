import setuptools
with open ("README.md", "r", encoding='utf-8') as f:
    long_desription = f.read()  

__version__ = "0.0.0"
REPO_NAME= "Text_summarizer_Project"
AUTHOR_USER_NAME = "SidharthVerma"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sidharthvermaiiits@gmail.com"

setuptools.setup (
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A project on text summarization",
    long_description = "long_description",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"


),
