#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import json

with open('member.csv', newline='') as csvfile:

# 讀取 CSV 檔案內容
	rows = csv.reader(csvfile)
	json_result = []
	# 以迴圈輸出每一列
	for row in rows:
		x = {
			"chineseName": row[1],
			"englishName": row[2],
			"studentID": row[3],
			"status": "學會會員(未付費)",
			"phone": row[4],
			"wechat": row[5],
			"email": row[6],
			"major": row[7]
		}
		json_result.append(x)

with open('member_data2020.js', 'w', encoding='utf-8') as outfile:
	json.dump(json_result, outfile, ensure_ascii=False, indent=4)
