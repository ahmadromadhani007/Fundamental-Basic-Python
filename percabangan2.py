# If bersarang yaitu di dalam IF ada IF lagi dan merupakan lanjutan opsi dari percabangan sebelumnya

x = 11
if x < 10:
    print("x kurang dari 10")

    if x <= 4:
        print("x kurang dari atau sama dengan 4")
    else:
        print("x lebih dari 4")


elif x == 10:
    print("x samadengan 10")

else:
    print("x tidak kurang atau lebih dari 10")

print("Those are examples")