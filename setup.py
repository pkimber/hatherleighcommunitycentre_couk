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
    name='kb-hatherleighcommunitycentre-couk',
    packages=['web', 'project', 'project.management', 'project.management.commands', 'dash', 'settings'],
    package_data={
        'project': [
            'static/*.*',
            'static/ico/*.*',
            'static/img/*.*',
            'static/img/project/*.*',
            'static/project/*.*',
            'static/project/css/*.*',
            'static/project/js/*.*',
            'templates/*.*',
            'templates/project/*.*',
        ],

        'web': [
            'static/*.*',
            'static/web/*.*',
            'static/web/css/*.*',
            'templates/*.*',
            'templates/web/*.*',
        ],

        'dash': [
            'templates/*.*',
            'templates/dash/*.*',
        ],
    },
    version='0.0.17',
    description='Hatherleigh Community Centre',
    author='Patrick Kimber',
    author_email='code@pkimber.net',
    url='git@github.com:pkimber/hatherleighcommunitycentre_couk.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 1.8',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)