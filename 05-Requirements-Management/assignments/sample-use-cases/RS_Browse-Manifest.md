# Title: Browse Manifest

## Description
When the user searches by keyword, relevant manifests and corresponding SNC ("script, notebook or configuration") files are displayed with brief descriptions on what the data and files hold. The search results will include any manifests or SNC files that contain that keyword. The user will then be able to select each of the files to examine its contents and explore the terms, conditions and licensing of the files use. Navigating back to the result list should be simple.

## Triggers (What prompts the use case to start?)
1. User submits search request by entering or clicking "Search".

## Actors (Who is involved?)
1. Researchers
2. Students
3. Data scientists
4. System admins

## Preconditions (This includes things like “data loaded”. Or, project is flagged as “of interest”; etc.)
1. User has searched for manifests.

## Main Success Scenario
1. All datasets whose manifests contained searched keywords and corresponding SNC files are displayed with options to view and test files. If there are multiple pages of results, there is pagination.

## Alternate Success Scenarios 
1. User identifies a set of similar research projects and maintains a list for future inquiry
2. User determines that no projects similar to their own interests or work have yet been catalogued.

## Failed End Condition
1. No manifests were found and thus none are displayed.

## Extensions
1. Replicate research project from Manifest

## Steps of Execution (Requirements)
**Not Yet A Good Example**
1. "Date Uploaded" will be differentiating factors for multiple sets of SNC files for the same data set.
1. Buttons for "Open in Jupyter" and "Download" for each dataset and SNC file.
1. Sorting options (by date, by relevance).

## Dependent Use Cases
1. Search Manifest

## A use case diagram, following the UML Standard for expressing use cases.

![alt text](./images/browse_diagram.png)
