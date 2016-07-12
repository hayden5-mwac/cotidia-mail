import os
from distutils.core import setup


VERSION = __import__("cotimail").VERSION

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]

install_requires = [
    'django-form-utils==1.0.3',
    'django-filter==0.13.0'
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
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[9:]  # Strip "cotimail/" or "cotimail\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name="cotimail",
    description="A Django transaction email manager.",
    version=VERSION,
    author="Guillaume Piot",
    author_email="guillaume@cotidia.com",
    url="https://bitbucket.org/guillaumepiot/cotimail",
    package_dir={'cotimail': 'cotimail'},
    packages=packages,
    package_data={'cotimail': data_files},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
