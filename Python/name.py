print("Schaltjahrberechner;")

jahr = int(input("Welches Jahr soll ich berechnen?"))

if (jahr % 4) == 0 and (jahr % 100) != 0 or (jahr % 400) == 0:
    print("Schaltjahr")
else:
    print("kein Schaltjahr")


# Order of Operations
# 0. :=
# 1. lambda
# 2. if – else
# 3. or
# 4. and
# 5. not x
# 6. in, not in, is, is not, <, <=, >, >=, !=, ==
# 7. |
# 8. ^
# 9. &
#10. <<, >>
#11. +, -
#12. *, @, /, //, %
#13. +x, -x, ~x
#14. **
#14. await x
#15. x[index], x[index:index], x(arguments...), x.attribute
#16. (expressions...), [expressions...], {key: value...}, {expressions...}
