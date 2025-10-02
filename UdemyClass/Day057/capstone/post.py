import requests

class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
                
        self.blog_request = requests.get(self.blog_url)        
        self.blog_posts = self.blog_request.json()
        print(type(self.blog_posts))
        
    def get_blog_title(self, blogno):
        return self.blog_posts[blogno]["title"]
    
    def get_blog_subtitle(self, blogno):
         return self.blog_posts[blogno]["subtitle"]
     
    def get_blog_body(self, blogno):
         return self.blog_posts[blogno]["body"]
    