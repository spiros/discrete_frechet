import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='frechetdist',
    version='0.7',
    description='Calculate discrete Frechet distance',
    url='https://github.com/spiros/discrete_frechet',
    author='Spiros Denaxas',
    author_email='s.denaxas@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    py_modules=['frechetdist'],
    install_requires=[
        'numpy>=1.26.0',
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent"
    ]
)
