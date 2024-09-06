from .base_fal_api_flux_node import BaseFalAPIFluxNode

class FalAPIFluxNode(BaseFalAPIFluxNode):
    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES()

class FalAPIFluxProNode(BaseFalAPIFluxNode):
    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES("Pro")
        
NODE_CLASS_MAPPINGS = {
    "FalAPIFluxNode": FalAPIFluxNode
    "FalAPIFluxProNode": FalAPIFluxProNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxNode": "Fal API Flux"
    "FalAPIFluxProNode": "Fal API Flux Pro"
}
