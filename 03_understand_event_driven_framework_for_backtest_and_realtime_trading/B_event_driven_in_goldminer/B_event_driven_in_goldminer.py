# -*- coding: utf-8 -*-
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *


def init(context):
    # 订阅浦发银行, bar频率为一天和一分钟
    # 订阅订阅多个频率的数据，可多次调用subscribe
    subscribe(symbols='SHSE.600000', frequency='1d')
    subscribe(symbols='SHSE.600000', frequency='60s')
    subscribe(symbols='SHSE.603127', frequency='60s')
    subscribe(symbols='SHSE.600000', frequency='tick')
    subscribe(symbols='SHSE.603127', frequency='tick')


def on_tick(context, tick):
    print("-----------on tick-----------------")
    print(tick)
    
def on_bar(context, bars):

    # 打印bar数据
    print("-----------on bar-----------------")
    print(bars)
    


if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='bf949d17-1477-11ec-9359-a85e45b37bd3',
        filename='B_event_driven_in_goldminer.py',
        mode=MODE_BACKTEST,#MODE_LIVE, #MODE_BACKTEST
        token='f800d5397042d70c90afec4c2245742c7bac921c',
        backtest_start_time='2021-11-01 08:00:00',
        backtest_end_time='2021-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001,
        serv_addr="10.30.3.9:7001")



