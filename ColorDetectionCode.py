import cv2
import pandas as pd
image = cv2.imread(r'C:\Git\Color_Recognition\My_project_snip.png')
cv2.namedWindow('test')
cv2.imshow('test',image)
Columns=['color','colorName','value','R','G','B']
df=pd.read_csv(r'C:\Git\Color_Recognition\colors.csv',names=Columns,header=None)
def colorCalculation(b,g,r):
    minDelta=abs(b-df.iloc[0,5])+abs(g-df.iloc[0,4])+abs(r-df.iloc[0,3])
    clickColor='No color'
    for i,row in df.iterrows():
        currentDelta=abs(b-row['B'])+abs(g-row['G'])+abs(r-row['R'])
        if currentDelta<minDelta:
            minDelta=currentDelta
            clickColor=row['colorName']
    return clickColor

def click_detection(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        b,g,r=image[y,x]
        print("you clicked :",colorCalculation(b,g,r),"(",b,g,r,")color")
cv2.setMouseCallback('test',click_detection)
cv2.waitKey(0)
cv2.destroyAllWindows()

