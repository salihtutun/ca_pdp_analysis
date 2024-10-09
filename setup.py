
from setuptools import setup, find_packages

setup(
    name='ca_pdp_analysis',  # Your package name
    version='0.1.0',         # Initial release version
    author='Salih Tutun',
    author_email='salihtutun@wustl.edu',
    description='Partial Dependence Plot (PDP) Analysis Tool for Machine Learning Models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/salihtutun/ca_pdp_analysis',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'matplotlib',
        'xgboost',
        'seaborn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
