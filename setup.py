import setuptools
from setuptools import find_packages, setup


from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='numpanpar',
    packages=find_packages(),
    version='0.1.0',
    description='A numpy and pandas parallel utility package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Isaac Shamie',
    license='MIT',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License"],
    python_requires='>=3.6',
    url="https://github.com/isshamie/parallel_helper"
)

#
# with open("README.md", "r") as fh:
#     long_description = fh.read()
#      setup(
#      name='parnpd',
#      version='0.1',
#      author="Isaac Shamie",
#      author_email="isshamie@ucsd.edu",
#      description="A python parallel utility package",
#      long_description=long_description,
#      long_description_content_type="text/markdown",
#      url="https://github.com/isshamie/parallel_helper",
#      packages=find_packages(),
# )

 #     classifiers=[
 #         "Programming Language :: Python :: 3",
 #         "License :: OSI Approved :: MIT License",
 #         "Operating System :: OS Independent",
 #     ],
 # )

#     scripts=['numpanpar'] ,
