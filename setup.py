from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", encoding="utf-8") as f:
        l = f.readlines()
        return [line.strip() for line in l if line.strip() and not line.startswith("#")]

setup(
    name="RvLProMaster",
    version="0.1.1",
    packages=find_packages(),
    install_requires=read_requirements(),
    author="YudhoPatrianto",
    author_email="kydh01123@gmail.com",
    description="The Telegram Bot API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YudhoPRJKT-Teams/RvLProMaster",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.12',
)
