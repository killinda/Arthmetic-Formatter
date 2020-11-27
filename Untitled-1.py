


# %%
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
results = A[1:]
first_day = datetime.strptime(A[1].split(" ")[0],'%m/%d/%Y')
date =[]
tem =[]
missing = []
for result in results:
    days_text = result.split("  ")[0].split(" ")[0]
    days_text = days_text.split("/")[0].rjust(2,"0")+"-" + days_text.split("/")[1].rjust(2,"0") + "-" + days_text.split("/")[2]
    days = (datetime.strptime(days_text, '%m-%d-%Y') - first_day).days
    
    if result.split()[2].find("Missing") ==-1:
        tem.append(float(result.split()[2].strip()))
        date.append(days)
    else:
        missing.append(days)
Model = LinearRegression()
X = np.array(date).reshape(-1,1)
Y = np.array(tem).reshape(-1,1)
Model.fit(X,Y)
alpha = Model.intercept_[0]
beta = Model.coef_[0][0]
for i in missing:
    number = round(float(alpha + beta *i),2)
    print(number)





# %%
import pandas as pd
import numpy as np
from datetime import datetime
results = A[1:]
first_day = datetime.strptime(A[1].split(" ")[0],'%m/%d/%Y')
date =[]
tem =[]
missing = []
for result in results:
    days_text = result.split("  ")[0].split(" ")[0]
    days_text = days_text.split("/")[0].rjust(2,"0")+"-" + days_text.split("/")[1].rjust(2,"0") + "-" + days_text.split("/")[2]
    days = (datetime.strptime(days_text, '%m-%d-%Y') - first_day).days
    date.append(days)
    if result.split()[2].find("Missing") ==-1:
        tem.append(float(result.split()[2].strip()))
        missing.append(0)
        
    else:
        tem.append(np.nan)
        missing.append(1)
result = {"date":date,"tem":tem,"missing":missing}
result_total = pd.DataFrame(result)
result_total["tem"] = result_total["tem"].fillna(method='pad',limit=1)
result_total["tem"] = result_total["tem"].fillna(method='bfill',limit=1)
A = result_total["tem"][result_total["missing"] ==1].tolist()
print(A)


