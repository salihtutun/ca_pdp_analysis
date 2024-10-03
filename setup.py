
from setuptools import setup, find_packages

setup(
    name='ca_pdp_analysis',
    version='0.1',
    description='Context-Aware Partial Dependence Plot (CA-PDP) Analysis Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/your-repo/ca_pdp_analysis',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'scipy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
