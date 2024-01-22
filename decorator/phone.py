def wrapper(f):
    def fun(l):
        format_l = []
        for s in l:
            if s.startswith('0') and len(s) == 11:
                fomat_s = "+91 " + s[1:6] + " " + s[6:]
                format_l.append(fomat_s)
            elif s.startswith('91') and len(s) == 12:
                fomat_s = "+91 " + s[2:7] + " " + s[7:]
                format_l.append(fomat_s)
            elif s.startswith('+91') and len(s) == 13:
                fomat_s = "+91 " + s[3:8] + " " + s[8:]
                format_l.append(fomat_s)
            elif len(s) == 10:
                fomat_s = "+91 " + s[:5] + " " + s[5:]
                format_l.append(fomat_s)
        f(format_l)
        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


