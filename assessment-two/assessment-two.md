1.	What is Thread and Multithreading?
thread is a path of execution that is part of a process

multithreading is when you execute multiple threads concurrently


2. concurrency is when there tasks that occur in overlapping periods of time,
whilst parallelism is when tasks are split into subtasks that are executed in different processing units

3. garbage collector is part of python memory management that automatically frees up memory when objects are deleted or reassigned

4. transaction management in a database ensures that a sequence of operations are performed in database are done logically.
5. An endpoint is the url where you want to obtain information from
the most common methods to interact with api data source are get, post, delete and patch 

6. Data normalisation in SQL is when you organize database into tables so tables are created about one specific topic
It reduces duplicates in tables
example of database restructuring using primary key

ALTER TABLE email_address  
ADD  CONSTRAINT 
FK_email_address_customer 
FOREIGN KEY(customer_id)
REFERENCES customer (customer_id);





2.	Discuss Exception handling (4 pts) and debugging in Python (4 pts)

Exception handling can be done in Python using try, except, else and finally blocks. Exceptions can also be handled using raise.

Debugging can be done using the Debugger tool in Python. Debugging is when you check, find and correct errors within code.


5. Agile methodology: name and describe any 2 of the main roles in a Scrum Agile team.

Scrum master ensures the implementation of the Scrum framework during sprints
Product Owner sets the product backlog and sets out the requirements needed for a product. 
They have the final say if they are happy with a product.

6.
Advantages of TDD are that it tests prior to writing code.

Disadvantages are that you do this prior to actually writing code.

7. With a python DB cursor you can execute an SQL command from python terminal

example of python db cursor



8. SQL Question
select customer_id, max(purch_amt)
from orders
where customer_id between 3002 and 3009
group by customer_id
having max(purch_amt) > 1000;