
# Software Requirements Specification (Final)

## Overview

This document covers the core functionality of our web application, such as user authentication, water intake tracking, password recovery, and notifications, along with the non-functional requirements like performance, usability, security, etc.

## Software Requirements

### Functional Requirements

#### User Authentication

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| FR1  | Provide a login page for user authentication.     |
| FR2  | Allow users to sign up with username, first name, last name, email, and password.|
| FR3  | Validate email format during signup.              |
| FR4  | Validate password length (minimum 6 characters) during signup.|
| FR5  | Provide a password recovery option via email.     |
| FR6  | Provide login functionality with email and password.|
| FR7  | Display appropriate error messages for invalid credentials.|
| FR8  | Provide an option for users to reset their password via the "Forgot Password?" link.|
| FR9  | Allow users to navigate between the login, signup, and help pages.|
| FR10 | Ensure that users are redirected to the home page after successful login. |

#### User Profile Management

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| FR11 | Allow users to view and update their account information (first name, last name, email).|
| FR12 | Display user details (first name, last name, email) in the account section.|
| FR13 | Allow users to change their password securely via the "forgot password" feature.|
| FR14 | Display account details after successful login.   |

#### Water Intake Tracking

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| FR15 | Allow users to set a daily water intake goal.     |
| FR16 | Track the daily water intake in real-time.        |
| FR17 | Display the progress of the water intake goal (current intake vs goal).|
| FR18 | Allow users to log their water intake in milliliters.|
| FR19 | Provide feedback on the user’s progress towards the goal, including alerts when they are close to the goal.|
| FR20 | Display a notification when the user achieves or exceeds the daily water goal. |

#### Notifications

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| FR21 | Display in-app notifications about water intake progress.|
| FR22 | Send notifications to users when they are close to or have met their daily water goal.|
| FR23 | Provide clear feedback on the goal status (not met, close to, or achieved).|
| FR24 | Allow notifications to be displayed for 5 seconds. |

#### Password Recovery

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| FR25 | Allow users to request a password reset through their registered email.|
| FR26 | Send a password reset link to the user’s email upon request.|
| FR27 | Redirect users to a password reset page upon clicking the reset link in the email.|
| FR28 | Allow users to change their password using the reset token from the email.|
| FR29 | Provide a confirmation message once the password is successfully reset.|

#### Form Handling

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| FR30 | Implement client-side validation for all form inputs (signup and password reset).|
| FR31 | Show error messages for invalid input in signup and password forms.|
| FR32 | Display a success message when password reset is successfully initiated.|
| FR33 | Allow users to proceed to the login page after resetting their password. |

#### Email Notifications

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| FR34 | Send a hydration reminder email to all users between 8 AM and 8 PM.|
| FR35 | Ensure hydration reminder emails include a friendly message about staying hydrated.|
| FR36 | Allow users to opt out of receiving hydration reminder emails (future feature).|

### Non-Functional Requirements

#### Usability

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| NFR1 | Ensure the UI is mobile-responsive.              |
| NFR2 | Provide clear and user-friendly navigation throughout the application.|
| NFR3 | Display clear error and success messages in the UI.|
| NFR4 | Ensure that all forms provide instant feedback (e.g., password strength, email format).|
| NFR5 | Provide help and support sections with FAQs and contact information.|

#### Security

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| NFR6 | Encrypt passwords using a secure hashing algorithm before storing them in the database.|
| NFR7 | Use HTTPS for secure communication between the client and server.|
| NFR8 | Implement secure user authentication and password management.|
| NFR9 | Implement a time-sensitive password reset token to enhance security.|
| NFR10| Ensure user sessions are handled securely to protect user data. |
| NFR11| Provide secure login and signup forms with encrypted communication.|

#### Performance

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| NFR12| Ensure form submissions (signup, login, password reset) are processed within 2 seconds.|
| NFR13| Ensure email notifications are sent within 2 minutes after a password reset request.|
| NFR14| Send hydration reminder emails to users every 2 hours without delay. |

