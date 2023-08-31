 #Search function
    
    def search(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        
        con_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE '%"+str(self.txt_search.get())+"%'")
        rows=con_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()