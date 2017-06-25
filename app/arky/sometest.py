from arky import api
from arky.util import stats

api.use("ark")

#print api.Account.getAccount("AUahWfkfr5J4tYakugRbfow7RWVTK35GPW")

data = stats.getHistory("AJHsDRdyv5D62Btug5YQg598vqFTcGADqZ")
print data
for i in data:
    #print "HELLO", i["amount"] #/ 100000000)
    #sprint "hi", i["senderId"]
    if i["senderId"] == "AaPN5Sr4duPrwXX3E6smeQ7GfnXNaUPUCq":
        print "this transaction is biz interest"
        print i["amount"]


#data = stats.getBalanceHistory("AJHsDRdyv5D62Btug5YQg598vqFTcGADqZ")
