python getRDF2.py <<EOF
adv_bio.pdb
n
y
EOF

cat query.rq |sparql-query "http://localhost:8000/sparql/" -p
