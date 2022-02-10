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
        table=pandas.read_csv("./StructExcels/tcExcels/"+table_name,header=None)
        print(table)
    except:
        print("An error occured, please make sure your csv files exists and follow the necessary naming conditions")
    return table


incoming_data="00000010"+"00000001"
find_and_load_table(incoming_data)