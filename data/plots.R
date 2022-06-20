library(dplyr)
library(ggplot2)
library(ggthemes)
library(tidyr)

data <- data.frame(alpha = character(30), lambda = character(30), w1 = numeric(30), w2 = numeric(30))
i <- 1

for (alpha in c(0.05, 0.1, 0.2, 0.5, 0.75)) {
    for (lambda in c(0, 1, 3, 5, 10, 20)) {
        results <- read.csv(paste0("data_", alpha, "_", lambda, "_out.csv"))
        data[i, ] <- c(alpha, lambda, mean(results$welfare_pi), mean(results$welfare_liter))
        i <- i + 1
    }
}

data$lambda <- factor(data$lambda, c("0", "1", "3", "5", "10", "20"))

p1 <- ggplot(data, aes(alpha, lambda, fill = w1)) +
    geom_tile() +
    labs(x = "α", y = "λ", fill = "Σπ") +
    scale_fill_distiller(palette = "RdPu") +
    theme_pander()

p2 <- ggplot(data, aes(alpha, lambda, fill = w2)) +
    geom_tile() +
    labs(x = "α", y = "λ", fill = "outflow") +
    scale_fill_distiller(palette = "RdPu") +
    theme_pander()

results_ok <- read.csv("data_0.05_20_out.csv")
results_stoch <- read.csv("stochastic.csv")

probs_by_player <- function (player, df) {
    data2 <- data.frame(inv = character(0), action = character(0), avgprob = numeric(0))

    for (inv in c(0, 1, 2, 3)) {
        for (a in c(1, 2, 3, 4, 5)) {
            data2 <- rbind(data2, data.frame(inv = as.character(inv), action = paste0("A", a), avgprob = mean(df[, paste0("p", player, "i", inv, "A", a)])))
        }
    }

    ggplot(data2, aes(inv, action, fill = avgprob)) +
        geom_tile() +
        labs(x = "Investment in public good", y = "Action", fill = "Avg. probability of play") +
        scale_fill_distiller(palette = "RdPu") +
        theme_pander()
}

profits <- read.csv("profits.csv") %>%
    mutate(welfare = pi1 + pi2 + pi3 + pi4)

q025 <- function (x) {
    quantile(x, 0.025)
}

q975 <- function (x) {
    quantile(x, 0.975)
}

p3 <- ggplot(profits, aes(x = round, y = welfare)) +
    geom_line(stat = "summary", fun = "mean") + 
    geom_line(stat = "summary", fun = "q025", color = "#1e5bff") + 
    geom_line(stat = "summary", fun = "q975", color = "#1e5bff") + 
	coord_cartesian(xlim = c(0, 1000)) +
    theme_pander()

profits2 <- gather(profits, farmer, profit, pi1:pi4)
profits2$farmer <- substr(profits2$farmer, 3, 3)

p4 <- ggplot(profits2, aes(x = round, y = profit, group = farmer, color = farmer)) +
    geom_line(stat = "summary", fun = "mean") + 
	coord_cartesian(xlim = c(0, 1000)) +
    theme_pander()

# save:

ggsave(filename = "plot_learning_profits.pdf", plot = p4, device = cairo_pdf, width = 8, height = 6)
