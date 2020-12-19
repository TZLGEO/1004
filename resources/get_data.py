"""
This is where all  the queries happen
"""
def stay_on_chart(engine):
    x_values = []
    y_values = []
    values_list = []
    with engine.connect() as con:
        # change this to whatever query you want you want
        query_str = """SELECT "Song", count(*) AS cnt  
                        FROM billboard_chart 
                        GROUP BY "Song" 
                        ORDER BY cnt DESC
                        LIMIT 20"""

        rs = con.execute(query_str)

        for row in rs:
            values_list.append({"x_vals":row[0], "y_vals": row[1]})
            

            
    return values_list


def no1_on_chart(engine):
    x_values = []
    y_values = []
    values_list = []
    with engine.connect() as con:
        # change this to whatever query you want you want
        query_str = """SELECT "Song", count(*) AS cnt  
                        FROM billboard_chart 
                        WHERE ("Week Position" = 1)
                        GROUP BY "Song" 
                        ORDER BY cnt DESC
                        LIMIT 20"""

        rs = con.execute(query_str)

        for row in rs:
            values_list.append({"x_vals":row[0], "y_vals": row[1]})
            

            
    return values_list   

def get_data(engine, rows):
    with engine.connect() as con:
        # change this to whatever query you want you want
        query_str = f"""SELECT *  
                        FROM billboard_chart
                        LIMIT {rows}"""

        rs = con.execute(query_str)

        row_headers=rs.keys() #this will extract row headers
        rv = rs.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
    return json_data