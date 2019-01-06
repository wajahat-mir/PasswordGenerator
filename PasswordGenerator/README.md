#PasswordGenerator
Console Password Generator

2019-01-05 - Initial Implementation

You can call the PasswordGenerator function(Number of passwords to generate optional argument) to produce a list of random passwords
The first password generated is automatically copied to the clipboard

The ditionary dict_passwordReqs is available to update to add password requirements. With the key containing the question to ask the user and
the value containing the set of possible values.

Three values are already set as below in the dicitonary:

'What\'s the minimum length?' - List of characters lower and upper case
'How many special characters?'] - '!@#$%^&*)-'
'How many numbers?' - '0123456789'