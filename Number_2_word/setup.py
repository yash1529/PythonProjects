from setuptools import setup,find_packages


with open("README.txt", mode="r") as f:
    long_description = f.read()

setup(
    name="Convert_number_to_word", # Replace with your own username
    version="0.0.1",
    author="Yash Yadav",
    author_email="yashyadav1529@gmail.com",
    description="To convert positive integers into words as per international or Indian numbering system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)