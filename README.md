# MaximizarBeneficios_IA

## Practical case: Example of the use of Thompson sampling to maximize profits from an online sales business

### Problem to solve

Let's imagine an online retail business that has millions of customers. These customers are just people who buy some
products on the website from time to time and delivered to you at home (like Amazon). The business is doing well, but
the board of directors has decided to take some action plan to further maximize revenue. This plan consists of offering
customers the option to subscribe to a premium plan, which will give them some benefits such as reduced prices, offers
specials, etc. This premium plan is offered at an annual price of $ 100 and the goal of this online retail business
It is, of course, to get the maximum number of customers to subscribe to this premium plan. Discover the best strategy to
implementing will make the business maximize its additional income.

In this practical case we will face 9 different strategies, and our AI will have no idea which one is the best, and absolutely
no prior information on any of your conversion rates. These strategies were carefully developed and
by the marketing team, and each of them has the same goal: to convert the largest number of customers to the
premium plan. The 9 strategies are all different: they have different shapes, different packages, different
advertisements and different special offers to convince and persuade customers to subscribe to the premium plan. Of course,
the marketing team has no idea which of these 9 strategies is the best.

Instead of sending an email to your 100 million customers that would be expensive and they would risk ending up in spam,
the best strategy will be sought through online learning.

What is online learning? It will consist of implementing a strategy each time a client browses the website
of the business to hang out or buy some products. While the customer is browsing the website, they will suddenly receive
a pop-up ad, suggesting you subscribe to the premium plan. And for each customer who browses the website, only
will implement one of the 9 strategies. Then the user will choose, or not, to take action and subscribe to the premium plan. If he
customer subscribes, it is a success, otherwise it is a failure. The more customers do this, the more feedback we get
and we will have a better idea of what the best strategy is. Of course, we will not solve it manually,
visually or with some simple math. We will implement the smartest algorithm that finds out which
It is the best strategy in the shortest time possible.

#### Simulation

To simulate this Case Study, we will assume that these strategies have the following conversion rates. In a real life situation we would have no idea what these conversion rates would be. We only know about them here for simulation purposes, just so we can verify in the end that our AI manages to discover the best strategy, which according to the table below is strategy number 6 (the one with the highest conversion rate).

  
Strategy | Conversion Rate
---------| ----------------
0        | 0.05
1        | 0.13
2        | 0.09
3        | 0.16
4        | 0.11
5        | 0.04
6        | 0.20
7        | 0.08
8        | 0.01

### Definition of the environment

We have to define the rewards to build our reward matrix, where each row corresponds to a user who is implementing a strategy, and each column corresponds to one of the 9 strategies. Therefore, since we will actually run this e-learning experiment on 10,000 customers, this reward matrix will have 10,000 rows and 9 columns. Then each cell will get a 0 if the customer does not subscribe to the premium plan after being approached by the selected strategy, and a 1 if the customer subscribes after being approached by the selected strategy. And the values ​​in the cell are exactly, the rewards.

The reward matrix is ​​only here for simulation, and in real life we ​​would not have a reward matrix. We will simply simulate 10,000 clients being approached successively by one of the 9 strategies, and thanks to the rewards matrix we will simulate the client's decision to subscribe yes or no to the premium plan. If the cell for a specific customer and a specific selected strategy has a 1, that will simulate a conversion by the customer to the premium plan, and if the cell has a 0, it will simulate a rejection.

Thompson Sampling will collect feedback on whether each of these customers subscribe to the premium plan and thanks to its powerful algorithm, it will quickly discover the strategy with the highest conversion rate. This will be the strategy that will have to be implemented in the millions of clients, thus maximizing the company's income.

### AI solution

The AI solution that will determine the best strategy is called Thompson sampling. It is by far the best model for such problems in this branch of Artificial Intelligence Online Learning. In short, every time a new customer connects to the website, that's a new round n and we select one of our 9 strategies to attempt a conversion (subscription to premium plan). The goal is to select the best strategy in each round, and train for many rounds. 

### Implementation: "thomson_sampling.py"

By implementing Thompson sampling, we will also implement the random selection algorithm, which will simply select a random strategy each round. This will be our benchmark for evaluating the performance of our Thompson sampling model. Of course, the Thompson sampling and the random selection algorithm will compete in the same simulation, that is, using the same reward matrix. And in the end, once the complete simulation is done, we will evaluate the Thompson Sampling performance by calculating the relative performance, defined by the following formula:


Rendimiento Rel. = (Recompensa M. de Thomson) - (Recompensa Selección Aleatoria) / (Recompensa Selección Aleatoria) * 100

After applying the algorithm implemented in python, this would be the result in which it can be seen that Thomson Sampling is achieved rather than doubling the random selection.

![Resultado](https://raw.githubusercontent.com/mcpade/MaximizarBeneficios_IA/master/images/Resultado.png)

We will also render the histogram of the selected ads, just to verify that the strategy with the highest conversion rate (Strategy 6) was indeed the most selected. Thompson sampling has been able to quickly identify it

![Histograma](https://raw.githubusercontent.com/mcpade/MaximizarBeneficios_IA/master/images/HistogramaEstrategias.png)

### Regret curve

The regret curve of a model (with random strategy or with Sampling sampling) is the graphical representation of the difference between the best strategy and the deployed model, with respect to the rounds.

The best strategy is calculated simply by obtaining, in each round, the maximum of the accumulated rewards on all the different strategies.

**Random strategy regret curve:**

![ArrepentimientoAle](https://raw.githubusercontent.com/mcpade/MaximizarBeneficios_IA/master/images/RegretRS.png)

We observe absolutely no convergence of the random strategy towards the best strategy.

**Regret curve of the Thompson Sampling:**

![ArrepentimientoAle](https://raw.githubusercontent.com/mcpade/MaximizarBeneficios_IA/master/images/RegretTS.png)

The Thompson sampling is converging very well towards the best strategy.
