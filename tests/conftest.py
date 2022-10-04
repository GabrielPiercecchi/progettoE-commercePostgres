import pytest

from ecommerce.user.models import User


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """Fixture to execute before and after a test is run"""

    from config_test_db import override_get_db
    database = next(override_get_db())
    new_user = User(name='John', email='john@gmail.com', password='johnny123')
    database.add(new_user)
    database.commit()

    yield  # This is where testing happens

    # teardown
    database.query(User).filter(User.email == 'john@gmail.com').delete()
    database.commit()
