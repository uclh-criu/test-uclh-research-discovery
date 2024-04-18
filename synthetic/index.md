---
layout: page
---

# Use of synthetic data at UCLH

This document justifies the need for making health data public. We introduce the concept of manufactured or synthetic data, and explain why this protects privacy more effectively than anonymisation of real data. We propose a simple tiered approach to classify synthetic data products based on their relation to source data. This classification is used to describe the approval process for releasing synthetic data into the public domain. In brief, synthetic data generated independently from the real data can always be released, but data generated using information derived from the real data must first be evaluated using the principles of statistical disclosure control.

We conclude with a short series of principles endorsing the use of synthetic data at UCLH.

## Proposed Principles

1.  We support public data sharing for impactful and reproducible data science.

2.  We believe that releasing synthetic rather than anonymised data will better protect patient confidentiality.

3.  We believe that synthetic data generation has a quantifiable risk to patient privacy that depends on its relationship to the underlying data. The process for releasing synthetic data should be matched to that risk.

4.  Anonymisation and synthetic data generation may require complex tools and specialist knowledge. Where possible, we prefer simpler and more transparent tools that better allow audit and monitoring.

## Introduction

### Science requires collaboration, collaboration requires data

Access to health data is crucial for science and innovation. But data access is restricted to protect our privacy. Best practice is keep data within a Secure Data Environment (SDE), sometimes called a Trusted Research Environment (TRE). This works in a similar manner to logging on to a bank account, and all activity is audited and monitored. But these controls inevitably prevent collaborative working. Such collaboration is part and parcel of modern data science.

Data analysis has many parallels to software development. Analysis is written in code, and knits together separate components to clean, organise, and check the data as well as build statistical models. This is best done openly and in collaboration. Complex work is done by a team of analysts, and even simple work benefits from review by colleagues.

But unlike software development, the collaboration requires sharing of code *and* data. Without the data, colleagues struggle to understand and evaluate the code. It is like being given a prototype for a new car but with no fuel, and asked how well it drives.

To share data and protect privacy, the data must by anonymised. This means de-identifying the original data by removing or masking personally identifiable information (PII). Anonymisation is difficult, time-consuming, and requires considerable expertise.

An alternative to anonymisation is to share synthetic data instead. This means *manufacturing* data that has similar qualities to the original data. We never share the original data. Instead, we share *information*. This distinction is subtle but important.

### Information sharing versus data sharing

One metaphor is to consider anonymisation and synthetic data generation as having parallels with black listing and white listing. Imagine building a spam filter for your email. Black listing means maintaining a list of all the people you want to filter out. Unless you work very hard then the spammers will always beat your filter as they create a new persona that is not yet blacklisted. Anonymisation similarly requires care and attention to capture all the new possible ways that you might unwittingly disclose confidential information.

White listing is a more manageable and risk averse task. Now you maintain a list of all the people you want to filter *in*. It is possible that an email from an old friend does not reach you, but the spammer's job is now impossible. Synthetic data generation means maintaining a list of information that you are prepared to share because you are confident that this will not breach privacy.

With anonymisation, we share the data *after* removing information that we know *is unsafe*. With synthetic data generation, we manufacture similar data *after* deciding what information *is safe*.

### A worked example

Imagine, during the COVID pandemic, a team of computer scientists at the Alan Turing Institute offered to help the vaccine programme. It is the Autumn of 2020, and vaccine roll-out is being planned. We want to know who to vaccinate first. UCLH is asked to provide COVID outcome data, and the analysts will report which patients are most vulnerable. People like these patients will be vaccinated first.

Not only will access to data in a Secure Data Environment take time to organise, it is also crucial that the analysis is shared internationally. This means sharing both the results, but also the methods (i.e. the code used for the analysis) so that the work can be peer reviewed, and checked.

