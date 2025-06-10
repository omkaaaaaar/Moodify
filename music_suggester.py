def suggest_songs(mood, tastes):
    songs_db = {
        'Happy': {
            'Pop': [
                {"title": "Ishq – Donn Bhat", "url": "https://open.spotify.com/track/760n01fPMR7sqrn3msFBcT?si=452324cf89884f37"},
                {"title": "Kismat Ke Maare – Gunda", "url": "https://open.spotify.com/track/7qmNW0yvUa4QW9tEN1kr9P?si=b95dec4267204984"}
            ],
            'DHH': [
                {"title": "Naam Kaam Sheher – Seedhe Maut", "url": "https://open.spotify.com/track/2DbKS4DbtcCTRizgu0EmLa?si=970c5a93562a43cd"},
                {"title": "Ishaaro ki Zubaan – OG Lucifer, Encore ABJ", "url": "https://open.spotify.com/track/0GvivjeCKE334SZQXSCl5x?si=eeb9fa827eaf48b5"}
            ],
            'Rap': [
                {"title": "90210 – Travis Scott", "url": "https://open.spotify.com/track/51EC3I1nQXpec4gDk0mQyP?si=be31ab0c89a44337"},
                {"title": "One of Wun – Gunna", "url": "https://open.spotify.com/track/4Na2HfNSr58chvfX69fy36?si=febb6f2aabc3401c"}
            ],
            'EDM': [
                {"title": "Ten – Fred Again", "url": "https://open.spotify.com/track/6twB0uYXJYW9t5GHfYaQ3i?si=512f2922ec10421c"},
                {"title": "Adore You – Fred Again", "url": "https://open.spotify.com/track/3YgtkOxZsTuaZdL8McA1FQ?si=79a38db8c6c44dfb"}
            ],
            'Rock': [
                {"title": "Back to the Old House– The Smiths", "url": "https://open.spotify.com/track/6LUGvXEAK8WxIBYK43uoTb?si=b066c54cdf594825"},
                {"title": "Robbers– The 1975", "url": "https://open.spotify.com/track/73jVPicY2G9YHmzgjk69ae?si=6d63db4a818f46ee"}
            ]
        },
        'Sad': {
            'Pop': [
                {"title": "Somebody Else – The 1975", "url": "https://open.spotify.com/track/4m0q0xQ2BNl9SCAGKyfiGZ?si=04852871e12a499c"},
                {"title": "When I Was Your Man – Bruno Mars", "url": "https://open.spotify.com/track/3M1tRXsBw2DFGpm7xyVDbE"}
            ],
            'DHH': [
                {"title": "Bechara – Seedhe Maut", "url": "https://open.spotify.com/track/5GTpmHZKqhHWccoJ3o86KJ?si=bb9a82d6331e42be"},
                {"title": "EK Din – The Seige", "url": "https://open.spotify.com/track/1hlgWN4erCHPTVV7qhY6we?si=9d964d16604d4649"}
            ],
             'EDM': [
                {"title": "Little Mystery – Fred Again", "url": "https://open.spotify.com/track/0BVIfVKh1wkQjNK32GMHM2?si=bb77e0c1dfd74e15"},
                {"title": "The Nights –  Avicii", "url": "https://open.spotify.com/track/0ct6r3EGTcMLPtrXHDvVjc?si=278574a61d24468b"}
            ],
            'Rock': [
                {"title": "Sextape – Deftones", "url": "https://open.spotify.com/track/1EryAkZ0VHstC6haIxVBiE?si=1a22103bf5c843a9"},
                {"title": "The Night We Met – Lord Huron", "url": "https://open.spotify.com/track/6j7w2d1c5b6k3e4z9Z0aF?si=8f1f1f451878c4d17"}
            ],
            'Rap': [
                {"title": "Luther – Kendrick Lmar, SZA", "url": "https://open.spotify.com/track/45J4avUb9Ni0bnETYaYFVJ?si=5c8d7a1398be4289"},
                {"title": "Drugs You Should Try It – Travis Scott", "url": "https://open.spotify.com/track/4b7vk8SRcYgnxpk0JOIS7r?si=0377517f3c764632"}
                
            ]
        },
        'Neutral': {
            'DHH': [
                {"title": "Mausambi Drip – Dhanji", "url": "https://open.spotify.com/track/7o2YhfaZZE3eEV7GV5kFpc?si=4a4e3658343b4a9b"},
                {"title": "MatchStick – Gravity, Acharaya", "url": "https://open.spotify.com/track/14mZWOGUckCZbPecP3IBCs?si=c8fc13ed010a437e"}
            ],
            'EDM': [
                {"title": "Faded – Alan Walker", "url": "https://open.spotify.com/track/7gHs73wELdeycvS48JfIos"},
                {"title": "Alone – Marshmello", "url": "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a"}
            ],
            'Rap': [
                {"title": "Sicko Mode – Travis Scott", "url": "https://open.spotify.com/track/7t8rj2d1c5b6k3e4z9Z0aF"},
                {"title": "9 – Drake", "url": "https://open.spotify.com/track/1C7KSXR2GVxknex6I4ANco?si=e7f1f451878c4d17"}
                
            ],
            'Rock': [
                {"title": "Counting Stars – OneRepublic", "url": "https://open.spotify.com/track/6OzhJ6i8mD3MGxgjYclPCo"}
            ],
            'Pop': [
                {"title": "Shape of You – Ed Sheeran", "url": "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3"},
                {"title": "Prove it – Kendrick Lamar, Summer Walker", "url": "https://open.spotify.com/track/5wttBUDyaHAR5q9fYnN3YF?si=704a747223b143d4"}
            ]
        },

       'Angry': {
        'DHH': [
            {"title": "KYA – Chaar Diwari", "url": "https://open.spotify.com/track/6LA6D7TtczDd2GqT8zm7YS?si=0d6d6ec572e34f9f"},
            {"title": " Rent is Due – The Seige", "url": "https://open.spotify.com/track/7wHSZvDMvZpIMM6iYPjapF?si=b7faea22cf204a26"}
        ],
        'Rock': [
            {"title": "Break Stuff – Limp Bizkit", "url": "https://open.spotify.com/track/3szzS6GB01f4DmOaWojCqV"},
            {"title": "Killing in the Name – Rage Against the Machine", "url": "https://open.spotify.com/track/2ZIduOjMkq9tx3dr6v0U9L"}
        ],
        'Rap': [
            {"title": "Till I Collapse – Eminem", "url": "https://open.spotify.com/track/6QgjcU0zLnzq5OrUoSZ3OK"},
            {"title": "Fight the Power – Public Enemy", "url": "https://open.spotify.com/track/4PKod6f7Zj0wNfR8rw7KGd"},
            {"title": "HUMBLE. – Kendrick Lamar", "url": "https://open.spotify.com/track/7KXjTSCq5nL1LoYtL7XAwS"}
        ],
        'Pop': [
            {"title": "Bad Guy – Billie Eilish", "url": "https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m"},
            {"title": "You Oughta Know – Alanis Morissette", "url": "https://open.spotify.com/track/3sY4mQYFhyTn5NhfJZCZ4P"}
        ],
        'EDM': [
            {"title": "Bangarang – Skrillex", "url": "https://open.spotify.com/track/5y6hL7m52wV82GpXy2QJXf"},
            {"title": "Centipede – Knife Party", "url": "https://open.spotify.com/track/2bP2l30m5Z1X4Mpj4QXq5q"}
        ]
    },
    'Surprise': {
        'DHH': [
            {"title": "Prathana  – KR$NA", "url": "https://open.spotify.com/track/3l3BzT3Ovdx2mQK366r5Ei?si=63d51b4626e0451f"},
            {"title": "Taakat – Seedhe Maut", "url": "https://open.spotify.com/track/2AMP8Rey8W6sxsXKUpgWRb?si=03b7e34d35d34589"}
        ],
        'Pop': [
            {"title": "Can't Hold Us – Macklemore & Ryan Lewis", "url": "https://open.spotify.com/track/2vxeLyX666F8uXCJ0dZF8B"},
            {"title": "Happy – Pharrell Williams", "url": "https://open.spotify.com/track/60nZcImufyMA1MKQY3dcCH"},
            {"title": "Uptown Funk – Mark Ronson ft. Bruno Mars", "url": "https://open.spotify.com/track/32OlwWuMpZ6b0aN2RZOeMS"}
        ],
        'EDM': [
            {"title": "Animals – Martin Garrix", "url": "https://open.spotify.com/track/1Je1IMUlBXcx1Fz0WE7oPT"},
            {"title": "Wake Me Up – Avicii", "url": "https://open.spotify.com/track/0yN98RpRAEkXk1tw6kEsLZ"},
            {"title": "Clarity – Zedd ft. Foxes", "url": "https://open.spotify.com/track/7yCPwWs66K8Ba5lFuU2bcx"}
        ],
        'Rap': [
            {"title": "Can't Hold Us – Macklemore & Ryan Lewis", "url": "https://open.spotify.com/track/2vxeLyX666F8uXCJ0dZF8B"},
            {"title": "Power – Kanye West", "url": "https://open.spotify.com/track/1mKXFLRA179hdOWQBwUkFq"}
        ],
        'Rock': [
            {"title": "Mr. Blue Sky – Electric Light Orchestra", "url": "https://open.spotify.com/track/7s25THrKz86DM225dOYwnr"},
            {"title": "Are You Gonna Be My Girl – Jet", "url": "https://open.spotify.com/track/2WGQxO94wZ5VdZdC8gEwrE"}
        ]
    },
    'Fear': {
         'DHH': [
            {"title": "Mujhko Mila – Karun, Adil, Chaar Diwari", "url": "https://open.spotify.com/track/1q1bmGKkAiqFqDzt4e83Ez?si=23089da62e2b430b"},
            {"title": "Rahat – Seedhe Maut, Hurricane, DL91 Era", "url": "https://open.spotify.com/track/11Ik2ALTfkhuqGdCOALHPg?si=60e591a2c83f452a"}
        ],
        'Pop': [
            {"title": "Everybody Hurts – R.E.M.", "url": "https://open.spotify.com/track/0LcJLqbBmaGUft1e9Mm8HV"},
            {"title": "Creep – Radiohead", "url": "https://open.spotify.com/track/7oK9VyNzrYvRFo7nQEYkWN"},
            {"title": "Mad World – Tears for Fears", "url": "https://open.spotify.com/track/3ltFzE9M54kqg9bTKLT0kg"}
        ],
        'Rap': [
            {"title": "Fear – Kendrick Lamar", "url": "https://open.spotify.com/track/3QRiMvC9P9z93nErHp9vI8"},
            {"title": "Scared Straight – The Game", "url": "https://open.spotify.com/track/1MbEAGkOf3HuVqjOqS7Nwg"}
        ],
        'Rock': [
            {"title": "Behind Blue Eyes – The Who", "url": "https://open.spotify.com/track/3mH6tEpOvd86Gkafn2f0kR"},
            {"title": "The Sound of Silence – Disturbed", "url": "https://open.spotify.com/track/0IhNz5rRjNYo9v9nOrESX9"}
        ],
        'EDM': [
            {"title": "Ghosts 'n' Stuff – Deadmau5", "url": "https://open.spotify.com/track/7h7F8oXfXweRWQK3RLy68H"},
            {"title": "Shelter – Porter Robinson & Madeon", "url": "https://open.spotify.com/track/3CWzG53VxMG3TTAYI3gB7B"}
            ]
        }
    }

    selected = []
    mood_data = songs_db.get(mood, songs_db['Neutral'])  # fallback to Neutral
    for taste in tastes:
        selected.extend(mood_data.get(taste, []))
    return selected[:5]  # limit to top 5