from setuptools import setup

setup(name="scheduler",
      version='1.01',
      description='scheduler and shitty scheduler',
      packages=["scheduler"],
      install_requires=["datetime"],
      include_package_data=True,
      package_data={"": ["*.txt", "*.csv"]})
