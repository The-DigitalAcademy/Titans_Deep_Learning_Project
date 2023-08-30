
library(ggplot2, dplyr)

#reading the csv file

data <- read.csv("/Users/da_m1_22/Downloads/StudentsPerformance (1).csv")
data

#------------------------data exploration-------------------------------
summary(data)

str(data)

# Check for duplicate rows in the entire data frame
duplicated(data)

# Check for missing values in the entire dataset
sum(is.na(data))

# Using the names() function
all_features <- names(data)

# Alternatively, using the colnames() function
all_features <- colnames(data)

#-------- Data visualization:Univariate ----------
#How are the math scores distributed across different parental levels of education?
# Histogram or density plot of math scores by parental education
ggplot(data, aes(x = math.score, fill = parental.level.of.education)) +
  geom_histogram(binwidth = 5, position = "identity", alpha = 0.7) +
  labs(title = "Distribution of Math Scores by Parental Education",
       x = "Math Score",
       y = "Frequency") +
  theme_minimal()


#What is the distribution of reading scores for different lunch types?
# Density plot of reading scores by lunch type
ggplot(data, aes(x = reading.score, fill = lunch)) +
  geom_density(alpha = 0.5) +
  labs(title = "Distribution of Reading Scores by Lunch Type",
       x = "Reading Score",
       y = "Density") +
  theme_minimal()

#How do writing scores vary among different race/ethnicity groups?
# Box plot of writing scores by race/ethnicity
ggplot(data, aes(x = race.ethnicity, y = writing.score)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Variation of Writing Scores by Race/Ethnicity",
       x = "Race/Ethnicity",
       y = "Writing Score") +
  theme_minimal() +
  coord_flip()

#Does completion of the test preparation course impact math scores?
# Box plot of math scores by test preparation completion
ggplot(data, aes(x = test.preparation.course, y = math.score)) +
  geom_boxplot(fill = "lightgreen") +
  labs(title = "Impact of Test Preparation on Math Scores",
       x = "Test Preparation Completion",
       y = "Math Score") +
  theme_minimal()

#

#-------- Data visualization: Multivariate ----------

# How does parental level of education affect math, reading, and writing scores, considering different lunch types?
#Create box plots for math, reading, and writing scores
ggplot(data, aes(x = parental.level.of.education, y = math.score, fill = lunch)) +
  geom_boxplot() +
  labs(title = "Impact of Parental Education on Math Scores",
       x = "Parental Level of Education",
       y = "Math Score") +
  facet_wrap(~ lunch) +
  theme_minimal()

ggplot(data, aes(x = parental.level.of.education, y = reading.score, fill = lunch)) +
  geom_boxplot() +
  labs(title = "Impact of Parental Education on Reading Scores",
       x = "Parental Level of Education",
       y = "Reading Score") +
  facet_wrap(~ lunch) +
  theme_minimal()

ggplot(data, aes(x = parental.level.of.education, y = writing.score, fill = lunch)) +
  geom_boxplot() +
  labs(title = "Impact of Parental Education on Writing Scores",
       x = "Parental Level of Education",
       y = "Writing Score") +
  facet_wrap(~ lunch) +
  theme_minimal()


#Is there a correlation between math, reading, and writing scores, and how does this relationship vary by gender and race/ethnicity?
# Create a scatterplot matrix with color and shape aesthetics
scatterplot_matrix <- ggplot(data, aes(x = math.score, y = reading.score)) +
  geom_point(aes(color = gender, shape = race.ethnicity), alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE, color = "black") +
  labs(title = "Correlation between Math and Reading Scores",
       x = "Math Score",
       y = "Reading Score") +
  facet_grid(gender ~ race.ethnicity) +
  theme_minimal() +
  theme(legend.position = "top")

scatterplot_matrix

#What is the distribution of scores for students based on their gender, ethnicity, and completion of the test preparation course?
# Create histograms or density plots for each subject
subject_plots <- ggplot(data, aes(x = math.score, fill = test.preparation.course)) +
  geom_histogram(binwidth = 5, position = "identity", alpha = 0.5) +
  facet_grid(race.ethnicity ~ gender) +
  labs(title = "Distribution of Math Scores by Gender, Ethnicity, and Test Preparation",
       x = "Math Score",
       y = "Frequency") +
  theme_minimal() +
  theme(legend.position = "top")

