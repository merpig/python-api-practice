from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='testfolder',
      version='0.1',
      description='The best testfolder in the world',
      url='http://github.com/merpig/python-api-practice',
      author='merpig',
      author_email='peteram1@sewanee.edu',
      license='MIT',
      packages=['testfolder'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)