from tkinter import *
from functools import partial

root = Tk()
root.title("SQL to MongoDB Converter")
from SQltoMongo import sql_to_spec,create_mongo_shell_query
def convert():

    query = query_entry.get()
    spec = sql_to_spec(query)
    l=create_mongo_shell_query(spec)
    result_text.delete("1.0", END)
    spec_text.delete("1.0", END)
    spec_text.insert(END,str(spec))
    result_text.insert(END, str(l))

query_label = Label(root, text="Enter SQL query:")
query_label.grid(row=0, column=0, padx=10, pady=10)

query_entry = Entry(root,width=100)
query_entry.grid(row=0, column=1, padx=10, pady=10)

convert_button = Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=0, padx=10, pady=10)

result_label = Label(root, text="MongoDB Query:")
result_label.grid(row=2, column=0, padx=10, pady=10)

result_text = Text(root, height=10, width=50)
result_text.grid(row=2, column=1, padx=10, pady=10)

spec_label = Label(root, text="MongoDB specification:")
spec_label.grid(row=3, column=0, padx=10, pady=10)

spec_text = Text(root, height=10, width=50)
spec_text.grid(row=3, column=1, padx=10, pady=10)



root.mainloop()