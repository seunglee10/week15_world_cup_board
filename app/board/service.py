_posts = [
    {"id": 1, "title": "첫 게시글", "content": "미니 게시판 시작"},
]


def list_posts():
    return _posts


def create_post(title: str, content: str):
    post = {"id": len(_posts) + 1, "title": title, "content": content}
    _posts.append(post)
    return post
