def make_ravioli(size):
    line = ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    ra = 'zyxwvutsrqponmlkjihgfedcba'

    letter = (a[size-1])
    for j in range(1,size):
        i = size-j
        al = a[i+1:a.index(letter)+1]
        ral = ra[ra.index(letter):len(ra)-i]
        dashes = (size-len(ral))*'--'
        middle = ''
        for k in ral+al:
            middle += k+'-'
        middle = middle[:len(middle)-1]
        line+=(dashes+middle+dashes)+"\n"

    for i in range(size):
        al = a[i+1:a.index(letter)+1]
        ral = ra[ra.index(letter):len(ra)-i]
        dashes = (size-len(ral))*'--'
        middle = ''
        for k in ral+al:
            middle += k+'-'
        middle = middle[:len(middle)-1]
        line+=(dashes+middle+dashes)+'\n'
    return(line[0:len(line)-1])