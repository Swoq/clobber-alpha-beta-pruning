# ABC (Artificial Bee Colony) algorithm for solving TSP
Implementation of the Artificial Bee Colony algoritm for solving - **Traveling Salesman Problem** (heuristic)
## Get started
* `git clone https://github.com/Swoq/TSP-ABC-algorithm.git`
* `cd TSP-ABC-algorithm`
* `python tsp.py {cities_number} {employed_bees} {onlooker_bees} {iterations}`
## Usage
### tsp.py
Python script to solve **TSP** using ABC algorithm. The algorithm does not guarantee an exact solution, it's heuristic.
It accepts **4** parameters.
` python tsp.py [cities_number] [employed_bees] [onlooker_bees] [iterations]`
* `cities_number` —  dimension of the problem, number of nodes in the graph or number of cities to visit by salesman.
* `employed_bees` —  number of employed_bees in the ABC algorithm (number of solutions to improve at the same time)
* `onlooker_beesa` - number of onlooer_bees in the second phase of the algorithm. (Onlooker bee - the bee which tries to improve current solution via checking nearby solutions)
* `iterations` - number of iterations of the ABC algorithm. The bigger number the better solution algorithm will produce.
## Contributors
Mykhailo Kratiuk (Telegram: #Swoqe)
