from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR = "Peter Wainaina"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [
    'streamlit',]
setup(name =SRC_REPO,
      version='0.1.0', 
      author=AUTHOR,
      author_email="wainainavibora@gmai.com",
      description="A SMALL MOVIE RECOMMENDER SYSTEM",
      long_description=long_description,
        long_description_content_type="text/markdown",
        package = [SRC_REPO],
        install_requires=LIST_OF_REQUIREMENTS,
        python_requires='>=3.7')