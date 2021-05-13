import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="kingdom-guardian",
    version="0.0.1dev1",
    description="Simple but safe authentication & authorization facilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rui Conti",
    author_email="rui@t10.digital",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keyords="webserver, monolothic, modular, ddd, clean architecture",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    url="https://github.com/t10d/chisel",
    project_urls={
        "Issues": "https://github.com/t10d/chisel/issues",
        "Source": "https://github.com/t10d/chisel",
    },
)
