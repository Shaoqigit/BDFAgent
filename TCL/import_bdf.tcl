*clearmark loadcols 1
*clearmark loadcols 1
*entitybundleregister "__AUTOCONTACT_PREVIEW_BUNDLE_NASTRAN" "groups groups contactsurfs contactsurfs sets sets" 0
*templatefileset "C:/Program Files/Altair/2025/hwdesktop/templates/feoutput/nastran/general"
*loaddefaultattributevaluesfromxml 
*clearmark loadcols 1
*elementchecksettings 5 0 0 1 2 5 5 5 5 5 5 5 5 5 5 5 0 0 5 0 0 0 0
*entitybundleregister "__AUTOCONTACT_PREVIEW_BUNDLE_NASTRAN" "groups groups contactsurfs contactsurfs sets sets" 0
*templatefileset "C:/Program Files/Altair/2025/hwdesktop/templates/feoutput/nastran/general"
*loaddefaultattributevaluesfromxml 
*displayimporterrors 1
*feinputpreserveincludefiles 
*start_batch_import 2
*createinclude 0 "cbush_test.bdf" "C:/Project/CAEAgents/test_cases/cbush_test.bdf" 0
*createstringarray 26 "Nastran " "NastranMSC " "CREATE_ONE_COMP_ACROSS_INCLUDES " \
  "ASSIGNPROP_BYHMCOMMENTS " "CREATE_PART_HIERARCHY" "IMPORT_MATERIAL_METADATA" \
  "FE_GEOMETRY_CREATE" "FE_GEOMETRY_EDGE_FEATURE_METHOD 2" "FE_GEOMETRY_FEATURE_ANGLE 30" \
  "FE_GEOMETRY_VERTEX_ANGLE 60" "FE_GEOMETRY_ALLOW_OPEN_FEATURES" "EL_PRP_RATIO 3.0 " \
  "DELETE_DUPLICATE_NODES 1e-6 " "DELETE_DUPLICATE_SYSTEMS 1e-6 " "IMPORT_COMMENTS " \
  "ORGANIZE_ENTITIES " "ANSA " "ENGINEERINGENTITIES " "PATRAN " "FEMAP " "SPC1_To_SPC " \
  "HM_READ_PCL_GRUPEE_COMMENTS " "EXPAND_IDS_FOR_FORMULA_SETS " "IMPORT_MIX_IDPOOLS_ELEMENTIDS " \
  "ORGANIZE_ELEMENTS " "\[DRIVE_MAPPING= \]"
*feinputwithdata2 "\#nastran\\nastran" "C:/Project/CAEAgents/test_cases/cbush_test.bdf" 0 0 0 0 0 1 26 1 0
*setcurrentinclude 0 ""
*end_batch_import 
*removeview "Current"
*removeview "Current"
*rotateabout 1 0.100000001 0.100000001 0.25626565
*viewset 0.829671668 0.252052504 -0.49811089 0 -0.328773068 0.941729877 -0.0710852272 0 0.451168698 0.222742844 0.864194672 0 -0.0657088988 -0.0764595782 0.0917218532 1 -0.0254032296 -0.0254032296 0.211500087 0.211500087

