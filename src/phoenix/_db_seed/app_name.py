# from app_name.models import Sample, Another
#
#
# class SamplesGenerator:
#     @staticmethod
#     def create_samples():
#         """Creates sample objects from Sample model."""
#
#         print("Creating samples..")
#
#         samples = [
#             Sample(some_attr=i)
#             for i in range(10)
#         ]
#         Sample.objects.bulk_create(samples)
#
#         print("Done!")
#
#
# class AnothersGenerator:
#     @staticmethod
#     def create_anothers():
#         """Creates sample objects from Another model."""
#
#         print("Creating anothers..")
#
#         anothers = [
#             Another(some_attr=i)
#             for i in range(10)
#         ]
#         Another.objects.bulk_create(anothers)
#
#         print("Done!")
