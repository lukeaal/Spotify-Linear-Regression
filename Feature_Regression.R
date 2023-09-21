x = read.csv2("/data/FatherJohnMisty.csv",stringsAsFactors=FALSE,sep=",");
x = sapply(x, as.character)
x = data.matrix(x)
x = apply(x, 2, as.numeric) #changing the data type from character to numeric

new_data = scale(x[,9:11]) #Standardizing the dataset
View(new_data)
new_x = cbind(x[,1:8],new_data) #Binding the columns together
View(new_x)

X = as.matrix(new_x[,1:10]);
y = as.vector(new_x[,11]);
a = solve(t(X) %*% X, t(X) %*% y)
paste("coefficients are:")
yhat = X %*% a
sse = sum((y - yhat) ^ 2)
paste("sse =", sse) #Finding the sum of squared errors

new_sse = rep(0, 10)
diff = rep(0, 10)
for (i in 1:10) {
  newX = X[,-i]
  a = solve(t(newX) %*% newX, t(newX) %*% y)
  yhat = newX %*% a
  new_sse[i] = sum((y - yhat) ^ 2)
  diff[i] = abs(new_sse[i] - sse)
  cat(
    paste0(
      "Omit variable ",
      i ,
      ": new sse = ",
      new_sse[i],
      ", difference with old sse = ",
      diff[i],
      ".\n"
    )
  )
}
cat("Most difference is", max(diff), "\n")
cat("Least difference is", min(diff), "\n")
