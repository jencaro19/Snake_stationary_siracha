class Snake:

    def __init__(self, xstart, ystart):
        self.head = xstart, ystart
        self.tail = [self.head]
        self.growing = 0
        self.direction = 'right'

    def grow(self):
        """Memorizes that the snake should grow when it moves next time"""
        ... # this is called a elipsis 

    def forward(self):
        """Moves the snake one step ahead"""
        ...

    def set_direction(self, direction):
        """Moves the head to a new direction"""
        ...

    def eat(self, playground):
        """Eats food at the position of the head, if any"""
        ...

    def check_collision(self, playground):
        """Returns True if the head hits an obstacle or the tail"""
        ...