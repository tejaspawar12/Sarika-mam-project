# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:26:38 2024

@author: sarik
"""

import streamlit as st
import requests
import json

st.set_page_config(page_title="Object Detection")

st.header("Object Detection")

with st.form("upload_form"):
    file_uploader = st.file_uploader("Choose an image file")
    submit_button = st.form_submit_button("Upload")

if submit_button:
    if file_uploader is not None:
        response = requests.post("http://localhost:8001/detect_objects", files={"file": file_uploader})
        detections = json.loads(response.text)
        st.write("Detections:")
        for detection in detections:
            st.write(f"Class ID: {detection['class_id']}")
            st.write(f"Confidence: {detection['confidence']}")
            st.write(f"X: {detection['x']}")
            st.write(f"Y: {detection['y']}")
            st.write(f"W: {detection['w']}")
            st.write(f"H: {detection['h']}")
    else:
        st.error("No file uploaded")