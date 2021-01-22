from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
from django.utils import tree
# Create your models here.
from smart_selects.db_fields import ChainedForeignKey

class testout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null = True)
    phone_number = models.CharField(max_length=12, null=True)
    notes = models.TextField(null=True)
    items =models.JSONField(default=dict) 
        
    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=128, null=True)
    comments = models.TextField(max_length=128, null = True)

    def __repr__(self) -> str:
        return self.language

class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100, null=True)
    currency_code = models.CharField(max_length=30, null=True)
    currency_name = models.CharField(max_length=100, null=True)
    currency_symbol = models.CharField(max_length=30, null=True)
    comments = models.TextField(max_length=255, null=True)
    
    def __str__(self) -> str:
        return self.currency_name

class country_information(models.Model):
    country_id =  models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=128, null=True)
    nationality = models.CharField(max_length=128, null=True)
    dailing_code = models.CharField(max_length=128, null=True)
    country_name = models.CharField(max_length=128, null=True)
    currency_id = models.ForeignKey('Currency', on_delete=models.CASCADE, null=True)
    language_id = models.ForeignKey('Language', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.country_name


class section_template(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=128, null=True)
    section_desc = models.TextField(null=True)
    display_order = models.IntegerField(null=True)
    display_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.section_name



class JobDescriptionTemplate(models.Model):
    job_desc_id = models.AutoField (primary_key=True)
    description_title = models.CharField(max_length=255, null=True)
    organisation_description = models.CharField(max_length=255, null=True)
    organisation_job_description = models.TextField(null=True)
    qualifications_required = models.CharField(max_length=255, null=True)
    skills_required = models.CharField(max_length=255, null=True)
    essential_information = models.CharField(max_length=255, null=True)
    desired_information = models.CharField(max_length=255, null=True)
    comments = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.description_title




class IssueAuthority(models.Model):
    issue_authority_id = models.AutoField(primary_key=True)
    issue_country_id = models.ForeignKey('country_information', null=False,on_delete=models.CASCADE)
    # issue_authority_candidate_type_id = models.ForeignKey('issue_authority_candidate_type.id', null=True)
    authority_name = models.CharField(max_length=255, null=True)
    acronym = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    deleted = models.BooleanField(default=False)
    licensing = models.BooleanField(default=False)
    qualification = models.BooleanField(default=False)

    # relations
    # issue_country = relationship('CountryInfo')
    # issue_authority_candidate_type = relationship(
    #     'IssueAuthorityCandidateType', foreign_keys=[issue_authority_candidate_type_id])

    # def __repr__(self):
    #     return "{}/{}/{}".format(self.issue_authority_id, self.issue_country, self.authority_name)



class Qualification(models.Model):
    qualification_id = models.AutoField(primary_key=True)
    qualification_classification_id = models.ForeignKey('QualificationClassification', on_delete=models.CASCADE, null=True)
    country_id = models.ForeignKey('country_information', on_delete=models.CASCADE)
    qualification = models.CharField(max_length=128, null=True)
    qualification_level = models.IntegerField(null=True)
    description = models.CharField(max_length=255, null=True)
    acronym = models.CharField(max_length=128, null=True)
    english_translation = models.CharField(max_length=128, null=True)
    specialist_registration_reqd = models.BooleanField(default=False, null=True)
    by_exam = models.BooleanField(default=False)
    course_duration_reqd = models.BooleanField(default=False, null=True)
    comments = models.CharField(default=False, null=True, max_length=128)
    allow_subject_input = models.BooleanField(default=False, null=True)
    display_order = models.IntegerField(null=True)
    equivalent_qualification = models.BooleanField(default=False, null=True)


class CandidateType(models.Model):
    candidate_type_id = models.AutoField(primary_key=True)
    candidate_type = models.CharField(max_length=128, null=True)
    comments = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.candidate_type

class CandidateLevel(models.Model):
    level_id = models.AutoField(primary_key=True)
    candidate_type_id = models.ForeignKey('CandidateType', on_delete=models.CASCADE, null=True)
    country_id = models.ForeignKey('country_information', on_delete=models.CASCADE, null=True)
    issue_authority_id = models.ForeignKey('IssueAuthority', on_delete=models.CASCADE, null=True)
    candidate_level = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=128, null=True)
    seniority = models.IntegerField(null=True)
    comments = models.CharField(max_length=128, null=True)

    # candidate_type = relationship('CandidateType')
    # country = relationship('CountryInfo')
    # issue_authority = relationship('IssueAuthority')

    def __repr__(self):
        return self.candidate_level

