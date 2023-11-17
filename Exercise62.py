n={4.95: "Mon do A",
   9.95: "Mon do B",
   14.95: "Mon do C",
   19.95: "Mon do D",
   24.95: "Mon do E"}
print("{:<10} {:<15} {:<15}".format("Gia goc", "Chiet khau", "Gia moi"))
print("-"*45)
ti_le_giam= 0.6
for gia, mon_do in n.items():
    tien_giam = gia * ti_le_giam
    giam_gia = gia - tien_giam
    print("${:<9} ${:<14} ${:<14}".format(gia, round(tien_giam, 2), round(giam_gia, 2)))