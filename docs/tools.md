# List of scanners

## Bandit scanner

<https://bandit.readthedocs.io/en/latest/>

Bandit is a tool designed to find common security issues in Python code. To do this, Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files, it generates a report.

## Dependency Check

<https://www.owasp.org/index.php/OWASP_Dependency_Check>

Dependency-Check is a software composition analysis utility that identifies project dependencies and checks if there are any known, publicly disclosed, vulnerabilities. Currently, Java and .NET are supported; additional experimental support has been added for Ruby, Node.js, Python, and limited support for C/C++ build systems (autoconf and cmake). The tool can be part of a solution to the OWASP Top 10 2017 A9-Using Components with Known Vulnerabilities previously known as OWASP Top 10 2013 A9-Using Components with Known Vulnerabilities.

## findbugs

<http://findbugs.sourceforge.net/>

FindBugs, a program which uses static analysis to look for bugs in Java code.  It is free software, distributed under the terms of the Lesser GNU Public License. The name FindBugs™ and the FindBugs logo are trademarked by The University of Maryland. FindBugs has been downloaded more than a million times.

## clair

<https://github.com/coreos/clair>

Clair is an open source project for the static analysis of vulnerabilities in application containers (currently including appc and docker).

1. In regular intervals, Clair ingests vulnerability metadata from a configured set of sources and stores it in the database.
2. Clients use the Clair API to index their container images; this creates a list of features present in the image and stores them in the database.
3. Clients use the Clair API to query the database for vulnerabilities of a particular image; correlating vulnerabilities and features is done for each request, avoiding the need to rescan images.
4. When updates to vulnerability metadata occur, a notification can be sent to alert systems that a change has occured.

Our goal is to enable a more transparent view of the security of container-based infrastructure. Thus, the project was named Clair after the French term which translates to clear, bright, transparent.

## inspec

<https://www.inspec.io/>

Chef InSpec is compliance as code
Turn your compliance, security, and other policy requirements into automated tests.
