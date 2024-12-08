 # Software Requirements Specification (Final)

## Overview

This document covers the core functionality of our web application such as user authentication, water intake tracking, password recovery and notifications along with the non-functional requirements like performance, usability, security, etc.

## Software Requirements

The key functional and non-functional requirements for the AquaSync application are listed in the Software Requirements section. These features, which guarantee the program meets user needs, include user authentication, water intake tracking, email notifications, and performance benchmarks.

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

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| NFR22| Ensure the application can handle at least 100 concurrent users without performance degradation.|
| NFR23| Design the database schema to accommodate future extensions, such as additional user attributes or hydration metrics.|

#### Reliability

| ID   | Requirement                                       |
|------|---------------------------------------------------|
| NFR24| Ensure that the application uptime is at least 99.5% to provide consistent service availability.|
| NFR25| Implement logging mechanisms to capture errors and monitor system health for debugging purposes.|

## Change Management Plan

### **Training Plan**

#### **Objective**:

Ensure all users understand and can effectively use the application to log and track daily water intake and manage their hydration goals.

#### **Training Methods**

**Interactive Workshops**:
Conduct virtual or in-person sessions where users can learn and practice using the application features, such as logging water intake and setting goals.

**User Guide**:
Provide a detailed digital manual with step-by-step instructions and annotated screenshots for key features like signup, login, and water intake tracking. We have already provided one help tab in our website for user guide.

**Video Tutorials**:
Create short, targeted videos demonstrating core functionalities, such as setting daily water goals, viewing progress, and understanding notifications.

**Below are the list of topics that covers during training**
- Topics Covered
- User Authentication and Password Recovery
- Navigating the Dashboard and Hydration Progress
- Setting and Managing Water Intake Goals
- Logging Water Intake
- Notifications for Goal Progress
- Understanding Optional Features (e.g., hydration reminders via email)

### **Integration with Existing Ecosystem / Software**

#### **Steps to Integrate**

**Compatibility Testing**
- The application has been tested to work seamlessly on all major browsers including Chrome, Firefox, Safari and Edge.
- Usability has been verified across various devices such as desktops, tablets and smartphones.
- Functionality has been ensured on common operating systems like Windows, macOS and Linux.

**Database and Data Handling**
- MongoDB has been utilized to securely store user data, including water intake logs and hydration goals.
- Data consistency and reliability have been ensured through robust backend operations.

**User Authentication and Notifications**
- User accounts are secured with encrypted passwords using Flask’s built-in security and encryption tools.
- Personalized hydration reminders are sent via email using SMTP integration.
- Notifications are scheduled to encourage users to meet their hydration goals throughout the day.

**Future Improvements**
The application is designed to expand easily, allowing potential integration with external health tracking devices or APIs for more comprehensive functionality.

### **Issue Resolution and Support Plan**

#### **Objective**:

Ensure timely identification, reporting, and resolution of any issues to maintain smooth operations of the Water Intake Tracking Application.

**Support Channels**:
- Dedicated Support Email: Provide a support email address where users can report issues or request assistance.
- In-App Feedback Form: Allow users to report problems directly within the application through a feedback form.

**Issue Resolution Process**:
- Continuous Monitoring: Use Flask logs and backend monitoring tools to track system performance and proactively identify potential issues before they affect users.
- Bug Reporting and Fixing: Users can report issues through the in-app feedback form or support email.
Reported bugs are triaged based on severity and addressed promptly.
- Software Updates: Regularly release updates to resolve bugs, enhance application performance, and introduce new features. Also, notify users in advance of upcoming updates and provide release notes detailing significant changes or improvements.
- Documentation Updates: Maintain up-to-date user guides and FAQs, reflecting changes introduced in software updates to assist users with any new features or functionality.


## Traceability Links

### Use Case Diagram Traceability

| Artifact ID    | Artifact Name                      | Requirement ID                 |                        
|---------------------|--------------------------------------------------------|-------------------------------------------------|
| UseCase1     | Send Notification Emails             | FR21, FR22, NFR6, NFR12         |              
| UseCase2     | User Account Management           | FR6, FR7, FR11, FR13, NFR4, NFR6  |
| UseCase3     | Log Hydration Data                 | FR15, FR16, FR18, FR19, NFR4, NFR12|      
| UseCase4     | Password Recovery                  | FR25, FR26, FR28, FR29, NFR7, NFR10 |
| UseCase5     | Validate Form Inputs                | FR30, FR31, FR33, NFR3, NFR4       |
| UseCase6     | Schedule Hydration Reminders       | FR34, FR35, NFR6, NFR12           |
| UseCase7     | Display User Hydration Progress      | FR17, FR20, NFR1, NFR5           |
| UseCase8     | Manage Notifications               | FR23, FR24, NFR1, NFR8           | 


### Class Diagram Traceability

| Artifact Name           | Requirement ID                            |
|-------------------------------------|-------------------------------------------------------------------|
| UserNotificationService   | FR21, FR22, FR23, FR24, NFR6, NFR12         |
| UserAccountManagement  | FR6, FR7, FR11, FR13, NFR4, NFR6           |
| HydrationLog           | FR15, FR16, FR17, FR18, FR19, NFR4, NFR12    |
| PasswordRecoveryService  | FR25, FR26, FR28, FR29, NFR7, NFR10         |
| FormValidationService    | FR30, FR31, FR33, NFR3, NFR4               |
| NotificationScheduler     | FR34, FR35, NFR6, NFR12                   |
| ProgressTrackingService   | FR17, FR20, NFR1, NFR5                    |

### Activity Diagram Traceability

| Artifact Name                  | Requirement ID                      |
|-------------------------------------------------|---------------------------------------------------------|
| Login and Signup Workflow       | FR6, FR7, FR9, FR13, NFR4, NFR6       |
| Password Recovery Process        | FR25, FR26, FR28, FR29, NFR7, NFR10   |
| Hydration Logging Activity        | FR15, FR16, FR18, FR19, NFR4, NFR12   |
| Notification Scheduling Flow      | FR21, FR22, FR34, FR35, NFR6, NFR12   |
| Progress Tracking Activity        | FR17, FR20, NFR1, NFR5               |
| Form Validation Workflow        | FR30, FR31, FR33, NFR3, NFR4         |
| Data Synchronization Workflow   | FR11, FR12, NFR5, NFR12              |

## Software Artifacts

- [Mid Term SRS Document](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/software_requirements_specification.md)
- [System Request](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/artifacts/IC1%20System%20Rquest.pdf)
- [Use Case Diagram and Activity Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/artifacts/IC2%20Use%20Case%20Diagrams%20%2B%20Activity%20Diagrams.pdf)
- [CRC Card, Class and Object Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/artifacts/IC3%20CRC%20%2B%20Class%20%2B%20Object%20Models.docx)
- [State Machine and Sequence Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/artifacts/IC4%20Sequence%20%2B%20State%20Diagrams.docx)
- [Class Specification](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/artifacts/IC5%20-%20Class%20Specification.pdf)
- [Windows Nav Diagram](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/artifacts/IC6%20Windows%20Nav%20Diagrams.pdf)
- [Proposal Document](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/proposal-template.md)
- [Final SRS](https://github.com/likhitha333/GVSU-CIS641-Data-Wizards/blob/main/docs/software_requirements_specification_final.md)
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