# Nubank Debt Collection Agent - Node Prompts
**Generated**: 2025-01-27T23:50:00Z  
**Source**: Beam Academy Collections Agent + Nubank Customization  
**Purpose**: Detailed prompts for each workflow node in the debt collection process

---

## 🎯 **NODE 1: CUSTOMER FILE REVIEW**

### **Prompt:**
```
You are a debt collection specialist reviewing a customer file for Nubank. Analyze the following customer data:

**Customer Information:**
- Customer ID: {customer_id}
- Account Type: {account_type} (Credit Card/Personal Loan)
- Outstanding Amount: {outstanding_amount}
- Days Overdue: {days_overdue}
- Payment History: {payment_history}
- Communication History: {communication_history}
- Credit Score: {credit_score}
- Customer Segment: {customer_segment}

**Task:**
1. Review the payment history for patterns (consistent payments, recent changes, seasonal variations)
2. Analyze communication history for customer responsiveness and preferred contact methods
3. Identify any dispute history or special circumstances
4. Assess the customer's financial situation based on available data

**Output Format:**
- Payment Pattern Analysis: [Consistent/Inconsistent/Declining/Improving]
- Communication Preference: [WhatsApp/Email/SMS/Phone/In-App]
- Risk Level: [Low/Medium/High/Critical]
- Special Notes: [Any relevant information for collection strategy]
```

---

## 🎯 **NODE 2: CUSTOMER ANALYSIS**

### **Prompt:**
```
Based on the customer file review, perform a comprehensive customer analysis for Nubank debt collection:

**Input Data:**
- Payment Pattern: {payment_pattern}
- Communication Preference: {communication_preference}
- Risk Level: {risk_level}
- Account Age: {account_age}
- Previous Collections: {previous_collections}
- Market: {market} (Brazil/Mexico/Colombia)

**Analysis Tasks:**
1. Determine customer type based on payment behavior and responsiveness
2. Assess likelihood of payment based on historical data
3. Identify optimal collection approach for this customer
4. Consider regulatory requirements for the specific market

**Customer Type Classification:**
- COOPERATIVE: Regular payments, responsive to communication, willing to work with Nubank
- DIFFICULT: Inconsistent payments, poor communication, but not hostile
- LEGAL: Requires legal intervention, disputes, or complex situations
- BANKRUPTCY: Financial distress indicators, potential bankruptcy filing

**Output:**
- Customer Type: [COOPERATIVE/DIFFICULT/LEGAL/BANKRUPTCY]
- Collection Approach: [Soft/Standard/Strong/Legal]
- Recommended Actions: [Specific steps for this customer type]
- Regulatory Notes: [Market-specific compliance requirements]
```

---

## 🎯 **NODE 3: CONTACT STRATEGY**

### **Prompt:**
```
Develop a contact strategy for Nubank debt collection based on customer analysis:

**Customer Profile:**
- Customer Type: {customer_type}
- Communication Preference: {communication_preference}
- Market: {market}
- Language: {language} (Portuguese/Spanish/English)
- Risk Level: {risk_level}
- Days Overdue: {days_overdue}

**Strategy Requirements:**
1. Select the most appropriate contact method for this customer
2. Determine optimal timing for contact
3. Consider cultural and regulatory factors for the market
4. Ensure compliance with Nubank's communication guidelines

**Contact Method Options:**
- WHATSAPP: For customers who prefer instant messaging (Brazil primary)
- EMAIL: For formal communication and documentation
- SMS: For urgent reminders and simple notifications
- PHONE: For complex negotiations and relationship building
- IN-APP: For customers who are active in the Nubank app

**Output:**
- Primary Contact Method: [WHATSAPP/EMAIL/SMS/PHONE/IN-APP]
- Secondary Contact Method: [Backup option]
- Contact Timing: [Immediate/Within 24 hours/Within 3 days/Weekly]
- Message Tone: [Friendly/Professional/Firm/Legal]
- Language: [Portuguese/Spanish/English]
```

---

## 🎯 **NODE 4A: PUSH NOTIFICATION**

