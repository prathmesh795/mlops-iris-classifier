# DVC Workflow

## 1. DVC Initialization

DVC was initialized inside the existing Git repository using:

dvc init

The DVC configuration files were committed to Git.

## 2. DVC Remote Configuration

A local folder was used as the DVC remote.

Remote:

~/dvc-remote-storage

The remote was configured using:

dvc remote add -d myremote ~/dvc-remote-storage

## 3. Dataset Version 1

The Iris dataset was generated using:

python src/generate_data.py

The dataset was saved as:

data/raw/iris_v1.csv

Version 1 contained 150 data rows.

The dataset was tracked using:

dvc add data/raw/iris_v1.csv

The DVC metafile was added to Git using:

git add data/raw/iris_v1.csv.dvc data/raw/.gitignore

The Version 1 dataset was committed using:

git commit -m "data: add iris_v1 raw dataset (150 rows) tracked via DVC"

The dataset was uploaded to the DVC remote using:

dvc push

## 4. Dataset Version 2

The dataset was modified by adding 20 synthetic rows.

The dataset changed from:

150 rows -> 170 rows

The augmentation script was:

src/augment_data.py

It was executed using:

python src/augment_data.py

The modified dataset was tracked again using:

dvc add data/raw/iris_v1.csv

The updated DVC metafile was committed using:

git add data/raw/iris_v1.csv.dvc

The Version 2 dataset was committed using:

git commit -m "data: augment iris dataset with 20 synthetic rows (150 -> 170)"

The new dataset object was uploaded using:

dvc push

## 5. Dataset Version History

Git was used to view the history of the DVC metafile:

git log --oneline -- data/raw/iris_v1.csv.dvc

Version 1:

Git commit: 1e463e9
Dataset: 150 rows
MD5: 21d441a28bce4417276097df955afc50

Version 2:

Git commit: c250e84
Dataset: 170 rows
MD5: 674c8c36bb7c4ba8d851dee9e6ee67af

## 6. Comparing Dataset Versions

The current dataset was compared with Version 1 using:

dvc diff 1e463e9

The result showed:

Modified:
data/raw/iris_v1.csv

## 7. Restoring Version 1

The Version 1 DVC pointer was restored using:

git checkout 1e463e9 -- data/raw/iris_v1.csv.dvc

The actual Version 1 dataset was restored using:

dvc checkout data/raw/iris_v1.csv.dvc

The dataset was verified using:

wc -l data/raw/iris_v1.csv

Result:

151 lines

This represents 150 data rows plus one header row.

## 8. Restoring Version 2

The latest DVC pointer was restored using:

git checkout HEAD -- data/raw/iris_v1.csv.dvc

The latest dataset was restored using:

dvc checkout data/raw/iris_v1.csv.dvc

The dataset was verified using:

wc -l data/raw/iris_v1.csv

Result:

171 lines

This represents 170 data rows plus one header row.

## 9. Complete DVC Workflow

For every meaningful dataset change:

dvc add
    ->
git add *.dvc
    ->
git commit
    ->
dvc push

Git stores the lightweight DVC metadata while DVC stores the actual dataset.

## 10. Conclusion

This experiment demonstrated:

- DVC installation and initialization
- DVC remote configuration
- Dataset tracking with DVC
- Dataset Version 1 with 150 rows
- Dataset Version 2 with 170 rows
- Dataset comparison using dvc diff
- Dataset restoration using dvc checkout
- Integration of DVC with Git
- Reproducible dataset versioning
