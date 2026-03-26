day = input("Enter a day: ").lower()

match day:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("ini Hari kerja")
    case "sabtu" | "minggu":
        print("Ini Hari Libur")
    case _:
        print("Invalid day")