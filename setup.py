# Copyright 2021 ncdhz

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
import os
from sys import platform as _platform

NAME = 'sentenceLabel'
APP = [NAME + '.py']
REQUIRES_PYTHON = '>=3.0.0'
required_packages = find_packages()
here = os.path.abspath(os.path.dirname(__file__))
about = {}

with open(os.path.join(here, 'libs', '__init__.py')) as f:
    exec(f.read(), about)

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icons/logo.icns'
}

# OS specific settings
SET_REQUIRES = []
if _platform == "linux" or _platform == "linux2":
   # linux
   print('linux')
elif _platform == "darwin":
   # MAC OS X
   SET_REQUIRES.append('py2app')

setup(
    app=APP,
    name=NAME,
    version=about['__version__'],
    author='ncdhz',
    author_email='1137436221@qq.com',
    description='多项选择文章打标软件',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    url='https://github.com/ncdhz/sentence-label',
    python_requires=REQUIRES_PYTHON,
    package_dir={'sentenceLabel': '.'},
    packages=required_packages,
    entry_points={
        'console_scripts': [
            'sentence-label=sentenceLabel.sentenceLabel:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        'pyqt5',
        'nltk'
    ],
    zip_safe=False,
    license="Apache license",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Science/Research",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    options={'py2app': OPTIONS},
    setup_requires=SET_REQUIRES,
)
