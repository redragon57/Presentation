library(ggplot2)
library(cowplot)
myData <- read.csv("result_ex7.csv", header=TRUE, sep="\t")
pm <- ggplot(myData, aes(number, eat, color=type)) + labs(x="Taille de la structure",y="Temps en milliseconde",title="eat") + geom_point() + geom_smooth(method="loess", se = FALSE)
ggsave("result_eat.png", width = 7, height = 3, dpi = 300)

pa <- ggplot(myData, aes(number, carrot, color=type)) + labs(x="Taille de la structure",y="Temps en milliseconde",title="carrot") + geom_point() + geom_smooth(method="loess", se = FALSE)
ggsave("result_carrot.png", width = 7, height = 3, dpi = 300)

pr <- ggplot(myData, aes(number, purify, color=type)) + labs(x="Taille de la structure",y="Temps en milliseconde",title="purify") + geom_point() + geom_smooth(method="loess", se = FALSE)
ggsave("result_purify.png", width = 7, height = 3, dpi = 300)

p <- plot_grid(pm, pa, pr, labels = c("eat", "carrot", "purify"), ncol = 2, nrow = 2)
ggsave("result_ex7.png", width = 14, height = 6, dpi = 400)