Sharing the anonymised data will require removal of names, dates of birth, and NHS numbers. This is straightforward but as more data is gathered then we must constantly review the data to avoid the leak of confidential information. For example, perhaps we choose to include household size (number of rooms) in the data to understand whether household crowding is a risk factor for COVID transmission. But unwittingly, we will have shared Queen Elizabeth's COVID history since there's only one house in London with more than 700 rooms (Buckingham Palace has 775 rooms). With the appropriate skills and expertise, these risks are avoidable but it requires constant vigilance.

Instead, we could decide to manufacture synthetic data. The international reviewers tell us that the first step in checking the code is to know the structure of the data being analysed. How many different data items are there? What types of data should they expect to see? How are these data items connected.[^1] Our first synthetic data release actually contains no information derived from the data subjects: we simply share the structure of the data, and there is zero risk of leaking confidential information.

Next the international reviewers raise a concern that we properly check how COVID outcomes vary by age and by ethnicity. They need us to either safely anonymise the real data, or manufacture synthetic data that captures how patient's outcomes vary by age and ethnicity.

This latter option actually mirrors how eventual results would be reported in the public domain. That is we would expect to see a table telling us how many patients died by age band from the youngest groups (less than 18 years) to the oldest (greater than 80 years). There would likely be separate tables (or separate columns in a table) for each ethnic group. [^2] We provide synthetic data generation process with these tables which ensures that the balance of COVID outcome, age, and ethnicity is replicated.

We can achieve the same result by anonymising each of outcome, age, and ethnicity but we must be confident this is sufficient, and that no other patient characteristic (e.g. household size) might be used by an attacker.

## A tiered approach to synthetic and anonymised data

We propose aligning the conversation about synthetic data with the concept of tiers used to describe privacy risk in SDE/TRE design. [^3] We follow their definitions of personal, pseudonymised, and anonymised which are explicitly grounded in the process of re-identification rather than the qualities of the data.

Personal data

> Information relating to an identifiable living individual. We extend this to included the deceased, and note that identifiers include names, and other information that would directly or indirectly link those data to that individual.

Pseudonymised data

> These are personal data where additional information that is physically or organisationally separated from the index data is required for re-identification. Pseudonymised data are personal data until that separate route to re-identification is permanently destroyed, and we have high confidence that no other statistical approach can re-identify an individual.

Anonymised data

> These are data where there is absolute or high confidence that there are no circumstances can be used to re-identify an individual.

### The tiers

#### Tier 0

These are publicly available open data. We have absolute confidence (zero doubt) that re-identification is possible. This also excludes data that might have commercial, legal or reputational impact. These data are ready for publication.

#### Tier 1

These are data that are intended for publication but are protected to give the research team a competitive advantage. The data are protected for the benefit of the research team, not because of qualities of the data itself. The data may be anonymised or synthetic. By definition, these data are not personal, and we are confident that anonymisation is robust but the data are not publicly available.

#### Tier 2

These environments manage information not linked to personal data: that is "pseudonymised or synthetic information generated from personal data where classifiers have strong confidence in the quality of the pseudonymisation."[^4] There is nonetheless a residual risk of re-identification. This corresponds to the UK Data service's concept of *Safeguarded data*: "Data \... in this category are not personal, but the data owner considers there to be a residual risk of disclosure in the data."

#### Tier 3

This tier corresponds to data that are personal, and where disclosure could potentially have an important impact on the data subjects. Identifiable health data would meet this definition, and additionally includes synthetic or pseudonymised data where the classifier has only a weak confidence in the quality of the pseudonymisation.

Personal data, or pseudonymised data but with only weak (low) confidence in the process. Unlike Tier 4, disclosure of data is not considered to pose a *substantial* risk to the health, safety or security of the data subject. Attacks on the data, or attempts to re-identify would be conducted by the Information Commissioner's Office's concept of a 'motivated intruder'. This corresponds to the UK governments 'OFFICIAL-SENSITIVE descriptor'.

#### Tier 4

Personal data where disclosure is considered to pose a substantial risk to the health, safety or security of the data subject. Re-identification methods, or attacks to egress the data are likely to be well-resourced, sophisticated and determined. This corresponds to the UK government 'SECRET' category.

