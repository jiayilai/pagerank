import networkx as nx
base = "/Library/WebServer/Documents/solr-6.5.0/crawl_data/"
target = "/Users/laijiayi/PycharmProjects/pagerank/external_pageRankFile.txt"
edgelistPath="/Users/laijiayi/IdeaProjects/hw4_572/src/main/resources/Edgelist.txt"
G = nx.read_edgelist(edgelistPath, create_using=nx.DiGraph())
pr = nx.pagerank(G, alpha=0.85, personalization=None, max_iter=30, tol=1e-06, nstart=None, weight='weight',dangling=None)
file = open(target, "w")
for k, v in pr.items():
    print(k, v)
    file.write(base + "%s=%f\n"%(k, v));
file.flush();
file.close();
