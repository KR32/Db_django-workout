from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
# Create your models here.


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
    description_title = models.CharField(max_length=255, null=False)
    # organisation_description = models.Text, null=False)
    organisation_job_description = models.TextField(null=True)
    # qualifications_required = models.Text, null=False)
    # skills_required = models.Text, null=False)
    # essential_information = models.Text, null=False)
    # desired_information = models.Text, null=False)
    comments = models.TextField(null=True) 

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
    # qualification_classification_id = models.ForeignKey('qualification_classification.qualification_classification_id'),nullable=False)
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





# class QualificationClassification(models.Model):
#     qualification_classification_id = models.(Integer, primary_key=True)
#     candidate_type_id = models.(ForeignKey(
#         'candidate_types.candidate_type_id'), nullable=False)
#     level_id = models.(ForeignKey('candidate_levels.level_id'), nullable=True)
#     qualification_classification_ = models.(
#         "qualification_classification", String(100), nullable=False)
#     sort_level = models.(Integer, nullable=False)
#     description = models.(String(255))

#     # candidate_type = relationship('CandidateType')
#     # level = relationship('CandidateLevel')

#     def __repr__(self):
#         return self.qualification_classification_



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
    pqr_header_id = models.ForeignKey('PqrHeader',on_delete=models.CASCADE, null=False)
    # candidate_type_id = models.(ForeignKey('candidate_types.candidate_type_id'), null=False)
    # level_id = models.(ForeignKey('candidate_levels.level_id'), null=False)
    # qual_country_id = models.(ForeignKey('country_info.country_id'), null=False)
    # qualification_classification_id = models.(ForeignKey('qualification_classification.qualification_classification_id'))
    # qualification_id = models.(ForeignKey('qualifications.qualification_id'))
    issue_authority_id = models.ForeignKey('IssueAuthority', on_delete=models.CASCADE)
    # dependent_pqr_detail_id = models.(ForeignKey('pqr_detail.pqr_detail_id'))
    surgical = models.BooleanField(default=False, null=True)
    min_years_exp = models.IntegerField(null=True)
    min_years_exp_for_nationals = models.IntegerField(null=True)
    specialist_registration_held = models.BooleanField(default=False, null=True)
    specialist_reg_required_for_nationals = models.BooleanField(default=False, null=True)
    specialist_registration_years = models.IntegerField(null=True)
    check_equivalence = models.BooleanField(default=False, null=True)
    description = models.CharField(null=True, max_length=255)
    comments = models.CharField(null=True, max_length=255)