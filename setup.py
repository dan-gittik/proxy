import setuptools


package = dict(
    name             = 'proxy',
    version          = '0.1.0',
    author           = 'Dan Gittik',
    author_email     = 'dan.gittik@gmail.com',
    description      = 'Context managers to route Python via proxies and TOR',
    license          = 'MIT',
    url              = 'https://github.com/dan-gittik/proxy',
    packages         = setuptools.find_packages(),
    install_requires = [
        'pysocks',
        'stem',
    ],
    tests_require    = [
        'pytest',
        'requests',
    ],
)


if __name__ == '__main__':
	setuptools.setup(**package)
