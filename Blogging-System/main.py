from blog_manager import BlogManager

def initialize_blog_posts():
    """Initialize the blog_posts.json file if it doesn't exist."""
    import os
    import json
    if not os.path.exists('blog_posts.json'):
        with open('blog_posts.json', 'w') as file:
            json.dump([], file)

def main():
    # Initialize the blog_posts.json file
    initialize_blog_posts()

    # Initialize the BlogManager
    manager = BlogManager("blog_posts.json")

    while True:
        print("1. Create a new blog post")
        print("2. View all blog posts")
        print("3. Update a blog post")
        print("4. Delete a blog post")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the blog post: ")
            content = input("Enter the content of the blog post: ")
            author = input("Enter the author of the blog post: ")
            manager.create_post(title, content, author)
            print("Blog post created successfully!")

        elif choice == "2":
            posts = manager.get_all_posts()
            if posts:
                for post in posts:
                    print(f"ID: {post['id']}, Title: {post['title']}, Content: {post['content']}, Author: {post['author']}, Timestamp: {post['timestamp']}")
            else:
                print("No blog posts available.")

        elif choice == "3":
            post_id = input("Enter the ID of the blog post to update: ")
            new_content = input("Enter the new content for the blog post: ")
            if manager.update_post(post_id, new_content):
                print("Blog post updated successfully!")
            else:
                print("Blog post not found.")

        elif choice == "4":
            post_id = input("Enter the ID of the blog post to delete: ")
            if manager.delete_post(post_id):
                print("Blog post deleted successfully!")
            else:
                print("Blog post not found.")

        elif choice == "5":
            print("Exiting the Blogging System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()