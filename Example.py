import pandas as pd
source = pd.read_csv("Description_Source.csv")
#print(source)

target = pd.read_csv("Description_Target.csv")
#print(target)

widen_value_mapping = pd.read_excel("Widen_Polyyy.xlsx", sheet_name = "Value_Mapping")
#print(widen_value_mapping) 

widen_key_mapping = pd.read_excel("Widen_Polyyy.xlsx", sheet_name = "Key_Value_Mapping")
#print(widen_key_mapping)

df_merge = pd.merge(source, target, left_on="id ", right_on ="Migration_id")

filtered_value_map = widen_value_mapping[widen_value_mapping['Widen_Field'] == 'Description']
filtered_value_map

def get_result(x, df_merge, filtered_value_map, key_mapping):

  value1 = str(df_merge["description_string"].loc[x])
  value2 = str(df_merge["description_string_multi"].loc[x])
  value3 = str(df_merge["Description"].loc[x])
  print(value3)


  if(value1.lower() == "nan" or value1.strip() == ''):

    check = list(filtered_value_map[filtered_value_map["Legacy DAM Value"] == value2]["Widen Value"].values)
    print("This is check 1",check)
    check = ''.join(map(lambda y: y.strip().replace('"',''),check))
    print("This is check2",check)
    check2 = list(widen_key_mapping[widen_key_mapping["Final Key"].isin(check.split(','))]["Final Value"].values)
    check2 = ''.join(map(lambda y: y.strip().replace('"',''),check2)).strip(' ')
    print(check2)
    #print(check2)
    if(value3.strip() == check2):
      print("Success")
      return "Success"

    else:
      print("Fail----")
      return "Fail"


  elif(value2.lower() == "nan" or value2.strip() == ''):

    check = list(filtered_value_map[filtered_value_map["Legacy DAM Value"] == value1]["Widen Value"].values)
    print("This is check 3", check)
    check = ''.join(map(lambda y: y.strip().replace('"',''),check))

    
    print("This is check 4",check)
    check2 = list(widen_key_mapping[widen_key_mapping["Final Key"].isin(check.split(','))]["Final Value"].values)
    check2 = ''.join(map(lambda y: y.strip().replace('"',''),check2)).strip(' ')
    print(check2)
    if(value3.strip() == check2):
      print("Success")
      return "Success"

    else:
      print("Fail+++++")
      return "Fail"

  elif((value1.lower() == "nan") or (value1.strip() == '')) and ((value2.lower() == "nan") or (value2.strip() == '')):


    check = list(filtered_value_map[filtered_value_map["Legacy DAM Value"] == "nan"]["Widen Value"].values)
    check2 = list(widen_key_mapping[widen_key_mapping["Final Key"] == "nan"]["Final Value"].values)

    if(value3.strip() == check2):
      print("Success")
      return "Success"

    else:
      print("Fail***********")
      return "Fail"







sa = pd.DataFrame()
sa["Final_result"] = df_merge.index.map(lambda row_no: get_result(row_no, df_merge, filtered_value_map, widen_key_mapping))
print(sa)

#get_result(4, df_merge, filtered_value_map, key_mapping)

    
