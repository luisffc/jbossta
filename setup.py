from setuptools import setup
setup(name='jbossta',
      version='0.0.1',
      py_modules=['jbossta'],
      install_requires = ['watchdog'],
      entry_points={
            'console_scripts': [
            'jbossta = jbossta:main',
            ]},
      description = 'This is a script that provides a "save and run" for JSPs in a JBoss application like PHP does',
      author='Luis FF Cavalcante',
      author_email='luis@coffeetech.com.br',
      url='https://github.com/luisffc/jbossta',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        ]
      )