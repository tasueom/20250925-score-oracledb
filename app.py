import oracledb
from flask import Flask, render_template as ren, request, redirect, url_for

oracledb.init_oracle_client(
    lib_dir=r"C:\oraclexe\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9"
)

app = Flask(__name__)

def conn_db():
    conn = oracledb.connect(
    user="hr",
    password="1234",
    dsn="localhost:1521/XE"
    )
        
    cur = conn.cursor()
    
    return conn, cur

@app.route("/")
def index():
    conn, cur = conn_db()
    cur.execute("select * from students")
    rows = cur.fetchall()
    conn.close()
    
    return ren("list.html", rows=rows)

@app.route("/insert_score", methods=['GET','POST'])
def insert_score():
    if request.method=="POST":
        sname = request.form["sname"]
        kor = int(request.form["kor"])
        eng = int(request.form["eng"])
        mat = int(request.form["mat"])
        tot, avg, grade = calculate(kor, eng, mat)
        
        conn, cur = conn_db()
        cur.execute("""
                    insert into students(sno, sname, kor, eng, mat, tot, avg, grade) 
                    values (student_seq.nextval, :1, :2, :3, :4, :5, :6, :7)
                    """,(sname, kor, eng, mat, tot, avg, grade))
        conn.commit()
        conn.close()
        
        return redirect(url_for("index"))
    return ren("insert_score.html")

def calculate(kor, eng, mat):
    tot = kor+eng+mat
    avg = round(tot/3,2)
    match int(avg//10):
        case 19|9:
            grade = "A"
        case 8:
            grade = "B"
        case 7:
            grade = "C"
        case 6:
            grade = "D"
        case _:
            grade = "F"
            
    return tot, avg, grade

if __name__ == "__main__":
    app.run(debug=True)