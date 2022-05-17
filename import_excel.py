import streamlit as st
import pandas as pd
import numpy as np
st.write("""
# Machine Allocation
""")
df_mc_avail=pd.read_excel('mc_avail.xlsx')
df_mc_prior=pd.read_excel('mc_prior.xlsx')

def convert_df(machine_data):
       return machine_data.to_excel().encode('utf-8')


mc_prior_excel = convert_df(df_mc_prior)

st.download_button(
      label='Press to Download machine priority sample file',
      data=mc_prior_excel,
      file_name="mc_prior.xlsx",
      key='download-excel'
      )

mc_avail_excel = convert_df(df_mc_avail)
st.download_button(
      label='Press to Download machine availability sample file',
      data =mc_avail_excel,
      file_name='mc_avail.xlsx'
      key='download-excel'
      )
st.subheader('Click here to download sample files')
mc_prior_ip= st.file_uploader("Choose a Machine Priority XLSX file", type="xlsx")
mc_avail_ip= st.file_uploader("Choose a Machine Availability XLSX file", type="xlsx")




try:
    if mc_prior_ip:
           mp = pd.read_excel(mc_prior_ip) #mp-machine priority data frame
    if mc_avail_ip:
           ma = pd.read_excel(mc_avial_ip) #ma-machine availabilty data frame

    
    ndf = pd.merge(mp,ma,on ='location',how ='inner') #ndf-merged data frame

    n_p=ndf['location'].count() #Counting no of location
    j=1
    mac_data={} #mac_data new dictionary
    start='maf' 
    mac_data1=[start] 
    d=1000 #initialize location value to 1000
    

    for i in range(n_p):
        
        if(d!=ndf.iloc[j-1,0]):
            a=ndf.iloc[j-1,8]
            b=ndf.iloc[j-1,9]
            c=ndf.iloc[j-1,10]
            d=ndf.iloc[j-1,0]
    
            
        if (ndf.iloc[j-1,5]==1.0)and(ndf.iloc[j-1,2]<=a):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,3]<=b):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
        
        elif (ndf.iloc[j-1,7]==1.0)and(ndf.iloc[j-1,4]<=c):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
    # Above condtion to check first machine
        elif (ndf.iloc[j-1,5]==1.0)and(ndf.iloc[j-1,2]>a)and(ndf.iloc[j-1,3]<=b)and(ndf.iloc[j-1,6]==2.0):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,2]>a)and(ndf.iloc[j-1,4]<=c)and(ndf.iloc[j-1,7]==2.0):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
        
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,3]>b)and(ndf.iloc[j-1,2]<=a)and(ndf.iloc[j-1,5]==2.0):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,3]>b)and(ndf.iloc[j-1,4]<=c)and(ndf.iloc[j-1,7]==2.0):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
        
        elif (ndf.iloc[j-1,7]==1.0)and(ndf.iloc[j-1,4]>c)and(ndf.iloc[j-1,2]<=a)and(ndf.iloc[j-1,5]==2.0):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        elif (ndf.iloc[j-1,7]==1.0)and(ndf.iloc[j-1,4]>c)and(ndf.iloc[j-1,3]<=b)and(ndf.iloc[j-1,6]==2.0):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
    # Above condition to check second machine
        elif (ndf.iloc[j-1,5]==3.0)and(ndf.iloc[j-1,2]<=a):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        
        elif (ndf.iloc[j-1,6]==3.0)and(ndf.iloc[j-1,3]<=b):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
        
        elif (ndf.iloc[j-1,7]==3.0)and(ndf.iloc[j-1,4]<=c):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
    # Above condition to check third machine
        
        else:
            mac_data='nm'
        mac_data1.append(mac_data)
        j=j+1
        
    mac_data1.remove("maf")
    ndf['Machine_allocated']=pd.DataFrame(mac_data1)
    st.subheader('Download Excel')

    def convert_df(ndf):
       return ndf.to_csv().encode('utf-8')


    csv = convert_df(ndf)

    st.download_button(
      "Press to Download",
      csv,
      "file.csv",
      "text/csv",
      key='download-csv'
      )
    st.subheader('Machine Plan')
    st.table(ndf)
except:
    pass

