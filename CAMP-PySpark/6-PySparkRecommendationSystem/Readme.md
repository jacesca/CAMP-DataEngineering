## Data sources
Some files were splitted in smaller size to allow syndicalization in GitHub, this can be read as if they were normal csv files:
```
spark.read.csv(warehouse_file_location, header=False, sep=' ', schema=schema_file)
```

The files that were replaced are:
- `data-sources/movies/ratings.csv` → `spark-warehouse/movies-ratings.csv`
- `data-sources/movies/tags.csv` → `spark-warehouse/movies-tags.csv`
- `data-sources/songs/disks.txt` → `spark-warehouse/songs-disks.csv`
- `data-sources/songs/ratings.txt` → `spark-warehouse/songs-ratings.csv`

## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/pyspark-ml.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```
- Required libraries
```
pip install pyspark
pip install findspark
pip install pandas
pip install pyspark[connect]
pip install pyspark[sql]
pip install plotly
pip install ipympl
pip install pyspark-dist-explore
pip install handyspark
```