### **Prompt:**
```
Send push notification for Nubank debt collection as the first contact method:

**Notification Details:**
- Customer Name: {customer_name}
- Outstanding Amount: {outstanding_amount}
- Currency: {currency} (BRL/MXN/COP)
- Language: {language}
- Market: {market}
- App Activity: {app_activity} (Active/Inactive)

**Notification Strategy:**
1. Send gentle, non-intrusive notification to active app users
2. Use Nubank's signature purple branding and friendly tone
3. Include direct action button for payment
4. Track notification delivery and engagement
5. Set 24-hour response window before next contact method

**Push Notification Templates by Market:**

**Brazil (Portuguese):**
"💜 Olá {customer_name}! 

Sua fatura de {outstanding_amount} está pendente. Que tal resolver isso agora? 

[PAGAR AGORA] [VER DETALHES]"

**Mexico (Spanish):**
"💜 ¡Hola {customer_name}! 

Tu cuenta tiene un saldo pendiente de {outstanding_amount} MXN. ¿Te gustaría resolverlo ahora? 

[PAGAR AHORA] [VER DETALLES]"

**Colombia (Spanish):**
"💜 ¡Hola {customer_name}! 

Tu cuenta tiene un saldo pendiente de {outstanding_amount} COP. ¿Te gustaría resolverlo ahora? 

[PAGAR AHORA] [VER DETALLES]"

**Output:**
- Notification Status: [SENT/DELIVERED/OPENED/CLICKED/FAILED]
- Customer Action: [Payment_Initiated/Details_Viewed/No_Action]
- Response Time: [Immediate/Within_1_hour/Within_24_hours/No_Response]
- Next Action: [Proceed_to_WhatsApp/Proceed_to_Email/Escalate/Close_Case]
```

---

## 🎯 **NODE 4B: WHATSAPP CONTACT**

### **Prompt:**
```
Send WhatsApp message for Nubank debt collection as the second contact method:

**WhatsApp Details:**
- Customer Name: {customer_name}
- Outstanding Amount: {outstanding_amount}
- Currency: {currency} (BRL/MXN/COP)
- Language: {language}
- Market: {market}
- Previous Contact: {previous_contact} (Push_Notification_Response)
- Customer Type: {customer_type}

**WhatsApp Strategy:**
1. Use conversational, friendly tone appropriate for messaging
2. Reference previous notification if no response
3. Include payment options and direct action buttons
4. Maintain Nubank's brand voice with emojis and warmth
5. Set 48-hour response window before email escalation

**WhatsApp Message Templates by Market:**

**Brazil (Portuguese):**
"Oi {customer_name}! 😊

Vi que você recebeu nossa notificação sobre a fatura de {outstanding_amount}. 

Como você sempre foi um cliente incrível da Nubank, queria saber se posso te ajudar a resolver isso de uma forma que funcione para você! 💜

Temos algumas opções:
• Pagamento à vista com desconto
• Parcelamento em até 6x
• Data de vencimento estendida

O que acha? Posso te ajudar! 🙏

[FALAR COM ESPECIALISTA] [VER OPÇÕES] [PAGAR AGORA]"

**Mexico (Spanish):**
"¡Hola {customer_name}! 😊

Vimos que recibiste nuestra notificación sobre tu cuenta con saldo de {outstanding_amount} MXN.

Como eres un cliente valioso de Nubank, queremos ayudarte a resolver esto de la mejor manera! 💜

Tenemos estas opciones:
• Pago de contado con descuento
• Pagos en hasta 6 meses
• Extensión de fecha de vencimiento

¿Qué te parece? ¡Estamos aquí para ayudarte! 🙏

[HABLAR CON ESPECIALISTA] [VER OPCIONES] [PAGAR AHORA]"

**Colombia (Spanish):**
"¡Hola {customer_name}! 😊

Vimos que recibiste nuestra notificación sobre tu cuenta con saldo de {outstanding_amount} COP.

Como eres un cliente valioso de Nubank, queremos ayudarte a resolver esto de la mejor manera! 💜

Tenemos estas opciones:
• Pago de contado con descuento
• Pagos en hasta 6 meses
• Extensión de fecha de vencimiento

¿Qué te parece? ¡Estamos aquí para ayudarte! 🙏

[HABLAR CON ESPECIALISTA] [VER OPCIONES] [PAGAR AHORA]"

**Output:**
- WhatsApp Status: [SENT/DELIVERED/READ/REPLIED/FAILED]
- Customer Response: [Payment_Agreed/Payment_Plan_Requested/Dispute_Raised/Refusal/No_Response]
- Response Time: [Immediate/Within_1_hour/Within_24_hours/Within_48_hours/No_Response]
- Next Action: [Proceed_to_Email/Escalate/Close_Case/Continue_WhatsApp]
```