#### Maintainability

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| NFR15| Organize code into modular functions for easier updates and testing.|
| NFR16| Maintain a clear structure for HTML, CSS, and JavaScript files to support easy modification.|
| NFR17| Document the purpose of each major function and component in the code.|
| NFR18| Ensure that error handling is consistent across the application. |

#### Accessibility

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| NFR19| Provide alt text for images for accessibility purposes.|
| NFR20| Ensure that the application is usable with keyboard navigation only.|
| NFR21| Implement color contrast and text size adjustments for better readability. |

#### Scalability

| NFR22| Ensure the application can handle at least 100 concurrent users without performance degradation.|
| NFR23| Design the database schema to accommodate future extensions, such as additional user attributes or hydration metrics.|

#### Reliability

| NFR24| Ensure that the application uptime is at least 99.5% to provide consistent service availability.|
| NFR25| Implement logging mechanisms to capture errors and monitor system health for debugging purposes.|

## Change Management Plan

### **Purpose**

The purpose of the change management plan is to ensure that all changes to the project requirements, scope, or implementation are documented, reviewed, and approved in a controlled manner to maintain the integrity of the project.

### **Steps for Managing Changes**

1. **Submission of Change Request**:
   - Team members or stakeholders submit a formal change request describing the required modifications.
   - The change request should include:
     - Description of the change.
     - Rationale for the change.
     - Impact of the change on current requirements or system components.

2. **Impact Analysis**:
   - Assess the impact of the proposed change on:
     - Functional and non-functional requirements.
     - Existing artifacts (e.g., diagrams, documents, code).
     - Project timeline and resources.

3. **Approval Process**:
   - The change request is reviewed by the project team and stakeholders.
   - Based on the analysis, the team will decide whether to:
     - Approve the change.
     - Reject the change.
     - Postpone the change for future phases.

4. **Implementation and Testing**:
   - If approved, the change is implemented by the development team.
   - Ensure that appropriate testing is conducted to verify that the change does not introduce defects.

5. **Documentation Updates**:
   - Update all relevant artifacts, including:
     - Software requirements specification (SRS).
     - Design diagrams (use case, class, etc.).
     - Traceability matrices.

6. **Communication**:
   - Notify all team members and stakeholders about the approved change and its implementation.

## Traceability Links

### Use Case Diagram Traceability

| Artifact ID  | Artifact Name             | Requirement ID      |
|--------------|---------------------------|---------------------|
| UseCase1     | Send Notification Emails  | FR1, FR3, NFR3      |
| UseCase2     | User Account Management   | FR6, FR7, NFR4, FR10|
| UseCase3     | Log Hydration Data        | FR11, FR12, NFR4    |
| UseCase4     | Generate Analytics Reports| FR16, FR18, NFR9    |

### Class Diagram Traceability

| Artifact Name           | Requirement ID      |
|--------------------------|---------------------|
| UserNotificationService  | FR1, FR2, FR3, NFR1|
| UserAccountManagement    | FR6, FR7, FR9, NFR4|
| HydrationLog            | FR11, FR12, NFR5   |
| AnalyticsService        | FR16, FR19, NFR8   |

## Software Artifacts

- [Mid Term SRS Document](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/software_requirements_specification.md)
- [System Request](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/IC1-SAD%202.pdf)
- [Use Case Diagram and Activity Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/IC2.pdf)
- [CRC Card, Class and Object Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/CIS%20641%20IC3.docx)
- [State Machine and Sequence Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/CIS%20641%20IC4.docx)
- [Class Specification](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/IC5%20-%20Class%20Specification.pdf)
- [Windows Nav Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/Ic6.pdf)
- [Proposal Document](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/proposal-template.md)
- [Midterm SRS](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/software_requirements_specification.md)
- [Project README](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/README.md)

## Installation Instructions

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/likhitha333/GVSU-CIS641-Data-Wizards.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd GVSU-CIS641-Data-Wizards
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    Python3 app.py
    ```

