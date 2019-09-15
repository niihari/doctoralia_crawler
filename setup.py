from setuptools import setup

setup(
    name='doctoralia_crawler',
    version='1.0',
    packages=['data', 'pages', 'pages.base', 'selenium_utils'],
    url='',
    license='Apache 2.0',
    author='Gustavo Shinji Inoue',
    author_email='gs.inoue@gmail.com',
    description='Doctoralia Crawler',
    scripts=['doctoralia_crawler.py']
)
