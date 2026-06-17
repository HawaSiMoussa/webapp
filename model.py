
from httpx import post


class Post(db.Model):

    title = post.title
    description = post.description
    views = post.views
    username = post.username
    createDate = post.createDate
    expireDate = post.expireDate
    locationOfLoss = post.locationOfLoss
    dateOfLoss = post.dateOfLoss
    status= post.status
    mail = post.hwrMail