import arcpy
from arcpy import env
env.workspace = "L:/Buffalo/Williams_NYRE/Data/Analysis/Data_Routine/Data.gdb"
inFeatures = 'Project_Features_10m_buffer'
inFeatures = [r'L:\Buffalo\Williams_NYRE\Data\Analysis\Data_Routine\Data.gdb\Data\dtl_cnty',r'L:\Buffalo\Williams_NYRE\Data\Analysis\Data_Routine\Data.gdb\Data\NWI_Wetlands',r'L:\Buffalo\Williams_NYRE\Data\Analysis\Data_Routine\Data.gdb\Data\SSURGO',r'L:\Buffalo\Williams_NYRE\Data\Analysis\Data_Routine\Data.gdb\Data\Townships_Merged',r'L:\Buffalo\Williams_NYRE\Data\Analysis\Data_Routine\Data.gdb\Data\WBDHU10',r'L:\Buffalo\Williams_NYRE\Data\Analysis\Data_Routine\Data.gdb\Data\WBDHU8']
boundary =r'L:\Buffalo\Williams_NYRE\Data\Analysis\Data_Routine\Data.gdb\Data\Project_Features_10m_buffer'
xy_tolerance = ""
for feature in inFeatures:
    arcpy.Clip_analysis(inFeatures, boundary, feature + "_Clip", xy_tolerance)
    
inFeatures = ['NWI_Wetlands','dtl_cnty','WBDHU8','WBDHU10','SSURGO','Townships_Merged']
boundary ='Project_Features_10m_buffer'
xy_tolerance = ""
for feature in inFeatures: 
    arcpy.Clip_analysis(inFeatures, boundary, inFeatures + "_Clip", xy_tolerance)
    
for feature in inFeatures: 
    arcpy.Clip_analysis(inFeatures, boundary, feature + "_Clip", xy_tolerance)
    
for feature in inFeatures: 
    arcpy.Clip_analysis(feature, boundary, feature + "_Clip", xy_tolerance)
    

