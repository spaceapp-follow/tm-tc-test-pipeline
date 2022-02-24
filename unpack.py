#BUKET ZEREN, EMİRHAN YILMAZ GÜNEY
import pandas

def find_and_load_table(packed_data):
    '''
    this function takes the packed data as bit string, finds the corresponding struct table and returns it
    '''
    node_id=int(packed_data[:8],2)
    channel_id=int(packed_data[8:16],2)
    table_name="Node_"+str(node_id)+"_Channel_"+str(channel_id)+".csv"
    try:
        table=pandas.read_csv("./StructExcels/tcExcels/"+table_name)
    except:
        print("An error occured, please make sure your csv files exists and follow the necessary naming conditions")
    return table

def decode(packed_data,struct_table):
    cursor=0
    decoded_data=[]
    for i in range(len(struct_table)):
        #read the row
        d_type=struct_table.loc[i,"type"]
        bit_count=struct_table.loc[i,"bit_count"]
        data_to_decode=packed_data[cursor:cursor+bit_count]

        if d_type=="str":
            pass
        elif d_type=="float":
            pass
        elif d_type=="int":
            pass
        

incoming_data="00000001"+"00000001"
table=find_and_load_table(incoming_data)
decode(table)