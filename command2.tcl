*begin "version 2025.0.0.24  4-15-2025  9:58:53"
*createstringarray 20 " 0 penalty value              0.00    0.00    0.80    1.00   10.00" \
  "  1 min length        1 1.0  10.000   9.000   4.000   2.000   1.000    1   59    0" \
  "  2 max length        1 1.0  10.000  12.000  15.000  20.000  30.000    0   39    1" \
  "  3 aspect ratio      1 1.0   1.000   2.000   4.400   5.000  10.000    0   41    2" \
  "  4 warpage           1 1.0   0.000   5.000  13.000  15.000  30.000    0   56    3" \
  "  5 max angle quad    1 1.0  90.000 110.000 134.000 140.000 160.000    0   28    4" \
  "  6 min angle quad    1 1.0  90.000  70.000  46.000  40.000  20.000    0   61    5" \
  "  7 max angle tria    1 1.0  60.000  80.000 112.000 120.000 150.000    0   19    6" \
  "  8 min angle tria    1 1.0  60.000  50.000  34.000  30.000  15.000    0   22    7" \
  "  9 skew              1 1.0   0.000  10.000  34.000  40.000  70.000    0   46    8" \
  " 10 jacobian          1 1.0   1.000   0.900   0.700   0.600   0.300    0   57    9" \
  " 11 chordal dev       0 1.0   0.000   0.300   0.800   1.000   2.000    0   29   10" \
  " 12 taper             1 1.0   0.000   0.200   0.500   0.600   0.900    0   53   11" \
  " 13 % of trias        1 1.0   0.000   6.000  10.000  15.000  20.000    0    0   -1" \
  " 14 QI color legend            32      32       7       6       3           3   -1" \
  " 15 time_step         0        10.000                       0.01            0   59   12" \
  " 16 area_skew         0        10.000                      0.500            0   39   13" \
  " 17 cell_squish       0        10.000                      0.600            0   53   14" \
  " 18 equi_skew         0        10.000                      0.600            0   34   15" \
  "   Global_solver -1"
*setqualitycriteria 1 20 0
*templatefileset "C:/Program Files/Altair/2025/hwdesktop/templates/feoutput/optistruct/optistruct"
*menufilterset "*"
*menufilterdisable 
*setoption show_scale=0
*setscaleoption position=bottom
*viewset 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 10 10
*viewset 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 10 10
*viewset 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 10 10
*graphicfont 2
*menufont 2
*ME_CoreBehaviorAdjust "allowable_actions_policy=default"
*loaddefaultattributevaluesfromxml 
*clearmark loadcols 1
*clearmark loadcols 1
*clearmark loadcols 1
*clearmark groups 1
*clearmark contactgroups 1
*setoption highlight-active_color=#feb317
*setoption highlight-glow_color=#feb317
*clearmarkall 1
*setoption topoedgecolor=0
*setoption topofacecolor=4
# Session ended at "4-15-2025  9:59:12"
return; # Stop script and return to application 
# *quit 1; # Uncomment to exit application
*do_markrejectclear 0
*begin "version 2025.0.0.24  4-15-2025  10:32:33"
*createstringarray 20 " 0 penalty value              0.00    0.00    0.80    1.00   10.00" \
  "  1 min length        1 1.0  10.000   9.000   4.000   2.000   1.000    1   59    0" \
  "  2 max length        1 1.0  10.000  12.000  15.000  20.000  30.000    0   39    1" \
  "  3 aspect ratio      1 1.0   1.000   2.000   4.400   5.000  10.000    0   41    2" \
  "  4 warpage           1 1.0   0.000   5.000  13.000  15.000  30.000    0   56    3" \
  "  5 max angle quad    1 1.0  90.000 110.000 134.000 140.000 160.000    0   28    4" \
  "  6 min angle quad    1 1.0  90.000  70.000  46.000  40.000  20.000    0   61    5" \
  "  7 max angle tria    1 1.0  60.000  80.000 112.000 120.000 150.000    0   19    6" \
  "  8 min angle tria    1 1.0  60.000  50.000  34.000  30.000  15.000    0   22    7" \
  "  9 skew              1 1.0   0.000  10.000  34.000  40.000  70.000    0   46    8" \
  " 10 jacobian          1 1.0   1.000   0.900   0.700   0.600   0.300    0   57    9" \
  " 11 chordal dev       0 1.0   0.000   0.300   0.800   1.000   2.000    0   29   10" \
  " 12 taper             1 1.0   0.000   0.200   0.500   0.600   0.900    0   53   11" \
  " 13 % of trias        1 1.0   0.000   6.000  10.000  15.000  20.000    0    0   -1" \
  " 14 QI color legend            32      32       7       6       3           3   -1" \
  " 15 time_step         0        10.000                       0.01            0   59   12" \
  " 16 area_skew         0        10.000                      0.500            0   39   13" \
  " 17 cell_squish       0        10.000                      0.600            0   53   14" \
  " 18 equi_skew         0        10.000                      0.600            0   34   15" \
  "   Global_solver -1"
