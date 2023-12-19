from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# register_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Registratsiyadan otish", request_contact=True)
#         ]
#     ], resize_keyboard=True
# )
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Choose Cars"),
            KeyboardButton(text="Problems🔧")
        ],
    ], resize_keyboard=True
)
cars_co = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Germany 🇩🇪"),
            KeyboardButton(text="Japan 🇯🇵")
        ],
        [
            KeyboardButton(text="Britan 🇬🇧 "),
            KeyboardButton(text="American 🇺🇸")

        ],
        [
            KeyboardButton(text="Next ➡️")

        ],
        [
            KeyboardButton(text="🔚 Main menu")

        ]
    ], resize_keyboard=True
)
German = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="AUDI"),
            KeyboardButton(text="BMW"),
        ],
        [
            KeyboardButton(text="PORSCHE"),
            KeyboardButton(text="MERCEDES"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),
        ]

    ]
)
bmw = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="m5 comp"),
            KeyboardButton(text="7 series"),
        ],
        [
            KeyboardButton(text="m8 comp"),
            KeyboardButton(text="x5 comp"),
        ],
        [
            KeyboardButton(text="other bmw ➡️")

        ],
        [
            KeyboardButton(text="⬅️ Back"),
        ]

    ]
)
Japan = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TOYOTA"),
            KeyboardButton(text="NISSAN"),
        ],
        [
            KeyboardButton(text="LEXUS"),
            KeyboardButton(text="MITSUBISHI"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),
        ]

    ]
)
Britain = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BENTLEY"),
            KeyboardButton(text="MCLAREN"),
        ],
        [
            KeyboardButton(text="ASTON MARTIN"),
            KeyboardButton(text="ROVER"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),
        ]

    ]
)
us = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="FORD"),
            KeyboardButton(text="DODGE"),
        ],
        [
            KeyboardButton(text="CHEVROLET"),
            KeyboardButton(text="TESLA🔋"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),

        ]

    ]
)

next_cars = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sweden 🇸🇪"),
            KeyboardButton(text="Italian 🇮🇹"),
        ],
        [
            KeyboardButton(text="Chinese 🇨🇳"),
            KeyboardButton(text="French 🇫🇷"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),
        ]

    ]
)

swed = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="KOENIGSEGG 👻"),
            KeyboardButton(text="VOLVO"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),

        ]
    ]
)
china = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BYD"),
            KeyboardButton(text="JETOUR"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),

        ]
    ]
)
italian = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="FERRARI"),
            KeyboardButton(text="LAMBORGHINI"),
        ],
        [
            KeyboardButton(text="PAGANI"),
            KeyboardButton(text="MASERATI"),
        ],
        [
            KeyboardButton(text="   🔚 Main menu")

        ]
    ]
)
