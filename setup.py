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
          'tensorflow',
          'tensorflow_hub',
          'scipy',
          'numpy'
      ],
      dependency_links=[
        "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz"
      ]
      ,
      zip_safe=False)
