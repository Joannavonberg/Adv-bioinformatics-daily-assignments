from pymongo import MongoClient

client = MongoClient()
db = client.ex2
cursor = db.vcf.find({{"rec.samples.s.dp": { "$gt: 7" }},{"rec.samples[2-3]"}})
n=0
for document in cursor:
    n=n+1
print(n)
