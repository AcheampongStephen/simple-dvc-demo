1. Create enivronment
```
conda create -n wine1 python=3.7 -y
```
2. Activate env
```
conda activate wine1
```
3. Create requirements.txt
```
pip install -r requirements.txt
```
4. Create template.py

5. Create a folder as data_given where it will act as a remote data source.

6. Dwnload the dataset into data_given
7. git init
8. dvc init
9. dvc add data_given/winequality.csv
10. git add . && commit -m "first commit"
11. git commit -m "first commit"
12. git remote add origin https://github.com/AcheampongStephen/simple-dvc-demo.git
13. git branch -M main