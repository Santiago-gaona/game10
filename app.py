import streamlit as st
import time
import random

# Configuración de la pantalla
WIDTH, HEIGHT = 400, 600
BALLOON_SIZE = 40
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 30

# Clase del globo
class Balloon:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = 10
    
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH - BALLOON_SIZE:
            self.x += self.speed

# Clase de obstáculos
class Obstacle:
    def __init__(self):
        self.x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
        self.y = 0
        self.speed = 5
    
    def move(self):
        self.y += self.speed

# Función principal del juego
def run_game():
    st.write("### Juego del Globo")
    st.write("Usa las flechas izquierda y derecha para mover el globo y esquivar obstáculos.")
    
    balloon = Balloon()
    obstacles = []
    running = True
    
    while running:
        time.sleep(0.1)
        
        if random.randint(1, 50) == 1:
            obstacles.append(Obstacle())
        
        for obstacle in obstacles:
            obstacle.move()
            if (obstacle.y + OBSTACLE_HEIGHT > balloon.y and
                obstacle.x < balloon.x + BALLOON_SIZE and
                obstacle.x + OBSTACLE_WIDTH > balloon.x):
                running = False
        
        st.write(f"Posición del globo: {balloon.x}, {balloon.y}")
        st.write(f"Número de obstáculos: {len(obstacles)}")
    
    st.write("### ¡Game Over!")

# Streamlit UI
st.title("Juego del Globo en Streamlit")
if st.button("Iniciar Juego"):
    run_game()
