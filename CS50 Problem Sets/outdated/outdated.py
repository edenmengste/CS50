lit = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
  try:
    change = input("Date: ").title()

    if "/" in change:
       mo , dy , yr = change.split("/")
       m = int(mo)
       d = int(dy)
       y = int(yr)

       if not(1<=m<=12 and 1<=d<=31):
          raise ValueError

       print(f"{y}-{m:02d}-{d:02d}")
       break

    elif "," in change:
       out = change.replace(",", " ")
       mo, dy, yr = out.split()

       ind = lit.index(mo) + 1

       d=int(dy)
       y = int(yr)

    
       if not(1<=ind<=12 and 1<=d<=31):
          raise ValueError


       print(f"{y}-{ind:02d}-{d:02d}")
       break


    else:
        continue


  except ValueError:
    continue




