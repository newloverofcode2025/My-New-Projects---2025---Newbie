import json
import os
import uuid
from datetime import datetime

class BlogPost:
    def __init__(self, title, content, author):
        self.id = str(datetime.now().timestamp())
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Convert the blog post to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "timestamp": self.timestamp
        }

class BlogManager:
    def __init__(self, filename):
        self.filename = filename
        self.posts = self.load_posts()

    def load_posts(self):
        """Load posts from a file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_posts(self):
        """Save posts to a file."""
        with open(self.filename, 'w') as file:
            json.dump(self.posts, file, indent=4)

    def create_post(self, title, content, author):
        """Create a new blog post."""
        new_post = BlogPost(title, content, author)
        self.posts.append(new_post.to_dict())
        self.save_posts()

    def get_all_posts(self):
        """Return all blog posts."""
        return self.posts

    def update_post(self, post_id, new_content):
        """Update the content of a blog post by its ID."""
        for post in self.posts:
            if post["id"] == post_id:
                post["content"] = new_content
                post["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_posts()
                return True
        return False

    def delete_post(self, post_id):
        """Delete a blog post by its ID."""
        for post in self.posts:
            if post["id"] == post_id:
                self.posts.remove(post)
                self.save_posts()
                return True
        return False