***
# Schema for Minty-Rain-Online-Judge
***

## UserDetails(UID, UName, AboutSection)

> ### Primary Key: UID
> ### Functional dependencies:
> + UID -> UName
> + UID -> AboutSection

> The above relation is in BCNF, 3NF, 2NF, 1NF.

## ProblemSetters(UID, ProblemID, TimeStamp)

> ### Primary key: (UID, ProblemID)
> ### Functional dependencies:
> + (UID, ProblemID) -> TimeStamp

> The above relation is in BCNF, 3NF, 2NF, 1NF.

## Submissions(TransactionID, UID, ProblemID, Solution, TimeStamp, Correctness)

> ### Primary key: TransactionID
> ### Functional dependencies:
> + TransactionID -> (UID, ProblemID, Solution, TimeStamp, Correctness)

> The above relation is in BCNF, 3NF, 2NF, 1NF.

> Reasons:
> + The same solution can be submitted twice within nano seconds, i.e. clicking the mouse twice can submit the same solution twice, all the fields other than TransactionID will be same and TransactionID proves to be the primary key.

> + Solution -> ProblemID does not hold because, because the Solution can be either correct or wrong. Let us say that there are two problems one that has to print "Hello world" and another that has to print "Fibonnaci series". If the user submits the same hello world program from both the problems then the solution cannot uniquely identify the problem. But if the solution is correct it can identify the problem. If all the submitted solutions were always true, the above relation will not be in BCNF and that is a contradiction.

## ProblemInfo1(ProblemID, ProblemName, ProblemText)

> ### Primary key: ProblemID
> ### Functional dependencies:
> + ProblemID -> ProblemText
> + ProblemID -> ProblemName

> The above relation is in BCNF, 3NF, 2NF, 1NF.

## ProblemInfo2(ProblemID, TestCase, ExpectedResult)

> ### Primary key: (ProblemID, TestCase)
> ### Functional dependencies:
> + (ProblemID, TestCase) -> ExpectedResult

> The above relation is in BCNF, 3NF, 2NF, 1NF.

> Reasons:
> + TestCase -> ExpectedResult does not hold because different problems can have the same test case and they can have different expected result. For example if there are two problems addition and subtraction, if they take the same input 1 and 1 they have different results.
