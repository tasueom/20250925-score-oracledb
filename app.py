import oracledb
from flask import Flask, render_template as ren, request, redirect, url_for

oracledb.init_oracle_client(
    lib_dir=r"C:\oraclexe\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9"
)

def conn_db():
    conn = oracledb.connect(
    user="hr",
    password="1234",
    dsn="localhost:1521/XE"
    )
        
    cur = conn.cursor()
    
    return conn, cur