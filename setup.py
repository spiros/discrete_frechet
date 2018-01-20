from setuptools import setup

setup(name='frechetdist',
      version='1.0.0.dev0',
      description='Calculate discrete Frechet distance',
      url='https://github.com/spiros/frechetdist',
      author='Spiros Denaxas',
      author_email='s.denaxas@gmail.com',
      license='Apache License 2.0',
      packages=['frechetdist'],
      install_requires=[
          'numpy',
      ],
      zip_safe=False)