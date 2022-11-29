"""
:script
:type tool
:desc Merges all selected objects into one object
"""
import pymxs


class MergeSelection(object):
    def __init__(self):
        self.run()

    def log(self, info, error=False):
        if(error):
            pymxs.runtime.messageBox(str(info), title="Merge Selection - Failed!")
        print("MergeSelection: " + str(info))

    @property
    def selection(self):
        return [x for x in pymxs.runtime.selection]

    @property
    def run_mode(self):
        output_type = None
        num_geometry = 0
        num_spline = 0
        num_other = 0
        num_total = 0

        for i in self.selection:
            if(pymxs.runtime.superClassOf(i) == pymxs.runtime.geometryClass):
                num_geometry += 1
            elif(pymxs.runtime.superClassOf(i) == pymxs.runtime.shape):
                num_spline += 1
            else:
                num_other += 1
            num_total += 1

        if(num_total):
            if(num_geometry == num_total):
                output_type = pymxs.runtime.geometryClass
            elif(num_spline == num_total):
                output_type = pymxs.runtime.shape
            else:
                output_type = None

        return output_type

    def run(self):
        run_mode = self.run_mode

        if(run_mode and len(self.selection) > 1):
            copies = []
            num_merged = 1
            final_object = None
            if(run_mode == pymxs.runtime.geometryClass):
                for i in self.selection:
                    copy = pymxs.runtime.copy(i)
                    pymxs.runtime.convertToPoly(copy)
                    copies.append(copy)
                final_object = copies[0]
                for copy in copies[1:]:
                    pymxs.runtime.polyOp.attach(final_object, copy)
                    num_merged += 1

            elif(run_mode == pymxs.runtime.shape):
                for i in self.selection:
                    copy = pymxs.runtime.copy(i)
                    pymxs.runtime.convertToSplineShape(copy)
                    copies.append(copy)
                final_object = copies[0]
                for copy in copies[1:]:
                    pymxs.runtime.addAndWeld(final_object, copy, -1)
                    num_merged += 1
            pymxs.runtime.select(final_object)
            final_object.name = pymxs.runtime.uniqueName("merged_selection_")
            self.log("Merged " + str(num_merged) + " objects.")

        elif(not run_mode):
            self.log(
                "Unable to merge selection Make sure the selection only consists of either Geometry or Splines.",
                error=True
            )

        elif(len(self.selection) <= 1):
            self.log(
                "Unable to merge selection. You must select 2 or more objects.",
                error=True
            )



tool = MergeSelection()
