#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         api
   Description:  
   Author:       Acer
   Date:           2026/10/31
-------------------------------------------------------------------------------
   Change Activity:
                 2026/10/31
"""

__author__ = "baiyi"
__version__ = "1.0.0"

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("sk-af52e40383284c8a8ae583c0f4365191"),
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

print(response.choices[0].message.content)


print(response.choices[0].message.content)