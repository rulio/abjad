from experimental.tools.scoremanagertools.editors.get_dynamic_handler_editor import get_dynamic_handler_editor
from experimental.tools.scoremanagertools.materialpackagemakers.MaterialPackageMaker import MaterialPackageMaker
from experimental.tools.scoremanagertools.wizards.DynamicHandlerCreationWizard import DynamicHandlerCreationWizard
from experimental.tools.handlertools.DynamicHandler import DynamicHandler


class DynamicHandlerMaterialPackageMaker(MaterialPackageMaker):

    ### CLASS VARIABLES ###

    generic_output_name = 'dynamic handler'
    output_material_checker = staticmethod(lambda x: isinstance(x, DynamicHandler))
    output_material_editor = staticmethod(get_dynamic_handler_editor)
    output_material_maker = DynamicHandlerCreationWizard
    output_material_module_import_statements = [
        'from abjad.tools import durationtools',
        'from experimental.tools import handlertools',
        ]