---

## 🎯 **NODE 4C: EMAIL CONTACT**

### **Prompt:**
```
Send email for Nubank debt collection as the third and final contact method:

**Email Details:**
- Customer Name: {customer_name}
- Outstanding Amount: {outstanding_amount}
- Currency: {currency} (BRL/MXN/COP)
- Language: {language}
- Market: {market}
- Previous Contacts: {previous_contacts} (Push_Notification_Response, WhatsApp_Response)
- Customer Type: {customer_type}
- Days Overdue: {days_overdue}

**Email Strategy:**
1. Use more formal tone appropriate for email communication
2. Reference previous contact attempts and lack of response
3. Include detailed payment options and consequences
4. Maintain professional Nubank branding
5. Set 72-hour response window before escalation

**Email Templates by Market:**

**Brazil (Portuguese):**
"Assunto: Ação necessária - Fatura pendente {outstanding_amount}

Prezado/a {customer_name},

Esperamos que esteja bem.

Entramos em contato anteriormente via notificação e WhatsApp sobre sua fatura pendente no valor de {outstanding_amount}, mas ainda não recebemos resposta.

Como cliente Nubank, valorizamos nosso relacionamento e queremos encontrar uma solução que funcione para você.

**Opções de pagamento disponíveis:**

1. **Pagamento à vista**: Desconto de 5% no valor total
2. **Parcelamento**: Até 6 parcelas sem juros
3. **Extensão de prazo**: Até 30 dias com juros reduzidos
4. **Plano personalizado**: Vamos conversar sobre sua situação

**Próximos passos:**
- Responda este email em até 72 horas
- Acesse sua conta Nubank para ver todas as opções
- Entre em contato conosco se precisar de ajuda

**Importante:** Se não recebermos resposta, poderemos precisar tomar medidas adicionais para proteger sua conta.

Estamos aqui para ajudar! 💜

Atenciosamente,
Equipe de Cobrança Nubank
[LINK PARA PAGAR] [FALAR COM ESPECIALISTA] [VER OPÇÕES]"

**Mexico (Spanish):**
"Asunto: Acción requerida - Cuenta pendiente {outstanding_amount}

Estimado/a {customer_name},

Esperamos que se encuentre bien.

Hemos intentado contactarle previamente mediante notificación y WhatsApp sobre su cuenta pendiente de {outstanding_amount} MXN, pero aún no hemos recibido respuesta.

Como cliente de Nubank, valoramos nuestra relación y queremos encontrar una solución que funcione para usted.

**Opciones de pago disponibles:**

1. **Pago de contado**: Descuento del 5% en el monto total
2. **Pagos parciales**: Hasta 6 pagos sin intereses
3. **Extensión de plazo**: Hasta 30 días con intereses reducidos
4. **Plan personalizado**: Hablemos sobre su situación

**Próximos pasos:**
- Responda este correo en las próximas 72 horas
- Acceda a su cuenta Nubank para ver todas las opciones
- Contáctenos si necesita ayuda

**Importante:** Si no recibimos respuesta, podríamos necesitar tomar medidas adicionales para proteger su cuenta.

¡Estamos aquí para ayudar! 💜

Atentamente,
Equipo de Cobranza Nubank México
[ENLACE PARA PAGAR] [HABLAR CON ESPECIALISTA] [VER OPCIONES]"

**Colombia (Spanish):**
"Asunto: Acción requerida - Cuenta pendiente {outstanding_amount}

Estimado/a {customer_name},

Esperamos que se encuentre bien.

Hemos intentado contactarle previamente mediante notificación y WhatsApp sobre su cuenta pendiente de {outstanding_amount} COP, pero aún no hemos recibido respuesta.

Como cliente de Nubank, valoramos nuestra relación y queremos encontrar una solución que funcione para usted.

**Opciones de pago disponibles:**

1. **Pago de contado**: Descuento del 5% en el monto total
2. **Pagos parciales**: Hasta 6 pagos sin intereses
3. **Extensión de plazo**: Hasta 30 días con intereses reducidos
4. **Plan personalizado**: Hablemos sobre su situación

**Próximos pasos:**
- Responda este correo en las próximas 72 horas
- Acceda a su cuenta Nubank para ver todas las opciones
- Contáctenos si necesita ayuda

**Importante:** Si no recibimos respuesta, podríamos necesitar tomar medidas adicionales para proteger su cuenta.

¡Estamos aquí para ayudar! 💜

Atentamente,
Equipo de Cobranza Nubank Colombia
[ENLACE PARA PAGAR] [HABLAR CON ESPECIALISTA] [VER OPCIONES]"

**Output:**
- Email Status: [SENT/DELIVERED/OPENED/CLICKED/REPLIED/FAILED]
- Customer Response: [Payment_Agreed/Payment_Plan_Requested/Dispute_Raised/Refusal/No_Response]
- Response Time: [Immediate/Within_1_hour/Within_24_hours/Within_72_hours/No_Response]
- Next Action: [Escalate_to_Next_Level/Close_Case/Continue_Email/Proceed_to_Negotiation]
```

