from setuptools import setup
setup(name='jbossta',
      version='0.0.1',
      py_modules=['jbossta'],
      install_requirements = ['watchdog'],
      entry_points={
        'console_scripts': [
                'jbossta = jbossta:main',
          ]}
      )