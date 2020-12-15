

def get_data(df, rows):

    billboard_sample = df.iloc[:rows]
    result = billboard_sample.to_json(orient='records')
    return result

def no1_on_chart():
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
            values_list.append({"x_vals":row[1], "y_vals": row[1]})
            

            
    return json.dumps(values_list)

def stay_on_chart():
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
            values_list.append({"x_vals":row[1], "y_vals": row[1]})
            

            
    return json.dumps(values_list)
