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
* `input.*` testcaselarning input formati qanday bo'lishi kerakligini yozib chiqasiz. Yozib bo'lgandan so'ng, `generate.*` faylini ishga tushiring.
* `main.*` masala yechimining kodini shu yerga joylayiz (output fayllarni generatsiya qilish uchun). So'ng, `compile.*` faylini ishga tushiring.
* Tayyor bo'lgan testlar `tests` nomli faylda saqlanadi. Ushbu faylni zip holatga keltirib, tizimga yuklashingiz mumkin.
