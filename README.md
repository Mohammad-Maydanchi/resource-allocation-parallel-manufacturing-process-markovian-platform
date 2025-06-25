# Inspection Allocation in Parallel Genetic Manufacturing – Markovian Platform
This project extends previous work on inspection allocation by modeling a genetic manufacturing system (GMS) with two parallel synthesis lines using a Markov Decision Process (MDP). The system produces two DNA fragments simultaneously and merges them using Gibson assembly, requiring inspection strategies that account for parallel operations and final sequencing.

🎯 Objective
Optimize inspection allocation strategies in a parallel GMS to:

Minimize total cost from inspection, errors, and rework

Improve overall product quality and reliability

Balance resource allocation across multiple synthesis lines

🧠 Methodology
Model Type: Finite-horizon MDP

Structure: Two parallel fragment synthesis lines followed by a Gibson assembly step

Inspections: Applied after each synthesis stage and after final assembly

Flexibility: Model supports differing Type I/II error rates and varying non-conformance probabilities

Advantages over Simulation:

Faster computation

More accurate and flexible error modeling

📊 Key Insights
Optimal strategies shift based on line-specific inspection accuracy and defect rates

Trade-offs between early-stage inspection and final sequencing costs

Final sequencing plays a critical role in quality assurance

MDP-based approach significantly outperforms previous simulation-based models in speed and flexibility

📌 Application
This model is valuable for:

Researchers in synthetic biology and manufacturing optimization

Practitioners designing inspection policies in DNA synthesis and assembly

Complex, high-precision multi-line production environments
