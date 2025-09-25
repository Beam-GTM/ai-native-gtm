# Ryno Demo Form Responses

## Dependent Properties Form

### **Demo Date**: 25.09.2025

### **Situation**:
Ryno is a Canadian manufacturer of asphalt road repair equipment with ~4,000 annual orders. They operate a drop-ship model through a dealer network, shipping primarily from Canada to the US. Currently, they manually monitor shipment tracking by copying tracking numbers from their Odoo ERP system and pasting them into UPS and FedEx websites to check for delays. This manual process is handled by 2 people (order entry and customer service) and is reactive - they only discover issues when customers complain about delayed shipments.

### **Pain**:
- **Manual Tracking Process**: Daily/weekly manual copy/paste of tracking numbers into carrier websites
- **Reactive Customer Service**: Only discover delays when customers complain, leading to frustrated customers
- **Time Consumption**: 2 people spending significant time on manual monitoring
- **Customs Delays**: Canada-US border delays causing unpredictable delivery times
- **Customer Satisfaction Risk**: Delayed shipments without proactive communication damage customer relationships
- **Seasonal Business Complexity**: Weather-dependent business cycle makes ROI calculation challenging

### **Impact**:
- **Customer Satisfaction**: "It's the life or death of a company" - frustrated customers from delayed shipments
- **Operational Efficiency**: 2 people spending time on manual tracking instead of higher-value activities
- **Business Risk**: Potential lost business due to poor customer experience
- **Scalability Issues**: Manual process doesn't scale with business growth
- **Competitive Disadvantage**: Competitors may have automated solutions
- **Revenue Impact**: Customer dissatisfaction could lead to lost dealer relationships

### **Integrations**:
- **Primary System**: Odoo ERP (has API capabilities)
- **Shipping Carriers**: UPS (primary), FedEx (primary), freight carriers
- **Current Process**: Manual export from Odoo → copy/paste into carrier websites
- **Desired Integration**: Direct API connection to Odoo for automatic tracking number extraction and status updates
- **Data Flow**: Odoo → Beam AI → Carrier APIs → Automated alerts and customer notifications
- **Additional Systems**: Email system for customer notifications, potential CRM integration

### **Timeline**: 12.10.2025

**Rationale**: 
- October 1st kickoff slot available with 20 complimentary development hours
- Allows 2+ weeks for implementation before potential peak season preparation
- Gives time for Odoo integration setup and team training
- Seasonal business timing - implement during slower period, ready for summer peak
- Sufficient time for pilot testing and refinement before full deployment
