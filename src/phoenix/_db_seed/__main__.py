import os
import sys
from pathlib import Path

import django

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phoenix.settings")
django.setup()

# from _db_seed.app_name import SamplesGenerator, AnothersGenerator


if __name__ == "__main__":
    print("Running database seeding..")

    # SamplesGenerator.create_samples()
    # AnothersGenerator.create_anothers()

    print("Finished seeding database successfully!")
