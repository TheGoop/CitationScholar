# Citation Scholar

This tool helps high schoolers with literature review.


# How to Use

To run the frontend, run `npm install` in the `frontend` directory. Then, run `npm start`.
To run the backend, install all dependencies in `requirements.txt` -- this can be done via `pip install -r requirements.txt`. After the dependencies are in place, run `python app.py` to start the Flask backend. 

Now, visit `localhost:3000` to view the website. 

## Inspiration 

When first exploring a new field, one can easily become lost in the sea of papers. Increasingly, we see K-12 students stumbling upon the academic world out of personal interest or for advanced classes. But without prior experience, navigating between different papers can quickly come a nightmare. What if there was a utility made to connect related papers and illustrate how citations are related to each other? Our application alleviates the challenge of getting into the research world through an intuitive display combining data science and visualization.

## Combine and Choose From Different Sources

When putting in a topic or original paper you want to build off of, Citation Scholar provides a variety of selections. In our first implementation, these sources can include arxiv, google scholar, acm, and ieee. Once selected, Citation Scholar looks for paper citations from the original source in each of these respective databases.

## View Your Citation Network From Different Angles


Sometimes a change of perspective can paint research in an entirely new light! By using a dynamic force graph, Citation Scholar makes it easy to view research. We utilized D3.js and a force graph to allow for manipulation of the graph structure while keeping edges intact. Notably, the shade of each node highlights its date. The older the paper is, the darker its shade: a useful visual indicator when trying to find papers of related topics.

The red node shows the starting origin of the inputted research paper. Once hovering over a node, the selection boldens and zooms to provide visual clarity. Double clicking brings you to the research paper featuring that title. And voila, we have a force graph visualization of the world of academia!

## How We Built the Frontend

We used React and a Graph building library to build a graph based on the data sent to us by our backend. 

## How We Built the Backend

Backend was written in Python, interfacing with the Frontend via Flask + Flask endpoints. 

## Challenges We Ran Into

Web scraping is a task that's very easy to dismiss as "trivial" or a "small part of the project". 
This is usually never true. 

When writing plugins for scraping Google Scholar, we ran into a number of issues. Google Scholar doesn't provide an API, and presents numerous Capchas to prevent automated scraping (such as what we need now). We worked around most of these issues, but in the process spent enough time that we put the rest of our project in jeopardy. 

## Accomplishments that we're proud of

Brandon's frontend graph is beautiful. 

## What we learned

It's difficult for everybody to stay on the same page when working asynchronously with varying levels of experience. 

## What's next for Citation Scholar

Our code is designed to scrape papers from multiple websites and aggregate the results. To add new functionality, all we have to do is add new "scraper" modules to the scrapers directory. 

Because of time constraints, our current prototype only interfaces with arXiv.org. We have setup a plug-in system to add GoogleScholar and other features in the future. We also aim to improve our algorithms to create a reference list that ranks based on the relevance of each paper (i.e., number of times cited by other papers). 

## Citations

Thank you to arXiv for use of its open access interoperability.
