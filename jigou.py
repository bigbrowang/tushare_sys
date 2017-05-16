from sqlalchemy import create_engine
import tushare as ts
import pandas
import pymysql
import datetime
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/gushi?charset=utf8')
dt=ts.inst_detail()
dt.to_sql('jigou', engine, if_exists='append',index=False)


