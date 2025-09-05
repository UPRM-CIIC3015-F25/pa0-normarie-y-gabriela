from tkinter import font

import pygame, sys, random

def ball_movement():
    """
    Handles the movement of the ball and collision detection with the player and screen boundaries.
    """
    global ball_speed_x, ball_speed_y, score, start, high_score, difficulty_level, losing_screen

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Start the ball movement when the game begins
    # TODO Task 5 Create a Merge Conflict
    speed = 1
    if start:
        ball_speed_x = speed * random.choice((-2, 7))  # Randomize initial horizontal direction
        ball_speed_y = speed * random.choice((-2, 2))  # Randomize initial vertical direction
        start = False

    # Ball collision with the player paddle
    if ball.colliderect(player) or ball.colliderect(player_2):
        if abs(ball.bottom - player.top) < 10 or abs(ball.bottom - player_2.top) < 10:  # Check if ball hits the top of the paddle
            # Task 2: Fix score to increase by 1
            score += 1  # Increase player score- Normarie
            #high score system
            if score > high_score:
                high_score = score


            ball_speed_y *= -1  # Reverse ball's vertical

            # TODO Task 6: Add sound_effects HERE
            pygame.init()
            pygame.mixer.init()

            paddle_sfx1 = pygame.mixer.Sound("sound_effects/wheee.wav")
            paddle_sfx2 = pygame.mixer.Sound("sound_effects/whooo.wav")
            paddle_sounds = [paddle_sfx1, paddle_sfx2]

            random_sfx = random.choice(paddle_sounds)
            random_sound = pygame.mixer.Sound.play(random_sfx)

            # difficulty levels
            ball_speed_x *= 1.2
            ball_speed_y *= 1.2
            difficulty_level += 1 # we increased difficulty each time the score increases by one
                #restart difficulty

    # Ball collision with top boundary
    if ball.top <= 0:
        ball_speed_y *= -1  # Reverse ball's vertical direction

    # Ball collision with left and right boundaries
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # Ball goes below the bottom boundary (missed by player)
    if ball.bottom > screen_height:
        losing_screen = True


def player_movement():
    """
    Handles the movement of the player paddle, keeping it within the screen boundaries.
    """
    player.x += player_speed  # Move the player paddle horizontally
    player_2.x += player2_speed #player two movement

    # Prevent the paddle from moving out of the screen boundaries
    if player.left <= 0:
        player.left = 0
    if player.right >= screen_width:
        player.right = screen_width
    #PLayer 2
    if player_2.left <= 0:
        player_2.left = 0
    if player_2.right >= screen_width:
        player_2.right = screen_width

def restart():
    """
    Resets the ball and player scores to the initial state.
    """
    global ball_speed_x, ball_speed_y, score, difficulty_level, show_menu, losing_screen
    ball.center = (screen_width / 2, screen_height / 2)  # Reset ball position to center
    ball_speed_y, ball_speed_x = 0, 0  # Stop ball movement
    score = 0  # Reset player score
    difficulty_level = 0

# General setup
pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
clock = pygame.time.Clock()

# Main Window setup
screen_width = 900  # Screen width (can be adjusted)
screen_height = 700  # Screen height (can be adjusted)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong 33')  # Set window title
#Start Screen
start_screen_image = pygame.image.load('start_up.png')  #the menu of pong 33
start_screen_image = pygame.transform.scale(start_screen_image, (screen_width, screen_height)) #fit
#Losing Screen
losing_screen_image = pygame.image.load('expedition_failed.png')  #the menu of pong 33
losing_screen_image = pygame.transform.scale(losing_screen_image, (screen_width, screen_height)) #fit
# Colors
bg_color = pygame.Color('grey12')

# Game Rectangles (ball and player paddle)
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)  # Ball (centered)
# TODO Task 1 Make the paddle bigger
player_height = 15
player_width = 200
player = pygame.Rect(screen_width/2 - 45, screen_height - 20, player_width, player_height)  # Player 1 paddle

#BONUS: multiplayer
player_2_height = 15
player_2_width = 100
player_2 = pygame.Rect( 45, screen_height - 20, player_width, player_height)  # Player 2 paddle


# Game Variables
ball_speed_x = 2 #edit the speed in each direction to increase difficulty
ball_speed_y = 2
player_speed = 0
player2_speed = 0
# Score Text setup
score = 0
high_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 25)  # Font for displaying score
difficulty_level = 0
show_menu = True #shows the menu
start = False  # Indicates if the game has started
losing_screen = False #indicarted when player fails

# Main game loop
while True:
    # Event handling
    # TODO Task 4: Add your name
    name = "Normarie Martinez"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed -= 6  # Move paddle left
            if event.key == pygame.K_RIGHT:
                player_speed += 6  # Move paddle right
            if event.key == pygame.K_SPACE:
                show_menu = False # Hide the menu of Pong 33
                start = True  # Start the ball movement
            if event.key == pygame.K_y:
                losing_screen = False  # Hide Losing Screen
                show_menu = True # Show the menu of Pong 33
                restart()  # Reset the game

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT:
                player_speed += 6  # Stop moving left
            if event.key == pygame.K_RIGHT:
                player_speed -= 6  # Stop moving right
        #player 2 movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player2_speed -=6 # player two movement
            if event.key == pygame.K_d:
                player2_speed += 6  # player two movement
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_a:
                player2_speed += 6  # player two movement
            if event.key == pygame.K_d:
                player2_speed -= 6  # player two movement
    # Trying to display the menu screen
    if show_menu == True:
        # Show the start screen
        screen.blit(start_screen_image, (0, 0))
        pygame.display.flip()
        continue  # It keeps showing the menu until the space is pressed
    # After game menu
    if losing_screen == True:
        screen.blit(losing_screen_image, (0, 0))
        pygame.display.flip()
        continue  # keeps the losing screen

    # Game Logic
    ball_movement()
    player_movement()

    # Visuals
    light_grey = pygame.Color('grey83')
    red = pygame.Color('red')
    yellow = pygame.Color('yellow')
    screen.fill(bg_color)  # Clear screen with background color
    pygame.draw.rect(screen, light_grey, player)  # Draw player 1 paddle
    pygame.draw.rect(screen, light_grey, player_2)  # Draw player 2 paddle
    # TODO Task 3: Change the Ball Color
    pygame.draw.ellipse(screen, yellow, ball)  # Draw ball
    player_text = basic_font.render(f'Score:{score}', False, light_grey)  # Render player score
    player_high_score = basic_font.render(f'High score: {high_score}', False, light_grey)  # Render player score
    screen.blit(player_text, (screen_width/ 1.5 -15, 10))  # Display score on screen
    screen.blit(player_high_score, (screen_width /  100 , 10))  # Display score on screen

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 frames per second