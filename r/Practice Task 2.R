books <- data.frame(
  Title = c("মেঘের দেশে", "নীল আকাশ", "সোনার খেলা", "রঙিন স্বপ্ন", "ছায়ার ছায়া"),
  Author = c("রবীন্দ্রনাথ", "সেলিনা হোসেন", "হুমায়ূন আহমেদ", "শীর্ষা রহমান", "কাজী নজরুল"),
  Pages = c(120, 200, 150, 180, 220),
  Published = c(2010, 2015, 2012, 2018, 2020)
)

View(books)

mean(books$Pages)

books[books$Pages > 150,]
books[books $Published > 2015,]


books $prefraence <- c(3, 4, 2, 5,1)
View(books)
