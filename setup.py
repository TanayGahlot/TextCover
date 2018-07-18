"""it installs TextCover package."""
#oggpnosn
#hkhr
from setuptools import setup

setup(name='TextCover',
      version='0.1',
      description='A text summarization module.',
      url='https://github.com/TanayGahlot/TextCover',
      author='Tanay Gahlot',
      author_email='tanaygahlot@gmail.com',
      license='MIT',
      packages=['TextCover'],
      install_requires=[
          'spacy',
          'tensorflow'
      ],
      zip_safe=False)
