(
    global g_rolloutMergeSelection
    try(destroyDialog g_rolloutMergeSelection)catch()

    function this_script_path =
    (
        return getFileNamePath (getThisScriptFileName())
    )

    rollout g_rolloutMergeSelection "Bailey3D - Merge Selection" width:250
    (
        group "Merge Selection"
        (
            button btnMergeSelection "Merge Selection" width:200 tooltip:"Merges all selected objects"
        )

        group "Extras.."
        (
            button btnArtstation "More by Bailey3D" width:200
        )



        on btnMergeSelection pressed do
        (
            script_path = this_script_path() + "scripts/merge_selection.py"
            python.executeFile script_path
        )

        on btnArtstation pressed do
        (
            ShellLaunch "http://bailey3d.com/" ""
        )
    )

    createDialog g_rolloutMergeSelection
)