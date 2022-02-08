#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2022/2/2 22:43
Desc: 收盘收益率曲线历史数据
http://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1
"""
import pandas as pd
import requests


def bond_china_close_return_map() -> pd.DataFrame:
    """
    收盘收益率曲线历史数据
    http://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1
    :return: 收盘收益率曲线历史数据
    :rtype: pandas.DataFrame
    """
    url = "http://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvCurvGO"
    r = requests.post(url)
    data_json = r.json()
    temp_df = pd.DataFrame(data_json["records"])
    return temp_df


def bond_china_close_return(
    symbol: str = "国债",
    period: str = "1",
    start_date: str = "20220104",
    end_date: str = "20220104",
) -> pd.DataFrame:
    """
    收盘收益率曲线历史数据
    http://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1
    :param symbol: 需要获取的指标
    :type period: choice of {'0.1', '0.5', '1'}
    :param period: 期限间隔
    :type symbol: str
    :param start_date: 开始日期, 结束日期和开始日期不要超过 1 个月
    :type start_date: str
    :param end_date: 结束日期, 结束日期和开始日期不要超过 1 个月
    :type end_date: str
    :return: 收盘收益率曲线历史数据
    :rtype: pandas.DataFrame
    """
    name_code_df = bond_china_close_return_map()
    symbol_code = name_code_df[name_code_df["cnLabel"] == symbol]["value"].values[0]
    url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis"
    params = {
        "lang": "CN",
        "reference": "1,2,3",
        "bondType": symbol_code,
        "startDate": '-'.join([start_date[:4], start_date[4:6], start_date[6:]]),
        "endDate": '-'.join([end_date[:4], end_date[4:6], end_date[6:]]),
        "termId": period,
        "pageNum": "1",
        "pageSize": "15",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    r = requests.get(url, params=params, headers=headers)
    data_json = r.json()
    temp_df = pd.DataFrame(data_json["records"])
    del temp_df["newDateValue"]
    temp_df.columns = [
        "日期",
        "期限",
        "到期收益率",
        "即期收益率",
        "远期收益率",
    ]
    temp_df = temp_df[
        [
            "日期",
            "期限",
            "到期收益率",
            "即期收益率",
            "远期收益率",
        ]
    ]
    temp_df['日期'] = pd.to_datetime(temp_df['日期']).dt.date
    temp_df['期限'] = pd.to_numeric(temp_df['期限'])
    temp_df['到期收益率'] = pd.to_numeric(temp_df['到期收益率'], errors='coerce')
    temp_df['即期收益率'] = pd.to_numeric(temp_df['即期收益率'], errors='coerce')
    temp_df['远期收益率'] = pd.to_numeric(temp_df['远期收益率'], errors='coerce')
    return temp_df


if __name__ == "__main__":
    bond_china_close_return_df = bond_china_close_return(
        symbol="国债", period="1", start_date="20220104", end_date="20220104"
    )
    print(bond_china_close_return_df)
