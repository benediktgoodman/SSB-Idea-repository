import papermill as pm
from IPython.display import display, Markdown
import os
import glob

def auto_kjoreplan(mapper: list):
    """
    Parameter1: List of postfixes for folders in current working directory to scan trhough for notebooks to run.
    Only looks 1 level deep. Will not run notebooks ending in "_output.ipynb", as that is what papermill spits out.
    Returns: Nothing, but prints progress
    """

    # Fyll ut mappenavn
    for i, mappe in enumerate(mapper):
        mapper[i] = glob.glob(mappe + "*")[0]
        # Lag mappe for output, om det ikke fins
        if not os.path.exists(f'{mapper[i]}/output'): os.makedirs(f'{mapper[i]}/output')
    # Finn alle notebooks rett innenfor mappene, gjerne sortert i rett rekkefølge...
    filer = []
    for mappe in mapper:
        # Sortering på en comprehension, som i teorien fjerner det som ikke er notebooks vi skal kjøre.
        filer_i_mappen = sorted([mappe + "/" + x for x in os.listdir(mappe) if x.endswith('.ipynb') and 'output' not in x])
        filer += filer_i_mappen
    # Kjør alle arkene med papermill
    for ark in filer:
        kjor_ark(ark)

def kjor_ark(ark):
    if "_output.ipynb" not in ark:
            # Klikkbare direktelinker til de individuelle arkene, om feil skulle oppstå under
            display(Markdown('[' + ark + '](./' +  ark + ')'))
            ark = ark.replace(".ipynb" , "")
            pm.execute_notebook(
                ark + ".ipynb",
                ark.split("/")[0] +"/output/" + ark.split("/")[1] + "_output.ipynb",
                cwd = f"{os.getcwd()}/{ark.split('/')[0]}")
