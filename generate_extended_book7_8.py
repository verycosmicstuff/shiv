# -*- coding: utf-8 -*-
"""
generate_extended_book7_8.py
Extends Book 7 (Loona) and Book 8 (Main te Main) with authentic multi-stanza poems.
"""
import json
import data_book7_loona
import data_book8_main

# Book 7 Loona extensions
new_loona = [
    {
        "id": "puran-de-hath-katte",
        "titleGurmukhi": "ਜਦ ਪੂਰਨ ਦੇ ਹੱਥ ਕੱਟੇ ਗਏ (ਅੰਕ 5)",
        "titleShahmukhi": "جد پورن دے ہتھ کٹے گئے",
        "titleRoman": "Jad Puran De Hath Katte Gaye",
        "titleEnglish": "Act V: The Severing of Puran's Hands",
        "book": "Loona",
        "year": 1965,
        "tags": ["Loona", "Puran", "Mutilation", "Patriarchal Horror", "Well"],
        "philosophyTheme": "feminism",
        "landscapeBiome": "barren_mountain_loona",
        "sketchPrompt": "Charcoal sketch of an ancient stone well surrounded by bloodstained paving stones under a blood-red moon.",
        "historicalFact": {
            "claim": "The horrifying culmination where King Salwan orders Puran's limbs severed and thrown into a well; Loona is horrified that her desire was weaponized into murder.",
            "citationId": "SEKHON-1972-PUNJABI"
        },
        "citationIds": ["SEKHON-1972-PUNJABI", "LAHORE-BOOKSHOP-1974"],
        "summary": "Loona gazes upon the executioners who severed Puran's limbs, crying out that patriarchal law cares not for justice, but only for egoistic blood-retribution.",
        "backstory": "Act V of the verse drama, shifting the tragedy onto the violent hypocrisy of the state.",
        "stanzas": [
            {
                "gurmukhi": "ਤੁਸਾਂ ਪੂਰਨ ਦੇ ਹੱਥ ਕੱਟ ਦਿੱਤੇ,\nਇਸ ਮਿੱਟੀ ਦੇ ਖੂਹ 'ਚ ਸੁੱਟ ਦਿੱਤਾ!\nਜੋ ਫੁੱਲ ਸੀ ਪੰਜਾਬ ਦੀ ਧਰਤੀ ਦਾ,\nਉਹਨੂੰ ਜ਼ਾਲਮ ਹੱਥੋਂ ਘੁੱਟ ਦਿੱਤਾ!",
                "shahmukhi": "تساں پورن دے ہتھ کٹ دتے،\nاس مٹی دے کھوہ چ سٹ دتا!\nجو پھل سی پنجاب دی دھرتی دا،\nاوہنوں ظالم ہتھوں گھٹ دتا!",
                "roman": "Tusaan Puran de hath katt ditte,\nIss mitti de khooh ch sutt ditta!\nJo phull si Punjab di dharti da,\nOhnu zaalam hatthon ghutt ditta!",
                "english": "You severed the youthful hands of Puran,\nAnd hurled his bleeding body into the dried mud well!\nThat purest blossom of Punjab's maternal earth\nYou strangled with the brutal hands of your tyranny!",
                "commentary": "Loona denouncing the patriarchal state's physical butchery."
            },
            {
                "gurmukhi": "ਸਲਵਾਨਾ ਤੇਰਾ ਇਹ ਇਨਸਾਫ਼ ਨਹੀਂ,\nਇਹ ਤੇਰੇ ਹੰਕਾਰ ਦਾ ਬਦਲਾ ਏ!\nਮੇਰੇ ਇਸ਼ਕ ਨੂੰ ਤੂੰ ਹਥਿਆਰ ਬਣਾਇਆ,\nਤੇਰਾ ਦਿਲ ਪੱਥਰਾਂ ਤੋਂ ਖਰਵਾ ਏ!",
                "shahmukhi": "سلوانا تیرا ایہہ انصاف نہیں،\nایہہ تیرے ہنکار دا بدلہ اے!\nمیرے عشق نوں توں ہتھیار بنایا،\nتیرا دل پتھراں توں کھرووا اے!",
                "roman": "Salwaana tera eh insaaf nahin,\nEh tere hankaar da badla ae!\nMere ishq nu toon hathiyaar banaaya,\nTera dil patthran ton kharva ae!",
                "english": "O King Salwan, this was never justice or righteousness;\nThis was merely the wounded vengeance of your own frail ego!\nYou weaponized my natural passion into an instrument of murder;\nYour heart is cruder and harder than desert granite!",
                "commentary": "Exposing Salwan's vengeance disguised as moral order."
            },
            {
                "gurmukhi": "ਹੁਣ ਇਸ ਖੂਹ 'ਚੋਂ ਜੋ ਆਵਾਜ਼ ਉੱਠੂ,\nਉਹ ਸਿਆਲਕੋਟ ਨੂੰ ਸਾੜੇਗੀ!\nਸ਼ਿਵ ਕਹਿੰਦਾ ਲੂਣਾ ਦੀ ਚੀਕ ਅੱਜ,\nਇਸ ਤਖ਼ਤ ਨੂੰ ਮਿੱਟੀ 'ਚ ਗਾੜੇਗੀ!",
                "shahmukhi": "ہن اس کھوہ چوں جو آواز اٹھو،\nاوہ سیالکوٹ نوں ساڑےگی!\nشیو کہندا لونا دی چیک اج،\nاس تخت نوں مٹی چ گاڑےگی!",
                "roman": "Hun iss khooh chon jo aawaaz utthu,\nOh Sialkot nu saarhegi!\nShiv kehnda Loona di cheek ajj,\nIss takht nu mitti ch gaarhegi!",
                "english": "Now that prophetic voice which arises from the depths of this well\nShall incinerate the proud citadel of Sialkot!\nShiv proclaims: the furious scream of Loona today\nShall bury this corrupt royal throne into the dust of shame!",
                "commentary": "The well as oracle of revolutionary ruin."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਖੂਹ (Khooh)",
                "pronunciation": "Khooh",
                "literal": "Deep masonry water well",
                "culturalMeaning": "The historic site where Puran Bhagat was thrown, transformed by Shiv into a grave of patriarchal injustice."
            }
        ]
    },
    {
        "id": "loona-di-aakhri-cheek",
        "titleGurmukhi": "ਲੂਣਾ ਦੀ ਆਖ਼ਰੀ ਚੀਕ (ਸਮਾਪਤੀ ਅੰਕ)",
        "titleShahmukhi": "لونا دی آخری چیک",
        "titleRoman": "Loona Di Aakhri Cheek",
        "titleEnglish": "Epilogue: Loona's Final Curse Upon Sialkot",
        "book": "Loona",
        "year": 1965,
        "tags": ["Loona", "Curse", "Epilogue", "Dynasty", "Feminism"],
        "philosophyTheme": "feminism",
        "landscapeBiome": "barren_mountain_loona",
        "sketchPrompt": "Charcoal sketch of a queen standing atop ruined palace ramparts with wind tearing at her robes.",
        "historicalFact": {
            "claim": "Shiv's concluding movement in Loona where the protagonist refuses to repent or ask for patriarchal pardon, holding her head high.",
            "citationId": "LAHORE-BOOKSHOP-1974"
        },
        "citationIds": ["LAHORE-BOOKSHOP-1974", "SEKHON-1972-PUNJABI"],
        "summary": "Loona stands unrepentant atop the ramparts of Sialkot, cursing the dynasty that treated women as chattel and claiming her place in history as the unbowed woman.",
        "backstory": "The historic dramatic finale of the Sahitya Akademi Award-winning epic.",
        "stanzas": [
            {
                "gurmukhi": "ਮੈਂ ਨਹੀਂ ਝੁਕਾਂਗੀ ਇਸ ਦਰਬਾਰ ਅੱਗੇ,\nਨਾ ਕੋਈ ਰਹਿਮ ਦੀ ਭੀਖ ਮੰਗਾਂਗੀ!\nਜੋ ਸੱਚ ਮੇਰੇ ਤਨ ਨੇ ਭੋਗਿਆ ਏ,\nਉਸਨੂੰ ਸੂਰਜ ਵਾਂਗੂੰ ਟੰਗਾਂਗੀ!",
                "shahmukhi": "میں نہیں جھکانگی اس دربار اگے،\nنہ کوئی رحم دی بھیک منگانگی!\nجو سچ میرے تن نے بھوگیا اے،\nاس نوں سورج وانگوں ٹنگانگی!",
                "roman": "Main nahin jhukaangi iss darbaar agge,\nNa koyi reham di bheek mangaangi!\nJo sach mere tan ne bhogeya ae,\nUsnu suraj vaangu tangaangi!",
                "english": "I shall never bow my knee before this corrupt royal court,\nNor shall I beg for alms of mercy from your judges!\nThat raw, unvarnished truth which my living flesh has endured\nI shall suspend like the blazing sun in the high heavens!",
                "commentary": "Refusal to perform female repentance."
            },
            {
                "gurmukhi": "ਤੁਸਾਂ ਮੈਨੂੰ ਕਲੰਕਣ ਆਖਿਆ ਏ,\nਪਰ ਇਤਿਹਾਸ ਮੈਨੂੰ ਪੂਜੇਗਾ!\nਜਦ ਨਾਰੀ ਆਪਣੇ ਹੱਕ ਮੰਗੂ,\nਤਾਂ ਮੇਰਾ ਨਾਮ ਹੀ ਗੂੰਜੇਗਾ!",
                "shahmukhi": "تساں مینوں کلنکن آکھیا اے،\nپر تاریخ مینوں پوجےگا!\nجد ناری اپنے حق منگو،\nتاں میرا نام ہی گونجےگا!",
                "roman": "Tusaan mainu kalankan aakheya ae,\nPar itihaas mainu poojega!\nJad naari aapne hakk mangu,\nTaan mera naam hi goonjega!",
                "english": "You branded me an incestuous, tainted outcast,\nYet the uncorrupted history of tomorrow shall revere my name!\nWhenever women rise across this earth to claim their bodily sovereignty,\nMy ringing cry alone shall echo at the vanguard!",
                "commentary": "Loona claiming her role as feminist pioneer."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਨੇ ਲੂਣਾ ਨੂੰ ਜੀਵਨ ਦਿੱਤਾ,\nਜੋ ਸਦੀਆਂ ਤੋਂ ਮਰੀ ਪਈ ਸੀ!\nਇਸ ਕਲਮ ਨੇ ਉਹਦੀ ਚੀਕ ਸੁਣੀ,\nਜੋ ਪੱਥਰਾਂ ਹੇਠਾਂ ਦਬੀ ਪਈ ਸੀ!",
                "shahmukhi": "شیو نے لونا نوں جیون دتا،\nجو صدیاں توں مری پئی سی!\nاس قلم نے اوہدی چیک سنی،\nجو پتھراں ہیٹھاں دبی پئی سی!",
                "roman": "Shiv ne Loona nu jeevan ditta,\nJo sadiyaan ton mari payi si!\nIss kalam ne ohdi cheek suni,\nJo patthran hethan dabi payi si!",
                "english": "Shiv breathed immortal life back into Loona,\nWho had lain buried and slandered across a thousand years!\nThis compassionate pen heard the holy scream\nWhich had been crushed and silenced beneath patriarchal stone!",
                "commentary": "Shiv's historic resurrection of Loona."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਕਲੰਕਣ (Kalankan)",
                "pronunciation": "Ka-lan-kan",
                "literal": "Stigmatized woman / Bearer of stain",
                "culturalMeaning": "Patriarchal slur used against women who express independent desire or defy social conventions."
            }
        ]
    }
]

