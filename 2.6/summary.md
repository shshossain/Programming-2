## 'Software Engineering for Machine Learning: Characterizing and Detecting Mismatch in Machine-Learning Systems' by Lewis and Ozkaya (2021)

The article discusses the challenges of integrating machine learning models into software systems. The authors identify several categories of mismatches that can occur during development. The authors propose using machine-readable descriptors to capture information about machine learning models. These descriptors could be used to identify potential mismatches early in the development process.

**Trained Model Mismatch**: This occurs when there's insufficient information about the model's specifications, causing integration challenges. For example, a software engineer may find it difficult to integrate an ML model into a system due to a lack of clear documentation on its components and specifications.

**Operational Environment Mismatch**: This arises when there's a disparity between the runtime environment and the assumptions made during development. For instance, operations staff might struggle to monitor an ML model properly because they weren't informed about the required runtime metrics and data.

**Task and Purpose Mismatch**: Stemming from unclear business goals or task specifications, this leads to inefficiencies in model development. For instance, a data scientist might receive vague instructions to "work on the data," resulting in a lack of clarity on project objectives and requirements.

**Raw Data Mismatch**: This arises due to insufficient metadata or descriptions of raw data, hindering effective data processing. Without proper documentation, data scientists may struggle to understand the context and quality of the data they're working with.

**Development Environment Mismatch**: This occurs when there's a disparity in programming languages or frameworks used between different teams, leading to compatibility issues. For instance, attempting to replicate a ML model developed in one language for instance R using a different language for example Python may result in unexpected errors.

**Operational Data Mismatch**: This arises when the data used to train the model doesn't accurately represent the operational environment, impacting model performance. For example, the training data may not account for certain real-world scenarios, leading to inaccuracies during model deployment.

**Training Data Mismatch**: Stemming from inadequate details about data preparation pipelines, this hinders effective feature engineering and model development. For instance, a lack of documentation on data preprocessing steps restricts the exploration of alternative feature engineering approaches.



## 'Tackling Collaboration Challenges in the Development of ML-Enabled Systems' by Lewis (2023)
In this article, the author discusses the challenges of collaboration encountered during the development of ML-powered systems and presents insights gleaned from a study on this subject. The study, which involved interviews with professionals engaged in building ML-driven systems and a comprehensive review of literature on software engineering for such systems, identified three primary collaboration focal points: requirements and planning, training data, and product-model integration.

In the realm of requirements and planning, tensions often emerge between product specifications and model necessities. To address this, the article suggests early involvement of data scientists, simultaneous development tracks for product and model teams, conducting ML training sessions for both clients and product teams, and adopting more structured requirements documentation.

In the domain of training data, challenges stem from discrepancies in ownership, comprehension, and coordination between product and model teams. Recommendations include proactive planning for data collection and access to domain experts, formalizing contracts specifying data quality and quantity expectations, establishing clear guidelines for collaboration with dedicated data teams, and implementing robust data validation and monitoring mechanisms.

The integration of product and model components demands close collaboration between data scientists and software engineers, with potential conflicts arising from cultural disparities, ambiguous processes, and differing quality assurance methodologies. To mitigate these conflicts, the article suggests refining processes, delineating responsibilities and boundaries, fostering transparent communication, and preventing the isolation of data scientists.

Quality assurance for both the model and the product presents challenges in ensuring adequacy, transparency in evaluation, and accountability for system testing. Recommendations include structuring feedback loops from the product engineering team to the model team, and establishing explicit quality criteria for both the model and the product.

In conclusion, the article underscores the critical importance of enhancing collaboration in the development of ML-powered systems. It advocates for improvements in communication, documentation practices, engineering proficiency, and alignment of processes to facilitate effective collaboration between data scientists and software engineers.
