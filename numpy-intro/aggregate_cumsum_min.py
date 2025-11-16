import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("Total Sum : ",np.sum(a),"\nColumn Wise sum : ",np.sum(a,0),"\nRow Wise sum : ",np.sum(a,1))
print("Cumilative Sum :",np.cumsum(a),"\nRow Wise Cummlative sum : ",np.cumsum(a,1),"\nColumn Wise Cummlative sum : ",np.cumsum(a,0))
print("Min Val : ",np.min(a),"\nColumn Wise min val : ",np.min(a,0),"\nRow Wise Min val : ",np.min(a,1))
