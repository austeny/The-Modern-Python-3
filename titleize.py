def titleize(s):
    sl = s.split(' ')
    print(sl)
    # sl = [f"{s[0].upper()}{s[1::]}" for s in sl]
    sl = [s[0].upper()+s[1::] for s in sl]
     
    print(sl)
    return ' '.join(sl)

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"