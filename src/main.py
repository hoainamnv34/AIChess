import pygame
import sys
from game import *
from const import *
from time import time
from ai import AI
import time
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGH))
        pygame.display.set_caption('Chess') 
        self.game = Game()
        self.clock = pygame.time.Clock()
        self.engine = AI(3) 
        
        
    
    def mainloop(self):
        
        self.clock.tick(100)
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = game.board
          
        running = True
        player = True
        
    
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
            
            
            
            
            if not player:
                pygame.display.flip()
                try:
                    board.push(self.engine.calculate_ab(board.fen()))
                    print(board.fen())
                except:
                    print("exception")
                player = True
            
            
            if(dragger.draggging):
                game.update_blit(screen)
            
            
            if board.is_game_over():
                time.sleep(3)
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

                
                #click release
                elif event.type == pygame.MOUSEBUTTONUP :
                    
                    initial = Const.colRowToIndex(dragger.initial)
                    released = Const.colRowToIndex(dragger.mouse_square)
                    
                    from_square = chess.SQUARE_NAMES[initial]
                    to_square = chess.SQUARE_NAMES[released]
                    
                    try:
                        move = chess.Move.from_uci(from_square + to_square)
                        
                   
                        if move in game.legal_move_from_square():
                            game.play_sound(board.is_capture(move))
                            board.push(move)
                            player = False
                        
                        #pawn promotion
                        try:
                            move = chess.Move.from_uci(from_square + to_square + 'q')
                        except:
                            pass
                        
                        if move in game.legal_move_from_square():

                            # #en passant capture
                            game.play_sound(True)
                            board.push(move)
                            player = False
                            

                    except:
                        move = None
                        print('exception')
                        
                    dragger.undrag_piece()
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
        
            pygame.display.flip()
                    
main = Main()
main.mainloop()  