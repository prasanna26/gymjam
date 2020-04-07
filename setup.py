from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["gym>=0.14"]

setup(
    name="gymjam",
    version="0.0.1",
    author="Matthew Fontaine",
    author_email="tehqin@gmail.com",
    description="A package for testing action sequence generation in OpenAI Gym.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tehqin/gymjam/",
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={
        'console_scripts': [
            "gymjam = gymjam.__main__:main",
        ]
    },
)


