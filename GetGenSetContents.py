import powerfactory as pf
app = pf.GetApplication()

# Get active study case
active_case = app.GetActiveStudyCase()
app.PrintPlain(active_case)

# get contents of Study Case folder
contents_studycase = active_case.GetContents()
contents_studycase_GenSet = active_case.GetContents('*.SetSelect')

genSets = contents_studycase_GenSet[0].GetContents() # first genSet

# first genSet
for obj in genSets:
    app.PrintPlain(obj.loc_name)
    # app.PrintPlain(type(obj))
    # app.PrintPlain(obj.GetContents())
    # app.PrintPlain(obj.GetAttribute('loc_name'))
    
    # returns (not actual name_label)
        # Ref2
        # Ref3
        # Ref4
        # Ref5
        # Ref6
        # Ref7
        # Ref1