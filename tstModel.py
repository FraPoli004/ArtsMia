from model.model import Model

mdl = Model()
mdl.buildGraph()
print(f"Number of nodes: {mdl.getNumNodes()} and number of edges: {mdl.getNumEdges()}")

mdl.getInfoCompConnessa(1224)