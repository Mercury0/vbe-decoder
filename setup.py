from setuptools import setup, find_packages

setup(
    name='vbe-decoder',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'vbe-decoder=vbe_decoder.__main__:main',
        ],
    },
    description='Decode an encoded VBScript, often seen as a .vbe file',
    author='John Hammond',
    author_email='your-email@example.com',
    url='https://github.com/Mercury0/vbe-decoder',
)
