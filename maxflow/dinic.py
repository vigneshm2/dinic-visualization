""" Implementation of Dinic's algorithm for max flow """
from gui.image_display import ImageSequence
import matplotlib.image as mpimg
from graph import display_graph

INF = 1000000000


def find_distances(graph, source):
    """ Find distances using bfs """
    # TODO implement
    return [INF for _ in graph]


class DinicImageSequence(ImageSequence):
    """ subclass image sequence """
    def __init__(self, graph, source, sink):
        ImageSequence.__init__(self)
        self.graph = graph
        self.source = source
        self.sink = sink
        self.flow = 0
        self.done = False
        self.status = 0  # status=1 when blocking flow is in progress
        print "dinic with", graph
        # set init image

    def init_image(self):
        # set init image
        display_graph(self.graph, 'dinic_output')
        return mpimg.imread('dinic_output.png')

    def next_image(self):
        if self.status == 1:
            _next = self.blocking_flow.next()
            if self.blocking_flow.complete():
                self.status = 0
            return _next
        else:
            dist = find_distances(self.graph, self.source)
            if dist[self.sink] == INF:
                self.done = True
                return self.init_image()
            else:
                # find blocking flow
                self.blocking_flow = BlockingFlowImageSequence(self.graph, dist, self.source, self.sink)
                self.status = 1
                return self.next()

    def complete(self):
        return self.done


class BlockingFlowImageSequence(ImageSequence):
    """ find blocking flow from source to sink,
        given graph and distances array
    """
    def __init__(self, graph, dist, source, sink):
        ImageSequence.__init__(self)
        print "blocking flow", graph, dist