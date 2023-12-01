# Advent of Code 2023 in Python  
  
When each next puzzle comes out, I'll publish my solve for the last day here!  
I'm using python, so a few notes:  
  
> [!NOTE]
> my solutions requires the use of the requests library because I'm pulling the puzzle input right from the website with the code, so after installing a recent version of python (needs to be 3.7+ I think), you're going to need to do  
> `pip install requests`  
> that should be it though, and should work out of the box otherwise! Well, except one more thing:  
>  
  
> [!IMPORTANT]
> for the code to work properly, you need to have an account with advent of code, and then you have to pull the cookie value out of your storage in the browser and put it into the code here's how:  
> 1. Get onto the advent of code website.  
> 2. From there, inspect the page.  
> 3. In the inspector, navigate to the storage. In Firefox, this is under the storage tab. In Chrome, it's under application (I think) and if you're using a different browser, I'm sure a quick search can help you out.  
> 4. In the storage, navigate to the cookie field. In the table you will find "session", and from there you need to get the "value" out. Double click the big token string under value and copy it.  
> 5. Now go to the code files. Open getdata.py and paste the token string you copied from your browser into the quotes next to cookie, setting cookie equal to that value.  
> 6. Now the code should be prepped to run. Run the python file you want!  
> 7.   
