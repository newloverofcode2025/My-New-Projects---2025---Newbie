import json
import os
import uuid
from datetime import datetime

class BlogPost:
    def __init__(self, title, content, author):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "timestamp": self.timestamp
        }

class BlogManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.posts = self.load_posts()

    def load_posts(self):
        """Load blog posts from the JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_posts(self):
        """Save blog posts to the JSON file."""
        with open(self.file_path, 'w') as file:
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