## Minimax Algorithm and Alpha-Beta Pruning

The objective of this project is to create adversarial agents that can beat other agents in a game called 2 Queens Isolation. An adversarial search agent is one that plans ahead in a world where other agents are planning against them.

In this game, there are two players, four game pieces and a 7-by-7 grid of squares.
At the beginning of the game, the first player places both the pieces on any two different squares. From that point on, the players alternate turns moving both the pieces like a Queen in chess (any number of open squares vertically,
horizontally, or diagonally). When the piece is moved, the square that was previously occupied is blocked. That square can not be used for the remainder of the game. The piece can not move through blocked squares.
The first player who is unable to move any one of the queens loses.

The goal is to implement the following parts of the agent in the class CustomPlayer:

1. Evaluation functions (OpenMoveEvalFn() and CustomEvalFn())
2. The minimax algorithm (minimax())
3. Alpha-beta pruning (alphabeta())

### Open Move Eval Function

The Open Move Evaluation function outputs a score equal to how many moves are open for my AI player minus how many moves are open for the opponent's player on the board. The evaluation function determines a score for every board state in the tree formed by the minimax algorithm.

### Minimax Algorithm

Minimax is a backtracking algorithm that is used to find the most optimal move for an agent assuming that the opponent is also playing optimally. The algorithm creates a tree recursively of two players: a maximizer and a minimizer. The maximizer generates all possible moves for your agent, when it is your turn. It tries to get your agent the highest evaluation function possible. The minimizer, on the other hand, generates the hypothetical moves that the opponent will take. The minimizer step assumes that the opponent will make the move that hurt your agent the most, and hence, picks the move that minimizes the evaluation function the most. 
The algorithm runs the maximizer and minimizer upto a certain depth, and then returns the best possible move for the maximizer. The tree below shows how the algorithm picks a move.
