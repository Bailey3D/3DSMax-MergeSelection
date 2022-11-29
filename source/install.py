"""
Installs the scripts as macros to 3DS Max
"""
import os
import pymxs


def create_a_macro(name, tooltip, script_path, maxscript=False):
    macro_category = "Bailey3D"
    auto_undo_enabled = True
    script_path = script_path.replace("\\", "/")

    if(maxscript):
        command = "fileIn"
    else:
        command = "python.executeFile"

    macro_text = """
        macroScript {} category:"{}" toolTip:"{}" autoUndoEnabled:{}
        (
            script_path = "{}"
            {} script_path
        )
    """.format(
        name, macro_category, tooltip, str(auto_undo_enabled), script_path, command
    )
    pymxs.runtime.execute(macro_text)


create_a_macro(
    "MergeSelection",
    "Merge Selection",
    os.path.join(os.path.dirname(__file__), "scripts\\merge_selection.py")
)

create_a_macro(
    "MergeSelectionGUI",
    "Merge Selection (GUI)",
    os.path.join(os.path.dirname(__file__), "merge_selection_gui.ms"),
    maxscript=True
)