library(ggplot2)
library(cowplot)
myData <- read.csv("result.csv", header=TRUE, sep="\t")
pm <- ggplot(myData, aes(number, min, color=type)) + labs(x="Taille de la structure",y="Temps en milliseconde",title="Minimum") + geom_point() + geom_smooth(method="loess", se = FALSE)
ggsave("result_min.png", width = 7, height = 3, dpi = 300)

pa <- ggplot(myData, aes(number, add, color=type)) + labs(x="Taille de la structure",y="Temps en milliseconde",title="Add") + geom_point() + geom_smooth(method="loess", se = FALSE)
ggsave("result_add.png", width = 7, height = 3, dpi = 300)

pr <- ggplot(myData, aes(number, remove, color=type)) + labs(x="Taille de la structure",y="Temps en milliseconde",title="Remove") + geom_point() + geom_smooth(method="loess", se = FALSE)
ggsave("result_remove.png", width = 7, height = 3, dpi = 300)

p <- plot_grid(pm, pa, pr, labels = c("min", "add", "remove"), ncol = 2, nrow = 2)
ggsave("result.png", width = 14, height = 6, dpi = 400)
