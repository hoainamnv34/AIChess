import pygame
import sys
from game import *
from const import *
from time import sleep, time
from ChessEngine import Engine2
from chess_engine import Engine
from ai import AI
import time
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGH))
        pygame.display.set_caption('Chess') 
        self.game = Game()
        self.clock = pygame.time.Clock()
        
    
    def mainloop(self):
        
        self.clock.tick(100)
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = game.board
        

        # test
        
        
         
        # Qb3 Qf6
        # e5 Qg6
        # Re1 Nge7
        
        engine = AI(3) 
          
        running = True
        
        play = False
        
        
        
        while running:
            self.clock.tick(100)
            game.show_bg(screen)
            
            if(dragger.draggging):
                game.show_move(screen) 
                
            game.show_last_move(screen) 

            if(dragger.draggging):
                game.show_move(screen) 

            game.show_hover(screen)
            

            game.show_pieces(screen)
            
            
            # if not play:
    
            #     pygame.display.flip()
                
            #     try:
            #         # engine1 = Engine(board.fen())
            #         # board.push(engine1.calculate_ab(4))
            #         # board.push(engine.calculate_ab(board.fen()))

            #     except:
            #         print("xxxx")
                
                
            #     play = True
            
            if play:
                # engine = ChessEngine.Engine(board, 3) 
                # board.push(engine.getBestMove())
                pygame.display.flip()
                try:
                    # engine2 = Engine2(board, 4)
                    # board.push(engine2.engine(None, 0))
                    board.push(engine.calculate_ab(board.fen()))
        

                except:
                    print("except")
                play = False
            
            
            if(dragger.draggging):
                # print('yes')
                game.update_blit(screen)
            
            
            # game.show_pieces(screen)
            
            
            # time.sleep(5)
            
            # if play:
            #     # engine = ChessEngine.Engine(board, 3) 
            #     # board.push(engine.getBestMove())
                
            #     engine = AI(board, 4)
            #     try:
            #         board.push(engine.calculate_ab())

            #     except:
            #         print("xxxx")
            #     play = False
            
            
            # while time.time() - km < 5:
            #     pass
            
            # game.show_bg(screen)
            # game.show_pieces(screen)
            
            
            # while not play:
                
            #     engine = AI(board, 1)
            #     try:
            #         board.push(engine.calculate_ab(1))

            #     except:
            #         print("xxxx")
                    
            #     # engine = ChessEngine.Engine(board, 3) 
            #     # board.push(engine.getBestMove())
            #     play = True
        
            if board.is_game_over():
                time.sleep(2)
                running = False
                print(board.result())    
                 
            for event in pygame.event.get():
                #click                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    # print('click {}'.format(event.pos))
                    print(dragger.mouse_square)
                    
                    
                    if board.piece_at(Const.colRowToIndex(dragger.mouse_square)):
                        
                        dragger.save_initial(event.pos)
                        # print(dragger.initial)
                        pos = Const.colRowToIndex(dragger.initial)
                        # print(pos)
                        piece = board.piece_at(pos)
                        
                        # print(chess.piece_name(piece.piece_type))
                        
                        dragger.drag_piece(piece)
        
    
        
                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion = event.pos
                    game.set_hover(motion)
                    
                    if dragger.draggging: 
                        dragger.update_mouse(event.pos) 
                        game.update_blit(screen)

                        
                        # print('den day')
                
                #click release
                elif event.type == pygame.MOUSEBUTTONUP :
                    
                    
        
                    initial = Const.colRowToIndex(dragger.initial)
                    released = Const.colRowToIndex(dragger.mouse_square)
                    
                    from_square = chess.SQUARE_NAMES[initial]
                    to_square = chess.SQUARE_NAMES[released]
                    
                    try:
                        move = chess.Move.from_uci(from_square + to_square)
                    except:
                        move = None
                        print('exception')
                    
                    if move in game.legal_move_from_square():
                        game.play_sound(board.is_capture(move))
                        board.push(move)
                        play = True
                       
                    #pawn promotion
                    try:
                        move = chess.Move.from_uci(from_square + to_square + 'q')
                    except:
                        pass
                    
                    if move in game.legal_move_from_square():

                        # #en passant capture
                        game.play_sound(True)
                        board.push(move)
                        play = True
                        
                    dragger.undrag_piece()
                    bt = True
                    game.show_pieces(screen)
                    
                                    
                    
                # key press
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        game.change_theme()
                    
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        screen = self.screen
                        dragger = self.game.dragger
                    if event.key == pygame.K_z:
                        # update later
                        game.undo_move()
                
                                   
                #quit application
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
            # game.show_pieces(screen)
            # pygame.display.update()
            
            
            # if bt:
            #     k = input("hellloo")
                  
                        
                        
            # game.show_pieces(screen)
            
            # while play:
            #     # engine = ChessEngine.Engine(board, 3) 
            #     # board.push(engine.getBestMove())
                
            #     engine = AI(board, 4)
            #     try:
            #         board.push(engine.calculate_ab(4))

            #     except:
            #         print("xxxx")
            #     play = False            
            
            # pygame.display.update()
            pygame.display.flip()
                    
main = Main()
main.mainloop()  