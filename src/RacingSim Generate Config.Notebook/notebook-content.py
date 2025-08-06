# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.11"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

%pip install ms-fabric-cli --quiet

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# # Config Template

# CELL ********************

config = {
	"Settings": {
		"ipAddress": "0.0.0.0",
		"port": 5300,
		"dataEncoding": "Json",
		"cloudEventEncoding": "Binary",
		"dataMode": "Automatic",
		"dataRate": 10,
		"tenantId": None,
		"carId": 1
	}
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# # Load Libraries

# CELL ********************

import subprocess
import sempy.fabric as fabric
import json

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# # Variables

# CELL ********************

eventstream = "RacingSim.Eventstream"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# ## Definition of deployment functions

# CELL ********************

# Set environment parameters for Fabric CLI
token = notebookutils.credentials.getToken('pbi')
os.environ['FAB_TOKEN'] = token
os.environ['FAB_TOKEN_ONELAKE'] = token

def run_fab_command( command, capture_output: bool = False, silently_continue: bool = False):
    result = subprocess.run(["fab", "-c", command], capture_output=capture_output, text=True)
    if (not(silently_continue) and (result.returncode > 0 or result.stderr)):
       raise Exception(f"Error running fab command. exit_code: '{result.returncode}'; stderr: '{result.stderr}'")    
    if (capture_output): 
        output = result.stdout.strip()
        return output

def fab_get_id(name):
    id = run_fab_command(f"get /{workspace_name}.Workspace/{name} -q id" , capture_output = True, silently_continue= True)
    return(id)

def fab_get_item(name):
    item = run_fab_command(f"get /{workspace_name}.Workspace/{name}" , capture_output = True, silently_continue= True)
    return(item)

def fab_list_item():
    items = run_fab_command(f"ls /{workspace_name}.Workspace" , capture_output = True, silently_continue= True)
    return(items)

def fab_get_display_name(name):
    display_name = run_fab_command(f"get /{workspace_name}.Workspace/{name} -q displayName" , capture_output = True, silently_continue= True)
    return(display_name)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# ## Get current Workspace
# This cell gets the current workspace to deploy FUAM automatically inside it

# CELL ********************

workspace_id = fabric.get_notebook_workspace_id()
workspace_name = fabric.list_workspaces(filter=f"id eq '{workspace_id}'")['Name'][0]

eventstream_id = fab_get_id(eventstream)

conn_id = json.loads(run_fab_command(f"api workspaces/{workspace_id}/eventstreams/{eventstream_id}/topology" , capture_output = True, silently_continue= True)).get("text",{}).get("sources",[])[0].get('id')

connection = json.loads(run_fab_command(f"api workspaces/{workspace_id}/eventstreams/{eventstream_id}/sources/{conn_id}/connection" , capture_output = True, silently_continue= True)).get("text",{})

config["Settings"]["eventHubConnectionString"] = connection.get("accessKeys",{}).get("primaryConnectionString")
config["Settings"]["eventHubName"] = connection.get("eventHubName")
config["Settings"]["namespace"] = connection.get("fullyQualifiedNamespace")

print(config)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

out_file = open("./builtin/appsettings.json", "w")

json.dump(obj=config,fp=out_file,indent=6)

out_file.close()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
