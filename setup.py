#!/usr/bin/env python

from setuptools import setup


# Dynamically retrieve the version information from the Dialogflow module
version = __import__('dialogflow').__version__
author = __import__('dialogflow').__author__
author_email = __import__('dialogflow').__email__

req = open('requirements.txt')
requirements = req.readlines()
req.close()

setup(
    name='dialogflow',
    version=version,
    url='https://github.com/vkosuri/Dialogflow',
    description='Python implementation for Dialogflow .',
    author=author,
    author_email=author_email,
    packages=[
        'dialogflow'
    ],
    package_dir={'dialogflow': 'dialogflow'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=True,
    platforms=['any'],
    keywords=['dialogflow', 'api.ai', 'dialogflow python', 'bot', 'speech', 'voice'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=[]
)