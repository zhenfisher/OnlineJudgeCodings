# Write your MySQL query statement below
select FirstName, LastName, City, State
from Person a
left join Address b
on a.PersonId = b.PersonId
