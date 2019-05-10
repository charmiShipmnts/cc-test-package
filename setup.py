import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='cc_test_package',  
     version='0.1',
     author="Charmi Chokshi",
     author_email="charmi@shipmnts.com",
     description="An Enum (currency, freight terms, and weight UOM) utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/charmiShipmnts/test_package",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
