"""FAST API app imports."""


from uuid import UUID

from fastapi import FastAPI, HTTPException

from mainapp.models import Project

# UUID stands for Universally Unique Identifier

# Create FastAPI instance
app = FastAPI()



projects: dict[UUID, Project] = {
    UUID("47003432-436b-4e57-876e-2ca584dd0187") :
    Project(id=UUID("47003432-436b-4e57-876e-2ca584dd0187"), name="Item1",
             description="Description of Item 1"),
    UUID("4acb1d0e-7f6b-46f4-83c3-4bdd6ccddae2"):
    Project(id=UUID("4acb1d0e-7f6b-46f4-83c3-4bdd6ccddae2"), name="Item 2",
            description="Description of Item 2"),
   UUID("e737bdaa-7bb5-4e88-8504-8196d9a0a1bd"):
   Project(id=UUID("e737bdaa-7bb5-4e88-8504-8196d9a0a1bd"), name="Item 3",
            description="Description of Item 3"),
}


@app.get("/")
async def root() -> dict[str, str]:
    """Get dict (JSON) for root path."""
    return {"message": "Hello World"}


# get projects
@app.get("/projects")
async def get_projects() -> list[Project]:
    """Get list of projects full info(details + documents)."""
    return list(projects.values())


@app.get("/project/{project_id}/info", response_model=Project)
def get_project_by_id(project_id: UUID) -> Project:
    """Get project's details based on id."""
    project = projects.get(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


# create project
@app.post("/projects", response_model=Project)
def create_item(project: Project)  -> Project:
    """Post project."""
    if project.id in projects:
        raise HTTPException(status_code=404,
                            detail
                            =f"Project with {project.id} already exists.")
    projects[project.id] = project
    return project


# PUT
@app.put("/project/{project_id}/info", response_model=Project)
def update_item(project_id: UUID, project: Project = None) -> Project:
     """Update project."""
     if project_id not in projects:
         raise HTTPException(status_code=404,
                            detail=f"Project with {project.id} doesn't exist.")
     if project.id != project_id:
        raise HTTPException(status_code=400, detail="Project ID mismatch.")
     projects[project_id] = project
     return project




# DELETE
@app.delete("/project/{project_id}")
def delete_item(project_id: UUID)-> dict[str,str]:
     """Delete project."""
     if project_id not in projects:
         raise HTTPException(status_code=404,
                            detail=f"Project with {project_id} doesn't exist.")
     del projects[project_id]
     return {"detail": f"Project with {project_id} sucessfully deleted!."}
