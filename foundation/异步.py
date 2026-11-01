#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         异步
   Description:  
   Author:       Acer
   Date:           2026/10/31
-------------------------------------------------------------------------------
   Change Activity:
                 2026/10/31
"""

__author__ = "baiyi"
__version__ = "1.0.0"


import asyncio
import time


async def async_work(name):
    print(f"{name} start")
    await asyncio.sleep(2)
    print(f"{name} end")

async  def main():
    task1 = asyncio.create_task(async_work("A"))
    task2 = asyncio.create_task(async_work("B"))
    await task1
    await task2
start = time.time()
asyncio.run(main())
print("耗时", time.time()-start)