class QualificationClassification(models.Model):
    qualification_classification_id = models.AutoField(primary_key=True)
    candidate_type_id = models.ForeignKey('CandidateType',on_delete=models.CASCADE, null=True)
    level_id = models.ForeignKey('CandidateLevel',on_delete=models.CASCADE, null=True)
    qualification_classification = models.CharField(max_length=128, null=True)
    sort_level = models.IntegerField(null=True) 
    description = models.CharField(max_length=128, null=True)

    # candidate_type = relationship('CandidateType')
    # level = relationship('CandidateLevel')

    def __repr__(self):
        return self.qualification_classification



class PqrHeader(models.Model):
    pqr_header_id = models.AutoField(primary_key=True)
    country_id = models.ForeignKey('country_information', on_delete=models.CASCADE)
    issue_authority_id = models.ForeignKey('IssueAuthority', on_delete=models.CASCADE)
    pqr_name = models.CharField(null=True, max_length=128)
    issue_date = models.DateField(null=True)
    version_no = models.IntegerField(null=True)
    description = models.CharField(null=True, max_length=255)
    comments = models.CharField(null=True, max_length=255)

    # country = relationship('CountryInfo')
    # issue_authority = relationship('IssueAuthority')

    # @property
    # def country_name(self):
    #     if self.country_id:
    #         return self.country.country_name

    # @property
    # def issue_authority_name(self):
    #     if self.issue_authority_id:
    #         return self.issue_authority.authority_name

    # def __str__(self):
    #     return self.pqr_name




class PqrDetail(models.Model):
    pqr_detail_id = models.AutoField(primary_key=True)
    pqr_header_id = models.ForeignKey('PqrHeader',on_delete=models.CASCADE, null=True)
    candidate_type_id = models.ForeignKey('CandidateType', on_delete=models.CASCADE, null=True)
    level_id = models.ForeignKey('CandidateLevel', on_delete=models.CASCADE, null=True)
    qual_country_id = models.ForeignKey('country_information', on_delete=models.CASCADE, null=True)
    qualification_classification_id = models.ForeignKey('QualificationClassification', on_delete=models.CASCADE, null=True)
    qualification_id = models.ForeignKey('Qualification', on_delete=models.CASCADE, null=True)
    issue_authority_id = models.ForeignKey('IssueAuthority', on_delete=models.CASCADE, null=True)
    dependent_pqr_detail_id = models.ForeignKey('PqrDetail', on_delete=models.CASCADE, null=True)
    surgical = models.BooleanField(default=False, null=True)
    min_years_exp = models.IntegerField(null=True)
    min_years_exp_for_nationals = models.IntegerField(null=True)
    specialist_registration_held = models.BooleanField(default=False, null=True)
    specialist_reg_required_for_nationals = models.BooleanField(default=False, null=True)
    specialist_registration_years = models.IntegerField(null=True)
    check_equivalence = models.BooleanField(default=False, null=True)
    description = models.CharField(null=True, max_length=255)
    comments = models.CharField(null=True, max_length=255)





class Continent(models.Model):
    name = models.CharField(max_length=128)

class Country(models.Model):
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

class Location(models.Model):
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE) 
    country = ChainedForeignKey(
        Country,
        chained_field="continent",
        chained_model_field="continent",
        show_all=False,
        auto_choose=True,
        sort=True
        )
    
    # area = 
    city =  models.CharField(max_length=128)
    street =  models.CharField(max_length=128)