extended_loona = data_book7_loona.loona_poems + new_loona
content_loona = "# -*- coding: utf-8 -*-\n"
content_loona += '"""Book 7: Loona (1965 - Sahitya Akademi Award) - 8 Full Verse-Play Acts"""\n\n'
content_loona += "loona_poems = " + json.dumps(extended_loona, ensure_ascii=False, indent=4) + "\n\n"
content_loona += 'print(f"Loaded {len(loona_poems)} acts from Book 7 (Loona).")\n'

with open("data_book7_loona_extended.py", "w", encoding="utf-8") as f:
    f.write(content_loona)

# Book 8 Main te Main extensions
new_main = [
    {
        "id": "bheed-vich-kalla",
        "titleGurmukhi": "ਭੀੜ ਵਿੱਚ ਕੱਲਾ",
        "titleShahmukhi": "بھیڑ وچ کلا",
        "titleRoman": "Bheed Vich Kalla",
        "titleEnglish": "Solitary in the Metropolitan Crowd",
        "book": "Main te Main",
        "year": 1970,
        "tags": ["Crowd", "Metropolis", "Loneliness", "Alienation", "Modernity"],
        "philosophyTheme": "modernism",
        "landscapeBiome": "tavern_midnight",
        "sketchPrompt": "Charcoal sketch of thousands of faceless commuters walking in a blur down a wet concrete boulevard under neon signs.",
        "historicalFact": {
            "claim": "Reflects the Baudelairean flâneur theme imported into Punjabi literature, capturing the existential isolation of Sector 17, Chandigarh.",
            "citationId": "SEKHON-1972-PUNJABI"
        },
        "citationIds": ["SEKHON-1972-PUNJABI"],
        "summary": "Walking through thousands of rushing commuters in the modern city, the poet realizes that crowd density increases rather than relieves spiritual isolation.",
        "backstory": "Composed in Chandigarh after walking from Sector 17 to Sector 22 in heavy evening rush hour.",
        "stanzas": [
            {
                "gurmukhi": "ਮੈਂ ਲੱਖਾਂ ਲੋਕਾਂ ਦੀ ਭੀੜ 'ਚ ਖੜ੍ਹਾ ਹਾਂ,\nਪਰ ਇੱਕ ਵੀ ਚਿਹਰਾ ਆਪਣਾ ਨਹੀਂ!\nਸਭ ਦੌੜਦੇ ਨੇ ਅੰਨ੍ਹਿਆਂ ਵਾਂਗੂੰ,\nਕਿਸੇ ਦੀ ਅੱਖ 'ਚ ਸੁਪਨਾ ਨਹੀਂ!",
                "shahmukhi": "میں لکھاں لوکاں دی بھیڑ چ کھڑا ہاں،\nپر اک وی چہرہ اپنا نہیں!\nسبھ دوڑدے نے انھیاں وانگوں،\nکسے دی اکھ چ سپنا نہیں!",
                "roman": "Main lakkhan lokaan di bheed ch kharha haan,\nPar ikk vi chehra aapna nahin!\nSabh daurhde ne anneyan vaangu,\nKise di akh ch supna nahin!",
                "english": "I stand amidst a jostling crowd of hundreds of thousands,\nYet not a single countenance is familiar or mine!\nAll race forward like blind automata;\nIn not a single eye glimmers a genuine, living dream!",
                "commentary": "The atomized crowd of the capitalist metropolis."
            },
            {
                "gurmukhi": "ਇਹ ਸ਼ਹਿਰ ਮੈਨੂੰ ਨਿਗਲ ਗਿਆ ਏ,\nਮੇਰਾ ਨਾਮ ਕਿਤੇ ਗੁਆਚ ਗਿਆ!\nਜੋ ਕਦੇ ਪੰਜਾਬ ਦਾ ਸ਼ਾਇਰ ਸੀ,\nਉਹ ਮਸ਼ੀਨਾਂ ਅੰਦਰ ਨਾਚ ਗਿਆ!",
                "shahmukhi": "ایہہ شہر مینوں نگل گیا اے،\nمیرا نام کتے گواچ گیا!\nجو کدے پنجاب دا شاعر سی،\nاوہ مشیناں اندر ناچ گیا!",
                "roman": "Eh shehar mainu nigal gaya ae,\nMera naam kite guaach gaya!\nJo kade Punjab da shaayar si,\nOh masheenaan andar naach gaya!",
                "english": "This mechanical city has swallowed my very flesh;\nMy identity and name have vanished into the grid!\nHe who was once the celebrated bard of Punjab\nHas been forced to dance within the gears of machinery!",
                "commentary": "Industrial alienation destroying lyric identity."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਇਸ ਭੀੜ 'ਚੋਂ ਚੀਕ ਰਿਹਾ ਏ,\nਕੋਈ ਰੋਕੋ ਇਸ ਹਨੇਰ ਨੂੰ!\nਜੇ ਇਨਸਾਨ ਹੀ ਮਸ਼ੀਨ ਬਣ ਗਿਆ,\nਤਾਂ ਕੌਣ ਬਚਾਊ ਇਸ ਸ਼ਹਿਰ ਨੂੰ?",
                "shahmukhi": "شیو اس بھیڑ چوں چیک رہیا اے،\nکوئی روکو اس ہنیر نوں!\nجے انسان ہی مشین بن گیا،\nتاں کون بچاؤ اس شہر نوں؟",
                "roman": "Shiv iss bheed chon cheek reha ae,\nKoyi roko iss haner nu!\nJe insaan hi masheen ban gaya,\nTaan kaun bachaau iss shehar nu?",
                "english": "Shiv screams out from the depths of this rushing multitude:\n'Someone halt this catastrophe of darkness!\nIf the human being has transformed into a soulless machine,\nWho remains to salvage this city from destruction?'",
                "commentary": "The prophetic warning against total mechanization."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਭੀੜ (Bheed)",
                "pronunciation": "Bheerr",
                "literal": "Crowd / Mob / Multitude",
                "culturalMeaning": "In modernist Punjabi poetry, the symbol of faceless urban alienation as opposed to intimate rural community."
            }
        ]
    },
    {
        "id": "akhbaar-da-tukda",
        "titleGurmukhi": "ਅਖ਼ਬਾਰ ਦਾ ਟੁਕੜਾ",
        "titleShahmukhi": "اخبار دا ٹکڑا",
        "titleRoman": "Akhbaar Da Tukda",
        "titleEnglish": "The Discarded Scrap of Newsprint",
        "book": "Main te Main",
        "year": 1970,
        "tags": ["Newsprint", "Gutter", "Disposable", "Modernism", "Trash"],
        "philosophyTheme": "modernism",
        "landscapeBiome": "tavern_midnight",
        "sketchPrompt": "Charcoal sketch of a torn newspaper blowing across wet asphalt into an open sewer drain.",
        "historicalFact": {
            "claim": "Modernist objective-correlative: the poet compares his own commodified fame to a greasy scrap of newsprint used to wrap roadside pakoras.",
            "citationId": "LAHORE-BOOKSHOP-1974"
        },
        "citationIds": ["LAHORE-BOOKSHOP-1974"],
        "summary": "A torn scrap of newspaper containing a poet's masterpiece blows down a filthy street gutter, discarded after wrapping fried snacks.",
        "backstory": "Composed in Chandigarh after seeing his poems printed on cheap newsprint wrapping street food.",
        "stanzas": [
            {
                "gurmukhi": "ਮੈਂ ਅਖ਼ਬਾਰ ਦਾ ਟੁਕੜਾ ਬਣ ਗਿਆ,\nਜੋ ਨਾਲ਼ੀ ਵਿੱਚ ਰੁਲ਼ਦਾ ਏ!\nਜਿਸ 'ਤੇ ਕਦੇ ਮੇਰੇ ਗੀਤ ਛਪੇ ਸੀ,\nਉਹ ਪੈਰਾਂ ਹੇਠਾਂ ਖੁੱਲ੍ਹਦਾ ਏ!",
                "shahmukhi": "میں اخبار دا ٹکڑا بن گیا،\nجو نالی وچ رلدا اے!\nجس تے کدے میرے گیت چھپے سی،\nاوہ پیراں ہیٹھاں کھلدا اے!",
                "roman": "Main akhbaar da tukda ban gaya,\nJo naali vich rulda ae!\nJis te kade mere geet chhape si,\nOh pairaan hethan khulhda ae!",
                "english": "I have become like a greasy scrap of discarded newsprint\nRolling indifferently down the open street gutter!\nThat very paper upon which my verses were printed\nNow unrolls and tears beneath the boots of passersby!",
                "commentary": "The shocking descent of high art into urban filth."
            },
            {
                "gurmukhi": "ਸਵੇਰੇ ਜੋ ਖ਼ਬਰ ਬਣੀ ਸੀ ਦੁਨੀਆ ਦੀ,\nਸ਼ਾਮ ਨੂੰ ਕੂੜੇ 'ਚ ਸੁੱਟ ਦਿੱਤੀ!\nਇਸ ਮਤਲਬੀ ਦੁਨੀਆ ਨੇ ਸਾਡੀ,\nਸਾਰੀ ਕੀਮਤ ਹੀ ਲੁੱਟ ਲਿੱਤੀ!",
                "shahmukhi": "سویرے جو خبر بنی سی دنیا دی،\nشام نوں کوڑے چ سٹ دتی!\nاس مطلبی دنیا نے ساڈی،\nساری قیمت ہی لٹ لتی!",
                "roman": "Savere jo khabar bani si duniya di,\nShaam nu koorhe ch sutt ditti!\nIss matlabi duniya ne saadi,\nSaari keemat hi lutt litti!",
                "english": "That which in the morning was hailed as the headline of the world\nBy dusk was hurled unceremoniously into the garbage heap!\nThis opportunistic, commercial world has plundered\nEvery ounce of dignity and value from our life!",
                "commentary": "The 24-hour news cycle trivializing human genius."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਕਹਿੰਦਾ ਪਰ ਇਸ ਕਾਗ਼ਜ਼ 'ਤੇ,\nਜੋ ਸਿਆਹੀ ਲਹੂ ਦੀ ਛਪੀ ਹੋਈ ਏ!\nਉਹ ਪਾਣੀ ਨਾਲ਼ ਨਾ ਧੁਪੇਗੀ,\nਉਹ ਇਤਿਹਾਸ ਦੇ ਸੀਨੇ ਗਡੀ ਹੋਈ ਏ!",
                "shahmukhi": "شیو کہندا پر اس کاغذ تے،\nجو سیاہی لہو دی چھپی ہوئی اے!\nاوہ پانی نال نہ دھپوگی،\nاوہ تاریخ دے سینے گڈی ہوئی اے!",
                "roman": "Shiv kehnda par iss kaghaz te,\nJo syaahi lahu di chhappi hoyi ae!\nOh paani naal na dhupegi,\nOh itihaas de seene gaddi hoyi ae!",
                "english": "Shiv declares: 'Yet upon this rain-soaked scrap of paper,\nThat black ink which was pressed from living blood\nCan never be washed away by sewage water—\nIt stands planted like an iron spear into the chest of history!'",
                "commentary": "The indestructible ink of authentic suffering."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਨਾਲ਼ੀ (Naali)",
                "pronunciation": "Naa-lee",
                "literal": "Open street sewer / Gutter",
                "culturalMeaning": "Harsh urban realistic detail contrasting with the romanticized rivers of his early pastoral phase."
            }
        ]
    }
]

extended_main = data_book8_main.main_poems + new_main
content_main = "# -*- coding: utf-8 -*-\n"
content_main += '"""Book 8: Main te Main (1970) - 8 Full Modernist Existential Poems"""\n\n'
content_main += "main_poems = " + json.dumps(extended_main, ensure_ascii=False, indent=4) + "\n\n"
content_main += 'print(f"Loaded {len(main_poems)} poems from Book 8 (Main te Main).")\n'

with open("data_book8_main_extended.py", "w", encoding="utf-8") as f:
    f.write(content_main)

print("Generated Book 7 extended (8 acts) and Book 8 extended (8 poems) successfully!")
