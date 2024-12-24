from django.db import models
from django_countries.fields import CountryField  # For standard country field

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Project Name")
    description = models.TextField(blank=True, null=True, verbose_name="Project Description")
    created_by = models.ForeignKey(
        'users.CustomUser', related_name='projects', on_delete=models.CASCADE, verbose_name="Creator"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        'users.CustomUser', related_name='modified_projects', on_delete=models.SET_NULL, null=True, blank=True
    )
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SampleProvider(models.Model):
    name = models.CharField(max_length=100, verbose_name="Provider Name")
    short_name = models.CharField(max_length=10, verbose_name="Short Name", unique=True)
    address = models.TextField(verbose_name="Address")
    country = CountryField(verbose_name="Country")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Contact Email")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    provided_by = models.ForeignKey(
        'users.CustomUser', related_name='sample_providers', on_delete=models.CASCADE, verbose_name="Added By"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Species(models.Model):
    order = models.CharField(max_length=100, verbose_name="Order")
    family = models.CharField(max_length=100, verbose_name="Family")
    genus = models.CharField(max_length=100, verbose_name="Genus")
    scientific_name = models.CharField(max_length=100, unique=True, verbose_name="Scientific Name")
    common_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Common Name")
    subspecies = models.CharField(max_length=100, blank=True, null=True, verbose_name="Subspecies")
    added_by = models.ForeignKey(
        'users.CustomUser', related_name='species', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Added By"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.scientific_name

class Storaging(models.Model):
    name = models.CharField(max_length=100, verbose_name="Location Name")
    short_name = models.CharField(max_length=10, verbose_name="Short Name", unique=True)
    type = models.CharField(max_length=100, verbose_name="Type")

    def __str__(self):
        return self.name


class Sample(models.Model):
    species = models.ForeignKey(Species, related_name='samples', on_delete=models.CASCADE, verbose_name="Species")
    sample_provider = models.ForeignKey(
        SampleProvider, related_name='samples', on_delete=models.CASCADE, verbose_name="Sample Provider"
    )
    project = models.ForeignKey(
        Project, related_name='samples', on_delete=models.CASCADE, verbose_name="Project"
    )
    created_by = models.ForeignKey(
        'users.CustomUser', related_name='samples', on_delete=models.CASCADE, verbose_name="Created By"
    )
    storaging = models.ForeignKey(
        Storaging, related_name='samples', on_delete=models.CASCADE, verbose_name="Storage Location"
    )
    uid = models.CharField(max_length=10, unique=True, verbose_name="Unique Identifier")
    name = models.CharField(max_length=100, verbose_name="Sample Name")
    description = models.TextField(blank=True, null=True, verbose_name="Sample Description")
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_samples = models.PositiveIntegerField(default=1, verbose_name="Number of Subsamples")
    collection_date = models.DateField(blank=True, null=True, verbose_name="Collection Date")
    modified_by = models.ForeignKey(
        'users.CustomUser', related_name='modified_samples', on_delete=models.SET_NULL, null=True, blank=True
    )
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (UID: {self.uid})"
    
    def save(self, *args, **kwargs):
        samples_to_create = []
        max_id = Sample.objects.all().aggregate(models.Max('id'))['id__max']
        if max_id is None:
            max_id = 0
        self.uid = 'LME' + str(max_id + 1).zfill(4)
        if self.number_of_samples > 1:
            for _ in range(self.number_of_samples):
                sample = Sample(
                    species=self.species,
                    sample_provider=self.sample_provider,
                    project=self.project,
                    created_by=self.created_by,
                    storaging=self.storaging,
                    uid=self.uid,
                    name=self.name,
                    description=self.description,
                    collection_date=self.collection_date
                )
                max_id += 1
                self.uid = 'LME' + str(max_id + 1).zfill(4)
                samples_to_create.append(sample)
            Sample.objects.bulk_create(samples_to_create)
        else:
            super(Sample, self).save(*args, **kwargs)
