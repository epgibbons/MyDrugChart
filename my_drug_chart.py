# open file , read content and display
# 2

# keys in archive:
# drug_lists - list of drug_list items.
# drugs - list of drug items
#
# types:
# drug_list - dictionary with the keys:
#     list_id - unique identifier of the drug_list
#     name - non unique name of the drug_list
#     drugs - list of drug_dosage items
# drug_dosage - dictionary with keys:
#     drug_id - identifier of a drug
#     Dosage - dosage
# drug - dictionary with keys:
#     drug_id - unique identifier of drug_list
#     name - name of the drug
#     to be extended


import datetime
def create_drug_list_archive_entry(current_drug_list):
    return {"drug_list_id":current_drug_list["list_id"], "date":datetime.datetime.now()}

filename = "myDrugChart.data"



import shelve
m_d_d = shelve.open( filename)


if not "drugs" in m_d_d:
    print "Initialise drugs"
    drugs = []
    drugs.append({"drug_id": len(drugs), "name":"Prednisolone"})
    drugs.append({"drug_id": len(drugs), "name":"Digoxin"})
    drugs.append({"drug_id": len(drugs), "name":"Allopurinol"})
    m_d_d["drugs"] = drugs

if not "drug_lists" in m_d_d:
    print "Initialise drug_lists"
    drug_lists = []

    morning_drugs = []
    morning_drugs.append({"drug_id":0, "Dosage": "25mg"})
    morning_drugs.append({"drug_id":1, "Dosage": "0.125mg"})

    drug_lists.append ({"list_id": len(drug_lists), "name": "morning drugs", "drugs": morning_drugs})

    morning_drugs_2 = []
    morning_drugs_2.append({"drug_id":0, "Dosage": "25mg"})
    morning_drugs_2.append({"drug_id":1, "Dosage": "0.125mg"})
    morning_drugs_2.append({"drug_id": 2, "Dosage": "20 mg"})

    drug_lists.append( {"list_id": len(drug_lists), "name": "morning drugs", "drugs": morning_drugs_2})

    m_d_d["drug_lists"] = drug_lists

if not "current_drug_list_id" in m_d_d:
    print "initialise current_drug_list_id"
    drug_lists = m_d_d["drug_lists"]
    m_d_d["current_drug_list_id"] = drug_lists[len(drug_lists)-1]["list_id"]

current_drug_list_id = m_d_d["current_drug_list_id"]
current_drug_list=None
print "Initialise current_drug_list"
for drug_list in m_d_d["drug_lists"]:
    if drug_list["list_id"] == current_drug_list_id:
        current_drug_list=drug_list
        break

if current_drug_list==None:
    print("Cannot find drug_list with list_id equal to current_drug_list_id '"+current_drug_list_id +"'")
    exit(-1)

#add an instance of an record
records=[]
if m_d_d.has_key("records"):
    print "Read existing records"
    records = m_d_d["records"]

print("add record")
records.append(create_drug_list_archive_entry(current_drug_list))

m_d_d["records"]=records
m_d_d.close()

m_d_d_readback = shelve.open( filename)
print m_d_d_readback
print len(m_d_d_readback["records"])


current_drug_list_id = m_d_d_readback["current_drug_list_id"]
for drug_list in m_d_d_readback["drug_lists"]:
    if drug_list["list_id"] == current_drug_list_id:
        print drug_list["name"]
        print drug_list["drugs"]
        break

print m_d_d_readback["drugs"]