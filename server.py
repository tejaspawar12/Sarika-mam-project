#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI, File, UploadFile

# In[2]:


from fastapi.responses import JSONResponse

# In[3]:


from fastapi.requests import Request

# In[4]:


import cv2

# In[5]:


app=FastAPI()

# In[6]:


model=cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")

# In[7]:


import numpy as np

# In[8]:


@app.post("/detect_objects")
async def detect_objects(file:UploadFile=File(...)):
    image=await file.read()
    image=np.frombuffer(image,np.uint8)
    image=cv2.imdecode(image,cv2.IMREAD_COLOR)
    blob=cv2.dnn.blobFromImage(image,1/255,(416,416),(0,0,0),True, crop=False)
    model.setInput(blob)
    output_layers=model.getUnconnectedOutLayersNames()
    outputs=model.forward(output_layers)
    #Draw BOUNDING BOXES AND LABELS
    detections=[]
    for output in outputs:
        for detection in output:
            scores=detection[5:]
            class_id = np.argmax(scores)
            confidence=scores[class_id]
            if confidence>0.5:
                print(response.content)
                detections = response.json()["detections"]
                x,y,w,h=detection[0:4]*np.array([image.shape[1],image.shape[0],image.shape[1],image.shape[0]])
                x,y,w,h=int(x), int(y),int(w),int(h)
                detections.append((x,y,w,h,class_id,confidence))
    # return the detections as JSON 
                return JSONResponse(content={"detections":detections},media_type="application/json")
    
                

# In[ ]:



