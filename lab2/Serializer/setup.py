from setuptools import setup, find_packages

setup(name='Serializer', version='1.0', description='Lab2',
      packages=['Factory', 'picker', 'json_serializer',
                'toml_serializer', 'yaml_serializer'],
      author_email='shamaich007@gmail.com',
      install_requires=['PyYaml == 6.0',
                        'PyToml == 0.1.21'],
      entry_points={'console_scripts': ['console_argparse = Serializer.console_argparse:arg_func']}
      )
