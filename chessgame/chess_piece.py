class ChessPiece:
    selected = False
    is_king = False

    def __init__(self, x, y, is_red, direction):
        self.x = x
        self.y = y
        self.is_red = is_red
        self.direction = direction

    def is_north(self):
        return self.direction == 'north'

    def is_south(self):
        return self.direction == 'south'

    def get_move_locs(self, board):
        moves = []
        for x in range(9):
            for y in range(10):
                if (x, y) in board.pieces and board.pieces[x, y].is_red == self.is_red:
                    continue
                if self.move(board, x - self.x, y - self.y):
                    moves.append((x, y))
        return moves

    def move(self, board, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if (nx, ny) in board.pieces:
            board.remove(nx, ny)
        board.remove(self.x, self.y)
        # print 'Move a chessman from (%d,%d) to (%d,%d)'%(self.x, self.y, self.x+dx, self.y+dy)
        self.x += dx
        self.y += dy
        board.pieces[self.x, self.y] = self
        return True

    def count_pieces(self, board, x, y, dx, dy):
        sx = dx / abs(dx) if dx != 0 else 0
        sy = dy / abs(dy) if dy != 0 else 0
        nx, ny = x + dx, y + dy
        x, y = x + sx, y + sy
        cnt = 0
        while x != nx or y != ny:
            if (x, y) in board.pieces:
                cnt += 1
            x += sx
            y += sy
        return cnt


class Che(ChessPiece):

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RRS.gif"
            else:
                return "images/BRS.gif"
        else:
            if self.is_red:
                return "images/RR.gif"
            else:
                return "images/BR.gif"

    def get_selected_image(self):
        if self.is_red:
            return "images/RRS.gif"
        else:
            return "images/BRS.gif"

    def can_move(self, board, dx, dy):
        if dx != 0 and dy != 0:
            # print 'no diag'
            return False
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print 'blocked by yourself'
                return False
        cnt = self.count_pieces(board, self.x, self.y, dx, dy)
        # print 'Che cnt', cnt
        if (nx, ny) not in board.pieces:
            if cnt != 0:
                # print 'blocked'
                return False
        else:
            if cnt != 0:
                # print 'cannot kill'
                return False
            print('kill a chessman')
        return True


class Bing(ChessPiece):

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RPS.gif"
            else:
                return "images/BPS.gif"
        else:
            if self.is_red:
                return "images/RP.gif"
            else:
                return "images/BP.gif"

    def get_selected_image(self):
        if self.is_red:
            return "images/RPS.gif"
        else:
            return "images/BPS.gif"

    def can_move(self, board, dx, dy):
        if abs(dx) + abs(dy) != 1:
            # print('Too far')
            return False
        if (self.is_north() and dy == -1) or (self.is_south() and dy == 1):
            # print('cannot go back')
            return False
        if dy == 0:
            if (self.is_north() and self.y < 5) or (self.is_south() and self.y >= 5):
                # print('behind river')
                return False
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print('blocked by yourself')
                return False
            else:
                pass
                # print 'kill a chessman'
        return True


class Ma(ChessPiece):

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RNS.gif"
            else:
                return "images/BNS.gif"
        else:
            if self.is_red:
                return "images/RN.gif"
            else:
                return "images/BN.gif"

    def get_selected_image(self):
        if self.is_red:
            return "images/RNS.gif"
        else:
            return "images/BNS.gif"

    def can_move(self, board, dx, dy):
        x, y = self.x, self.y
        nx, ny = x + dx, y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if dx == 0 or dy == 0:
            # print 'no straight'
            return False
        if abs(dx) + abs(dy) != 3:
            # print 'not normal'
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print 'blocked by yourself'
                return False
        if (x if abs(dx) == 1 else x + dx / 2, y if abs(dy) == 1 else y + (dy / 2)) in board.pieces:
            # print 'blocked'
            return False
        return True


class Pao(ChessPiece):

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RCS.gif"
            else:
                return "images/BCS.gif"
        else:
            if self.is_red:
                return "images/RC.gif"
            else:
                return "images/BC.gif"

    def get_selected_image(self):
        if self.is_red:
            return "images/RCS.gif"
        else:
            return "images/BCS.gif"

    def can_move(self, board, dx, dy):
        if dx != 0 and dy != 0:
            # print 'no diag'
            return False
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print 'blocked by yourself'
                return False
        cnt = self.count_pieces(board, self.x, self.y, dx, dy)
        # print 'Pao cnt',cnt
        if (nx, ny) not in board.pieces:
            if cnt != 0:
                # print 'blocked'
                return False
        else:
            if cnt != 1:
                # print 'cannot kill'
                return False
        return True


class Xiang(ChessPiece):

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RBS.gif"
            else:
                return "images/BBS.gif"
        else:
            if self.is_red:
                return "images/RB.gif"
            else:
                return "images/BB.gif"

    def get_selected_image(self):
        if self.is_red:
            return "images/RBS.gif"
        else:
            return "images/BBS.gif"

    def can_move(self, board, dx, dy):
        x, y = self.x, self.y
        nx, ny = x + dx, y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print 'blocked by yourself'
                return False
        if (self.is_north() and ny > 4) or (self.is_south() and ny < 5):
            # print 'no river cross'
            return False

        if abs(dx) != 2 or abs(dy) != 2:
            # print 'not normal'
            return False
        sx, sy = dx / abs(dx), dy / abs(dy)
        if (x + sx, y + sy) in board.pieces:
            # print 'blocked'
            return False
        return True


class Shi(ChessPiece):

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RAS.gif"
            else:
                return "images/BAS.gif"
        else:
            if self.is_red:
                return "images/RA.gif"
            else:
                return "images/BA.gif"

    def get_selected_image(self):
        if self.is_red:
            return "images/RAS.gif"
        else:
            return "images/BAS.gif"

    def can_move(self, board, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print 'blocked by yourself'
                return False
        x, y = self.x, self.y
        if not (self.is_north() and 3 <= nx <= 5 and 0 <= ny <= 2) and \
                not (self.is_south() and 3 <= nx <= 5 and 7 <= ny <= 9):
            # print 'out of castle'
            return False
        if self.is_north() and (nx, ny) == (4, 1) or (x, y) == (4, 1):
            if abs(dx) > 1 or abs(dy) > 1:
                # print 'too far'
                return False
        if self.is_south() and (nx, ny) == (4, 8) or (x, y) == (4, 8):
            if abs(dx) > 1 or abs(dy) > 1:
                # print 'too far'
                return False
        # below modified by Fei Li
        if abs(dx) != 1 or abs(dy) != 1:
            # print 'no diag'
            return False
        return True


class Shuai(ChessPiece):

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)
        self.is_king = True

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RKS.gif"
            else:
                return "images/BKS.gif"
        else:
            if self.is_red:
                return "images/RK.gif"
            else:
                return "images/BK.gif"

    def get_selected_image(self):
        if self.is_red:
            return "images/RKS.gif"
        else:
            return "images/BKS.gif"

    def can_move(self, board, dx, dy):
        # print 'king'
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print 'blocked by yourself'
                return False
        if dx == 0 and self.count_pieces(board, self.x, self.y, dx, dy) == 0 and ((nx, ny) in board.pieces) and \
                board.pieces[nx, ny].is_king:
            return True
        if not (self.is_north() and 3 <= nx <= 5 and 0 <= ny <= 2) and not (
                self.is_south() and 3 <= nx <= 5 and 7 <= ny <= 9):
            # print 'out of castle'
            return False
        if abs(dx) + abs(dy) != 1:
            # print 'too far'
            return False
        return True
