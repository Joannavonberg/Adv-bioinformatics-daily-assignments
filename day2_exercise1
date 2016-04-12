from pymongo import MongoClient

client = MongoClient()
db = client.test2
# look for annotations that contain a certain Ensembl name
cursor = db.vcf.find({"rec.ann": "/ENST00000263967/i" })
# count how many there are
n=0
for document in cursor:
    n=n+1
print(n)
