

[![Build Status](https://travis-ci.org/LandRegistry/lr-utils.svg)](https://travis-ci.org/LandRegistry/lr-utils.svg?branch=master)

## Some stuff used by more than one LR Flask app


### Using these utilities

**Add the following to your requirements.txt**

```
lrutils==0.1
```

### Push new versions to PYPI public repository

Note this code is currently hosted on PYPI. The LR may want to run their own PYPI repo in LR envs and host this and other LR packages there. An easy way to do this is use [localshop](https://github.com/mvantellingen/localshop).

The travis build will push tagged versions of this package to pypy (currently using my account - this should be transferred to an LR dev/webops person, or as mentioned above pushed to your own pypi)

##### When you want to push a new version

* Set version number in setup.py
```
git tag [version number] -m "update version"
git push --tags origin master
```


