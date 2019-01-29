## Exercise


**Write a small script to show passwords or hints for passwords of different accounts from different website you're users.**  

How it should go:

    - Create variables  
        - website: e.g ```website1 = Facebook```  
        - account_name: e.g ```account1 = myaccount@gmail.com```  
        - password: e.g ``` password1 = 123456```  
        - And more websites and counts and password  
    - Print out the question for users to ask, ```"what website's password do you want to see"```

    - Print out options for users to choose  
        ```
        1. Facebook
        2. Twitter
        ...
        ```

    - Show the account and password base on what users choose. E.g  
    ```
    If users want to see facebook, they press 1, and you have to print out account1 and password1.  
    And so on.
    ```
**Extra:**  

    - Make it into a loop, so that when users choose an option and the account, password are printe, you ask an other question: "Do you want to continue? Y/N"
    - If users says Y or Yes or yes or YES or y, we start again from beginning, asking what website's password....
    - If users say N or No or no or NO or n, loop breaks and stop the script


