import powerfactory as pf

app = pf.GetApplication()

# Get active study case
active_case = app.GetActiveStudyCase()
app.PrintPlain(active_case)
# returns: <class 'powerfactory.DataObject'>

# get Script folder 
scripts_folder = app.GetProjectFolder('script')

scripts_folder_contents = scripts_folder.GetContents()

for script in scripts_folder_contents:
    script_contents = script.GetContents()
    app.PrintPlain(script_contents)         # list

    for obj in script_contents:
        # list - of contents
        obj_id = obj.GetContents()    
        # list - of contents     
        app.PrintPlain(obj_id)         


