from setuptools import setup

install_requires = [
    'html5lib',
    ]

setup(name='toc',
      description='Table of contents generator for html',
      author='Youngrok Pak',
      author_email='pak.youngrok@gmail.com',
      keywords= 'toc table contents html',
      url='https://github.com/youngrok/toc',
      version='0.0.11',
      packages=['toc',
                ],
      classifiers = [
                     'Development Status :: 3 - Alpha',
                     'Topic :: Software Development :: Libraries',
                     'License :: OSI Approved :: BSD License']
      )
