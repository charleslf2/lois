# lois
The fastest and easy way to get insight of your dataset

#### Purpose of the package
+  The purpose of this package is to provide to data scientist and data analyst a faster way to get insight of  their dataset .


#### Features
+  EDA automation


### Getting Started
The package can be found on pypi hence you can install it using pip

#### Installation

```bash
pip install lois
```
### Usage
```python|jupyter notebook

>>> import pandas as pd
>>> from lois import lois_ds_report
>>> data=pd.read_csv("your data path")
>>> lois_ds_report(data,target_variable="gender", report_complexity="simple" )
```


### Contribution
Contribution are welcome.
Notice a bug ? let us know. Thanks you

### Author
+ Main Maitainer : Charles TCHANAKE
+ email : datadevfernolf@gmail.com 