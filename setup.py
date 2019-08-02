from setuptools import setup

setup(name='frechetdist',
      version='0.3',
      description='Calculate discrete Frechet distance',
      url='https://github.com/spiros/discrete_frechet',
      author='Spiros Denaxas',
      author_email='s.denaxas@gmail.com',
      license='Apache License 2.0',
      packages=['frechetdist'],
      install_requires=[
          'numpy',
      ],
      zip_safe=False)