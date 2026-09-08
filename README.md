# Assignment #1 - Designing a Product Recommendation Engine

You’ve just joined a small e-commerce startup, and your first task is to prototype a basic product recommendation tool. Each product in the catalog includes tags like `"eco-friendly"`, `"durable"`, or `"stylish"`. This looks like the list of dictionaries shown below.
```python
products = [ 
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]}, 
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]}, 
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]}, 
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]}, 
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
    ...
]
```

When a customer lists their preferences, the tool should return products with the most matching tags. An example input and output is shown below.

**Example Input**
```bash
Input a preference:
eco-friendly
Do you want to add another preference? (Y/N): Y
Input a preference:
durable
Do you want to add another preference? (Y/N): N
```

**Example Output**
```bash
Recommended Products:
- Eco Water Bottle (2 match(es))
- Bamboo Toothbrush (1 match(es))
- Smartwatch (1 match(es))
```

At this stage in the course, you’re not designing full-scale systems. Instead, you’re learning to manipulate data using core structures like lists and sets. This assignment helps you practice the kind of logic that underpins real-world software tools while making key decisions about data structure selection and iteration. 

This work directly supports your final project, where you’ll complete a mock technical interview. There, you’ll face an open-ended coding challenge and be expected to select the best data structure for the job. The core skills you build here—gathering inputs, cleaning data, selecting the right structure, and explaining trade-offs—are the foundation for those high-stakes problem-solving moments.