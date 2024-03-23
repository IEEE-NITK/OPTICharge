# OPTICharge

<br>
<details>
  <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#introduction">Introduction</a>
            <ul>
                <li><a href="#technologies-used">Technologies Used</a></li>
            </ul>
        </li>
        <li><a href="#literature-survey">Literature Survey</a>
        </li>
        <li><a href="#getting-started">Getting Started</a>
        </li>
         <li>
            <a href="#user-guide">User Guide</a>
            <ul>
                <li><a href="# Training & Testing">Training & Testing</a></li>
            </ul>
            <ul>
                <li><a href="# Evaluation & Visualization">Evaluation & Visualization</a></li>
            </ul>           
        </li>
        </li>
        <li><a href="#references">References</a> 
        </li>
        <li><a href="#project-mentors">Project Mentors</a></li>
        </li>
        <li><a href="#project-members">Project Members</a></li>
        </li> 
        <li><a href="#license">License</a></li>
        </li> 
    </ol>
</details>

<hr>

## Introduction
* OPTICHARGE,this is the application of reinforcement learning (RL) for battery fast-charging in the advanced battery management system (BMS). Using deep deterministic policy gradient (DDPG) algorithm, the RL agent is able to achieve fast-charging control strategy compared to existing model-based control strategies. In this repo, the RL results are reproduced by using the publicly available Lithium cobalt battery (LiCoO2) battery chemistry. Specifically, we present the RL agent in terms of state-feedback and output-feedback learning policy, which can be found in the sub-folders

* The primary objective of OPTICharge is to create a generalized BMS environment that ensures compatibility with a range of RL algorithms. By establishing a flexible framework, the project aims to facilitate seamless integration and evaluation of various RL techniques for BMS optimization. This adaptability is crucial given the diverse nature of RL algorithms and their applicability across different scenarios.
Subsequently, the project focuses on implementing and evaluating RL algorithms within the developed BMS environment. Specifically, the Deep Q-Network (DQN), Advantage Actor-Critic (A2C), and Deep Deterministic Policy Gradient (DDPG) algorithms will be deployed and rigorously assessed. These algorithms offer distinct approaches to reinforcement learning, providing insights into their efficacy in addressing the complex challenges of balancing State of Charge (SOC) and temperature within battery cells.
* A critical aspect of the OPTICharge project involves conducting a comprehensive performance comparison among the deployed RL algorithms. Through rigorous experimentation and analysis, each algorithm's capability in optimizing SOC and temperature will be thoroughly investigated. This comparative evaluation will yield valuable insights into the strengths and weaknesses of each algorithm, guiding the selection of the most promising candidates for further optimization.
* In summary, the OPTICharge project embarks on a multidimensional exploration of BMS optimization through RL algorithms. By developing a generalized BMS environment, implementing and evaluating various RL techniques, conducting a comprehensive performance comparison, and optimizing the most promising algorithms, OPTICharge seeks to advance the state-of-the-art in electric vehicle battery management. Through these endeavors, the project endeavors to pave the way for more efficient, reliable, and sustainable electric vehicle technologies.

## Objectives
* Develop a Generalized BMS Environment: Ensure compatibility with various RL algorithms.
* Implement & Evaluate RL Algorithms: Deploy DQN, A2C and PPO on the developed environment.
* Performance Comparison: Investigate each algorithm’s capability in balancing SOC and temperature.
* Optimization: Fine-tune the most promising algorithm(s) for enhanced performance.

