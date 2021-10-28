# faker_animal
Provider for Faker which adds fake animal names.

# Usage
```python
from faker import Faker

from faker_animal import AnimalProvider

fake = Faker()
fake.add_provider(AnimalProvider)

fake.animal()
# Narwhal
```