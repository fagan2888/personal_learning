## R Workshop

## file:///Users/MariaAthena/Downloads/presentation.html#23

# reading and writing data
install.packages("readr")
# data manipulation
install.packages("dplyr")
# data pipelines
install.packages("magrittr")
# reading data from Excel
install.packages("readxl")
# tidying data
install.packages("tidyr")
# working with dates and times
install.packages("lubridate")


# Read from .csv
# data <- read_csv("[some data].csv", col_names = TRUE, skip = 0, col_types = NULL)

# Reading from other flat file sources
# data <- read_delim("path/to/file",...)

# Reading from Excel -> AVOID AT ALL COSTS
# library(readxl)
# data <- read_excel("path/to/excel/file", sheet = "[the sheet you want]", col_names = T)

# Writing data with R
# write_delim(data, file = "./outputs/file.txt", delim = "|")
# write_csv(data, file = "./outputs/file.csv")
# library(xlsx)
# write.xlsx(data, file = "/path/to/file.xlsx")

library(readr)

oyster <- read_csv("/Users/MariaAthena/Dropbox/00 Imperial College/Intro to R/Workshop/oyster.csv")
station <- read_csv("/Users/MariaAthena/Dropbox/00 Imperial College/Intro to R/Workshop/stations.csv")

# View() command from the script or the command line - this will also open the viewer
# print the first few lines of the data to the console
head(oyster, 1)
head(stations, 1)

# force everything to lower case
names(oyster) <- tolower(names(oyster))

# prints an overview of your data, incl dimensions and data type (class) of each column
str(oyster)
# presents a summary of each column, depending on the class of data within it
summary(oyster)

# Fixing problems - changing data types
as.character(oyster$credit) # Forces the values to be characters
as.numeric(oyster$credit)    # Forces the values to be numbers
oyster$credit <- as.character(oyster$credit) # Change the length to text
str(oyster)    # Check what we've done
oyster$credit <- as.numeric(oyster$credit) # Change it back


# OTHER DATA SUMMARIES
min(data$field)    # Gives the minimum
mean(data$field)   # Gives the mean
max(data$field)    # Gives the maximum
range(data$field)  # Gives the min and max
unique(data$field) # Gives unique values - similar to SQL "DISTINCT"
table(data$field)  # Gives a frequency table

# MISSING VALUES
x <- c(1, 2, 3, 4, 5, NA)
mean(x)
# We can get around this by adding the na.rm argument to the function:
mean(x, na.rm = TRUE)


# What are the top 5 journeys?
# What was the longest journey, how long was it, and when was it?
# What is the average journey time for each day of the week?
# What is the average number of journeys per day of the week?
# Where does Jim live, and what are the coordinates of the station?



library(magrittr)
# take some_data, then perform some function on it
some_data %>% some_function


library(dplyr)

# Selecting and dropping variables
# SELECT, used to select columns in a data frame.
select([data], [fields to select]) # The general form of the function
oyster %>% select(Date, journey.action, charge) # Select just date, journey and charge
oyster %>% select(1, 2, 3) # We can also use column positions to select
oyster %>% select(1:3, 5, 7)

# We can combine also use "negative selection" to drop variables we don't want any more
oyster %>% select(-journey.action, -charge)
oyster %>% select(-c(4, 6, 7))

# FILTER 
# Think of filter as a WHERE clause - it subsets by rows
filter([data], [filter conditions]) # the general form of the function
oyster %>% filter(charge != 0) # Numeric condition
oyster %>% filter(note != "") # Text condition
# To combine multiple filters use & for AND and | for OR
whoops <- oyster %>% filter(balance < 0) # filtering with assignment
noteworthy <- oyster %>% filter(note != "" & charge >= 2) # multiple conditions

# SUMMARISE verb is a powerful way to compute summaries over the data:
summarise([data], [new_field] = some_function([existing_field])) # the general function
oyster %>% summarise(avg_charge = mean(charge, na.rm = TRUE)) # average charge
# Multiple summaries functions separated by a comma:
oyster %>% summarise(avg_charge = mean(charge, na.rm = TRUE), # average charge
sd_charge = sd(charge, na.rm = TRUE)) # charge std. deviation

# Aggregating by groups
# we need to group before we summarise
group_by([data], [field_to_group_by_1], [field_to_group_by_2]) # general form
oyster %>% group_by(journey.action) # this doesn't tell us much - add a summary!
oyster %>% 
    group_by(journey.action) %>% 
    summarise(avg_cost = mean(charge, na.rm = TRUE)) # more interesting


# ARRANGE verb, which sorts data.
arrange([data], [fields_to_order_by]) # general form
oyster %>% arrange(date)
# Reverse ordering:
oyster %>% arrange(-charge)
# Multiple ordering fields:
oyster %>% arrange(journey.action, -charge)


# Putting it all together
# What are the top 5 journeys?
oyster_summary <- oyster %>% 
    group_by(journey.action) %>% 
    summarise(journeys = n()) %>% 
    arrange(-journeys) %>% 
    head(5)


# SLICE allows rows to be filtered by index
badRecords <- "Topped-up|Season ticket|Unspecified location"
# grep([what to search], [where to search for it])
# grep searches for patterns called regular expressions, they're a compact way
# of specifying patterns to search for.
records <- grep(badRecords, oyster$journey.action) 
# slice([data], [rows to keep or exclude]) the general form
oyster <- oyster %>% slice(-records)


# MUTATE -> add variables to a data set
mutate([data], [some_new_field]) # general form
oyster %>%  mutate(newField = 4) # set up a new field with the value 4 (always) - useless

# We can also use simple functions to do calculations, 
# and specify multiple new fields by separating them with commas.
oyster %>% mutate(cost_plus_bal = charge + balance, # add charge to balance
cost_plus_bal_clean = sum(charge, balance, na.rm = TRUE)) # clean up
# Or, use conditions to create variables (similar to a CASE statement):
oyster %>% mutate(no_cost = ifelse(charge == 0 | is.na(charge), 1, 0))


# PASTE
paste(string1, string2, string3, ..., sep = " ") # paste strings together with a space
paste0(string1, string2, string3, ...) # paste things together with no space

# Combining this with mutate it's easy to add cleaned up fields:
oyster <- oyster %>% 
            mutate(start.time.clean = paste0(start.time, ":00"),
                    end.time.clean = paste0(end.time, ":00"))


# Splitting fields
library(tidyr)
separate([data], [column to separate], [new columns], sep = [separator], remove = FALSE)
oyster <- oyster %>% 
    separate(col = journey.action, 
             into = c("from", "to"), 
             sep = " to ", 
             remove = FALSE)


# Working with dates and times
library(lubridate)












