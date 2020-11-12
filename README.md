<img width="1151" alt="Screen Shot 2020-11-11 at 3 59 06 PM" src="https://user-images.githubusercontent.com/62911364/98870336-c95cc200-2438-11eb-8897-35d80e82d53a.png">

## Background
### All the data science students recieved the email below. Follow the instructions to deliver a email answering the questions below along with a single slide.
<details>
  <summary>EMAIL</summary>

I have some questions for you that I need answered before the board meeting Thursday morning. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well. 
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
7. Which lessons are least accessed? 
8. Anything else I should be aware of? 

- Due Thursday 11/12 no later than 9:00 a.m., send email to datascience@codeup.com
- Submit link to GitHub notebook that asks and answers questions - document the work you do to justify findings
- Compose an email with the answers to the questions/your findings, and in the email, include the link to your notebook in  GitHub and attach your slide. 
- You will not present this, so be sure that the details you need your need your leader to convey/understand are clearly communicated in the email. 
- Slide should be like an exec. Summary and be in form to present. 
- Continue using best practices of acquire.py, prepare.py, etc. 
- No modeling to be done, and no need to split the data into train/validate/test. 
- alumni.codeup.com has info about cohorts/dates/names

</details>

# Goals
- Explore the ```anonymized-curriculum-access.txt```
- Create an explore.ipynb to explore data
- Create a google slide to summarize findings
- Create an acquire.py and prepare.py file to aid in exploring data

# Data Dictionary
| Feature                 | Description                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| index                   | YYYY-MM-DD hh:mm:ss Date of page viewed by user                                                          |
| page                    | End of url of curriculum accessed ie. ds.codeup.com/<page>                                               |
| user_id                 | Unique id for user                                                                                       |
| cohort_id               | Unique id for cohort                                                                                     |
| ip                      | Internet Protocol address by user. Users may may have multiple ips depending where they are taking class |
| times_accessed          | Column used to see how many times an individual column was used. One entered per row per entry           |
| name                    | Name of cohort                                                                                           |
| start_date              | Start date of cohort                                                                                     |
| program_id              | ID used to identify if cohort is web dev (1 & 2) and data science (3)                                    | 
| is_ds                   | Boolean mask used to determine if user is in data science or in web dev. True user is in ds              | 
| accessed_while_enrolled | User accessed pages after graduating from Codeup                                                         |  

# Project Planning
### Acquire
  - Use ```anonymized-curriculum-access.txt``` and pandas to read in txt
  
### Prepare
  - Rename columns
  - Create ```is_ds``` and ```times_accessed``` columns
  - Merge ```anonymized-curriculum-access.txt``` and ```cohort.csv``` data frames
  - Drop some page values (home page, table of contents, and unwanted searches), cohort_id == 28 (staff)
  - Set date as index
  - Set start_date and end_date as datetime format
 
### Explore
  - Explore data to answer questions in email
