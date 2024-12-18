import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from mixer.backend.django import mixer


def test_reviews_title_of_length_51_raises_exception(db):
    review = mixer.blend('reviews.review', title='A'*51)
    with pytest.raises(ValidationError) as err:
        review.full_clean()
    assert 'at most 50 characters' in '\n'.join(err.value.messages)

def test_reviews_title_not_null(db):
    review = mixer.blend('reviews.review')
    review.title = None
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_reviews_title_not_empty(db):
    review = mixer.blend('reviews.review')
    review.title = ''
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_reviews_content_too_much(db):
    review = mixer.blend('reviews.review')
    review.content = "A "*1000
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_reviews_content_too_short(db):
    review = mixer.blend('reviews.review')
    review.content = ""
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_reviews_content_not_null(db):
    review = mixer.blend('reviews.review')
    review.content = None
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_reviews_genre_of_length_51_raises_exception(db):
    review = mixer.blend('reviews.review', genre='A'*51)
    with pytest.raises(ValidationError) as err:
        review.full_clean()
    assert 'at most 50 characters' in '\n'.join(err.value.messages)

def test_reviews_genre_not_null(db):
    review = mixer.blend('reviews.review')
    review.genre = None
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_reviews_genre_not_empty(db):
    review = mixer.blend('reviews.review')
    review.genre = ''
    with pytest.raises(ValidationError) as err:
        review.full_clean()
def test_reviews_venue_of_length_51_raises_exception(db):
    review = mixer.blend('reviews.review', venue='A'*51)
    with pytest.raises(ValidationError) as err:
        review.full_clean()
    assert 'at most 50 characters' in '\n'.join(err.value.messages)

def test_reviews_venue_not_null(db):
    review = mixer.blend('reviews.review')
    review.venue = None
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_reviews_venue_not_empty(db):
    review = mixer.blend('reviews.review')
    review.venue = ''
    with pytest.raises(ValidationError) as err:
        review.full_clean()

def test_review_rating_default_value_is_zero(db):
    review = mixer.blend('reviews.review')
    assert review.rating == 0


def test_review_rating_allows_valid_values(db):
    review = mixer.blend('reviews.review', rating=5)
    review.full_clean()  # Non dovrebbe sollevare eccezioni


def test_review_rating_negative_value_raises_exception(db):
    review = mixer.blend('reviews.review', rating=-1)
    with pytest.raises(ValidationError) as err:
        review.full_clean()
def test_review_rating_value_too_high(db):
    review = mixer.blend('reviews.review', rating=11)
    with pytest.raises(ValidationError) as err:
        review.full_clean()
def test_review_return_title(db):
    review = mixer.blend('reviews.review')
    stringa = review.__str__()
    assert stringa == review.title

def test_date_concert_accepts_positive_integer(db):
    review = mixer.blend('reviews.review', date_concert=2024)
    review.full_clean()  # Non dovrebbe sollevare eccezioni
    assert review.date_concert == 2024
def test_review_date_concert_negative_value_raises_exception(db):
    review = mixer.blend('reviews.review', rating=-1)
    with pytest.raises(ValidationError) as err:
        review.full_clean()