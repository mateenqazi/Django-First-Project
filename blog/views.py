from django.shortcuts import render
from datetime import date


posts_data = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened.",
        "content": """
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups

        """
    },
    {"slug": "programming-is-fun",
     "image": "coding.jpg",
     "author": "Qazi Mateen",
     "date": date(2020, 4, 10),
     "title": "Programming is great",
     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened.",
     "content": """
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups
        Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
        layouts and visual mockups
        """},
    {"slug": "nature-is-beauty",
     "image": "woods.jpg",
     "author": "Peter John",
     "date": date(2022, 5, 1),
     "title": "Nature At Its Best",
     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened.",
     "content": """
      Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
      layouts and visual mockups
      Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
      layouts and visual mockups
      Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
      layouts and visual mockups
      Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing 
      layouts and visual mockups
      """}
]


def get_date(post):
    return post['date']


# Create your views here.


def starting_page(request):
    sorted_list = sorted(posts_data, key=get_date)
    latest_posts = sorted_list[-3:]
    print(latest_posts)
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": posts_data
    })


def post_detail(request, slug):
    print("slug", slug)
    identify_post= next(post for post in posts_data if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identify_post
    })
