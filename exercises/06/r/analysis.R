library(ggplot2)
library(dplyr)
library(tidyr)
library(viridis)
library(ggpubr)

df = read.csv("../data/n_anonymization.csv") %>%
  filter(
    n <= 20,
    operation == 'deterministic',
  ) %>%
  group_by(mode, n) %>%
  summarise(
    mean_ncp = mean(ncp),
    sd_ncp = sd(ncp),
  )
df$mode = factor(df$mode)
levels(df$mode) = c("Relaxed", "Strict")

ggplot(df, aes(x = n, y = mean_ncp, color = mode, shape = mode)) +
  geom_point() +
  theme_minimal() +
  labs(x = "k-anonymity", y = "NCP", color = "Mode") +
  guides(shape = FALSE) +
  theme(legend.text = element_text("Mode")) +
  scale_y_continuous(
    labels = scales::percent_format(accuracy = 1)
  ) + 
  ggsave("../resources/k_anonymity_ncp.png", dpi = "print")


df_randomized = read.csv("../data/n_anonymization.csv") %>%
  filter(
    n <= 20,
    mode == 'strict',
  ) %>%
  group_by(operation, n) %>%
  summarise(
    mean_ncp = mean(ncp),
    sd_ncp = sd(ncp),
  )
df_randomized$operation = factor(df_randomized$operation)
levels(df_randomized$operation) = c("Deterministic", "Randomized")

ggplot(df_randomized, aes(x = n, y = mean_ncp, color = operation, shape = operation)) +
  geom_point() +
  theme_minimal() +
  labs(x = "k-anonymity", y = "NCP", color = "Mode") +
  guides(shape = FALSE) +
  theme(legend.text = element_text("Mode")) +
  scale_y_continuous(
    labels = scales::percent_format(accuracy = 1)
  ) + 
  ggsave("../resources/k_anonymity_ncp_randomized.png", dpi = "print")
