#from nose.commands import nosetests
from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages


try:
    # Optional tasks, only needed for development
    import paver.doctools
    import paver.misctasks
    from paved import *
    from paved.dist import *
    from paved.util import *
    from paved.docs import *
    from paved.pycheck import *
    from sphinxcontrib import paverutils
    ALL_TASKS_LOADED = True
except ImportError, e:
    info("some tasks could not not be imported.")
    debug(str(e))
    ALL_TASKS_LOADED = False

def read_project_version(py=None, where='.', exclude=['bootstrap', 'pavement', 'doc', 'docs', 'test', 'tests', ]):
    if not py:
        py = path(where) / find_packages(where=where, exclude=exclude)[0]
    py = path(py)
    if py.isdir():
        py = py / '__init__.py'
    __version__ = None
    for line in py.lines():
        if '__version__' in line:
            exec line
            break
    return __version__

NAME = 'EasyProcess'
URL = 'https://github.com/ponty/easyprocess'
DESCRIPTION = 'Easy to use python subprocess interface.'
VERSION = read_project_version()


classifiers = [
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ]

install_requires = [
    'setuptools',
    ]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.rst', 'r').read(),
    classifiers=classifiers,
    keywords='subprocess interface',
    author='ponty',
    #author_email='',
    url=URL,
    license='BSD',
    packages=find_packages(exclude=['bootstrap', 'pavement', ]),
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=False,
    install_requires=install_requires,
    )


options(
    sphinx=Bunch(
        docroot='docs',
        builddir="_build",
        ),
    pdf=Bunch(
        builddir='_build',
        builder='latex',
    ),
    )

if ALL_TASKS_LOADED:
    
    options.paved.clean.patterns += ['*.pickle', '*.doctree', '*.gz' , 'nosetests.xml', 'sloccount.sc']
    
    options.paved.dist.manifest.include.remove('distribute_setup.py')
    
    
    @task
    @needs('sloccount', 'paver.doctools.html', 'pdf', 'sdist', 'nose')
    def hudson():
        '''task collection for hudson.
        '''
        pass
    
    @task
    @needs('sphinxcontrib.paverutils.html')
    def html():
        pass