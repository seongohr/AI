<b>Introduction</b><br />
In this project, you will write a program to play an adversarial board game called the ​Laser Checkmate.​ Your program will generate one move at a time, taking turns against an AI opponent. Your goal is to win the game.<br /><br />

<b>Rules of the Game</b><br />
Laser Checkmate is a board game in which two players take turns placing laser emitters on a square ​N×​ ​N board. Each emitter shoots laser beams in eight directions: up, down, left, right, and all four diagonal directions. The beams travel up to 3 squares in each direction, but are unable to travel through walls (around the border of the grid) or blocks (occupying squares within the grid). The goal of the game is to place emitters so that your beams cover more squares than your opponent’s lasers do.<br /><br />
Figure 1 shows a 5×5 board with one laser emitter placed in the middle square. The black squares are blocks. The blue squares are covered by the emitter’s laser beams. In this example, the emitter covers 12 squares.<br /><br />
<p>
  <img src="" width="300" title="Figure1">
</p>

The other player can now place an emitter in only the white squares. However, once the players places a new laser emitter in a white square, its beams can travel through blue squares as well. In other words, coverage of a square is not mutually exclusive, and a square can be covered by both players at the same time.<br /><br />
The game terminates when there are no valid moves. The final score for each player is the number of squares that their laser beams cover, including the squares where their laser emitters are placed. The game winner is the one who has the higher score in the end.<br /><br />

<b>Valid Moves</b><br />
The players take turns placing laser emitters on the grid. On each player’s turn, a player places a new laser emitter on a square that contains no laser emitter, wall, or brick and that is not covered by any laser (from either player).<br /><br />
A move is specified by two numbers, a row number followed by a column number, each in the range 0 to ​N-​ 1, as illustrated in the 7​×​7 board below:<br /><br />
<p>
  <img src="" width="300" title="Figure2">
</p>


Figure 3 shows a board (​N​=7) after one move. There are blocks at (0,4), (2,5), and (6,2). The player has chosen (3,5) as the first move. The squares covered by this new laser emitter are colored blue. The laser beam traveling up is blocked at (2,5), so the emitter does not cover (0,5) or (1,5). Because the beams all have a range of 3 squares, the beam traveling left does not reach (3,0) or (3,1). Overall, there are 15 squares covered by this emitter, so the player is currently winning 15-0.<br /><br />
<p>
  <img src="" width="300" title="Figure3">
</p>

It is now the other player’s turn. Any squares not colored blue or black in Figure 3 are possible moves, so there are 31 moves to choose from. The player selects (1,2), and Figure 4 shows the resulting board. Squares covered by only this new emitter are colored red, while squares that are covered by both emitters are colored purple. The second player’s emitter covers 17 squares, so now the first player is losing 15-17.<br /><br />
<p>
  <img src="" width="300" title="Figure4">
</p>

It is now the first player’s move again. The only valid moves are the 19 white squares in Figure 4. The game continues until there are no valid moves left (i.e., no white squares).<br /><br />

<b>Your Task</b><br />
Your task is to write a program that can play the Laser Checkmate Board Game. Given a board in a game, your program needs to make an optimal move; in other words, your program must specify a square for your next laser emitter that will maximize your chances of winning.<br /><br />

<B>Input and Output Format</b><br />
Your program must not require any command-line arguments. It should read the input file named “input.txt” in the same directory that contains a problem definition. The output should be written to a file named “output.txt” with your chosen move to the same current directory. Format for the “input.txt” and “output.txt” files is specified below.<br /><br />
<b>Input:</b><br />
The file “input.txt” in the current directory of your program will be formatted as follows:<br /><br />
First line:​ strictly positive integer ​N,​ the width and height of the ​N​ x ​N​ grid.<br /><br />
Next ​N ​lines: ​a series of ​N digits representing each grid space. ​0 ​represents an empty space, ​1 represents one of your laser emitters, ​2 ​represents one of your opponent’s laser emitters, and ​3 represents a block.<br /><br />
The input file for the grid shown in Figure 2 would be:<br />
7<br />
0000300<br />
0000000<br />
0000030<br />
0000000<br />
0000000<br />
0000000<br />
0030000<br /><br />
<b>Output:</b><br />
Two integers separated by a space, indicating the coordinates (row followed by column) of the square where you choose to put your next laser emitter.<br /><br />
The output file for the move that produced the board in Figure 3 would be:<br />
3 5<br />
<b>Sample Input</b><br />
You are provided sample input files. The goal of the samples input is for you to check if your program can correctly and repeatedly parse the boards and generate moves to successfully complete a whole game of Laser Checkmate. The samples are representative of the grading test cases, but it should not be assumed that if your program works on the samples it will work on all grading test cases. It is your task to make sure that your program will work correctly on any valid input. Please note that the output of your program should match the specified format ​exactly.​ Failure to do so will most certainly lose points.<br />
