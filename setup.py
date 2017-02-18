import ast
import os.path

from setuptools import find_packages, setup


def get_version():
    filename = os.path.join(os.path.dirname(__file__),
                            'publicdns', '__init__.py')
    version = None
    with open(filename, 'r') as f:
        tree = ast.parse(f.read(), filename)
        for node in ast.iter_child_nodes(tree):
            if not isinstance(node, ast.Assign) or len(node.targets) != 1:
                continue
            target, = node.targets
            if (isinstance(target, ast.Name) and
                    target.id == '__version_info__'):
                version = ast.literal_eval(node.value)
            return '.'.join([str(x) for x in version])


filename = os.path.join(os.path.dirname(__file__), 'test-requirements.txt')
with open(filename, 'r') as f:
    test_requirements = list(filter(None, f.read().split('\n')))

filename = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(filename, 'r') as f:
    reqs = list(filter(None, f.read().split('\n')))
    install_requirements = reqs + test_requirements

setup(
    name='publicdns',
    version=get_version(),
    description='',
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/ssut/publicdns',
    author='SuHun Han',
    author_email='ssut' '@' 'ssut.me',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    tests_require=test_requirements,
    install_requires=install_requirements,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ]
)
