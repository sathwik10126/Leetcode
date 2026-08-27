#!/usr/bin/env python3
"""
Generate a LeetHub-style README by reading local solution folders and fetching
problem metadata from LeetCode's public API.
"""

import os
import re
import json
import requests
from collections import defaultdict
from pathlib import Path

# LeetCode API endpoint for problem list
LEETCODE_API = "https://leetcode.com/api/problems/all/"

def fetch_leetcode_problems():
    """Fetch all problem metadata from LeetCode's public API."""
    try:
        response = requests.get(LEETCODE_API, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching LeetCode problems: {e}")
        return None

def parse_folder_name(folder_name):
    """
    Extract problem number and name from folder name.
    Format: 0001-two-sum or 1-two-sum
    """
    match = re.match(r'(\d+)-(.+)', folder_name)
    if match:
        return int(match.group(1)), match.group(2).replace('-', ' ').title()
    return None, None

def build_problem_map(api_data):
    """Build a map of problem_id -> problem_info from LeetCode API."""
    problem_map = {}
    if not api_data or 'stat_status_pairs' not in api_data:
        return problem_map
    
    for item in api_data['stat_status_pairs']:
        stat = item.get('stat', {})
        problem_id = stat.get('question_id')
        
        if problem_id:
            problem_map[problem_id] = {
                'title': stat.get('question__title', ''),
                'slug': stat.get('question__title_slug', ''),
                'difficulty': item.get('difficulty', {}).get('level', 1),
                'difficulty_name': {1: 'Easy', 2: 'Medium', 3: 'Hard'}.get(
                    item.get('difficulty', {}).get('level', 1), 'Unknown'
                ),
                'category': item.get('category', ''),
            }
    
    return problem_map

def get_problem_topics(problem_slug):
    """Fetch topics for a specific problem from LeetCode."""
    try:
        url = f"https://leetcode.com/graphql"
        query = {
            "query": f"""
            query getTopicTags {{
              question(titleSlug: "{problem_slug}") {{
                topicTags {{
                  name
                  slug
                }}
              }}
            }}
            """
        }
        response = requests.post(url, json=query, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'question' in data['data']:
                tags = data['data']['question'].get('topicTags', [])
                return [tag['name'] for tag in tags]
    except Exception as e:
        print(f"Warning: Could not fetch topics for {problem_slug}: {e}")
    
    return []

def scan_local_problems(root_dir="."):
    """Scan local directory for LeetCode solution folders."""
    problems = []
    
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and re.match(r'^\d+', item):
            problem_id, problem_name = parse_folder_name(item)
            if problem_id:
                problems.append({
                    'id': problem_id,
                    'folder': item,
                    'parsed_name': problem_name,
                })
    
    return sorted(problems, key=lambda x: x['id'])

def generate_readme(output_file="README.md"):
    """Generate README with problems organized by topic."""
    
    print("Fetching LeetCode problem data...")
    api_data = fetch_leetcode_problems()
    problem_map = build_problem_map(api_data)
    
    print("Scanning local problem folders...")
    local_problems = scan_local_problems()
    
    if not local_problems:
        print("No problem folders found. Make sure you're in your LeetCode repo root.")
        return
    
    print(f"Found {len(local_problems)} problems. Fetching topic data...")
    
    # Organize by topic
    topics = defaultdict(list)
    other_problems = []
    
    for prob in local_problems:
        prob_id = prob['id']
        folder = prob['folder']
        
        # Get problem info from API
        if prob_id in problem_map:
            prob_info = problem_map[prob_id]
            prob['title'] = prob_info['title']
            prob['difficulty'] = prob_info['difficulty_name']
            prob['slug'] = prob_info['slug']
            
            # Fetch topics
            topics_list = get_problem_topics(prob_info['slug'])
            
            if topics_list:
                # Add to first topic category
                main_topic = topics_list[0]
                topics[main_topic].append(prob)
            else:
                other_problems.append(prob)
        else:
            other_problems.append(prob)
    
    # Generate README content
    readme_content = f"""# LeetCode Solutions

> A collection of {len(local_problems)} LeetCode problems solved and organized by topic.

## 📊 Stats
- **Total Problems Solved**: {len(local_problems)}
- **Topics Covered**: {len(topics)}

## 📑 Table of Contents
"""
    
    # Add TOC
    for topic in sorted(topics.keys()):
        count = len(topics[topic])
        readme_content += f"- [{topic}](#{topic.lower().replace(' ', '-')}) ({count})\n"
    
    if other_problems:
        readme_content += f"- [Other](#{count})\n"
    
    readme_content += "\n---\n"
    
    # Add problems organized by topic
    for topic in sorted(topics.keys()):
        problems_in_topic = sorted(topics[topic], key=lambda x: x['id'])
        readme_content += f"\n## {topic}\n\n"
        readme_content += "| # | Title | Difficulty | Solution |\n"
        readme_content += "|---|-------|-----------|----------|\n"
        
        for prob in problems_in_topic:
            difficulty_emoji = {
                'Easy': '🟢',
                'Medium': '🟡',
                'Hard': '🔴'
            }.get(prob.get('difficulty', 'Unknown'), '⚪')
            
            difficulty = prob.get('difficulty', 'Unknown')
            title = prob.get('title', prob['parsed_name'])
            folder = prob['folder']
            
            readme_content += f"| {prob['id']} | {title} | {difficulty_emoji} {difficulty} | [View](/{folder}) |\n"
    
    # Add other problems if any
    if other_problems:
        problems_other = sorted(other_problems, key=lambda x: x['id'])
        readme_content += f"\n## Other\n\n"
        readme_content += "| # | Title | Solution |\n"
        readme_content += "|---|-------|----------|\n"
        
        for prob in problems_other:
            title = prob.get('title', prob['parsed_name'])
            folder = prob['folder']
            readme_content += f"| {prob['id']} | {title} | [View](/{folder}) |\n"
    
    readme_content += "\n---\n\n"
    readme_content += "*Last updated: Auto-generated by LeetCode sync*\n"
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(readme_content)
    
    print(f"\n✅ README.md generated successfully!")
    print(f"📁 {len(local_problems)} problems organized into {len(topics)} topics")
    print(f"📄 Output: {output_file}")

if __name__ == "__main__":
    generate_readme()