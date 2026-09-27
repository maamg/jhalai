setwd("Z:/Learning Programming/R")
getwd()
data_csv <- read.csv("Author.csv",  fileEncoding = "CP1252")
View(data_csv)
str(data_csv)

install.packages("readxl") 
library(readxl)

data_excel <- read_excel("students.xlsx")

str(data_excel)


# Install SPSS Package in R

install.packages("haven")

library(haven)
setwd("Z:/Learning Programming/R")
# read SPSS file 
spss_data <- read_sav("Employee data.sav")


# Quick dataset check
head(spss_data)
View(spss_data)
tail(spss_data)
summary(spss_data)

names(spss_data)

names(spss_data)[1] <- "Id"

names(spss_data)
is.na(spss_data)
colSums(is.na(spss_data))

str(spss_data)
summary(spss_data)
sum(is.na(spss_data))
numb <- is.na(spss_data)

sum(numb)
colSums(is.na(spss_data))
