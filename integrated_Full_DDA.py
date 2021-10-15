import pandas as pd
import numba as nb
Full_file_path = input("請給Fullscan.xlsx的檔案位置:")
DDA_file_path = input("請給DDA.xlsx的檔案位置:")
mz_tol = input("請給mz tolerance參數 ex:20 (ppm):")
mz_tol = float(mz_tol)
rt_tol = input("請給rt tolerance，單位為 秒:")
rt_tol = int(rt_tol)
DDA_low_intensity = input("請給DDA可定量的最低訊號強度參數 ex:100 ")
DDA_low_intensity = int(DDA_low_intensity)
DDA_low_intensity_num = input("請給DDA可定量的樣品數目 ex:3 (3個以上大於訊號強度就拿來定量)")
DDA_low_intensity_num = int(DDA_low_intensity_num)
Fullscan_data = pd.read_excel(Full_file_path)
DDA_data = pd.read_excel(DDA_file_path)
print(Full_file_path)
print(DDA_file_path)

#定義 Function
@nb.jit(nopython=True)
def integration_feature (Fullscan_data,DDA_data,mz_tol=20,rt_tol=20,DDA_low_intensity=100,DDA_low_intensity_num=3):
    DDA_rep3 = pd.DataFrame()
    DDA_rep1 = pd.DataFrame()
    DDA_data_index = list (DDA_data.index)
    ## 分類 DDA 特徵為可定量或只可定性
    for a in DDA_data_index:
        A= list(DDA_data.iloc[a,2:])
        B= len([i for i in A if i>= DDA_low_intensity])
        if B >= DDA_low_intensity_num:
            DDA_rep3 = DDA_rep3.append(DDA_data.iloc[a:a+1])
        else:
            DDA_rep1 = DDA_rep1.append(DDA_data.iloc[a:a+1]) 
    # print("總DDA特徵數量",len(DDA_data.index))
    # print("可定量的DDA特徵數量",len(DDA_rep3.index))
    # print("不可定量的DDA特徵數量",len(DDA_rep1.index))
    
    #比對Fullscan及DDA可定量特徵
    mz1 = Fullscan_data["mz"]
    mz2 = DDA_rep3["mz"]
    rt1 = Fullscan_data["rt"]
    rt2 = DDA_rep3["rt"]
    Full_DDA_match = pd.DataFrame()
    Full_DDA_match_index =[]
    DDA_rep3_index = list (DDA_rep3.index)
    Full_index = list (Fullscan_data.index)
    if DDA_low_intensity_num >=1:    
        # print("正在比對Fullscan及DDA可定量特徵")
        for x in DDA_rep3_index:
            mzdiff = abs((mz1-mz2[x])/mz2[x]*1000000)
            rtdiff = abs(rt1-rt2[x])
            for y in Full_index:
                if mzdiff[y] <= mz_tol and rtdiff[y] <= rt_tol:
                    Full_DDA_match_index = Full_DDA_match_index+[x]
        
        Full_DDA_match_index = set(Full_DDA_match_index)
        Full_DDA_match = Full_DDA_match.append(DDA_rep3.loc[Full_DDA_match_index])
        Full_DDA_No_match = DDA_rep3.drop(Full_DDA_match_index)
        #比對Fullscan與DDA不可定量之特徵
        print("正在比對Fullscan及DDA不可定量特徵")
        mz3 = DDA_rep1["mz"]
        rt3 = DDA_rep1["rt"]
        Full_DDA_rep1_match = pd.DataFrame()
        Full_DDA_rep1_match_index = []
        DDA_rep1_index = list (DDA_rep1.index)
        for Z in DDA_rep1_index:
            mzdiff = abs((mz1-mz3[Z])/mz3[Z]*1000000)
            rtdiff = abs(rt1-rt3[Z])
            for y in Full_index:
                if mzdiff[y] <= mz_tol and rtdiff[y] <= rt_tol:
                    Full_DDA_rep1_match_index = Full_DDA_rep1_match_index+[Z]
        
        Full_DDA_rep1_match_index = set(Full_DDA_rep1_match_index)
        Full_DDA_rep1_match = Full_DDA_rep1_match.append(DDA_rep1.loc[Full_DDA_rep1_match_index])
        Full_DDA_rep1_No_match = DDA_rep1.drop(Full_DDA_rep1_match_index)
        
        para_rows = [["mz_tol",mz_tol],["rt_tol",rt_tol],["DDA_low_intensity",DDA_low_intensity],["DDA_low_intensity_num",DDA_low_intensity_num],["Fullscan_file_path",Full_file_path],["DDA_file_path",DDA_file_path]]
        para_df = pd.DataFrame(para_rows, columns = ["parameter","value"])
        # with pd.ExcelWriter('Fullscan_DDA_integration_results.xlsx') as writer:  
        #     Full_DDA_match.to_excel(writer, sheet_name='Full_DDA_overlap')
        #     Full_DDA_No_match.to_excel(writer, sheet_name='Full_DDA_No_overlap')
        #     Full_DDA_rep1_No_match.to_excel(writer, sheet_name='Full_DDA_onlyID_No_overlap')
        #     DDA_rep1.to_excel(writer, sheet_name='DDA_only_ID_data')
        #     DDA_rep3.to_excel(writer, sheet_name='DDA_feature_data')
        #     para_df.to_excel(writer, sheet_name='parameters')
        
            
        print("完成比對")
        return (Full_DDA_match,Full_DDA_No_match,Full_DDA_rep1_No_match,DDA_rep1,DDA_rep3,para_df)
    else:    ## 比對Fullscan及所有DDA特徵
        print("正在將Fullscan及所有DDA特徵進行比對")
        for x in DDA_rep3_index:
            mzdiff = abs((mz1-mz2[x])/mz2[x]*1000000)
            rtdiff = abs(rt1-rt2[x])
            for y in Full_index:
                if mzdiff[y] <= mz_tol and rtdiff[y] <= rt_tol:
                    Full_DDA_match_index = Full_DDA_match_index+[x]
        
        Full_DDA_match_index = set(Full_DDA_match_index)
        Full_DDA_match = Full_DDA_match.append(DDA_rep3.loc[Full_DDA_match_index])
        Full_DDA_No_match = DDA_rep3.drop(Full_DDA_match_index)
        
        para_rows = [["mz_tol",mz_tol],["rt_tol",rt_tol],["DDA_low_intensity",DDA_low_intensity],["DDA_low_intensity_num",DDA_low_intensity_num],["Fullscan_file_path",Full_file_path],["DDA_file_path",DDA_file_path]]
        para_df = pd.DataFrame(para_rows, columns = ["parameter","value"])
        
        # with pd.ExcelWriter('Fullscan_DDA_integration_results.xlsx') as writer:  
        #     Full_DDA_match.to_excel(writer, sheet_name='Full_DDA_ovelap')
        #     Full_DDA_No_match.to_excel(writer, sheet_name='Full_DDA_No_overlap')
        #     para_df.to_excel(writer, sheet_name='parameters')
        print("完成比對")
        return (Full_DDA_match,Full_DDA_No_match,para_df)
        
        
integration_feature(Fullscan_data,DDA_data,mz_tol,rt_tol,DDA_low_intensity,DDA_low_intensity_num)
