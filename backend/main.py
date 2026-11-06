#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         main
   Description:  
   Author:       Acer
   Date:           2026/11/5
-------------------------------------------------------------------------------
   Change Activity:
                 2026/11/5
"""

__author__ = "baiyi"
__version__ = "1.0.0"

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class AnalyzeRequest(BaseModel):
    text: str

@app.get("/api/profile")
def get_profile():
    return profile

@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    return {
        "text": req.text,
        "score": 0.5,
        "label": "偏平静",
        "pinyin": "（模块 6 再说）",
    }
