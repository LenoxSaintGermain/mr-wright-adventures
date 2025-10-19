_Low-Fidelity Mockups_

# Low-Fidelity Mockups: Booking & Agent Flows

This document provides a low-fidelity, text-based representation of the key user flows for the Mr. Wright Adventures digital platform.

## 1. Traveler Booking Flow (Web)

### **Screen 1: Landing Page**

```
----------------------------------------------------------------
|                                                              |
|            Mr. Wright Adventures                             |
|                                                              |
|   Your trusted travel partner in Costa Rica.                 |
|                                                              |
|   [Book Now]                                                 |
|                                                              |
----------------------------------------------------------------
```

### **Screen 2: Booking Form - Step 1: Trip Details**

```
----------------------------------------------------------------
|                                                              |
|   Trip Details                                               |
|                                                              |
|   Arrival Date & Time: [Date Picker] [Time Picker]           |
|   Flight Number: [Text Input]                                |
|   Departure Date & Time: [Date Picker] [Time Picker]         |
|   Number of Passengers: [Number Input]                       |
|   Accommodation: [Text Input]                                |
|                                                              |
|   [Next]                                                     |
|                                                              |
----------------------------------------------------------------
```

### **Screen 3: Booking Form - Step 2: Service Selection**

```
----------------------------------------------------------------
|                                                              |
|   Select Services                                            |
|                                                              |
|   [ ] Airport Pickup & Luggage Management                    |
|   [ ] Transport: [Dropdown: Economy, Comfort, VIP, Heli]     |
|   [ ] Concierge Services: [Text Area for requests]           |
|   [ ] Tours & Excursions: [Dropdown of options]              |
|                                                              |
|   [Next]                                                     |
|                                                              |
----------------------------------------------------------------
```

### **Screen 4: Booking Form - Step 3: Personal Information**

```
----------------------------------------------------------------
|                                                              |
|   Your Information                                           |
|                                                              |
|   Full Name: [Text Input]                                    |
|   Email: [Text Input]                                        |
|   Phone Number: [Text Input]                                 |
|   Special Requirements: [Text Area]                          |
|                                                              |
|   [Confirm & Pay]                                            |
|                                                              |
----------------------------------------------------------------
```

### **Screen 5: Confirmation Page**

```
----------------------------------------------------------------
|                                                              |
|   Booking Confirmed!                                         |
|                                                              |
|   Thank you for booking with Mr. Wright Adventures.          |
|   A confirmation has been sent to your email.                |
|                                                              |
|   Booking Summary:                                           |
|   - Service: Airport Pickup                                  |
|   - Date: 2025-12-25                                         |
|   - ...                                                      |
|                                                              |
----------------------------------------------------------------
```

## 2. Agent Flow (WhatsApp-Based)

### **Flow 1: New Job Notification & Acceptance**

```
----------------------------------------------------------------
|   **Mr. Wright Bot**                                         |
|                                                              |
|   New job available: Airport pickup for John Doe at 3:00 PM  |
|   on 2025-12-25. Flight UA123.                               |
|                                                              |
|   Reply with 'ACCEPT' to take this job.                      |
----------------------------------------------------------------

----------------------------------------------------------------
|   **You**                                                    |
|                                                              |
|   ACCEPT                                                     |
----------------------------------------------------------------

----------------------------------------------------------------
|   **Mr. Wright Bot**                                         |
|                                                              |
|   Job confirmed. Please greet the traveler at the arrivals   |
|   hall. Traveler's phone: +1-555-123-4567.                    |
|   Luggage Tag QR: [Image of QR Code]                         |
----------------------------------------------------------------
```

### **Flow 2: Status Updates**

```
----------------------------------------------------------------
|   **You**                                                    |
|                                                              |
|   [Photo of tagged luggage]                                  |
|   Baggage collected.                                         |
----------------------------------------------------------------

----------------------------------------------------------------
|   **Mr. Wright Bot**                                         |
|                                                              |
|   Status updated to 'Baggage Collected'. Traveler has been   |
|   notified.                                                  |
----------------------------------------------------------------

----------------------------------------------------------------
|   **You**                                                    |
|                                                              |
|   En route to the hotel.                                     |
----------------------------------------------------------------

----------------------------------------------------------------
|   **Mr. Wright Bot**                                         |
|                                                              |
|   Status updated to 'En Route'. Traveler has been notified   |
|   with an ETA of 3:45 PM.                                    |
----------------------------------------------------------------

----------------------------------------------------------------
|   **You**                                                    |
|                                                              |
|   [Photo of luggage at hotel]                                |
|   Delivered to the Westin.                                   |
----------------------------------------------------------------

----------------------------------------------------------------
|   **Mr. Wright Bot**                                         |
|                                                              |
|   Job complete. Thank you!                                   |
----------------------------------------------------------------
```
