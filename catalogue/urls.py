from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = DefaultRouter()
router.register("books", views.BookViewSet, "books")
router.register("authors", views.AuthorViewSet, "authors")
router.register("reviews", views.ReviewViewSet, "reviews")

review_router = routers.NestedDefaultRouter(router, "books", lookup="book")
review_router.register("reviews", views.ReviewViewSet, 'review')
review_router.register("images", views.ImageViewSet, "images")

# urlpatterns = [
#     # path('books/', views.BookList.as_view(), name='books'),
#     # path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
#     path('authors/', views.AuthorList.as_view(), name='authors'),
#     path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
#     path("", include(router.urls))
#
# ]

urlpatterns = router.urls + review_router.urls
