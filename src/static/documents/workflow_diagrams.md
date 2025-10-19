# Mr. Wright Adventures - Service Delivery Workflows

**Version:** 1.0  
**Last Updated:** October 2025  
**Owner:** Operations Manager

---

## 1. Introduction to Workflows

These detailed workflows serve as the standard operating procedures (SOPs) for our core services. They are designed to ensure consistency, quality, and efficiency in every client interaction. Each workflow is broken down by phase and specifies the trigger, system actions, and human actions required at each step. These documents will be used for training all team members and will form the logic base for our future AI-powered operational assistants.

---

## 2. Workflow: VIP Airport Transfer

This workflow covers the end-to-end process for providing a seamless, high-touch airport transfer service from either SJO or LIR airports.

### **Visual Workflow Diagram**

*(A visual diagram will be generated and inserted here to provide an at-a-glance overview of the flow.)*

### **Detailed Workflow Steps**

| Phase | Step | Trigger | System Actions | Human Actions (Owner) |
|---|---|---|---|---|
| **1. Pre-Arrival** | **1.1 Booking Confirmation** | Customer completes booking via platform or agent. | - Generate unique Booking ID (e.g., `MWA-T-251018-001`).<br>- Send automated confirmation (WhatsApp/Email).<br>- Create event in shared Google Calendar.<br>- Add booking to CRM under client profile. | **Coordinator:**<br>- Review booking for completeness.<br>- Assign a primary and backup driver from the roster.<br>- Add driver details to the calendar event. |
| | **1.2 Flight & Logistics Prep** | 48 hours before arrival. | - Activate real-time flight tracking via FlightAware API.<br>- Flag any initial delays or schedule changes. | **Coordinator:**<br>- Verify flight number and airline.<br>- Confirm driver availability via WhatsApp.<br>- Pre-calculate route and travel time based on arrival day/time. |
| | **1.3 Customer Pre-Arrival Comms** | 24 hours before arrival. | - Send automated 24-hour reminder email. | **Coordinator:**<br>- Send a personalized WhatsApp message including:<br>  - Driver’s name and photo.<br>  - Vehicle make, model, and license plate.<br>  - A picture of the meeting point.<br>  - Reconfirm destination. |
| **2. Day of Arrival** | **2.1 Driver Dispatch** | 3 hours before scheduled landing. | - Send automated dispatch notification to driver's tablet with all booking details. | **Driver:**<br>- Complete pre-trip vehicle checklist (cleanliness, fuel, amenities).<br>- Confirm start of shift via WhatsApp to the coordinator.<br>**Coordinator:**<br>- Monitor driver's location via GPS as they head to the airport. |
| | **2.2 Airport Staging** | Flight lands. | - System sends alert: "[Flight #] has landed." | **Driver:**<br>- Move to the designated high-visibility meeting point in the arrivals hall.<br>- Hold branded sign with the client's name clearly visible.<br>- Send "On Station" message to the coordinator. |
| | **2.3 The Meet & Greet** | Driver makes visual contact with the client. | - None. | **Driver:**<br>- Greet client warmly by name.<br>- Offer cold water and a refreshing towel.<br>- Assist with all luggage.<br>- Escort clients to the pre-cooled vehicle.<br>- Confirm destination with the client before departing. |
| | **2.4 Journey Start** | Vehicle departs airport. | - GPS tracking status changes to "In Transit".<br>- Automated notification sent to coordinator: "[Booking ID] is en route." | **Driver:**<br>- Send "Client on board, en route to [Destination]" message to coordinator.<br>**Coordinator:**<br>- Acknowledge message and monitor the journey on the GPS dashboard. |
| **3. In-Transit** | **3.1 The Ride** | Duration of the transfer. | - None. | **Driver:**<br>- Provide a safe and comfortable ride.<br>- Engage in light conversation, offering local insights if the client is receptive.<br>- Respect client's privacy if they prefer to be quiet.<br>- Do not make unscheduled stops without coordinator approval. |
| | **3.2 Proactive Updates** | If the journey is > 1 hour. | - None. | **Coordinator:**<br>- If there are unexpected delays (e.g., traffic), inform the client via WhatsApp: "Just a heads up, there's a bit of traffic. We still expect to have you at the resort by [New ETA]."<br>- Notify the destination hotel/villa of the updated arrival time. |
| **4. Drop-off & Post-Trip** | **4.1 Arrival at Destination** | Vehicle arrives at the hotel/villa. | - GPS tracking logs arrival time. | **Driver:**<br>- Assist the client fully with their luggage, bringing it to the reception desk or inside the villa.<br>- Ensure the client is met by hotel staff or has access to the property.<br>- Politely request a digital signature on the tablet to confirm service completion. |
| | **4.2 Closing the Loop** | Driver departs from the destination. | - Booking status updated to "Completed".<br>- Automated trigger for payment processing (if not prepaid).<br>- Automated trigger for post-service feedback survey. | **Driver:**<br>- Send "Drop-off complete" message to the coordinator.<br>**Coordinator:**<br>- Send a final, personal WhatsApp to the client: "So glad you arrived safely! Was everything to your satisfaction?" |

