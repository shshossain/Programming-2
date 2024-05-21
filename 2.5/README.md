# Protein Annotation Analysis with Dask Dataframes
This script analyzes protein annotation data obtained from InterProScan using Dask Dataframes. InterProScan is a meta-annotator that runs different protein function annotators on amino-acid sequence files and collects the output, labeling them with unique identifiers called "InterPRO numbers."

## Questions to Answer:
1. How many distinct protein annotations are found in the dataset?
2. How many annotations does a protein have on average?
3. What is the most common GO Term found?
4. What is the average size of an InterPRO feature found in the dataset?
5. What are the top 10 most common InterPRO features?
6. What are the top 10 InterPRO features with sizes almost the same as the protein itself?
7. What are the top 10 most common words found in the textual annotation of features?
8. What are the top 10 least common words found in the textual annotation of features?
9. What are the 10 most common words found for the largest InterPRO features?
10. What is the coefficient of correlation between the size of the protein and the number of features found?