subject_plots <- subject_plots + 
  geom_histogram(binwidth = 5, position = "identity", alpha = 0.5, aes(x = reading.score)) +
  labs(title = "Distribution of Reading Scores by Gender, Ethnicity, and Test Preparation",
       x = "Reading Score",
       y = "Frequency") +
  theme_minimal() +
  theme(legend.position = "top")

subject_plots <- subject_plots + 
  geom_histogram(binwidth = 5, position = "identity", alpha = 0.5, aes(x = writing.score)) +
  labs(title = "Distribution of Writing Scores by Gender, Ethnicity, and Test Preparation",
       x = "Writing Score",
       y = "Frequency") +
  theme_minimal() +
  theme(legend.position = "top")

# Print the plot
print(subject_plots)


# Is there a relationship between parental level of education and test scores, and how does lunch type impact this relationship?
# Create scatterplots with regression lines
scatter_plots <- ggplot(data, aes(x = parental.level.of.education, y = math.score, color = lunch)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Relationship between Parental Education and Math Scores by Lunch Type",
       x = "Parental Education",
       y = "Math Score") +
  theme_minimal() +
  theme(legend.position = "top")

scatter_plots <- scatter_plots +
  geom_point(aes(y = reading.score)) +
  geom_smooth(method = "lm", se = FALSE, aes(y = reading.score)) +
  labs(title = "Relationship between Parental Education and Reading Scores by Lunch Type",
       x = "Parental Education",
       y = "Reading Score") +
  theme_minimal() +
  theme(legend.position = "top")

scatter_plots <- scatter_plots +
  geom_point(aes(y = writing.score)) +
  geom_smooth(method = "lm", se = FALSE, aes(y = writing.score)) +
  labs(title = "Relationship between Parental Education and Writing Scores by Lunch Type",
       x = "Parental Education",
       y = "Writing Score") +
  theme_minimal() +
  theme(legend.position = "top")

# Print the plot
print(scatter_plots)


#How do math, reading, and writing scores vary across different race/ethnicity groups, considering parental level of education?

# Create side-by-side box plots
box_plots <- ggplot(data, aes(x = race.ethnicity, y = math.score, fill = parental.level.of.education)) +
  geom_boxplot() +
labs(title = "Variation of Math Scores Across Race/Ethnicity and Parental Education",
     x = "Race/Ethnicity",
     y = "Math Score") +
  theme_minimal() +
  theme(legend.position = "top") +
  coord_flip()

box_plots <- box_plots +
  geom_boxplot(aes(y = reading.score)) +
  labs(title = "Variation of Reading Scores Across Race/Ethnicity and Parental Education",
       x = "Race/Ethnicity",
       y = "Reading Score") +
  theme_minimal() +
  theme(legend.position = "top") +
  coord_flip()

box_plots <- box_plots +
  geom_boxplot(aes(y = writing.score)) +
  labs(title = "Variation of Writing Scores Across Race/Ethnicity and Parental Education",
       x = "Race/Ethnicity",
       y = "Writing Score") +
  theme_minimal() +
  theme(legend.position = "top") +
  coord_flip()

# Print the plot
print(box_plots)

#Does the type of lunch (standard or free/reduced) have an impact on scores, and how does test preparation completion influence this relationship?
# Create an interaction plot or line plot
interaction_plot <- ggplot(data, aes(x = lunch, y = math.score, color = test.preparation.course, group = test.preparation.course)) +
  geom_line(aes(group = test.preparation.course)) +
  geom_point() +
  labs(title = "Impact of Lunch Type and Test Preparation on Math Scores",
       x = "Lunch Type",
       y = "Math Score") +
  theme_minimal() +
  theme(legend.position = "top")

interaction_plot <- interaction_plot +
  geom_line(aes(y = reading.score, group = test.preparation.course), linetype = "dashed") +
  geom_point(aes(y = reading.score)) +
  labs(title = "Impact of Lunch Type and Test Preparation on Reading Scores",
       x = "Lunch Type",
       y = "Reading Score") +
  theme_minimal() +
  theme(legend.position = "top")

interaction_plot <- interaction_plot +
  geom_line(aes(y = writing.score, group = test.preparation.course), linetype = "dotted") +
  geom_point(aes(y = writing.score)) +
  labs(title = "Impact of Lunch Type and Test Preparation on Writing Scores",
       x = "Lunch Type",
       y = "Writing Score") +
  theme_minimal() +
  theme(legend.position = "top")

# Print the plot
print(interaction_plot)

