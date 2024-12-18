import json

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient


@pytest.fixture()
def reviews(db):
    return [mixer.blend('reviews.review') for _ in range(3)]


def get_client(user=None):
    res = APIClient()
    if user is not None:
        res.force_login(user)
    return res


def parse(response):
    response.render()
    content = response.content.decode()
    return json.loads(content)


def contains(response, key, value):
    obj = parse(response)
    if key not in obj:
        return False
    return value in obj[key]


def test_review_anon_user_get_nothing():
    path = reverse('reviews-list')
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_review_user_get_list(reviews):
    path = reverse('reviews-list')
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == len(reviews)


def test_review_retrieve_a_single_review(reviews):
    path = reverse('reviews-detail', kwargs={'pk': reviews[0].pk})
    client = get_client(reviews[0].author)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert obj['title'] == reviews[0].title


def test_review_add_a_new_review(reviews, admin_user):
    path = reverse('reviews-list')
    client = get_client(admin_user)
    response = client.post(path, data={'author': reviews[0].author.pk})
    assert response.status_code == HTTP_201_CREATED
    obj = parse(response)
    #assert obj['title'] == 'Foo'