*setqualitycriteria 1 20 0
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
# Session ended at "4-15-2025  10:32:34"
return; # Stop script and return to application 
# *quit 1; # Uncomment to exit application
*begin "version 2025.0.0.24  4-15-2025  10:36:59"
*createstringarray 20 " 0 penalty value              0.00    0.00    0.80    1.00   10.00" \
  "  1 min length        1 1.0  10.000   9.000   4.000   2.000   1.000    1   59    0" \
  "  2 max length        1 1.0  10.000  12.000  15.000  20.000  30.000    0   39    1" \
  "  3 aspect ratio      1 1.0   1.000   2.000   4.400   5.000  10.000    0   41    2" \
  "  4 warpage           1 1.0   0.000   5.000  13.000  15.000  30.000    0   56    3" \
  "  5 max angle quad    1 1.0  90.000 110.000 134.000 140.000 160.000    0   28    4" \
  "  6 min angle quad    1 1.0  90.000  70.000  46.000  40.000  20.000    0   61    5" \
  "  7 max angle tria    1 1.0  60.000  80.000 112.000 120.000 150.000    0   19    6" \
  "  8 min angle tria    1 1.0  60.000  50.000  34.000  30.000  15.000    0   22    7" \
  "  9 skew              1 1.0   0.000  10.000  34.000  40.000  70.000    0   46    8" \
  " 10 jacobian          1 1.0   1.000   0.900   0.700   0.600   0.300    0   57    9" \
  " 11 chordal dev       0 1.0   0.000   0.300   0.800   1.000   2.000    0   29   10" \
  " 12 taper             1 1.0   0.000   0.200   0.500   0.600   0.900    0   53   11" \
  " 13 % of trias        1 1.0   0.000   6.000  10.000  15.000  20.000    0    0   -1" \
  " 14 QI color legend            32      32       7       6       3           3   -1" \
  " 15 time_step         0        10.000                       0.01            0   59   12" \
  " 16 area_skew         0        10.000                      0.500            0   39   13" \
  " 17 cell_squish       0        10.000                      0.600            0   53   14" \
  " 18 equi_skew         0        10.000                      0.600            0   34   15" \
  "   Global_solver -1"
*setqualitycriteria 1 20 0
*templatefileset "C:/Program Files/Altair/2025/hwdesktop/templates/feoutput/nastran/general"
*menufilterset "*"
*menufilterdisable 
*setoption show_scale=0
*setscaleoption position=bottom
*viewset 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 10 10
*graphicfont 2
*menufont 2
*ME_CoreBehaviorAdjust "allowable_actions_policy=default"
*loaddefaultattributevaluesfromxml 
*clearmark loadcols 1
*clearmark loadcols 1
*setoption highlight-active_color=#feb317
*setoption highlight-glow_color=#feb317
*clearmarkall 1
*setoption topoedgecolor=0
*setoption topofacecolor=4
*clearmark loadcols 1
*clearmark loadcols 1
*entitybundleregister "__AUTOCONTACT_PREVIEW_BUNDLE_NASTRAN" "groups groups contactsurfs contactsurfs sets sets" 0
*templatefileset "C:/Program Files/Altair/2025/hwdesktop/templates/feoutput/nastran/general"
*loaddefaultattributevaluesfromxml 
*clearmark loadcols 1
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
*viewset 0.829671668 0.252052504 -0.49811089 0 -0.328773068 0.941729877 -0.0710852272 0 0.451168698 0.222742844 0.864194672 0 0.00647242549 -0.0996689212 0.0917218532 1 -0.147956527 -0.137998193 0.325850107 0.33580844
*rotateabout 1 0.100000001 0.100000001 0.25626565
*viewset 0.578972552 0.475471942 -0.662357318 0 -0.315633117 0.879725165 0.355611263 0 0.751775579 0.00317274406 0.659411414 0 -0.0468068754 -0.0595421198 0.117955761 1 -0.147956527 -0.137998193 0.325850107 0.33580844
*rotateabout 1 0 0.150020003 0
*viewset -0.260540072 0.593992811 -0.761111957 0 0.12528742 0.802474135 0.58338523 0 0.957299291 0.0566374764 -0.283496496 0 -0.112953776 -0.0479529199 0.0837851102 1 -0.147956527 -0.137998193 0.325850107 0.33580844
# Session ended at "4-15-2025  10:43:18"
return; # Stop script and return to application 
# *quit 1; # Uncomment to exit application
*do_markrejectclear 0
