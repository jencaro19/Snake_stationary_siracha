from spicy_snake.move_snake import move

class Snake:

    def __init__(self, xstart, ystart):
        self.head = xstart, ystart
        self.tail = [self.head]
        self.growing = 0
        self.direction = 'right'

    def forward(self):
        """Moves the snake one step ahead"""
        self.head = move(self.head, self.direction) # no need to return the move def already retunrs new position
        self.tail.append(self.head) # need the tail to move with the head --> it is a new position
        if self.growing == 0:   # double ended queue
            self.tail.pop(0)
        else:
            self.growing -= 1
    
    def grow(self):
        """Memorizes that the snake should grow when it moves next time"""
        #... # this is called an unnecessary elipsis when running a pytest  
        self.growing += 1

    def set_direction(self, direction):
        """Moves the head to a new direction"""
        self.direction = direction

    def eat(self, playground):
        """Eats food at the position of the head, if any"""
        if playground.food == self.head:
            self.grow()
            playground.food = None #once eten it removes the food

    def check_collision(self, playground):
        """Returns True if the head hits an obstacle or the tail"""
        if playground.is_obstacle(self.head):
            return True
        else:
            # check tail-collisions
            return self.head in self.tail[:-1] # makes a copy of the tail 