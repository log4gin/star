order := table()

order.max = def _ (t) {
    n  := len(t)
    i := 0
    resoult := t[i]
    while (i < n){
        if (t[i] > resoult) {
            resoult = t[i]
        }
        i++
    }
    resoult
}

order.choose = def _ (t){

    // init 
    n := len(t)
    i := 0 
    min_idx := i
    j := (i + 1)

    // logic
    while (i < n) {
        min_idx = i
        j = ( i + 1 )  
        
        while (j < n) {
            if (t[j] < t[min_idx]) {
                min_idx = j
            }
            j++
        }

        if (min_idx != i) {
            tmp := t[min_idx]
            t[min_idx] = t[i]
            t[i] = tmp
        }
        i++
    }
    t  
}

// end with  it for export

order

