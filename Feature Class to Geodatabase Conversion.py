inFeatures =[r'L:/Buffalo/Whidbey_EIS/Data/From_Wyle/2015_11_13/10_MaxYr_Alt3B/NASWI_MaxYr_Alt3B_DNL60to90_Lines_20151102.shp',r'L:/Buffalo/Whidbey_EIS/Data/From_Wyle/2015_11_13/10_MaxYr_Alt3B/NASWI_MaxYr_Alt3B_DNL60to90_Polys_20151102.shp']
outLocation = 'L:/Buffalo/Whidbey_EIS/Data/From_Wyle/2015_11_13/Noise_Contours_2015_11_13.gdb/MaxYr_Alt3B_10'
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)
