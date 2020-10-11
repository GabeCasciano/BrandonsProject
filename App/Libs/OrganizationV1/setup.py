from setuptools import setup

setup(name="organization",
      version='1.01',
      description='organization and shitty scheduler',
      packages=["organization"],
      install_requires=["datetime"],
      include_package_data=True,
      package_data={"": ["*.txt", "*.csv"]})
