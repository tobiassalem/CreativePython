### Creative Python
Simple experiments with Python, probably the most awesome programming language! ^^

### Working with pip
Activate your virtual environment.
Install packages listed in the requirements file:
```
pip install -r requirements.txt
```

This will work for Mac, Windows, and Linux systems. 
To get the list of all pip packages in the requirements.txt file 
(Note: This will overwrite requirements.txt if exist else will create the new one).

```
pip freeze > requirements.txt
```

Now to remove one by one:
```
pip uninstall -r requirements.txt
```

If we want to remove all at once:
```
pip uninstall -r requirements.txt -y
```
If you're working on an existing project that has a requirements.txt file and your environment has diverged, 
simply replace requirements.txt from the above examples with toberemoved.txt. Then, once you have gone through the steps above, you can use the requirements.txt to update your now clean environment.

### References
* Python - Ref. https://www.python.org/
* Python W3 Tutorial - Ref. https://www.w3schools.com/python/
* Python YT Tutorial - Ref. https://www.youtube.com/watch?v=kqtD5dpn9C8&t=824s
* PIP and venv - Ref. https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
* Huggingface - Ref. https://huggingface.co/docs/datasets/use_dataset
* PyTorch - Ref. https://pytorch.org/