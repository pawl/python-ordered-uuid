from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

setup(
    name='python-ordered-uuid',
    version='1.3.1',
    description='A python implementation of Ordered UUID.',
    url='https://github.com/pawl/python-ordered-uuid',
    author='Paul Brown',
    author_email='paul90brown+pypi@gmail.com',
    long_description=long_description,
    py_modules=['ordered_uuid'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)
