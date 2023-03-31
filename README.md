# Find-All-Good-Strings
In this level, the hero must find the correct combination of letters to unlock a door to the next room. The hero is given a string of letters and must determine which letters to use to form a good string that meets the alphabetical constraints and avoids the substring evil.
--------------------------
Readme.md Outline for Level 2 Problem Solver

# Table of Contents

Introduction
Level 1 Problem
Level 2 Problem
Implementation Steps
Level 1 Steps
Level 2 Steps
Flowchart
References
Introduction

This readme provides an overview of the Level 2 Problem Solver, which is an advanced problem-solving algorithm that incorporates a Level 1 problem as part of its solution process. The following sections outline the steps to implement the solution, with a flowchart to visualize the process.

Level 1 Problem

The Level 1 problem consists of a hero navigating through a maze. This problem is an integral part of the Level 2 problem and serves as a foundation for it.

Level 2 Problem

The Level 2 problem involves the hero navigating the maze while also solving an additional challenge. This challenge requires the implementation of two functions:

oddEvenJumps(arr): A function to determine the number of good starting indices in the array, arr, using odd and even jumps.
countGoodStrings(n, s1, s2, evil): A function to count the number of good strings between two given strings s1 and s2 that do not contain the substring evil.
Implementation Steps

Level 1 Steps
Start
Hero enters the maze (Level 1)
Level 2 Steps
Define function oddEvenJumps(arr)
Get the length of arr as n
Initialize lists odd and even of length n with all elements set to False
Set the last elements of odd and even lists to True
Create sorted indices based on arr values
Call makeNext function with sorted indices to get oddNext
Sort the indices in reverse order based on arr values
Call makeNext function with reverse sorted indices to get evenNext
Iterate through arr from the second last element to the first element (in reverse)
If oddNext[i] is not None, set odd[i] to even[oddNext[i]]
If evenNext[i] is not None, set even[i] to odd[evenNext[i]]
Return the sum of odd
Hero starts navigating the maze (Level 2)
Define function countGoodStrings(n, s1, s2, evil)
Initialize a DP table
Define a recursive function count(prefix_len, last_char, is_s1, is_s2)
Check if evil is a substring of the current prefix
Check if the desired prefix length has been reached
Check if the result is memoized
Initialize a variable ans
Iterate through all characters from last_char to 'z'
Check if the current character is less than the corresponding character in s1
Check if the current character is greater than the corresponding character in s2
Call the count function recursively with updated parameters and add the result to ans
Update the memoized result
Return ans
