Problem Description
The virtual figure moves in a grid of size N * N, which means there are N * N square cells in the grid. There is a given cell or cells which contain(s) the cash rewards. In addition, there may be some cells containing walls. All other cells in the grid are empty. A typical grid is shown below:
 
 In the above example grid, the virtual figure’s current position is at square (1,1). There are two walls in this grid (squares (3,3) and (4,1)). There are two reward squares in this grid: (4,2) and (4,4).
At each non-reward state, the virtual figure has four possible moves: Up, Down, Left, or Right. At the terminal state, there is only one possible action: Exit.
Unfortunately, the environment in this game is stochastic, because sometimes wind may blow the virtual figure away from its intended direction. Whenever the virtual figure moves in a direction to an empty square, it successfully reaches that square with probability ​P.​ However, there is also a probability of (1 - ​P​)/2 that the figure will be blown off course either 45 degrees clockwise or 45 degrees counter-clockwise.
If the result of an action would move the virtual figure out of the grid, the virtual figure stays in its original cell. In the image below, the virtual figure attempts to move up from the top row in the grid, resulting in it remaining in its current position with probability 1:
 
  If the result of an action would move the virtual figure into a wall cell, the virtual figure also stays in its original cell. In the image below, the virtual figure attempts to move down, but there is a wall in the bottom right square surrounding it. Because there is a probability (1-P)/2 that the wind blows the figure into that wall, there is a (1-P)/2 probability that the figure ends up back in the current position:
On every turn, the virtual figure receives a reward R(s, a). For all non-reward squares, the reward for any movement action is:
R(s) = Rp
When performing the Exit action in a state with reward, ​Rt​ ,​ the corresponding reward is:
R(s) = Rt
 
 You are willing to play this game as long as it takes to get your money. On the other hand, you want to receive your money as soon as possible, so money received on your next turn is not always worth as much as money received right now, by a discount factor of 𝛾 (0≤𝛾≤1).
Given a grid, please determine the optimal move sequence for the virtual figure to follow from any square on the grid to maximize your winnings.
Input Format
You should read into the input parameters from a text file called “input.txt”. The file would be formatted as below:
<GRID SIZE>​ The first line contains a single integer N, indicating the size of the grid. <WALL STATES NUMBER>​ This line contains one integer M, indicating the number of wall cells in the grid.
<WALL STATES POSITION> ​The next M lines here are the coordinates of wall cells, each occupying one line. Each line has 2 integers separated by a comma “,” indicating the coordinates of the walls (row first, then column).
<TERMINAL STATES NUMBER> ​This line contains one integer T, indicating the number of terminal cells in the grid.
<TERMINAL STATES POSITION> ​The next T lines are the coordinates of terminal cells, each occupies one line. Each line has 3 integers separated by a comma “,”. The first two are the coordinates of the terminals (row first, then column), and the third value denotes the reward, Rt, received when exiting this square.
<TRANSITION MODEL> ​This line contains one floating-point number P, indicating the probability of moving as intended.
<REWARDS>​ This line contains one floating-point number indicating Rp.
<DISCOUNT FACTOR>​ This line contains a floating-point number 𝛾 in the interval [0,1] .
Output Format
<OPTIMAL ACTION GRID>​ The output file should contain N lines where each line includes N characters separated by commas (“,”). The j-th character at the i-th line should indicate the optimal action (one of “U”, “D”, “L” or “R” for non-reward states; “E” for reward states; “N” for wall states) at square (i, j).
● U: move up
● D: move down
● L: move left

● R: move right
● E: exit with the reward
● N: no actions in the wall state
Sample Input
5
2
4,2 1,4
2 5,3,10 3,5,5 0.7 -0.3 0.8
Sample Output
D,D,D,N,D R,D,D,D,D R,R,D,D,E D,N,D,D,L R,R,E,L,L
