import redis
import redisvl

from redisvl.extensions.router import Route, SemanticRouter
from redisvl.utils.vectorize import HFTextVectorizer
from redisvl.extensions.router import RoutingConfig

router = SemanticRouter.from_existing(name="topic_router",redis_url="redis://redis-15000.re-cluster1.ps-redislabs.org:15000")

# Example queries
queries = [
    "Tell me about the plot of Dune",
    "How to code a GPT model in Python",
    "Who wrote the symphony for Mozart?"
]

# Run queries
for q in queries:
    best_route = router(q)
    print(best_route.name)
