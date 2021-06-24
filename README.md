# techChallenge

**1Challenge_3tier.py**

Architecture used - GCP and
Programming language - Python

Step by Step process -

1. This python utility will read data from GCS storage which represents data layer, and processese data through Cloud Functions which represents Processing layer.
2. Cloud function has been used so that the moment a file arrives in a bucket CF will be triggered and starts processing the input file.
3. This also represents one aspect of real time processing since this use case is for processing and visualising online sales metrics.
4. Once the data is processed it will be moved to a BigQuery table and on top of BQ table a dashboard can be created.
5. for presentation layer- Tableau, and Google Data studio can be used.
6. Terraform script attached explains the reporducibility of this environment.
7. PPT attached explains the architecture.

How to run - python3 1Challenge_3tier.py

**Note** : Since i do not have a GCP billed account and was unble to execute this program explicitely. I have designed it to represents a 3 Tier environment.

---------------------------------------------------------------------------------------------------------------------------------------------------

**2Challenge_getMetadata.py**

Architecture used - GCP and
Programming language - Python

Step by Step process -

1. This python script will give query the metadata of an instance within GCP and provide a json formatted output.
2. A data key has to be passed in order to retrive the metadata information of that particular key.

How to run - python3 2Challenge_getMetadata.py disks
             python3 2Challenge_getMetadata.py licenses
Sample Output - 

priyasha464@cloudshell:~ (ga360-data-export)$ python3 2Challenge_getMetadata.py disks

Below is the metadata information of this VM -
-----------------------------------------------
[{'deviceName': 'boot', 'index': 0, 'interface': 'SCSI', 'mode': 'READ_WRITE', 'type': 'PERSISTENT-SSD'}, {'deviceName': 'home', 'index': 1, 'interface': 'SCSI', 'mode': 'READ_WRITE', 'type': 'PERSISTENT'}]

---------------------------------------------------------------------------------------------------------------------------------------------------

**3Challenge_getvalues.py**

Programming language - Python

Step by Step process -

1. This python script contains a function to which an object can be passed and values of the keys can be retrieved.

How to run - python3 3Challenge_getvalues.py

Sample Output for object - {“a”:{“b”:{“c”:”d”}}}
 
**priyasha464@cloudshell:~ (ga360-data-export)$ python3 getValues.py

{'a': {'b': {'c': {'z': 'a'}}}}

Value if this object is a**


