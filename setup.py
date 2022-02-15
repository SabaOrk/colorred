from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='colorize',
  version='0.0.1',
  description='An advanced color name identifier by hex or rgb',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Saba Orkoshneli',
  author_email='orkoshnelisaba@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='colorize', 
  packages=find_packages(),
  install_requires=['webcolors'] 
)