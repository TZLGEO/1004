

def get_data(df, rows):

    billboard_sample = df.iloc[:rows]
    result = billboard_sample.to_json(orient='records')
    return result


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

def test_chart(engine):
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
            values_list.append({"x_vals":row[1], "y_vals": row[1]})
            

            
    return values_list