## Technologies used
[![Tech_Used](https://skills.thijs.gg/icons?i=py)](https://skills.thijs.gg)
### Requirements
* Python 3.7 (it might work with Python 2, but I didn't test it)
* PyTorch 1.2.0
* OpenAI baselines

## Literature Survey

### Reinforcement Learning:

Reinforcement learning is a branch of machine learning that deals with decision-making processes where an agent learns to make sequential decisions by interacting with its environment. This section provides an overview of RL fundamentals, emphasizing key concepts such as state, action, reward, and the learning process through exploration and exploitation.

* Agent: The entity that makes decisions and takes actions within an environment.
    Role: The agent learns to perform tasks or achieve goals by interacting with the environment
* Environment: The external system or context in which the agent operates.
    Role: The environment provides feedback to the agent based on its actions and influences the state transitions
* State: A representation of the current situation or configuration of the environment.
    Role: States are crucial for decision-making, as they determine the information available to the agent at a given moment.
* Action:  The set of possible moves or decisions that an agent can take in a particular state.
    Role: Actions influence the state transitions and, consequently, the rewards received by the agent.
* Policy: A strategy or mapping from states to actions, representing the agent's decision-making strategy.
    Role: The policy guides the agent in choosing actions in different states to maximize expected cumulative rewards.
* Reward:  A numerical signal provided by the environment as feedback for the agent's actions.
    Role: Rewards serve as a reinforcement signal, guiding the agent to learn behaviors that lead to favorable outcomes.
* Value function: A function that estimates the expected cumulative future rewards associated with being in a particular state or taking a specific action.
    Role: Value functions help the agent evaluate the desirability of different states or actions, aiding in decision-making.
* Q-Value function: The expected cumulative future rewards of taking a particular action in a given state.
    Role: Q-values are crucial for determining the best action to take in a specific state and are often used in algorithms like Q-learning.

### Battery System Optimization:

Understanding the challenges associated with battery systems is essential for developing effective optimization strategies. This section examines common challenges, including battery degradation, charge/discharge control, and the impact of varying operating conditions on overall system performance.
An overview of current battery management systems is provided, emphasizing the limitations and areas where improvements are needed. This section sets the stage for discussing how RL can be integrated into existing BMS to overcome these limitations and optimize battery operations.


* Prevailing DDPG Application: Deep Deterministic Policy Gradient (DDPG) is a dominant choice for SOC and temperature management in Battery Management Systems (BMS) using Reinforcement Learning (RL).

* Alternate RL Algorithms: Other RL algorithms like DQN and A2C have demonstrated potential in diverse control scenarios, suggesting potential applicability in BMS.

* Research Gap in EV Context: Existing literature lacks dedicated, comparative studies of these algorithms within the context of BMS specifically tailored for Electric Vehicles (EVs), a domain demanding high reliability, safety, and energy efficiency.

* Objective of OptiCharge: This project aims to bridge this gap, offering a comprehensive evaluation of these RL algorithms for BMS in EV applications, providing crucial insights for the EV industry's future R&D initiatives.

  ### 

## Getting Started


## User Guide

* In the "settings_file.py" for each folder, the training settings and constraints are defined. For RL training configuration, the hyper-paramters are defined in "model.py".

* You can simply run the code and reproduce the results in the folder by following:

* You can try with different parameter initialization using additional argument, i.e., --id 0, --id 1, ...

## Training & Testing

* python main_training_testing_output_fdbk.py --id 0
* python main_training_testing_state_fdbk.py --id 0
* After training the RL agent, one can evaluate the performance of RL controller by executing notebook:

## Evaluation & Visualization
* jupyter notebook
* Launch the notebook file (.ipynb) in the sub-folder for deeper analysis.
* Figures and Results are saved in "figures" in each subfolders of the repository. The figures in the manuscript are different from repository results because the battery model is adopted from company-owned battery parameters.

## References
1.[Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto](http://incompleteideas.net/book/RLbook2020.pdf)

2.[Deep Reinforcement Learning with Python (DQN and variants) - Article](https://towardsdatascience.com/deep-reinforcement-learning-build-a-deep-q-network-dqn-to-play-cartpole-with-tensorflow-2-and-gym-8e105744b998)

3.[Reinforcement Learning for Optimal Control of Battery Charging](https://ieeexplore.ieee.org/document/10202845/footnotes#footnotes)

4.[Creating an Environment for RL](https://towardsdatascience.com/create-your-own-reinforcement-learning-environment-beb12f4151ef)

5.[RL — Reinforcement Learning Algorithms Comparison](https://jonathan-hui.medium.com/rl-reinforcement-learning-algorithms-comparison-76df90f180cf)


## Project Mentors
* Pooja M
* Priyanshu Bhandari
## Project Members
* Likith Raj A
* Rahul Gupta
* Shankaragouda
* Suksha Kiran
  
## License
This repository is licensed under the [MIT LICENSE](https://github.com/IEEE-NITK/OPTICharge/blob/main/LICENSE)