### Synthetic data generation and the tiers

With respect to synthetic data, the approach would be to align the terminology.

1.  **Complete Independence from Real Data**\
    In this tier, the synthetic data generation mechanism operates entirely independently from the actual patient data. For example, we might use a six-sided dice to generate random ages for hospital patients, ensuring no direct relation to the real data and eliminating the risk of releasing patient-specific information.

    These data would correspond to Tier 0: the separation of the source data from the synthetic data generating mechanism means that we have absolute confidence re-identification is impossible.

2.  **Informed Independence**\
    Here, while the generation process remains independent, it incorporates expert knowledge. For instance, acknowledging that hospital patients range from 0 to 100 years old, we might employ a 101-sided dice. This method enhances the realism of the synthetic data while maintaining complete separation from the actual patient data.

    As above, these data would correspond to Tier 0. Re-identification would require malicious intent on the part of the person generating the synthetic data as they would be required to deliberately encode PII.

3.  **Utilisation of Aggregate Data with Privacy Techniques**\
    This tier involves the use of aggregate or summary information from the real data. Suppose the average age of hospital patients is 65; we could weight a 100-sided dice to land on 65 more frequently. While this method improves the utility of synthetic data, it introduces a theoretical risk of re-identification. To address this, we employ standard privacy-preserving techniques such as small cell suppression, where cells (data points) with small counts are omitted to prevent identification.

    This approach mirrors the established processes used in public reporting of hospital patient characteristics and outcomes, where similar privacy measures are standard practice. By aligning the release of synthetic data with these well-established protocols, we ensure consistent and rigorous protection of patient privacy.

    These data could be classified between Tier 0 and Tier 2: that is the classification depends on the quality of the statistical disclosure control just as for anonymisation. Here synthetic data generation is more likely to meet the standards of Tier 0 as the choices to improve the fidelity of the data are explicitly designed in.


[^1]:  Data are often organised as a set of linked tables. There might be a table of patients describing age, gender, and ethnicity. This would be linked to a table of COVID tests describing the date of the test and the result, and another table of hospital admissions. Any analysis will need to navigate these tables and assemble the information so that we can ask which patients had tests, and who needed hospital admission following a positive test result.

[^2]:  We would always check these tables for small numbers; perhaps originally the highest age category was greater than 100 years, but there is only one person in that age band. This would present a re-identification risk if the local newspaper had reported people who had recently celebrated their 100th birthday, so we broaden the highest age band to greater than 80 years which now contains tens of individuals.

[^3]:  Arenas, D. et al. Design choices for productive, secure, data-intensive research at scale in the cloud. Preprint at [[https://doi.org/10.48550/arXiv.1908.08737]{.underline}](https://doi.org/10.48550/arXiv.1908.08737) (2019).

[^4]:  In 2006, Cynthia Dwork, Frank McSherry, Kobbi Nissim, and Adam D. Smith introduced a privacy safeguard called ε-differential privacy. They aimed to turn big sets of confidential data into statistics without breaching the privacy of the people who supplied the data.

    Their idea for ε-differential privacy was basically this: If your data isn\'t included in the database, you can\'t have your privacy breached. So, they aimed to make sure that everyone\'s privacy was about as safe as if their data had been left out. This means that the statistical analysis shouldn\'t overly rely on any one person\'s data.

    They also noted that how much each person contributes to the statistical results depends on how many people\'s data is included. For instance, if it\'s just one person\'s data, then they contribute 100%. But if 100 people\'s data is included, each only contributes 1%.

    The real breakthrough of differential privacy lies in its idea that the fewer people\'s data you have, the more \'noise\' (random data) you need to add to the results to keep privacy levels high. This is why they called their 2006 paper, \"Calibrating noise to sensitivity in private data analysis.\" Simply put, it means adjusting the balance between the amount of confidential data used and the randomness added to keep things private.

[^5]:
