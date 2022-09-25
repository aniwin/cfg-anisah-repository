**Question 1**

· Product backlog refinement- breaking down and refining the product backlog items to smaller items

· Sprint planning – starts the sprint by planning for the work to be done in the sprint. The whole team agrees to complete a set of product backlog items.

· Daily scrum- a daily meeting to find out the daily progress of the team. Each person answers what they are working on today, what they did yesterday and what impediments are in the way. 

· Sprint review- A meeting held at the end of a sprint which the team shows the team has done during the sprint. It is like a demo of new features added in the product

· Sprint retrospective- the sprint team looks at what went well, what didn’t go well and what could be improved for future sprints.


SCRUM ROLES

· ScrumMaster- ensures that the scrum framework is followed. They facilitate that team members follow scrum practices. They arrange the scrum meetings.

· Product Owner- They set out the items on the product backlog.

They order and prioritize the items on the product backlog. They are responsible for knowing and managing stakeholders needs.

· Development Team- Team of professionals that do the work to deliver a potentially viable product at the end of each Sprint.

Question 2

Epic

E1. Yoga booking system

Stories

` `S1. As a user I want to enter the date of a yoga class

S2. As a user I want to be able to class availability for each day

S3. As a user I want to be able to select which yoga instructor’s class I attend

S4. As an administrator I want to see all classes booked by users





S1.

1. Create welcome login page

S2.

1. Create function to input users which date they want to go to yoga class
1. Function to input time availability

S3.

1. Create a function to select from different yoga instructor

S4.

1. Create new database to store booked classes


Tasks that can be done in parallel

S1. (Task 1 ), S2. (Task 1, Task 2), S3. (Task 1)

S4. (Task1 ) needs to be done first

***Question 1***

**Design a cinema booking system.**

Think how you would approach the problem and what are potential ways of solving

it?

You do not need to write actual code, but describe the high-level approach:

· Draw a list of key requirements

List of key requirements

- Users should be able to see what movies are being screened, information about each movie, cinema venues and 
- Users should be able to select screening dates and times
- Users should be able to choose number of tickets and seating
- Users should be able to sign up and login before booking tickets
- System to send them e-tickets and cancellations with an email or to user’s phone by SMS notifications
- Creating a database to store payment data and for user queries

· What are your main considerations?

- Having a system where users must complete ticket purchase within 15 minute time slot or the tickets can be viewed by others who are looking to purchase
- Having large number of users trying to use the server at the same time


· What would be your common or biggest problems?

- Ensuring user’s personal information is kept private
- Multiple users trying to book the same seat/s
- Ensuring payments for tickets are kept secure
- Problems with payment system

· What components or tools would you potentially use?

- SQL for the database
- Server 
- Using third party payment system for payments to support different payment methods
- Using a cache to show users information on movies being shown  in each city
- UI- ReactJS
- Using analytical tools to see top performing movies and which cinema locations sell the most tickets