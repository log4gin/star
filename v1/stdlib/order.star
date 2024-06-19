order := table()

order.max = def _ (t) {
    n  := len(t)
    i := 0
    resoult := 0
    while (i < n){
        if (t[i] > resoult) {
            resoult = t[i]
        }
        i++
    }
    resoult
}

order

