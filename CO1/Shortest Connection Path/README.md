Shortest Connection Path

Description

This project contains a Python script that implements the Shortest Path algorithm using Dijkstra's Algorithm to find the shortest connection between two locations. The locations are represented as a weighted graph, where each connection has a distance in kilometers.

Algorithm

The script uses a shortest_path(graph, start, destination) function to find the shortest route efficiently. The step-by-step algorithm is as follows:

Initialize Distances: Set the distance of the starting location to 0 and the distance of all other locations to infinity.

Initialize Previous Locations: Store the previous location for each node so that the complete shortest route can be reconstructed later.

Create Priority Queue: Add the starting location to a priority queue with distance 0.

Select Closest Location: Remove the location with the smallest known distance from the priority queue.

Check Connections: Examine all locations directly connected to the current location.

Calculate New Distance: Add the distance from the current location to the neighboring location to the current shortest distance.

Update Distance: If the new distance is smaller than the previously known distance, update the distance and store the current location as the previous location.

Repeat: Continue selecting the closest unvisited location and updating its neighboring locations until the destination is reached.

Construct Path: Starting from the destination, follow the previous locations backward until reaching the starting location. Reverse the result to obtain the shortest route.

Not Found: If the destination cannot be reached, display a message indicating that no connection was found.

Input and Output

Input

Available locations:
Vijayawada, Guntur, Amaravati, Machilipatnam, Tenali, Narasaraopet, Mangalagiri, Gudivada

Enter starting location: Vijayawada

Enter destination: Mangalagiri

Output

Shortest connection path:
Vijayawada -> Amaravati -> Mangalagiri

Total distance: 30 km
