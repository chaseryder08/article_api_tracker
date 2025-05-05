# Article Workflow Tracker API

## Overview

This project simulates a tool designed to track the time it takes for support knowledge articles to be published after a defect is confirmed. It is based on real-world use at IDBS, where the goal is to optimize the process of article creation and publishing.

## Workflow

The tool follows the stages of an article's lifecycle:
1. **Draft** - Article draft is created in Salesforce.
2. **In Review** - Article is under review by relevant stakeholders.
3. **Needs Rework** - Article requires changes before being approved.
4. **Approved/Published** - Article is finalized and published.

The main objective is to track the time from when an article is created (Draft) to when it is published, with a target of **2 days**.

## Purpose

This project helps identify delays in the article publishing process, uncovering their causes to drive better performance and reduce time to publish.

## Future Enhancements

- Integration with AI for intelligent delay predictions.
- Email notifications for key status updates in the workflow.

## Tech Stack

- **Flask** (API Framework)
- **Python** (Programming Language)
- Optional future integrations (AI, Email Notifications)

Feel free to contribute or explore how this tool can be enhanced further!
