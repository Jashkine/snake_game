
class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW ################
        self.color = "cyan"                     #Snake color
        self.window_size = window_size
        self.width = window_size[0]
        self.height = window_size[1]
        self.offset = { "up": (0,20),
                        "down" :  (0,-20),
                        "left" :  (-20,0),
                        "right" :  (20,0)}
        self.shape = [[0,0],[0,20],[0,40]]      #Initial position and shape of Snake
        self.GAME_OVER = False
        self.direction = "up"                   #Inital snake direction

    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############
        if self.direction != 'down':    #When 'up' arrow is pressed, snake will move up if it is not moving down
            self.direction = 'up'
        ##########################################
    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'up':      #When 'down' arrow is pressed, snake will move down if it is not moving up
            self.direction = 'down'
        ##########################################

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'right':       #When 'left' arrow is pressed, snake will move left if it is not moving right
            self.direction = 'left'
        ##########################################

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'left':        #When 'right' arrow is pressed, snake will move right if it is not moving left
            self.direction = 'right'
        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """


        ############## WRITE BELOW ###############
        x1,y1 = self.shape[-1]                      #position of head of snake
        x2,y2 = current_food_position               #position of food
        distance = ((y2-y1)**2 + (x2-x1)**2)**0.5   #distance between food and snake head
        if distance<20:                             #Collision occur when distance is less than 20 pixels
            self.collision = True
            return True
        else:
            self.collision = False
            return False
        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """
        ############## WRITE BELOW ###############
        # The snippet below check if position each segment of the snake touches the boundary of the screen:
        # If yes then set its position as the opposite side of the boundary
        #This make the snake stay on the screen
        for i in range(len(self.shape)):
            if self.shape[-1+i][0] >= self.width/2:         #Check for right boundary
                self.shape[-1+i][0] = - self.width/2
            elif self.shape[-1+i][0] < -self.width/2:       #Check for left boundary
                self.shape[-1+i][0] = self.width/2
            elif self.shape[-1+i][1]>= self.height/2:       #Check for upper boundary
                self.shape[-1+i][1] = - self.height/2
            elif self.shape[-1+i][1]< -self.height/2:       #Check for lower boundary
                self.shape[-1+i][1] = self.height/2
            else:
                pass

        ##########################################

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """
        #assigning first segment of snake as its head
        new_head = self.shape[-1].copy()
        #Changing the head location to the next position of the first segment of snake
        new_head[0] = self.shape[-1][0] + self.offset[self.direction][0]
        new_head[1] = self.shape[-1][1] + self.offset[self.direction][1]

        ############## WRITE BELOW ###############
        #To update the snake position, we check the its collision with food
        #If collision with food occur, increase the snake length by appending head at front
        #Do not change the postition of other segment of snake

        if self.collision == True:
            self.shape.append((new_head))

        # If no collision with food occur, move the snake by one unit (20 pixels)
        elif self.collision ==False:
            for i in range(len(self.shape)-1):
                self.shape[i][0] = self.shape[i+1][0]
                self.shape[i][1] = self.shape[i+1][1]
            self.shape[-1][0] = new_head[0]
            self.shape[-1][1] = new_head[1]

            #game over
            #If snake collides with itself: set GAME_OVER = True
            for i in range(len(self.shape)-1):
                if self.shape[-1][0] == self.shape[i][0] and self.shape[-1][1] == self.shape[i][1]:
                    self.GAME_OVER = True
                    break






        ##########################################










