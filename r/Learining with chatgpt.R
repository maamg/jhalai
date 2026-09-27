data_frame <- data.frame(
  name   = c("Rahim", "Karim", "Aysha", "Nusrat"),
  age    = c(14, 14, 15, 30),
  score  = c(76, 87, 85, 89),
  passed = c(TRUE, TRUE, FALSE, TRUE)
)



# adding a new column
data_frame$Grade <-c('A', 'B', 'A+', 'B+')


View(data_frame)

# Simple Analysis 
mean(data_frame$age)
max(data_frame$score)
min(data_frame$age)


# Save Data
write.csv(data_frame, "student_data.csv", row.names =  FALSE)

