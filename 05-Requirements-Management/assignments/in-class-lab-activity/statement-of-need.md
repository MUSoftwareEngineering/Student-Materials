# Statement of Need

The CHAOSS-Augur of the Applications Division, hereafter referred to as the contractor, has the need to help teams understand how individuals contribute to open source projects through: 
    - commits of code
    - issue identification 
    - community management

To accomplish this, they have constructed an initial system, called "Augur".

One of the significant challenges for open source is to understand how projects, often composed of 3 - 12 or more .git repositories, look with regards to overall "health". We require a perspective that looks within that group of 3-12 or more repositories, as well as a perspective that allows people to compare "their project" with "other, similar projects", and possibly IDENTIFY other, similar projects. 

## Overview
People compare themselves with others. We build on this truth to help people make sense of the metrics we prototype. The aim of the Augur project is threefold:

1.Fast prototyping of metrics

2.Be human centered …. Build prototypes that make it possible for people to see a visualization and make sense of it before they become overwhelmed by the information and drown in a sea of data.

3.Represent trends over time. Its all time these days.

## Details

Open source software projects are gaining momentum and importance in society by any measure.
Over five billion dollars of direct labor costs are invested in the Linux Foundation’s open source
ecosystem. Annual revenue estimates for the Linux Kernel alone are currently 50 billion US dollars,
supporting a conservative 500 billion US dollar market valuation.2 Systematically discerning the
health of open source ecosystems is essential for firms investing capital, but financial measures
quickly prove inadequate when the role of open source in all of the systems that run the world comes
into view. Open source project health has various definitions and operationalizations, this study
adopts the general view that open source project health is a project’s ability to continue to produce
quality software [55, 62]. Following the Heartbleed OpenSSL security bug in 2014, the US Congress
went so far as to reach out to the Linux Foundation and seek their assistance to better understand
how to increase the transparency of open source project health and risk [88]. Open source software
also represents a significant source of the livelihood for highly skilled professionals in modern
society [86] and increasing the visibility of project health for such contributors is essential.
Work to date on metrics that may inform open source software health and sustainability is
significant, and spread across research communities in software repository mining [4, 8, 23, 46,
56, 68], information systems [19, 24, 36, 61, 90], social computing [10, 13, 14, 57, 87] and software
engineering [34, 38]. The aims of open source software health and sustainability metrics (metrics)
research are wide ranging, including metrics focused on code [23, 45, 48, 60, 66, 76], diversity [5,
6, 25], organizational dynamics [12, 58, 92, 93], risk [47, 49, 56], ecosystem state [46, 64, 65, 92],
large scale classification [64, 65, 80], adverse event prediction [1, 56, 68] and constructing end user
tools [41, 46, 69, 70]. Corporate engagement with open source [35, 36] is increasing the demand for
coherent, consistent and actionable metrics from open source community managers, who play a
role in the formal and informal nurturing of developer communities around open source projects
and ecosystems and internal open source program offices who manage portfolios of open source
projects a firm contributes to [26, 30]. The rapid growth of open source, the large number of ongoing
metrics development research studies and the evolving needs of corporations engaged in open
source lead to an overwhelming flood of answers to discrete questions about individual projects
and ecosystems.

Though many of the metrics that are developed for open source projects prove useful, metaphorically
they are blood tests on individuals and have limited value to a world that is seeking to
understand the health of a population or evaluate the health of individuals within populations. In
other words, open source metrics often contain the right answers to the wrong questions. Public
health research identifies this kind of issue as a Type III error, which emerges when we try to
generalize differences between populations and their causes to explain the health of a single population
[71]. In open source language, the causes of health and sustainability variation between all
projects, differences over time and the existence of specific risk factors can all be distinct; but there
are no open source metrics available today that distinguish between them. For example, depending
on where a project is in its life-cycle, a decline in activity could mean either an emergent risk of the
community losing contributor engagement or the stabilization of a fast-growing new technology.
Most cases are not so clear cut as those two.

Everyone involved in open source software wants a clearer understanding of project and ecosystem
health and sustainability. To close the gap between a need for instrumentation of health and
sustainability and the overwhelming milieu of available, discrete metrics that may inform health,
open source projects need indicators that enable orientation alongside measurement.
In this paper, we frame a two-year engaged field research and participatory design study within
the Linux Foundation’s Community Health Analytics in Open Source Software (CHAOSS) project
and present a candidate architecture and methodological approach for examining specific aspects of
open source software systems - AUGUR. The goal is to bring the CHAOSS metrics to life by designing
a system with a UI and API that serves CHAOSS metrics, and to enable comparisons between
similar projects. Our findings illustrate a pathway making open source health and sustainability
visible in context by emphasizing comparison, transparency, trajectory and visualization through
a set of design principles and a specific, implemented technology architecture called Augur. Our
contribution begins a discussion among open source and social computing researchers about
more systematically and consistently making sense of the ways individual and organizational
interests intersect in open source ecosystems. This work aims to enable the kind of comparative
research necessary for more wide-scale theory construction through the experience of open source
participants.
