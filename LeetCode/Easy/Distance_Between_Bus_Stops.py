class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start <= destination:
            l = start
            r = destination
        else:
            l = destination
            r = start
        length = len(distance)
        road1 = road2 = 0

        for i in range(l,r):
            road1 += distance[i]

        for i in range(r,length):
            road2 += distance[i]
        for i in range(l):
            road2 += distance[i]

        if road1 > road2:
            return road2
        else:
            return road1