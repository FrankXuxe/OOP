import Project as PR

projID1 = 1001
projDesc1 = "SAP Implementation"
consultants1 = 25
dueDate1 = "09/30/2022"


projID2 = 1002
projDesc2 = "Migration to CRM"
consultants2 = 10
dueDate2 = "06/30/2022"

instance1 = PR.Project(projID1, projDesc1, consultants1, dueDate1)
instance2 = PR.Project(projID2, projDesc2, consultants2, dueDate2)

dictionary = {instance1.get_projID(): instance1.get_duedate(),
              instance2.get_projID(): instance2.get_duedate()}

print(dictionary)
