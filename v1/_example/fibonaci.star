def fibonaci (n){
    if  (n < 2){
        1
    }else{
         (
            fibonaci((n - 1))
            +
            fibonaci((n - 2))
        )
    }
}


print(now())

times := 0

while (times < 15) {
    print(fibonaci(times))
    times++
}

print(now())
