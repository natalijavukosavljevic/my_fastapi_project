from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
#UUID stands for Universally Unique Identifier

# Create FastAPI instance
app = FastAPI()
#are name and description required
class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = None
    description: str = None

projects = [
    Project( name="Item 1", description="Description of Item 1"),
    Project(name="Item 2", description="Description of Item 2"),
    Project(name="Item 3", description="Description of Item 3"),
]
   

# Define route
@app.get("/")
async def root():
    return {"message": "Hello World"}

# get projects
@app.get("/projects")
async def get_projects():
    return projects

#create project
@app.post("/projects")
def create_item(project: Project):
    projects.append(project)
    return projects



#get project
projects_dict = {project.id: project for project in projects}

@app.get("/project/{project_id}/info", response_model=Project)
def get_project_by_id(project_id: UUID):
    get_project = projects_dict.get(project_id)
    if get_project:
        return get_project
    else:
         raise HTTPException(status_code=404, detail=f"Project {project_id} not found")
    
#PUT
@app.put("/project/{project_id}/info", response_model=Project)
def update_item(project_id: UUID, updated_project: Project = None):
    for index, project in enumerate(projects):
        if project.id == project_id:
            projects[index] = updated_project
            return updated_project
    raise HTTPException(status_code=404, detail="Project not found")


#DELETE
@app.delete("/project/{project_id}", response_model=Project)
def update_item(project_id: UUID, updated_project: Project = None):
    for index, project in enumerate(projects):
        if project.id == project_id:
            deleted_project = projects.pop(index)
            return deleted_project
    raise HTTPException(status_code=404, detail="Project not found")

