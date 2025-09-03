import redis
import redisvl

from redisvl.extensions.router import Route, SemanticRouter
from redisvl.utils.vectorize import HFTextVectorizer

# Initialize the vectorizer
vectorizer = HFTextVectorizer()

# Define the routes with their references and distance thresholds

routes = [
    Route(
        name="genai_programming",
        references=[
            "How do I implement a simple neural network in PyTorch step by step?",
            "Explain reinforcement learning with an example of a reward system.",
            "What are the latest advancements in AI programming and machine learning models?",
            "Describe how large language models are fine-tuned for specific tasks.",
            "What is prompt engineering and why is it important for LLMs?",
            "Explain the process of building a chatbot with GPT-like models in Python.",
            "How do LLM-based coding assistants generate code automatically?",
            "What techniques are used for evaluating prompt quality in AI systems?",
            "Describe how transformers work in natural language processing.",
            "What are the best practices for deploying AI models at scale in production?"
        ],
        metadata={"category": "GenAI Programming"},
        distance_threshold=0.5
    ),
    Route(
        name="sci_fi_entertainment",
        references=[
            "What are the top-rated science fiction movies released in 2024?",
            "Explain the story of the latest Dune movie adaptation in detail.",
            "Who are the main characters in the new Star Wars TV series?",
            "Discuss the importance of world-building in speculative fiction.",
            "What makes a good space opera story compared to regular sci-fi?",
            "Explain the role of technology in classic sci-fi films like Blade Runner.",
            "Which authors such as Isaac Asimov or Philip K. Dick shaped science fiction?",
            "How has Star Trek influenced modern science fiction television?",
            "What makes Dune unique among other science fiction franchises?",
            "Describe the difference between hard science fiction and soft science fiction."
        ],
        metadata={"category": "Science Fiction Entertainment"},
        distance_threshold=0.5
    ),
    Route(
        name="classical_music",
        references=[
            "Who composed The Four Seasons and what makes it special in baroque music?",
            "What is the historical significance of Beethoven’s Ninth Symphony?",
            "Explain the structure of a classical sonata in detail.",
            "Describe the differences between baroque, classical, and romantic music styles.",
            "How did Mozart influence the development of the classical symphony?",
            "Explain what orchestration means in the context of symphonic music.",
            "What is the role of concertos in classical music history?",
            "How did Bach shape the foundations of Western music theory?",
            "Describe the typical instruments used in a classical orchestra.",
            "What are the defining features of music from the romantic period?"
        ],
        metadata={"category": "Classical Music"},
        distance_threshold=0.5
    )
]

# Create a temporary router just to delete any old index

tmp_router = SemanticRouter(
    name="topic_router",
    routes=[],
    vectorizer=vectorizer,
    redis_url="redis://redis-15000.re-cluster1.ps-redislabs.org:15000"
)

try:
    tmp_router.delete()
    print("Old index deleted")
except Exception as e:
    print(f"No existing index found ({e})")

# Initialize the Semantic Router

router = SemanticRouter(
    name="topic_router",
    routes=routes,
    vectorizer=vectorizer,
    redis_url="redis://redis-15000.re-cluster1.ps-redislabs.org:15000"
)

print(f"Initialized router with {router._index.info()['num_docs']} docs")
