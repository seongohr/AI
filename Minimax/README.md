<b>Introduction</b><br />
In this project, you will write a program to play an adversarial board game called the ​Laser Checkmate.​ Your program will generate one move at a time, taking turns against an AI opponent. Your goal is to win the game.<br /><br />

<b>Rules of the Game</b><br />
Laser Checkmate is a board game in which two players take turns placing laser emitters on a square ​N×​ ​N board. Each emitter shoots laser beams in eight directions: up, down, left, right, and all four diagonal directions. The beams travel up to 3 squares in each direction, but are unable to travel through walls (around the border of the grid) or blocks (occupying squares within the grid). The goal of the game is to place emitters so that your beams cover more squares than your opponent’s lasers do.<br /><br />
Figure 1 shows a 5×5 board with one laser emitter placed in the middle square. The black squares are blocks. The blue squares are covered by the emitter’s laser beams. In this example, the emitter covers 12 squares.<br /><br />

The other player can now place an emitter in only the white squares. However, once the players places a new laser emitter in a white square, its beams can travel through blue squares as well. In other words, coverage of a square is not mutually exclusive, and a square can be covered by both players at the same time.<br /><br />
The game terminates when there are no valid moves. The final score for each player is the number of squares that their laser beams cover, including the squares where their laser emitters are placed. The game winner is the one who has the higher score in the end.<br /><br />

<b>Valid Moves</b><br />
The players take turns placing laser emitters on the grid. On each player’s turn, a player places a new laser emitter on a square that contains no laser emitter, wall, or brick and that is not covered by any laser (from either player).<br /><br />
A move is specified by two numbers, a row number followed by a column number, each in the range 0 to ​N-​ 1, as illustrated in the 7​×​7 board below:<br /><br />

Figure 3 shows a board (​N​=7) after one move. There are blocks at (0,4), (2,5), and (6,2). The player has chosen (3,5) as the first move. The squares covered by this new laser emitter are colored blue. The laser beam traveling up is blocked at (2,5), so the emitter does not cover (0,5) or (1,5). Because the beams all have a range of 3 squares, the beam traveling left does not reach (3,0) or (3,1). Overall, there are 15 squares covered by this emitter, so the player is currently winning 15-0.<br /><br />

It is now the other player’s turn. Any squares not colored blue or black in Figure 3 are possible moves, so there are 31 moves to choose from. The player selects (1,2), and Figure 4 shows the resulting board. Squares covered by only this new emitter are colored red, while squares that are covered by both emitters are colored purple. The second player’s emitter covers 17 squares, so now the first player is losing 15-17.<br /><br />
<p>
  <img src="" width="300" title="">
</p>
