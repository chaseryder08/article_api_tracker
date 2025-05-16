# Article Workflow Tracker API

## Overview

This project simulates a tool designed to track the time it takes for support knowledge articles to be published after a defect is confirmed. As a Support Analyst at IDBS, I lead a high-priority Key Performance Indicator (HPKI) initiative aimed at reducing the time it takes to publish defect knowledge articles. This lightweight internal API helps support teams track article turnaround time, flag delays, and streamline publishing workflows. Designed to improve internal accountability and reduce bottlenecks.

The tool follows the stages of an article's lifecycle:
1. **Draft** - Article draft is created in Salesforce.
2. **In Review** - Article is under review by relevant stakeholders.
3. **Needs Rework** - Article requires changes before being approved.
4. **Approved/Published** - Article is finalized and published.

The main objective is to track the time from when an article is created (Draft) to when it is published, with a target of **2 days**.

## Purpose

This tool helps identify delays in the article publishing process, uncovering their causes to drive better performance and reduce time to publish. It supports the HPKI initiative by providing insights into bottlenecks and contributing to more efficient workflows.

## Future Enhancements

- Integration with AI for intelligent delay predictions.
- Email notifications for key status updates in the workflow.

## Tech Stack

- **Flask** (API Framework)
- **Python** (Programming Language)
- Optional future integrations (AI, Email Notifications)

