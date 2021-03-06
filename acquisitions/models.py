from django.db import models
from django.core.validators import RegexValidator, ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from ordered_model.models import OrderedModel


# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=100, blank=False)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    omb_agency_code = models.IntegerField(null=True, blank=True)
    omb_bureau_code = models.IntegerField(null=True, blank=True)
    treasury_agency_code = models.IntegerField(null=True, blank=True)
    cgac_agency_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Agencies"
        ordering = ('name',)


class Subagency(models.Model):
    name = models.CharField(max_length=100, blank=False)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    agency = models.ForeignKey(Agency)

    def __str__(self):
        return "%s - %s" % (self.agency, self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Subagencies"


class ContractingOffice(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contracting Office"
        verbose_name_plural = "Contracting Offices"


class ContractingOfficer(models.Model):
    name = models.CharField(max_length=100)
    contracting_office = models.ForeignKey(ContractingOffice)

    def __str__(self):
        return "%s - %s" % (self.name, self.contracting_office)

    class Meta:
        ordering = ('name',)
        verbose_name = "Contracting Officer"
        verbose_name_plural = "Contracting Officers"


class COR(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Contracting Officer Representative"
        verbose_name_plural = "Contracting Officer Representatives"


# Is the acquisition internal or external?
class Track(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.name)


class Stage(OrderedModel):
    name = models.CharField(max_length=50)
    wip_limit = models.IntegerField(default=0, verbose_name="WIP Limit")

    def __str__(self):
        return "%s" % (self.name)

    class Meta(OrderedModel.Meta):
        pass


class Actor(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return "%s" % (self.name)


class Step(models.Model):
    actor = models.ForeignKey(
        Actor,
        blank=False
    )
    track = models.ManyToManyField(
        Track,
        blank=False,
        through="StepTrackThroughModel"
    )
    stage = models.ForeignKey(
        Stage,
        blank=False
    )

    def __str__(self):
        return "%s - %s" % (self.stage, self.actor,)

    class Meta:
        ordering = ('steptrackthroughmodel__order',)


class StepTrackThroughModel(OrderedModel):
    track = models.ForeignKey(Track)
    step = models.ForeignKey(Step)
    wip_limit = models.IntegerField(default=0, verbose_name="WIP Limit")
    order_with_respect_to = 'track'

    class Meta(OrderedModel.Meta):
        unique_together = ('track', 'step')
        ordering = ('track', 'order')


class Vendor(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    duns = models.CharField(max_length=9, blank=False, validators=[
        RegexValidator(regex='^\d{9}$', message="DUNS number must be 9 digits")
    ])

    def __str__(self):
        return self.name


class Role(models.Model):
    description = models.CharField(max_length=100, choices=(
            ('P', 'Product Lead'),
            ('A', 'Acquisition Lead'),
            ('T', 'Technical Lead')
        ), null=True, blank=True)
    teammate = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.get_description_display(), self.teammate)


class Acquisition(models.Model):
    SET_ASIDE_CHOICES = (
        ("AbilityOne", "AbilityOne"),
        ("HUBZone Small Business", "HUBZone Small Business"),
        ("Multiple Small Business Categories",
            "Multiple Small Business Categories"),
        ("Other Than Small", "Other Than Small"),
        ("Service Disabled Veteran-owned Small Business",
            "Service Disabled Veteran-owned Small Business"),
        ("Small Business", "Small Business"),
        ("Small Disadvantaged Business (includes Section 8a)",
            "Small Disadvantaged Business (includes Section 8a)"),
        ("To Be Determined-BPA", "To Be Determined-BPA"),
        ("To Be Determined-IDIQ", "To Be Determined-IDIQ"),
        ("Veteran-Owned Small Business", "Veteran-Owned Small Business"),
        ("Woman-Owned Small Business", "Woman-Owned Small Business"),
    )

    CONTRACT_TYPE_CHOICES = (
        ("Cost No Fee", "Cost No Fee"),
        ("Cost Plus Award Fee", "Cost Plus Award Fee"),
        ("Cost Plus Fixed Fee", "Cost Plus Fixed Fee"),
        ("Cost Plus Incentive Fee", "Cost Plus Incentive Fee"),
        ("Cost Sharing", "Cost Sharing"),
        ("Fixed Price Award Fee", "Fixed Price Award Fee"),
        ("Fixed Price Incentive", "Fixed Price Incentive"),
        ("Fixed Price Labor Hours", "Fixed Price Labor Hours"),
        ("Fixed Price Level of Effort", "Fixed Price Level of Effort"),
        ("Fixed Price Time and Materials", "Fixed Price Time and Materials"),
        ("Fixed Price with Economic Price Adjustment",
            "Fixed Price with Economic Price Adjustment"),
        ("Fixed Price", "Fixed Price"),
        ("Interagency Agreement", "Interagency Agreement"),
        ("Labor Hours and Time and Materials",
            "Labor Hours and Time and Materials"),
        ("Labor Hours", "Labor Hours"),
        ("Order Dependent", "Order Dependent"),
        ("Time and Materials", "Time and Materials"),
    )

    COMPETITION_STRATEGY_CHOICES = (
        ("A/E Procedures", "A/E Procedures"),
        ("Competed under SAP", "Competed under SAP"),
        ("Competitive Delivery Order Fair Opportunity Provided",
            "Competitive Delivery Order Fair Opportunity Provided"),
        ("Competitive Schedule Buy", "Competitive Schedule Buy"),
        ("Fair Opportunity", "Fair Opportunity"),
        ("Follow On to Competed Action (FAR 6.302-1)",
            "Follow On to Competed Action (FAR 6.302-1)"),
        ("Follow On to Competed Action", "Follow On to Competed Action"),
        ("Full and Open after exclusion of sources (competitive small business \
            set-asides, competitive 8a)",
            "Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)"),
        ("Full and Open Competition Unrestricted",
            "Full and Open Competition Unrestricted"),
        ("Full and Open Competition", "Full and Open Competition"),
        ("Limited Sources FSS Order", "Limited Sources FSS Order"),
        ("Limited Sources", "Limited Sources"),
        ("Non-Competitive Delivery Order", "Non-Competitive Delivery Order"),
        ("Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)",
            "Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)"),
        ("Not Competed (e.g., sole source, urgency, etc., all > SAT)",
            "Not Competed (e.g., sole source, urgency, etc., all > SAT)"),
        ("Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)",
            "Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)"),
        ("Partial Small Business Set-Aside",
            "Partial Small Business Set-Aside"),
        ("Set-Aside", "Set-Aside"),
        ("Sole Source", "Sole Source"),
    )

    PROCUREMENT_METHOD_CHOICES = (
        ("Ability One", "Ability One"),
        ("Basic Ordering Agreement", "Basic Ordering Agreement"),
        ("Blanket Purchase Agreement-BPA", "Blanket Purchase Agreement-BPA"),
        ("BPA Call", "BPA Call"),
        ("Call Order under GSA Schedules BPA",
            "Call Order under GSA Schedules BPA"),
        ("Commercial Item Contract", "Commercial Item Contract"),
        ("Contract modification", "Contract modification"),
        ("Contract", "Contract"),
        ("Definitive Contract other than IDV",
            "Definitive Contract other than IDV"),
        ("Definitive Contract", "Definitive Contract"),
        ("Government-wide Agency Contract-GWAC",
            "Government-wide Agency Contract-GWAC"),
        ("GSA Schedule Contract", "GSA Schedule Contract"),
        ("GSA Schedule", "GSA Schedule"),
        ("GSA Schedules Program BPA", "GSA Schedules Program BPA"),
        ("Indefinite Delivery Indefinite Quantity-IDIQ",
            "Indefinite Delivery Indefinite Quantity-IDIQ"),
        ("Indefinite Delivery Vehicle (IDV)",
            "Indefinite Delivery Vehicle (IDV)"),
        ("Indefinite Delivery Vehicle Base Contract",
            "Indefinite Delivery Vehicle Base Contract"),
        ("Multi-Agency Contract", "Multi-Agency Contract"),
        ("Negotiated", "Negotiated"),
        ("Order under GSA Federal Supply Schedules Program",
            "Order under GSA Federal Supply Schedules Program"),
        ("Order under GSA Schedules Program BPA",
            "Order under GSA Schedules Program BPA"),
        ("Order under GSA Schedules Program",
            "Order under GSA Schedules Program"),
        ("Order under IDV", "Order under IDV"),
        ("Purchase Order", "Purchase Order"),
        ("Sealed Bid", "Sealed Bid"),
    )

    subagency = models.ForeignKey(Subagency)
    task = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    track = models.ForeignKey(
            Track,
            blank=False,
            related_name="%(class)s_track"
    )
    step = ChainedForeignKey(
            Step,
            chained_field="track",
            chained_model_field="track",
            blank=False
    )
    dollars = models.DecimalField(decimal_places=2, max_digits=14, null=True,
                                  blank=True)
    period_of_performance = models.DateField(null=True, blank=True)
    product_owner = models.CharField(max_length=50, null=True, blank=True)
    roles = models.ManyToManyField(Role, blank=True)
    contracting_officer = models.ForeignKey(ContractingOfficer, null=True,
                                            blank=True)
    contracting_officer_representative = models.ForeignKey(COR, null=True,
                                                           blank=True)
    contracting_office = models.ForeignKey(ContractingOffice, null=True,
                                           blank=True)
    vendor = models.ForeignKey(Vendor, null=True, blank=True)
    rfq_id = models.IntegerField(null=True, blank=True, verbose_name="RFQ ID")
    naics = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="NAICS Code"
    )
    set_aside_status = models.CharField(max_length=100, null=True, blank=True,
                                        choices=SET_ASIDE_CHOICES)
    amount_of_competition = models.IntegerField(null=True, blank=True)
    contract_type = models.CharField(max_length=100, null=True, blank=True,
                                     choices=CONTRACT_TYPE_CHOICES)
    competition_strategy = models.CharField(
            max_length=100,
            null=True,
            blank=True,
            choices=COMPETITION_STRATEGY_CHOICES)
    procurement_method = models.CharField(
            max_length=100,
            null=True,
            blank=True,
            choices=PROCUREMENT_METHOD_CHOICES)
    award_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)

    def clean(self):
        print(self.step.track.all())
        print(self.track)
        if self.track not in self.step.track.all():
            raise ValidationError(_('Tracks are not equal.'))

    def __str__(self):
        return "%s (%s)" % (self.task, self.subagency)


class Evaluator(models.Model):
    name = models.CharField(max_length=100)
    acquisition = models.ManyToManyField(Acquisition)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Release(models.Model):
    acquisition = models.ForeignKey(Acquisition)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)
