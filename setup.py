import setuptools

with open("requirements.txt", "r") as f:
	requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discordservices.py",
    version="0.0.1",
    author="mischievousdev",
    author_email="miscdev.py@gmail.com",
    description="A simple API wrapper for discordservices.net",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiscordServices/discordservices.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)