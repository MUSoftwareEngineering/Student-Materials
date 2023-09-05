# Title: 4-oss

## Background
Open source community leaders want to understand their communities' health and
sustainability to manage them strategically. Health and sustainability metrics
provide community leaders with a tool to measure the effectiveness of
interventions and initiatives as well as to identify areas of improvement.

## Description
The user (leader) provides a URL to a GitHub repository for a community that
she manages. The software returns
[metrics](https://wiki.linuxfoundation.org/oss-health-metrics/metrics)
that indicate the health and sustainability of the repository.

## Triggers (What prompts the use case to start?)
1. A user (leader) seeks to understand the current health and sustainability
   of a repository to devise actions.
2. A manager seeks to understand the current health and sustainability of their projects to see the effectivness of interventions.

## Actors (Who is involved?)
1. Community Leaders
2. Managers

## Preconditions (This includes things like “data loaded”. Or, project is flagged as “of interest”; etc.)
1. User provides URL to a GitHub repository

## Main Success Scenario
1. All metrics that can be computed from the provided repository are displayed.

## Alternate Success Scenarios
1. Managers can see (via dashboard) the health and sustainability of their projects

## Failed End Condition
1. The provided URL points to a non-existent GitHub repository, metrics cannot
   be calculated, and an error message explaining the condition is shown to user.
2. The repository does not have enough contributions to calculate any metrics

## Extensions
1. Compare metrics between repositories.

## Steps of Execution (Requirements)
1. The use enters and submits the URL to a GitHub repository.
2. Metrics computed from the provided repository are displayed.

## Dependent Use Cases
1. N/A

## A use case diagram, following the UML Standard for expressing use cases.
![use case diagram](./diagram/ViewMetrics.png)
