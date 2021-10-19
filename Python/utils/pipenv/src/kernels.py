import json

py3 = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}

def swap_kernels(nbs_paths, spec = py3):
    """
    Parameters:
        First: Positional argument with list of strings, paths to notebooks that will have their kernel switched.
        Second: Keyword argument with a dict to replace in notebook['metadata']['kernelspec']. This describes the settings for the kernel.
    Raises:
        ValueError if nbs_paths is not a list of strings.
        ValueError if spec is not a dict with string values.
    Returns:
        Nothing, but prints progress and a warning to restart jupyterlab-server to incorporate changes.    
    """
    
    if not (isinstance(nbs_paths, list) and all(isinstance(elem, str) for elem in nbs_paths)):
        raise ValueError("Expecting list of strings as input for notebooks to set kernel on as first parameter.")
    
    if not (isinstance(spec, dict) and all(isinstance(elem, str) for elem in spec.values())):
        raise ValueError(f"Expecting dict, with strings as values in keyword-argument 'spec'. Default: {py3}")
        
    for path in nbs_paths:
        with open(path, "r") as json_file:
            notebook = json.loads(json_file.read())
            notebook['metadata']['kernelspec'] = spec
        print(path, 'set to', spec['display_name'])

        with open(path, "w") as json_file:
            json_file.write(json.dumps(notebook))
    print("\nRestart jupyterserver for simplicity?")