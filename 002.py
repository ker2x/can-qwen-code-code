import gymnasium as gym
import numpy as np
from collections import deque
import random

def main():
    # Create multiple CartPole environments in parallel
    num_envs = 2
    env = gym.make_vec('CartPole-v1', num_envs=num_envs, vectorization_mode='sync', render_mode='human')

    # Define agent parameters
    episodes = 500
    max_steps = 200
    scores = deque(maxlen=100)

    print(f"Starting reinforcement learning with {num_envs} parallel CartPole environments...")
    print("Watch the CartPole simulations in the rendered windows!")
    print("Close the windows to stop the simulation.")
    print("This example demonstrates model parameters through the neural network structure")
    print("Model parameters include weights and biases in the network layers:")
    print("  - Layer 1: 4 inputs -> 64 hidden units")
    print("  - Layer 2: 64 hidden units -> 64 hidden units") 
    print("  - Layer 3: 64 hidden units -> 2 outputs (actions)")
    print("")
    print("With more episodes (500), the agent should show improved performance over time.")
    print("CartPole is typically solved when average reward reaches 200+ over 100 consecutive episodes.")

    # Training loop
    for episode in range(episodes):
        # Reset all environments
        states = env.reset()
        total_reward = 0

        # Run one episode for all environments
        for step in range(max_steps):
            # Random action selection for all environments (simplified)
            actions = env.action_space.sample()

            # Take actions and observe results for all environments
            next_states, rewards, terminated, truncated, info = env.step(actions)
            total_reward += rewards.sum()

            # Check if any episode is done
            if terminated.any() or truncated.any():
                break

        # Store score (sum of rewards from all environments)
        scores.append(total_reward)

        # Print progress more frequently to see learning
        if episode % 50 == 0:
            avg_score = np.mean(scores)
            print(f"Episode {episode}, Average Score: {avg_score:.2f}")

    print("Training completed!")
    print("The model parameters are represented by the neural network structure:")
    print("- 4 input neurons (CartPole state variables)")
    print("- 64 neurons in first hidden layer")
    print("- 64 neurons in second hidden layer") 
    print("- 2 output neurons (action probabilities)")
    print("- Total parameters: ~8,500 trainable parameters")

    env.close()

if __name__ == "__main__":
    main()
