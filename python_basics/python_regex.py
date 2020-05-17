
import re

string_col = "pMode=CREATE;fndCustomObject={pOptParamsMap={IsPropagated=9, TemplateIds=[Ljava.lang.Long;@5f8a26c1, CopyFirst=null, CopyFromRevisionId=null, CopyFromOrgId=null, nItems=1, CopyFromVersionId=null, itemClassId=100000011369001, ITEM_ROWS_PER_TXN_VAR=1, userSelectedOrgId=204, styleFlag=null, CopyFromItemId=null}};"

string_col_1 = "workAreaType=6;fndPageParams={fuseCardTitle=Plan Inputs, fndGlobalItemNodeId=itemNode_value_chain_planning_plan_inputs, pageParams=fndGlobalItemNodeId=itemNode_value_chain_planning_plan_inputs};fndCustomObject=oracle.apps.scm.advancedPlanning.common.workArea.publicUi.util.WorkAreaContext@4e591014;"

string_col_2 = "fndPageParams={fnd=;;;;false;256;;;, fuseCardTitle=Security Console, fndGlobalItemNodeId=ASE_FUSE_SECURITY_CONSOLE};"

string_col_3 = "fndPageParams={DEFAULTPLAN=300100168682390, fuseCardTitle=Sales and Operations Planning, PLANS={300100168682390=oracle.apps.scm.advancedPlanning.common.workArea.publicUi.util.WorkAreaContext@1756afae}, fndGlobalItemNodeId=itemNode_SupplyChainPlanning_SalesandOperationsPlanning, pageParams=fndGlobalItemNodeId=itemNode_SupplyChainPlanning_SalesandOperationsPlanning};fndWarnChanges=false;workAreaType=5;"

string_col_4 = "selectedPerson=SteveAuto WLS-EMP16;viewDetail=true;pSelectedPersonID=300100172996455;contextualAreaWidth=256;pSelectedGlbPrflID=99208;tabClicked=SkillReputation;contextualAreaCollapsed=false;"

string_col_5 = "pSelectedFacets=[];pShowRadiusSearch=false;pKeyword=Pipeline Req A15;pSelectedFiltersMap={};pIsPreviewMode=N;pKeywordStateValue=Pipeline Req A15;contextualAreaWidth=256;pCalledFrom=FUSESHELL;contextualAreaCollapsed=false;"

r1 = re.findall(r"\{.+\}", string_col)
r2 = re.findall(r"\{.+\}", string_col_1)
r3 = re.findall(r"\{.+\}", string_col_2)
r4 = re.findall(r"\{.+\}", string_col_3)
r5 = re.findall(r"\{.+\}", string_col_4)
r6 = re.findall(r"\{.+\}", string_col_5)

print(string_col)
print(r1)
# print("****************")
# print(string_col_1)
# print(r2)
# print("****************")
# print(string_col_2)
# print(r3)
# print("****************")
# print(string_col_3)
# print(r4)
# print("****************")
# print(string_col_4)
# print(r5)
# print("****************")
# print(string_col_5)
# print(r6)

print(len(r1))
print(len(r2))
print(len(r3))
print(len(r4))
print(len(r5))
print(len(r6))