#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         fastapi
   Description:  
   Author:       Acer
   Date:           2026/10/31
-------------------------------------------------------------------------------
   Change Activity:
                 2026/10/31
"""

__author__ = "baiyi"
__version__ = "1.0.0"
from fastapi import FastAPI

app = FastAPI()

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

@app.get("/api/profile")
def get_profile():
    return profile


