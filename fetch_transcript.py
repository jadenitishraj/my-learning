#!/usr/bin/env python3
"""Fetch YouTube transcript given a video URL or ID."""

import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url_or_id):
    """Extract video ID from various YouTube URL formats."""
    patterns = [
        r'(?:v=|/v/|youtu\.be/|/embed/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$'
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_transcript.py <youtube_url_or_id>")
        sys.exit(1)

    video_id = extract_video_id(sys.argv[1])
    
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        for entry in transcript:
            text = entry.text.replace('\n', ' ')
            print(text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
