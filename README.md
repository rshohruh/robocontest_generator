# Robocontest tizimida testlarni generatsiya qilish.
## Kerakli fayllarni yuklab oling.

    git clone https://github.com/rshohruh/robocontest_generator.git

## Faylni Visual Studio Code da oching.

    code robocontest_generator

## Yangi masala yarating
Windows uchun:

    py main.py masala_nomi

Linux & Mac uchun:
  
    python3 main.py masala_nomi


## Ushbu amallarni bajarganingizdan so'ng, `masala_nomi` nomli yangi papka yaratiladi. 
Ushbu papka ichidagi fayllar:
*   `generate.cpp` testlarni tuzish uchun ishlatiladi. Siz masalalarning sonini, uning ichida nimalar bo'lishi kerakligini qo'lda yozishingiz kerak. `randint(a, b)` funksiyasi [a, b] oralig'idagi taxminiy son generatsiya qiladi. Generatsiya muvaffaqiyatli yakunlangan so'ng sizda `tests` nomli yangi papka va uning ichida testlar paydo bo'ladi.
*    Agar yechim C++ tilida bo'lsa, `main.cpp` ichiga kodni joylashtiring, agar Pythonda bo'lsa, `main.py` ichiga kodni joylashtiring.
*   `compile.cpp` - `generate.cpp` muvaffaqiyatli tugatilgan so'ng, ushbu dasturni ishga tushiring.
*   `checker.cpp`, `checker.py` Checker yozish uchun ishlatiladi.