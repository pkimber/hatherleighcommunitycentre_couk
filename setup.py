import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='kb-alphaee-couk',
    packages=['project', 'project.management', 'project.management.commands', 'web', 'dash', 'settings'],
    package_data={
        'project': [
            'static/*.*',
            'static/img/*.*',
            'static/img/project/*.*',
            'templates/*.*',
            'templates/project/*.*',
        ],

        'web': [
            'templates/*.*',
            'templates/web/*.*',
        ],

        'dash': [
            'templates/*.*',
            'templates/dash/*.*',
        ],
    },
    version='0.0.12',
    description='AlphaEE',
    author='Patrick Kimber',
    author_email='code@pkimber.net',
    url='ssh://git@bitbucket.org/pkimber/hatherleighcommunitycentre_couk.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)
