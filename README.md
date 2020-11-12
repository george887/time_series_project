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
  
# Conclusions
<details>
<summary>Findings</summary>
 
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)? 

For data science, the top five pages viewed across any cohort were:

- classification/overview - cohort 59 with 759 views.
- 1-fundamentals/modern-data-scientist.jpg - cohort 34 with 626 views.
- 1-fundamentals/AI-ML-DL-timeline.jpg	- cohort 34 with 624 views.
- 1-fundamentals/1.1-intro-to-data-science	- cohort 34 with 615 views.
- 6-regression/1-overview - cohort 55 with 595 views.

For WebDev, he top five pages viewed across any cohort were:

- javascript-i	 - cohort 33, 58, 24, & 29 with views ranging from 869 - 977. 
- index - cohort 14 with 877 views.
- java-iii	- cohort 24, 53, 29 with 742 - 770 views.
- html-css	- cohort 33 with 753 views and 56 with 708 views.
- spring - cohort 22 with 707 views and 24 & 29 with 650 views.

2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 

Data Science
Darden accessed classification/overview (759 views) over 7 times more than Curie (91 views). Bayes had 10 views.
Darden hardly accessed 6-regression/1-overview (7 views) compared to Bayes (512 views) and Curie (595 views).
Darden accessed sql/mysql-overview significantly more than Bayes (3 views) and Curie (99 views).

WebDev
Javascript-i was significantly looked at less in cohorts 12, 2, 6, 15, 19, 11, 7, 13, 16, 8, 17, & 18 with a range of 1 - 128 views as opposed to cohort 33 with 977 views.

Cohort 14 looked at the index.html (877 views) significantly more than any other cohort. Only 13 total cohorts looked at the index with cohort 13 closest at 84 views.
Java-iii was looked at significantly more in cohorts 22, 29, 24 and 53 with a range of 712 - 770 views. Cohorts 17, 15, 13, 62, 11, 19, 6, 12 had a range of views of 1-25.

3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 

Yes there are students who are rarely accessing the curriculum. Keep in mind when this info was found, I filtered out home pages and table of contents. Example, in cohorts 55 (user 787), 14 (user 593), 1 (user 212) and 7 (user 348) all accessed the curriculum one time. User 787 looked only at the appendix/interview_questions_students. User 593 and 165 looked at the index once. User 212 looked at students/units/75/sub_units/268. User 348 looked at content/php_iii/php-with-html/sessions-with-ph.

4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 

Users 53, 344, 570, 64 and 555 have the most pages viewed post graduating. User 53 has the most views and has 2800 more views than user 344 who is the second highest. Might want to look into these users more thoroughly to see if anything suspicious is going on.  User 53 had 11 different ip addresses which is suspect. 
In Curie, user 581 accessed 919 pages after graduating compared to 190 from user 580 who is the second highest value. There are interesting patterns with the amounts of pages accessed having the same amount of hits.

5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 

Data Science
There was some ds students looking at the webdev curriculum last year in Sept, Nov and Dec. Appears that it was cut off in Dec 2019 or beginning of 2020 as the page views stop. There does seem to be a hit in May of 2020.
WebDev
More webdev students access the ds curriculum. There were no hits before july 2019. Hits have slowed down since jan 2020. There is still wdev students accessing the the ds curriculum in 2020 up through oct. Not sure if the access was shut down.

6. What topics are grads continuing to reference after graduation and into their jobs (for each program)? 

Data Science
DS students are looking into 1-fundamentals the most with the top 3 views subsets of fundamentals. Then students are looking into sql, classification, regression, and anomaly detection.
WebDev
Webdev students are looking at javascript-i, spring, html-css, java-ii, and java i the most. 

7. Which lessons are least accessed? 

Data Science
While there is a lot of pages rarely accessed, tableau & various fundamentals lessons ie(/cli/creating-files-and-directories, /spreadsheets-overview) were hardly accessed
WebDev
There are hundreds of pages looked at only 1 or 2 times. Difficult to pin point what exact topics are not being utilized post graduating.

8. Anything else I should be aware of? 

I would take into consideration the classes post pandemic may have more traffic since the classes are being held virtual. Students may not seem to be accessing the curriculum however, a number of students leave their windows open and do not refresh pages that are kept open. On another note, depending on when lessons/topics are taught, the amount of accesses may differ from cohort to cohort. As the class progresses, topics are re-introduced over and over which may lead to less accesses as the students start to understand the material better.
</details>

# How to reporduce
- Download ```anonymized-curriculum-access.txt``` and ```cohort.csv```
- Download ```acquire.py``` and ```prepare.py```
- Run files in jupyter notebook