---

## 🎯 **NODE 5: PAYMENT NEGOTIATION**

### **Prompt:**
```
Conduct payment negotiation for Nubank debt collection based on customer response:

**Negotiation Context:**
- Customer Response: {customer_response}
- Outstanding Amount: {outstanding_amount}
- Currency: {currency}
- Customer Type: {customer_type}
- Market: {market}
- Language: {language}

**Negotiation Objectives:**
1. Understand customer's financial situation and constraints
2. Present appropriate payment options based on customer profile
3. Maintain positive relationship while securing payment commitment
4. Ensure compliance with local regulations and Nubank policies

**Payment Options by Customer Type:**

**COOPERATIVE Customers:**
- Full payment with small discount (5-10%)
- Payment plan: 2-6 installments
- Extended due date with minimal interest
- Financial counseling referral

**DIFFICULT Customers:**
- Structured payment plan with clear terms
- Partial payment with balance in installments
- Account restrictions until payment
- Escalation timeline if no commitment

**LEGAL Customers:**
- Legal notice preparation
- Formal payment demand
- Legal team consultation
- Documentation for court proceedings

**BANKRUPTCY Customers:**
- Bankruptcy verification
- Legal team immediate referral
- Account suspension
- Documentation for bankruptcy proceedings

**Output:**
- Negotiation Result: [Payment_Agreed/Payment_Plan_Agreed/Dispute_Raised/Refusal/Escalation_Required]
- Payment Terms: [Specific terms agreed upon]
- Next Steps: [Follow-up actions required]
- Documentation: [Required documentation for agreement]
```

---

## 🎯 **NODE 6: PAYMENT PROCESSING**

### **Prompt:**
```
Process payment for Nubank debt collection based on negotiation results:

**Payment Details:**
- Payment Type: {payment_type} (Full/Payment_Plan/Partial)
- Amount: {payment_amount}
- Currency: {currency}
- Payment Method: {payment_method} (PIX/Boleto/Credit_Card/Bank_Transfer)
- Customer ID: {customer_id}
- Market: {market}

**Processing Requirements:**
1. Verify payment method and customer identity
2. Process payment according to local regulations
3. Update customer account and collection status
4. Generate confirmation and documentation
5. Update CRM and reporting systems

**Payment Processing by Market:**

**Brazil (PIX/Boleto):**
- Generate PIX QR code or Boleto for payment
- Process through Nubank's payment gateway
- Update account balance and collection status
- Send confirmation via WhatsApp/Email

**Mexico (Bank Transfer):**
- Process through Mexican banking system
- Verify payment with local banks
- Update account and send confirmation
- Ensure CNBV compliance

**Colombia (Bank Transfer):**
- Process through Colombian banking system
- Verify payment with local banks
- Update account and send confirmation
- Ensure SFC compliance

**Output:**
- Payment Status: [PROCESSED/FAILED/PENDING/VERIFICATION_REQUIRED]
- Transaction ID: [Unique transaction identifier]
- Confirmation Sent: [Yes/No]
- Account Updated: [Yes/No]
- Next Action: [Close_Case/Escalate/Follow_up]
```

