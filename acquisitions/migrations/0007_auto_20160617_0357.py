# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acquisitions', '0006_auto_20160609_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquisition',
            name='competition_strategy',
            field=models.CharField(blank=True, choices=[('Sole Source', 'Sole Source'), ('Full and Open', 'Full and Open'), ('Set-Aside', 'Set-Aside'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside'), ('A/E Procedures', 'A/E Procedures'), ('Full and Open Competition', 'Full and Open Competition'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Follow On to Competed Action', 'Follow On to Competed Action'), ('Competed under SAP', 'Competed under SAP'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('Competitive Delivery Order Fair Opportunity Provided', 'Competitive Delivery Order Fair Opportunity Provided'), ('Non-Competitive Delivery Order', 'Non-Competitive Delivery Order'), ('Fair Opportunity', 'Fair Opportunity'), ('Sole-Source', 'Sole-Source'), ('Limited Sources', 'Limited Sources'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Full and Open after exclusion of sources (competitive small business             set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Full and Open Competition Unrestricted', 'Full and Open Competition Unrestricted'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('A/E Procedures', 'A/E Procedures'), ('Competed under SAP', 'Competed under SAP'), ('Follow On to Competed Action (FAR 6.302-1)', 'Follow On to Competed Action (FAR 6.302-1)'), ('Limited Sources FSS Order', 'Limited Sources FSS Order'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='contract_type',
            field=models.CharField(blank=True, choices=[('Cost No Fee', 'Cost No Fee'), ('Cost Plus Award Fee', 'Cost Plus Award Fee'), ('Cost Plus Fixed Fee', 'Cost Plus Fixed Fee'), ('Cost Plus Incentive Fee', 'Cost Plus Incentive Fee'), ('Cost Sharing', 'Cost Sharing'), ('Fixed Price', 'Fixed Price'), ('Fixed Price Award Fee', 'Fixed Price Award Fee'), ('Fixed Price Incentive', 'Fixed Price Incentive'), ('Fixed Price Labor Hours', 'Fixed Price Labor Hours'), ('Fixed Price Level of Effort', 'Fixed Price Level of Effort'), ('Fixed Price Time and Materials', 'Fixed Price Time and Materials'), ('Fixed Price with Economic Price Adjustment', 'Fixed Price with Economic Price Adjustment'), ('Interagency Agreement', 'Interagency Agreement'), ('Labor Hours', 'Labor Hours'), ('Labor Hours and Time and Materials', 'Labor Hours and Time and Materials'), ('Order Dependent', 'Order Dependent'), ('Time and Materials', 'Time and Materials')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='procurement_method',
            field=models.CharField(blank=True, choices=[('GSA Schedule', 'GSA Schedule'), ('Government-wide Agency Contract-GWAC', 'Government-wide Agency Contract-GWAC'), ('Basic Ordering Agreement', 'Basic Ordering Agreement'), ('Blanket Purchase Agreement-BPA', 'Blanket Purchase Agreement-BPA'), ('Multi-Agency Contract', 'Multi-Agency Contract'), ('BPA Call', 'BPA Call'), ('Purchase Order', 'Purchase Order'), ('Definitive Contract', 'Definitive Contract'), ('Ability One', 'Ability One'), ('Indefinite Delivery Indefinite Quantity-IDIQ', 'Indefinite Delivery Indefinite Quantity-IDIQ'), ('Negotiated', 'Negotiated'), ('Sealed Bid', 'Sealed Bid'), ('Contract', 'Contract'), ('Commercial Item Contract', 'Commercial Item Contract'), ('GSA Schedules Program BPA', 'GSA Schedules Program BPA'), ('Indefinite Delivery Vehicle (IDV)', 'Indefinite Delivery Vehicle (IDV)'), ('Purchase Order', 'Purchase Order'), ('Order under IDV', 'Order under IDV'), ('Order under GSA Schedules Program', 'Order under GSA Schedules Program'), ('Order under GSA Schedules Program BPA', 'Order under GSA Schedules Program BPA'), ('Definitive Contract other than IDV', 'Definitive Contract other than IDV'), ('Indefinite Delivery Vehicle Base Contract', 'Indefinite Delivery Vehicle Base Contract'), ('Order under GSA Federal Supply Schedules Program', 'Order under GSA Federal Supply Schedules Program'), ('Order under IDV', 'Order under IDV'), ('Purchase Order', 'Purchase Order'), ('Contract modification', 'Contract modification'), ('Ability One', 'Ability One'), ('Call Order under GSA Schedules BPA', 'Call Order under GSA Schedules BPA'), ('GSA Schedule Contract', 'GSA Schedule Contract'), ('Negotiated', 'Negotiated'), ('Sealed Bid', 'Sealed Bid'), ('Government-wide Agency Contract-GWAC', 'Government-wide Agency Contract-GWAC'), ('Commercial Item Contract', 'Commercial Item Contract'), ('GSA Schedules Program BPA', 'GSA Schedules Program BPA'), ('Basic Ordering Agreement', 'Basic Ordering Agreement'), ('Blanket Purchase Agreement-BPA', 'Blanket Purchase Agreement-BPA'), ('Multi-Agency Contract', 'Multi-Agency Contract')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='set_aside_status',
            field=models.CharField(blank=True, choices=[('AbilityOne', 'AbilityOne'), ('HUBZone Small Business', 'HUBZone Small Business'), ('Multiple Small Business Categories', 'Multiple Small Business Categories'), ('Other Than Small', 'Other Than Small'), ('Service Disabled Veteran-owned Small Business', 'Service Disabled Veteran-owned Small Business'), ('Small Business', 'Small Business'), ('Small Disadvantaged Business (includes Section 8a)', 'Small Disadvantaged Business (includes Section 8a)'), ('To Be Determined-BPA', 'To Be Determined-BPA'), ('To Be Determined-IDIQ', 'To Be Determined-IDIQ'), ('Veteran-Owned Small Business', 'Veteran-Owned Small Business'), ('Woman-Owned Small Business', 'Woman-Owned Small Business')], max_length=100, null=True),
        ),
    ]