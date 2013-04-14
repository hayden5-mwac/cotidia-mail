import os
from distutils.core import setup
from setuptools import find_packages


VERSION = __import__("cotimail").VERSION

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]

install_requires = [
    'djrill==0.3.1',
    'cssutils==0.9.10',
    # 'django-reversion==1.6.3',
    # 'PIL==1.1.7',
    # 'sorl-thumbnail==11.12',
    # 'south==0.7.6',
    # '-e git+https://bitbucket.org/guillaumepiot/cotidia-redactor.git',
    # '-e git+https://bitbucket.org/guillaumepiot/cotidia-filemanager.git',
    # '-e git+https://guillaumepiot@bitbucket.org/guillaumepiot/cotidia-admin-tools.git#egg=admin_tools',
]

# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('cotimail'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:] # Strip "cotimail/" or "cotimail\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name="cotimail",
    description="Transaction email management",
    version=VERSION,
    author="Guillaume Piot",
    author_email="guillaume@cotidia.com",
    url="https://bitbucket.org/guillaumepiot/cotimail",
    download_url="https://bitbucket.org/guillaumepiot/cotidia-cms-base/downloads/cotimail-%s.tar.gz" % VERSION,
    package_dir={'cotimail': 'cotimail'},
    packages=packages,
    package_data={'cotimail': data_files},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)