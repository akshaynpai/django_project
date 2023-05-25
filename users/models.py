# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountLists(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_name = models.CharField(max_length=191)
    initial_balance = models.FloatField()
    account_number = models.CharField(max_length=191)
    branch_code = models.CharField(max_length=191)
    bank_branch = models.CharField(max_length=191)
    created_by = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_lists'


class AllowanceOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allowance_options'


class Allowances(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    allowance_option = models.IntegerField()
    title = models.CharField(max_length=191)
    amount = models.FloatField()
    type = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allowances'


class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    start_date = models.DateField()
    end_date = models.DateField()
    branch_id = models.IntegerField()
    department_id = models.CharField(max_length=191)
    employee_id = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcements'


class AttendanceEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=191)
    clock_in = models.TimeField()
    clock_out = models.TimeField()
    late = models.TimeField()
    early_leaving = models.TimeField()
    overtime = models.TimeField()
    total_rest = models.TimeField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_employees'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Branches(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'


class ChMessages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=191)
    from_id = models.BigIntegerField()
    to_id = models.BigIntegerField()
    body = models.CharField(max_length=5000, blank=True, null=True)
    attachment = models.CharField(max_length=191, blank=True, null=True)
    seen = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_messages'


class Commissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    title = models.CharField(max_length=191)
    amount = models.FloatField()
    type = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commissions'


class DeductionOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deduction_options'


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_id = models.IntegerField()
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Designations(models.Model):
    id = models.BigAutoField(primary_key=True)
    department_id = models.IntegerField()
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designations'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    is_required = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class DucumentUploads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    role = models.CharField(max_length=191)
    document = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ducument_uploads'


class EmailTemplateLangs(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.IntegerField()
    lang = models.CharField(max_length=100)
    subject = models.CharField(max_length=191)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_langs'


class EmailTemplates(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    from_field = models.CharField(db_column='from', max_length=191, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    slug = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates'


class EmployeeDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    document_id = models.IntegerField()
    document_value = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_documents'


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=191)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=191)
    phone = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    vp = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=225, blank=True, null=True)
    employee_id = models.CharField(max_length=191)
    branch_id = models.IntegerField()
    department_id = models.IntegerField()
    designation_id = models.IntegerField()
    company_doj = models.CharField(max_length=191, blank=True, null=True)
    documents = models.CharField(max_length=191, blank=True, null=True)
    account_holder_name = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    bank_identifier_code = models.CharField(max_length=191, blank=True, null=True)
    branch_location = models.CharField(max_length=191, blank=True, null=True)
    tax_payer_id = models.CharField(max_length=191, blank=True, null=True)
    salary_type = models.IntegerField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField()
    api_token = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class EventEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_id = models.IntegerField()
    employee_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_employees'


