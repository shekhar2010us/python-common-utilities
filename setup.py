from setuptools import setup, find_packages

setup(name='common_utilities',
      version='0.1',
      description='HCM DS Common Utilities',
      long_description="""api for common utilities used for multiple projects""",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Programming Language :: Python :: 3.6',
          'License :: Other/Proprietary License'
      ],
      keywords='common utilities',
      url='https://alm.oraclecorp.com/dda/#projects/das-ai-commonutilities/scm/das-ai-commonutilities.git',
      author='Shekhar Agrawal',
      author_email='shekhar.a.agrawal@oracle.com',
      license='Property',
      packages=find_packages(),
      package_data={'':['*.json','*.cfg','*.ini','*.conf']},
      install_requires=['flask',\
                        'gensim',\
                        'spacy',\
                        'matplotlib',\
                        'xmltodict',\
                        'beautifulsoup4',\
                        'sklearn',\
                        'numpy',\
                        'nltk',\
                        'pandas',\
                        'torch',\
                        'xgboost',\
                        'pytest',\
                        'xlrd'],
      )