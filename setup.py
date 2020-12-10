import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="assingment-pkg-mohamed-abdo", # Replace with your own username
    version="0.0.1",
    author="Moahmed abdo",
    author_email="mohamad.abdo@gmail.com",
    description="algorithms toolbox course package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohamed-abdo/algorthims-toolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)