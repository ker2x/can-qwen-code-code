import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Double Pendulum Chaos Demonstration")

# Colors
BACKGROUND = (10, 10, 30)
PENDULUM_COLORS = [
    (255, 100, 100),  # Red
    (100, 255, 100),  # Green
    (100, 100, 255),  # Blue
    (255, 255, 100),  # Yellow
    (255, 100, 255),  # Magenta
    (100, 255, 255),  # Cyan
]
TRAIL_COLORS = [
    (255, 50, 50, 100),
    (50, 255, 50, 100),
    (50, 50, 255, 100),
    (255, 255, 50, 100),
    (255, 50, 255, 100),
    (50, 255, 255, 100),
]
TEXT_COLOR = (200, 200, 220)

# Physics parameters
G = 9.81
L1, L2 = 150, 150
M1, M2 = 20, 20

# Clock for controlling frame rate
clock = pygame.time.Clock()


class Pendulum:
    def __init__(self, theta1, theta2, color_idx=0):
        self.theta1 = theta1
        self.theta2 = theta2
        self.theta1_dot = 0
        self.theta2_dot = 0
        self.color_idx = color_idx
        self.trail = []
        self.max_trail_length = 500

    def update(self):
        # Calculate derivatives using equations of motion for double pendulum
        dt = 0.05

        # More accurate equations of motion for double pendulum
        # This uses the Lagrangian approach for better physics
        theta1_ddot = (-G * (2 * M1 + M2) * math.sin(self.theta1)
                       - M2 * G * math.sin(self.theta1 - 2 * self.theta2)
                       - 2 * math.sin(self.theta1 - self.theta2) * M2 * (
                                   self.theta2_dot ** 2 * L2 + self.theta1_dot ** 2 * L1 * math.cos(
                               self.theta1 - self.theta2)))
        theta1_ddot /= (L1 * (2 * M1 + M2 - M2 * math.cos(2 * self.theta1 - 2 * self.theta2)))

        theta2_ddot = (2 * math.sin(self.theta1 - self.theta2) * (
                    self.theta1_dot ** 2 * L1 * (M1 + M2)
                    + G * (M1 + M2) * math.cos(self.theta1)
                    + self.theta2_dot ** 2 * L2 * M2 * math.cos(self.theta1 - self.theta2)))
        theta2_ddot /= (L2 * (2 * M1 + M2 - M2 * math.cos(2 * self.theta1 - 2 * self.theta2)))

        # Update angular velocities
        self.theta1_dot += theta1_ddot * dt
        self.theta2_dot += theta2_ddot * dt

        # Update angles
        self.theta1 += self.theta1_dot * dt
        self.theta2 += self.theta2_dot * dt

        # Add current position to trail
        x1 = L1 * math.sin(self.theta1)
        y1 = L1 * math.cos(self.theta1)
        x2 = x1 + L2 * math.sin(self.theta2)
        y2 = y1 + L2 * math.cos(self.theta2)

        # Fix coordinate system: invert y for Pygame and center on screen
        self.trail.append((x2 + WIDTH // 2, y2 + HEIGHT // 2))
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)

    def draw(self, surface):
        # Calculate positions
        x1 = L1 * math.sin(self.theta1)
        y1 = L1 * math.cos(self.theta1)
        x2 = x1 + L2 * math.sin(self.theta2)
        y2 = y1 + L2 * math.cos(self.theta2)

        # Draw trail
        if len(self.trail) > 1:
            for i in range(1, len(self.trail)):
                alpha = int(255 * i / len(self.trail))
                color = (*TRAIL_COLORS[self.color_idx][:3], alpha)
                pygame.draw.line(surface, color, self.trail[i - 1], self.trail[i], 2)

        # Draw pendulum
        # For Pygame coordinate system, we need to be consistent with y-inversion
        pygame.draw.line(surface, PENDULUM_COLORS[self.color_idx],
                         (WIDTH // 2, HEIGHT // 2),
                         (x1 + WIDTH // 2, y1 + HEIGHT // 2), 3)
        pygame.draw.line(surface, PENDULUM_COLORS[self.color_idx],
                         (x1 + WIDTH // 2, y1 + HEIGHT // 2),
                         (x2 + WIDTH // 2, y2 + HEIGHT // 2), 3)

        # Draw circles at joints
        pygame.draw.circle(surface, PENDULUM_COLORS[self.color_idx],
                           (WIDTH // 2, HEIGHT // 2), 8)
        pygame.draw.circle(surface, PENDULUM_COLORS[self.color_idx],
                           (x1 + WIDTH // 2, y1 + HEIGHT // 2), 8)
        pygame.draw.circle(surface, PENDULUM_COLORS[self.color_idx],
                           (x2 + WIDTH // 2, y2 + HEIGHT // 2), 8)


def main():
    # Create multiple pendulums with slightly different initial conditions
    # Initial conditions with pendulums hanging vertically up (pi/2 = 90 degrees)
    pendulums = []
    base_angles = [
        (math.pi/2, math.pi/2),  # Starting vertically up (90 degrees)
        (math.pi/2 + 0.01, math.pi/2),  # Slightly different
        (math.pi/2, math.pi/2 + 0.01),  # Slightly different
        (math.pi/2 + 0.02, math.pi/2 + 0.02),  # More different
        (math.pi/2 - 0.01, math.pi/2 - 0.01),  # Opposite direction
        (math.pi/2 + 0.05, math.pi/2 - 0.05),  # Different angles
    ]

    for i, angles in enumerate(base_angles):
        pendulums.append(Pendulum(angles[0], angles[1], i))

    # Font for text
    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset simulation
                    pendulums = []
                    for i, angles in enumerate(base_angles):
                        pendulums.append(Pendulum(angles[0], angles[1], i))
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Fill background
        screen.fill(BACKGROUND)

        # Draw title
        title = font.render("Double Pendulum Chaos Demonstration", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

        # Draw instructions
        instructions = font.render("Press R to reset, ESC to quit", True, TEXT_COLOR)
        screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT - 40))

        # Update and draw pendulums
        for pendulum in pendulums:
            pendulum.update()
            pendulum.draw(screen)

        # Draw legend
        legend_y = 60
        for i, angles in enumerate(base_angles):
            pygame.draw.circle(screen, PENDULUM_COLORS[i], (50, legend_y + i * 25), 8)
            text = font.render(f"Pendulum {i + 1}", True, TEXT_COLOR)
            screen.blit(text, (70, legend_y + i * 25 - 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()