### **Exception Handling**

| Scenario | Trigger | Immediate Actions |
|---|---|---|
| **Flight Delay (>30 min)** | FlightAware API alert. | 1. **System:** Automatically updates booking time.<br>2. **Coordinator:** Notifies driver of new ETA. Informs client: "We are tracking your flight and have adjusted your pickup time. No need to worry!" |
| **Flight Cancellation** | FlightAware API alert. | 1. **Coordinator:** Immediately contacts the client to offer rebooking or a full refund.<br>2. **Coordinator:** Cancels driver assignment and updates the booking status. |
| **Client No-Show** | 45 minutes past gate arrival, no contact. | 1. **Driver:** Makes 3 attempts to call/message the client.<br>2. **Coordinator:** Also attempts contact and checks with the airline.<br>3. After 60 minutes, the booking is marked as a no-show, and the cancellation policy is applied. |
| **Vehicle Breakdown** | Driver reports an issue via emergency channel. | 1. **Coordinator:** Immediately dispatches the backup driver to the location.<br>2. **Coordinator:** Informs the client of the situation, provides the ETA for the new vehicle, and offers a service credit for the inconvenience.<br>3. **Driver:** Stays with the client, ensuring their safety and comfort until the backup arrives. |

---

## 3. Workflow: Concierge Service Request

This workflow outlines the process for handling any non-transportation request, from a simple dinner reservation to a complex multi-day activity itinerary.

### **Visual Workflow Diagram**

*(A visual diagram will be generated and inserted here.)*

### **Detailed Workflow Steps**

