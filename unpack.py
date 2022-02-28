#BUKET ZEREN, EMİRHAN YILMAZ GÜNEY
import pandas
from bitstring import BitArray

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
    print(packed_data)
    for i in range(len(struct_table)):
        #read the row
        d_type=struct_table.loc[i,"type"]
        bit_count=struct_table.loc[i,"bit_count"]
        
        #get the related part 
        data_to_decode=packed_data[cursor:cursor+bit_count]
        cursor+=bit_count
        
        if d_type=="str":
            binary_chars=[data_to_decode[i*8:(i+1)*8] for i in range(bit_count//8)]
            print(binary_chars)
            char_list=[chr(int(i,2)) for i in binary_chars]
            print(char_list)
            result="".join(char_list)
            print(result)
        elif d_type=="float":
            result=BitArray(float=data_to_decode,length=bit_count).float
        elif d_type=="int":
            result=int(data_to_decode,2)
        
        decoded_data.append(result)
    return decoded_data

incoming_data="00000001"+"00000001"+"01000010"+"01011010"+"00011100"+"00000010"
table=find_and_load_table(incoming_data)
print(decode(incoming_data[16:],table))