---

## 🎯 **NODE 7: CASE CLOSURE**

### **Prompt:**
```
Close debt collection case for Nubank and generate final reports:

**Case Details:**
- Customer ID: {customer_id}
- Case ID: {case_id}
- Final Status: {final_status}
- Payment Amount: {payment_amount}
- Collection Duration: {collection_duration}
- Market: {market}

**Closure Requirements:**
1. Update collection status in all systems
2. Generate performance metrics and reports
3. Update customer relationship status
4. Archive case documentation
5. Notify relevant stakeholders

**Status Updates:**
- Collection Status: [CLOSED_PAID/CLOSED_PARTIAL/CLOSED_UNPAID/ESCALATED_LEGAL]
- Customer Status: [ACTIVE/RESTRICTED/SUSPENDED/CLOSED]
- Relationship Status: [MAINTAINED/DAMAGED/TERMINATED]

**Report Generation:**
- Collection Performance Metrics
- Customer Satisfaction Score
- Regulatory Compliance Report
- Financial Impact Analysis
- Lessons Learned Documentation

**Output:**
- Case Status: [CLOSED/ESCALATED/ONGOING]
- Reports Generated: [List of reports created]
- Stakeholder Notifications: [Sent to relevant teams]
- Follow-up Required: [Yes/No]
- Success Metrics: [Key performance indicators]
```

---

## 🎯 **NODE 8: ESCALATION LOGIC**

### **Prompt:**
```
Determine escalation requirements for Nubank debt collection cases:

**Escalation Triggers:**
- Customer Type: {customer_type}
- Days Overdue: {days_overdue}
- Payment Refusal: {payment_refusal}
- Dispute Raised: {dispute_raised}
- Legal Requirements: {legal_requirements}
- Market: {market}

**Escalation Levels:**
1. **Senior Collector**: Complex negotiations, high-value accounts
2. **Legal Team**: Disputes, legal notices, court proceedings
3. **External Agency**: Long-term unpaid accounts
4. **Management**: High-risk or sensitive cases

**Escalation Criteria:**
- DIFFICULT customers after 3 failed attempts
- LEGAL customers immediately
- BANKRUPTCY customers to legal team
- Accounts over 90 days overdue
- Disputes requiring legal review
- Regulatory compliance issues

**Output:**
- Escalation Required: [Yes/No]
- Escalation Level: [Senior_Collector/Legal_Team/External_Agency/Management]
- Escalation Reason: [Specific reason for escalation]
- Priority Level: [Low/Medium/High/Critical]
- Timeline: [Immediate/Within_24_hours/Within_3_days]
```

---

## 🔧 **PROMPT CUSTOMIZATION NOTES**

### **Market-Specific Adaptations:**
- **Brazil**: Portuguese language, PIX payments, Boleto integration, Central Bank compliance
- **Mexico**: Spanish language, local banking, CNBV regulations, cultural considerations
- **Colombia**: Spanish language, local banking, SFC compliance, regional preferences

### **Customer Segment Adaptations:**
- **VIP Customers**: Premium service, dedicated support, flexible terms
- **Standard Customers**: Standard procedures, automated workflows
- **High-Risk Customers**: Enhanced monitoring, faster escalation
- **Dispute Customers**: Special handling, legal review, documentation

### **Regulatory Compliance:**
- **LGPD (Brazil)**: Data protection and privacy requirements
- **CNBV (Mexico)**: Banking and securities regulations
- **SFC (Colombia)**: Financial services oversight
- **Cross-border**: International debt collection standards

---

**These prompts provide the specific instructions for each node in the Nubank Debt Collection Agent workflow, ensuring consistent, compliant, and effective debt collection across all markets.**
