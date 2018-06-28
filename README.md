# RecSys-Challenge-2018-main-track
code used to generate the minrva team's submission to the 2018 RecSys Challenge in the main track

## Engine:

Apache PredictionIO (http://predictionio.apache.org/) 'similar product template' (https://github.com/apache/predictionio-template-similar-product) with Alternating Least Squares (ALS) algorithm, as implemented in Spark MLlib (https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html); system relied on PostgreSQL 10 (https://www.postgresql.org/) for data persistence.

## Software:

- Python data load (https://github.com/jimfhahn/RecSys-Challenge-2018-main-track/tree/master/load-data)

## System:

-  Ubuntu 18.04 LTS (GNU/Linux 4.15.0-20-generic x86_64)
-  java-8-openjdk-amd64
-  128GB RAM, 24 CPU Cores, 2.5 TB SSD
-  psql (10.4 (Ubuntu 10.4-0ubuntu0.18.04))