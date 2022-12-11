# Infranous
### Generate Network Graphs from Text
![image](https://user-images.githubusercontent.com/36832027/206894857-8ea2bd6d-1102-4b5b-a710-96935cacf1ad.png)

I'm in the process of replicating the "Infranodus" commercial software in python. It makes network graphs out of text, establishes weight between words based on how close they appear in the original text (`Word 1` -> `Word 2` gets a high weight, `Word 1` -> `Word 3` gets a medium weight, `Word 1` -> `Word 4` gets a low weight, `Word 1` -> `Word 4` is not connected). These plots scale the nodes by how many connections they have, so the "most important" words should scale up.  

### Examples
Check out the .html files in this repository.  
So far it seems to check out; "Moon" is huge in the Apollo graph, and "Invasion" is big in the UKR graph. The input was the first paragraph of each topic's wikipedia page (and that's why you'll see some random number trash after certain words, it's a slightly cleaned footnote number).  

### To Do
The original tool uses some more sophisticated approaches to scaling nodes and also re-colors the graph by some sort of voodoo... Community detection?
