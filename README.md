#### Dependencies
If you don't already have virtualenv:
```
pip install --upgrade virtualenv
```

Create and use the environment: 
```
virtualenv env
source env/bin/activate
```

Install pip dependencies:
```
pip install -r requirements.txt
```

#### Getting the data
It's recommended to just work directly with the committed dataframe, data/math_articles.pd. If you want to go through data downloading and processing for whatever reason, you can do the following:

```
data/get-articles.sh
lbzip2 -d data/*
data/run_cull.sh
python build_dataframe.py
```

This will generate data/math_articles.pd