| Phase | Step | Trigger | System Actions | Human Actions (Owner) |
|---|---|---|---|---|
| **1. Request Intake** | **1.1 Request Received** | Client sends a request via WhatsApp, email, or platform. | - If via platform, automatically create a new "Task" in the CRM linked to the client.<br>- If via WhatsApp, log the request in the CRM manually. | **On-Duty Concierge:**<br>- Send an immediate acknowledgment: "Request received! I am looking into this for you now and will be back with options shortly." |
| | **1.2 Clarify & Qualify** | Initial request is vague (e.g., "we want a nice dinner"). | - None. | **Concierge:**<br>- Ask clarifying questions to understand preferences: "My pleasure! What kind of cuisine are you in the mood for? Are you looking for something casual or more upscale? Any dietary restrictions?" |
| **2. Research & Propose** | **2.1 Research Options** | Concierge has clear requirements. | - CRM displays a list of preferred partners based on the request type and location. | **Concierge:**<br>- Contact 2-3 preferred partners to check real-time availability.<br>- Leverage established relationships for special requests (e.g., "chef's table"). |
| | **2.2 Propose to Client** | Research is complete. | - None. | **Concierge:**<br>- Present the options to the client in a clear, easy-to-compare format via WhatsApp, including photos, pricing, and a personal recommendation.<br>  *Example: "Option 1 is [Restaurant], known for its amazing sunset view... Option 2 is [Restaurant], a hidden gem loved by locals... I recommend Option 1 for a special occasion."* |
| **3. Booking & Confirmation** | **3.1 Client Makes Selection** | Client replies: "Let's do Option 1 at 7 PM." | - None. | **Concierge:**<br>- Immediately contact the partner to confirm the booking.<br>- Obtain a confirmation number or written confirmation. |
| | **3.2 Confirm with Client** | Booking is confirmed with the partner. | - Create a calendar event for the booking.<br>- Update the CRM task with the confirmation details. | **Concierge:**<br>- Send a final confirmation to the client: "All set! Your table for 2 at [Restaurant] is confirmed for 7 PM under your name. Enjoy!" |
| **4. Follow-up** | **4.1 Pre-Service Reminder** | 2-4 hours before the scheduled service. | - Automated reminder sent from CRM/Calendar. | **Concierge:**<br>- (Optional, for high-value bookings) Send a personal reminder: "Just a friendly reminder about your dinner reservation tonight. Hope you have a wonderful evening!" |
| | **4.2 Post-Service Feedback** | The morning after the service. | - None. | **Concierge:**<br>- Send a brief follow-up message: "Hope you enjoyed your dinner at [Restaurant] last night! How was everything?"<br>- Log any feedback (positive or negative) in the CRM under both the client and partner profiles. |

---

## 4. Workflow: Medical Tourism Support

This high-touch workflow is designed to provide maximum support and peace of mind to clients traveling for medical procedures.

### **Visual Workflow Diagram**

*(A visual diagram will be generated and inserted here.)*

### **Detailed Workflow Steps**

| Phase | Step | Trigger | System Actions | Human Actions (Owner) |
|---|---|---|---|---|
| **1. Pre-Arrival** | **1.1 Initial Consultation** | A potential medical client makes an inquiry. | - Create a new lead in the CRM with the "Medical" tag. | **Medical Liaison:**<br>- Schedule and conduct a detailed phone/video consultation to understand the client's needs, procedure details, and concerns.<br>- Provide a comprehensive overview of our support services. |
| | **1.2 Information Coordination** | Client decides to book. | - Securely create a client profile with encrypted storage for any sensitive medical information. | **Medical Liaison:**<br>- Act as the single point of contact between the client and the medical facility.<br>- Collect and transmit necessary documents (medical records, consent forms) via a secure portal.<br>- Create a detailed, day-by-day itinerary. |
| **2. On-Site Support** | **2.1 Accompanied Appointments** | Client has a pre-op or post-op appointment. | - Schedule and track all appointments in a dedicated calendar. | **Medical Liaison:**<br>- Arrange for discreet, comfortable transportation.<br>- Accompany the client to the appointment to assist with communication, paperwork, and patient advocacy. |
| | **2.2 Post-Procedure Care** | Client is discharged from the clinic. | - None. | **Medical Liaison:**<br>- Coordinate the pickup and ensure the client is comfortably settled in their recovery villa.<br>- Personally oversee the delivery of prescriptions, special dietary foods, and any other necessary medical supplies.<br>- Conduct a daily in-person or video check-in to monitor recovery and answer questions. |
| **3. Departure & Follow-up** | **3.1 Fit-to-Fly Confirmation** | Client's final check-up is complete. | - None. | **Medical Liaison:**<br>- Obtain the "fit-to-fly" certificate from the doctor.<br>- Coordinate the departure transfer, ensuring the driver is aware of the client's condition and can provide extra assistance.<br>- Send all post-care instructions and clinic contact information to the client via email. |
| | **3.2 Post-Trip Support** | Client returns home. | - Schedule automated follow-up emails at 1 week, 1 month, and 3 months. | **Medical Liaison:**<br>- Conduct a personal follow-up call 3 days after the client returns home.<br>- Remain available as a point of contact to facilitate any long-distance communication with the Costa Rican clinic. |