class Events(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_id = models.IntegerField()
    department_id = models.TextField()
    employee_id = models.TextField()
    title = models.CharField(max_length=191)
    start_date = models.DateField()
    end_date = models.DateField()
    color = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class ExperienceCertificates(models.Model):
    id = models.BigAutoField(primary_key=True)
    lang = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experience_certificates'


class GenerateOfferLetters(models.Model):
    id = models.BigAutoField(primary_key=True)
    lang = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generate_offer_letters'


class GoalTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal_types'


class IpRestricts(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_restricts'


class JobApplicationNotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    application_id = models.IntegerField()
    note_created = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_application_notes'


class JobStages(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    order = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_stages'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    requirement = models.TextField(blank=True, null=True)
    branch = models.IntegerField()
    category = models.IntegerField()
    skill = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    applicant = models.CharField(max_length=191, blank=True, null=True)
    visibility = models.CharField(max_length=191, blank=True, null=True)
    code = models.CharField(max_length=191, blank=True, null=True)
    custom_question = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class JoiningLetters(models.Model):
    id = models.BigAutoField(primary_key=True)
    lang = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joining_letters'


class LandingPageSections(models.Model):
    id = models.BigAutoField(primary_key=True)
    section_name = models.CharField(max_length=191)
    section_order = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    section_type = models.CharField(max_length=12)
    default_content = models.TextField()
    section_demo_image = models.TextField()
    section_blade_file_name = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'landing_page_sections'


class LeaveTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    days = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_types'


class LoanOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_options'


class Meetings(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_id = models.IntegerField()
    department_id = models.TextField()
    employee_id = models.TextField()
    title = models.CharField(max_length=191)
    date = models.DateField()
    time = models.TimeField()
    note = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)  # The composite primary key (permission_id, model_id, model_type) found, that is not supported. The first column is selected.
    model_type = models.CharField(max_length=191)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)  # The composite primary key (role_id, model_id, model_type) found, that is not supported. The first column is selected.
    model_type = models.CharField(max_length=191)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class NocCertificates(models.Model):
    id = models.BigAutoField(primary_key=True)
    lang = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noc_certificates'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Payees(models.Model):
    id = models.BigAutoField(primary_key=True)
    payee_name = models.CharField(max_length=191)
    contact_number = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payees'


class Payers(models.Model):
    id = models.BigAutoField(primary_key=True)
    payer_name = models.CharField(max_length=191)
    contact_number = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payers'


class PaymentTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_types'


class PayslipTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payslip_types'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Products(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=225, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Promotions(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    designation_id = models.IntegerField()
    promotion_title = models.CharField(max_length=191)
    promotion_date = models.DateField()
    description = models.CharField(max_length=191)
    created_by = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotions'


class Resignations(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    notice_date = models.DateField()
    resignation_date = models.DateField()
    description = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resignations'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)  # The composite primary key (permission_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SaturationDeductions(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    deduction_option = models.IntegerField()
    title = models.CharField(max_length=191)
    amount = models.FloatField()
    type = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saturation_deductions'


class SetSalaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_salaries'


class Settings(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    value = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'
        unique_together = (('name', 'created_by'),)


class TblEmployeeLogin(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    login_date = models.DateField(blank=True, null=True)
    login_time = models.TimeField(blank=True, null=True)
    logout_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_login'


class TblOrderDetails(models.Model):
    int_product_id = models.AutoField(primary_key=True)
    int_shop = models.ForeignKey('TblShopVisit', models.DO_NOTHING)
    product_name = models.CharField(max_length=250)
    product_quantity = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_order_details'


class TblShop(models.Model):
    int_shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    str_email = models.CharField(max_length=25)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50,null=True)
    pincode = models.IntegerField()
    str_instructions = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_shop'


class TblShopVisit(models.Model):
    login = models.ForeignKey(TblEmployeeLogin, models.DO_NOTHING)
    employee_id = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    type_visit = models.CharField(max_length=50, blank=True, null=True)
    marketing_note = models.CharField(max_length=100, blank=True, null=True)
    instructions = models.CharField(max_length=200, blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    sum = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_shop_visit'


class TerminationTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'termination_types'


class Terminations(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    notice_date = models.DateField()
    termination_date = models.DateField()
    termination_type = models.CharField(max_length=191)
    description = models.TextField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terminations'


class TicketReplies(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket_id = models.IntegerField()
    employee_id = models.IntegerField()
    description = models.CharField(max_length=191)
    created_by = models.IntegerField()
    is_read = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_replies'


class Tickets(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    employee_id = models.IntegerField()
    priority = models.CharField(max_length=191)
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    ticket_code = models.CharField(max_length=191)
    ticket_created = models.IntegerField()
    created_by = models.IntegerField()
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class TimeSheets(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    date = models.DateField()
    hours = models.FloatField()
    remark = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_sheets'


class Trainers(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.CharField(max_length=191)
    firstname = models.CharField(max_length=191)
    lastname = models.CharField(max_length=191)
    contact = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    address = models.TextField(blank=True, null=True)
    expertise = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers'


class TrainingTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_types'


class Trainings(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.IntegerField()
    trainer_option = models.IntegerField()
    training_type = models.IntegerField()
    trainer = models.IntegerField()
    training_cost = models.FloatField()
    employee = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    performance = models.IntegerField()
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainings'


class TransferBalances(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_account_id = models.IntegerField()
    to_account_id = models.IntegerField()
    date = models.DateField()
    amount = models.IntegerField()
    payment_type_id = models.IntegerField()
    referal_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer_balances'


class Transfers(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    branch_id = models.IntegerField()
    department_id = models.IntegerField()
    transfer_date = models.DateField()
    description = models.CharField(max_length=191)
    created_by = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfers'


class Travels(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    purpose_of_visit = models.CharField(max_length=191)
    place_of_visit = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    created_by = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travels'


class UserEmailTemplates(models.Model):
    id = models.BigAutoField(primary_key=True)
    template_id = models.IntegerField()
    user_id = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_email_templates'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    avatar = models.CharField(max_length=191, blank=True, null=True)
    lang = models.CharField(max_length=191)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    created_by = models.CharField(max_length=191)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    messenger_color = models.CharField(max_length=191)
    dark_mode = models.IntegerField()
    active_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Warnings(models.Model):
    id = models.BigAutoField(primary_key=True)
    warning_to = models.IntegerField()
    warning_by = models.IntegerField()
    subject = models.CharField(max_length=191)
    warning_date = models.DateField()
    description = models.CharField(max_length=191)
    created_by = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warnings'


class ZoomMeetings(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191, blank=True, null=True)
    meeting_id = models.CharField(max_length=191)
    user_id = models.CharField(max_length=191)
    password = models.CharField(max_length=191, blank=True, null=True)
    start_date = models.DateTimeField()
    duration = models.IntegerField()
    start_url = models.TextField(blank=True, null=True)
    join_url = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zoom_meetings'
