---
name: Postmortem report
about: Used to describe a downtime event that has since been resolved
title: "[Postmortem report]"
labels: postmortem
assignees: ''

---

**Status:** {draft|final}
**Owners:** {who worked on finding the resolution}

## Summary
Description: {brief description of symptoms and root cause}
Component: {affected area}
Date/time: {YYYY-MM-DD HH:MM}
Duration: {time from initial breakage to final resolution}
User impact: {who was affected by the incident}

## Timeline (all times in UTC+00:00)

### 2022-01-01

14:44 - something happened
14:45 - next thing happened **&lt;START OF OUTAGE&gt;**

### 1900-01-02

09:12 - another thing happened **&lt;END OF OUTAGE&gt;**

### Impact & root cause

{a more thorough summary of the problems that the outage caused, and **without blame**, describe the root cause of the outage}

### What worked

{list things where things worked as expected in a positive manner}

### Where we got lucky

{list things that mitigated this incident but not because of our foresight}

### What didn't work

{things that failed or prevented a quicker resolution}

## Action items for the future

{each item here should have an owner}

### Prevention

{things that would have prevented this failure from happening in the first place, such as input validation, pinning dependencies, etc}

### Detection

{things that would have detected this failure before it became an incident, such as better testing, monitoring, etc}

### Mitigation

{things that would have made this failure less serious, such as graceful degradation, better exception handling, etc}

### Process

{things that would have helped us resolve this failure faster, such as documented processes and protocols, etc}

### Fixes

{the fixes that were necessary to resolve this incident}

## Other

{any other useful information, such as relevant logs}