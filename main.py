import logging
from rich.console import Console

# Local tools imports
from tools.logging_config import configure_logging
from tools.search_engines.google_search import GoogleSearch
from tools.search_engines.bing_search import BingSearch
from tools.web_utils.web_search import SearchEngine, WebSearch

# LLMs imports
from llms.agent.agent import Agent

configure_logging()
logger = logging.getLogger(__name__)
console = Console()

if __name__ == "__main__":
    # Search Engine
    google_engine = SearchEngine(GoogleSearch)
    bing_engine = SearchEngine(BingSearch)

    # Web Search
    query = 'Python'
    web_search = WebSearch(google_engine, query=query)
    links = web_search.search()
    web_search.print_links(links)  
    web_page = web_search.open(links[0])
    # print(web_page.title)
    # print(web_page.body)

    agent = Agent(llm_identifier='chatgpt35turbo')
    console.print(agent)
    
    try:
        response = agent.get_response('This is my prompt')
        logger.info(f"Final response: {response}")
    except Exception as e:
        logger.error(e)
