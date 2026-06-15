with open("resource/data.bin", "wb") as file:
    file.write(b'DATA')
    file.write((1).to_bytes(2, "little"))
    file.write((3).to_bytes(4, "little"))

    file.write((100).to_bytes(8, "little"))
    file.write((1).to_bytes(4, "little"))
    file.write((2550).to_bytes(2, "little", signed=True))
    file.write((1).to_bytes(1, "little"))

    file.write((200).to_bytes(8, "little"))
    file.write((2).to_bytes(4, "little"))
    file.write((-1020).to_bytes(2, "little", signed=True))
    file.write((0).to_bytes(1, "little"))

    file.write((300).to_bytes(8, "little"))
    file.write((3).to_bytes(4, "little"))
    file.write((1800).to_bytes(2, "little", signed=True))
    file.write((5).to_bytes(1, "little"))

with open("resource/data.bin", "rb") as file:
    data = file.read(10)

    if len(data) < 10:
        print("Ошибка: файл слишком короткий!")
    else:
        signature = data[:4]
        version = int.from_bytes(data[4:6], "little")
        quantity = int.from_bytes(data[6:10], "little")

        print("Сигнатура:", signature)
        print("Версия:", version)
        print("Количество записей:", quantity)

        body = file.read()
        temps = []
        active_flags = 0
        rec_size = 15

        for i in range(quantity):
            start = i * rec_size
            rec = body[start : start + rec_size]
            temp_raw = int.from_bytes(rec[12:14], "little", signed=True)
            temps.append(temp_raw / 100)
            flag = rec[14]
            if flag != 0:
                active_flags += 1

        if temps:
            avg_temp = sum(temps) / len(temps)
            print(f"Средняя температура: {avg_temp} °C")
        else:
            print("Температурных данных нет")

        print(f"Активных флагов: {active_flags}")