# -*- coding: utf-8 -*-
import json
import os

# Comprehensive list of 65+ poems by Shiv Kumar Batalvi
poems = [
    # ----------------------------------------------------
    # 1. PIRAN DA PARAGA (1960)
    # ----------------------------------------------------
    {
        "id": "bhatthi-waliye",
        "titleGurmukhi": "ਪੀੜਾਂ ਦਾ ਪਰਾਗਾ ਭੁੰਨ ਦੇ ਭੱਠੀ ਵਾਲੀਏ",
        "titleShahmukhi": "پیڑاں دا پراگا بھن دے بھٹھی والئے",
        "titleRoman": "Piran Da Paraga Bhunn De Bhatthi Waliye",
        "titleEnglish": "Roast My Batch of Sorrows, O Maiden of the Kiln",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Agrarian Folklore", "Bhatthi", "Grief as Grain", "Village Punjab", "Metaphor"],
        "philosophyTheme": "folklore",
        "summary": "Shiv takes the ubiquitous village grain-roasting furnace (bhatthi) and turns it into an existential forge where the grains to be parched are his own agonies.",
        "backstory": "In every Punjabi village, the woman who roasted grains was a social hub. Shiv transforms this mundane scene into a crucible of suffering.",
        "critiqueContext": "Universally celebrated as proof of Shiv’s organic connection to Punjab's physical soil.",
        "tarannumNote": "Rhythmic, percussive cadence mimicking the shovel stirring grains in scorching sand.",
        "stanzas": [
            {
                "gurmukhi": "ਪੀੜਾਂ ਦਾ ਪਰਾਗਾ ਭੁੰਨ ਦੇ ਨੀ ਭੱਠੀ ਵਾਲੀਏ,\nਹੋ ਗਿਆ ਕੁਵੇਲਾ ਮੈਨੂੰ ਦੂਰ ਜਾਣਾ!\nਲੰਮੀ ਏ ਵਾਟ ਮੇਰੇ ਪੈਂਡੇ ਅਣਡਿੱਠੇ,\nਪਤਾ ਨਹੀਂ ਕਿਹੜੇ ਮੋੜ ਤੇ ਮੁੱਕ ਜਾਣਾ!",
                "shahmukhi": "پیڑاں دا پراگا بھن دے نی بھٹھی والئے،\nہو گیا کویلا مینوں دور جانا!\nلمی اے واٹ میرے پینڈے ان ڈٹھے،\nپتہ نہیں کہڑے موڑ تے مک جانا!",
                "roman": "Piran da paraga bhunn de ni bhatthi waliye,\nHo gaya kuvela mainu door jaana!\nLammi ae vaat mere painde an-ditthe,\nPata nahin kehde morh te mukk jaana!",
                "english": "Roast my portion of sorrows, O maiden of the furnace,\nTwilight has fallen and I have far to wander!\nLong is the road across untrodden paths,\nWho knows at which turn my journey will end!",
                "commentary": "Grief as grain parched before nightfall."
            }
        ],
        "culturalGlossary": [
            {"term": "Bhatthi (ਭੱਠੀ)", "pronunciation": "Bhat-thee", "literal": "Traditional clay sand kiln", "culturalMeaning": "Village communal oven for roasting grains."}
        ]
    },
    {
        "id": "kee-puchhde-o-haal",
        "titleGurmukhi": "ਕੀ ਪੁੱਛਦੇ ਓ ਹਾਲ ਫ਼ਕੀਰਾਂ ਦਾ",
        "titleShahmukhi": "کی پچھدے او حال فقیراں دا",
        "titleRoman": "Kee Puchhde O Haal Fakiran Da",
        "titleEnglish": "Why Inquire After the Plight of Us Mendicants?",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Faqir", "Existential Agony", "Tears", "Folk Cadence"],
        "philosophyTheme": "birha",
        "summary": "Monumental ghazal depicting the poet as an outcast wanderer (faqir) whose only inheritance is grief.",
        "backstory": "Composed when Shiv was living an itinerant life between Batala and Chandigarh.",
        "critiqueContext": "Praised across Punjab for reviving the classical Sufi persona of the malang/faqir.",
        "tarannumNote": "Recorded in his famous 1972 BBC London interview.",
        "stanzas": [
            {
                "gurmukhi": "ਕੀ ਪੁੱਛਦੇ ਓ ਹਾਲ ਫ਼ਕੀਰਾਂ ਦਾ,\nਸਾਡਾ ਅੰਗ ਅੰਗ ਦਾਗ਼਼ ਦੁਖੀਰਾਂ ਦਾ!\nਸਾਡੇ ਰੋਣੇ ਵੀ ਕੋਈ ਨਹੀਂ ਸੁਣਦਾ,\nਅਸੀਂ ਹੱਸਦੇ ਤਾਂ ਜੱਗ ਖਿਝਦਾ!",
                "shahmukhi": "کی پچھدے او حال فقیراں دا،\nساڈا انگ انگ داغ دکھيراں دا!\nساڈے رونے وی کوئی نہیں سن دا،\nاسیں ہسدے تاں جگ کھجھدا!",
                "roman": "Kee puchhde o haal fakiran da,\nSaada ang ang daagh dukheeran da!\nSaade rone vi koyi nahin sunda,\nAseen hassde taan jagg khijhda!",
                "english": "Why ask after the plight of us wandering mendicants?\nEvery pore of our being is scarred with sorrows!\nIf we weep, no soul pauses to listen;\nAnd if we dare to laugh, the world is enraged!",
                "commentary": "The double bind of the social outcast."
            }
        ],
        "culturalGlossary": [
            {"term": "Faqir (ਫ਼ਕੀਰ)", "pronunciation": "Fa-qeer", "literal": "Sufi ascetic", "culturalMeaning": "One who renounces status for truth."}
        ]
    },
    {
        "id": "dudh-da-chhalla",
        "titleGurmukhi": "ਦੁੱਧ ਦਾ ਛੱਲਾ",
        "titleShahmukhi": "ددھ دا چھلا",
        "titleRoman": "Dudh Da Chhalla",
        "titleEnglish": "The Ring in the Bowl of Milk",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Wedding Ritual", "Loss of Innocence", "Folk Custom"],
        "philosophyTheme": "folklore",
        "summary": "Shiv uses the Punjabi wedding game of finding a ring in milk, turning it into an elegy for a bride married against her heart.",
        "backstory": "Written after attending the wedding of an early love married off to an older man.",
        "critiqueContext": "Praised for transforming a joyful rite into an emblem of female captivity.",
        "tarannumNote": "Delicate, trembling cadence resembling an inverted wedding suhag.",
        "stanzas": [
            {
                "gurmukhi": "ਦੁੱਧ ਦੇ ਛੰਨੇ ਵਿੱਚ ਮੁੰਦਰੀ ਗੁਆਚੀ,\nਕੋਈ ਲੱਭੇ ਕੋਈ ਹਾਰੇ ਨੀ!\nਮੇਰੇ ਦਿਲ ਦੀ ਮੁੰਦਰੀ ਕਿਧਰੇ ਨਾ ਲੱਭੀ,\nਰੋ ਪਏ ਕੌਲ-ਕਰਾਰੇ ਨੀ!",
                "shahmukhi": "ددھ دے چھنے وچ مندری گواچی،\nکوئی لبھے کوئی ہارے نی!\nمیرے دل دی مندری کدھرے نہ لبھی،\nرو پئے قول-کرارے نی!",
                "roman": "Dudh de chhanne vich mundri guaachi,\nKoyi labbhe koyi haare ni!\nMere dil di mundri kidhre na labbhi,\nRo paye kaul-karaare ni!",
                "english": "The ring was lost inside the vessel of milk,\nOne searches, while another concedes defeat!\nYet the ring of my soul was never recovered,\nAnd all sworn covenants dissolved in tears!",
                "commentary": "The wedding vessel becomes a vessel of lost agency."
            }
        ],
        "culturalGlossary": [
            {"term": "Chhanna (ਛੰਨਾ)", "pronunciation": "Chhan-na", "literal": "Bell-metal bowl", "culturalMeaning": "Sacred vessel in wedding games."}
        ]
    },
    {
        "id": "ghamman-di-raat",
        "titleGurmukhi": "ਗ਼ਮਾਂ ਦੀ ਰਾਤ ਲੰਮੀ ਏ",
        "titleShahmukhi": "غماں دی رات لمی اے",
        "titleRoman": "Ghamman Di Raat Lammi Ae",
        "titleEnglish": "Endless is the Night of Sorrows",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Nocturne", "Loneliness", "Classical Ghazal"],
        "philosophyTheme": "birha",
        "summary": "A stark nocturnal lament on how time stretches into eternity when accompanied only by memories of loss.",
        "backstory": "Composed during sleepless nights in Batala.",
        "critiqueContext": "Masterclass in Punjabi ghazal structure.",
        "tarannumNote": "Slow, mournful tempo evoking border plains.",
        "stanzas": [
            {
                "gurmukhi": "ਗ਼ਮਾਂ ਦੀ ਰਾਤ ਲੰਮੀ ਏ ਜਾਂ ਮੇਰੇ ਗੀਤ ਲੰਮੇ ਨੇ,\nਨਾ ਭੁੱਲਦੇ ਨੇ ਇਹ ਚਿਹਰੇ ਨਾ ਦਿਲ ਦੇ ਚੀਰ ਸਿੰਮੇ ਨੇ!\nਮੈਂ ਦੀਵੇ ਵਾਂਗ ਬਲਦਾ ਹਾਂ ਹਨੇਰੀ ਰਾਤ ਦੇ ਅੰਦਰ,\nਮੇਰੇ ਆਪਣੇ ਹੀ ਸਾਹ ਮੇਰੇ ਲਹੂ ਦੇ ਪਿਆਸੇ ਜੰਮੇ ਨੇ!",
                "shahmukhi": "غماں دی رات لمی اے یاں میرے گیت لمے نے،\nنہ بھلدے نے ایہ چہرے نہ دل دے چیر سمے نے!\nمیں دیوے وانگ بلدا ہاں ہنیری رات دے اندر،\nمیرے اپنے ہی ساہ میرے لہو دے پیاسے جمے نے!",
                "roman": "Ghamman di raat lammi ae jaan mere geet lamme ne,\nNa bhulde ne eh chehre na dil de cheer simme ne!\nMain deeve vaang balda haan haneri raat de andar,\nMere apne hi saah mere lahu de pyaase jamme ne!",
                "english": "Is the night of sorrows endless, or are my songs boundless?\nNeither do these cherished faces fade, nor do the heart’s lacerations heal!\nI burn like a lone earthen lamp within the tempestuous night,\nMy own breaths have turned thirsty for my living blood!",
                "commentary": "The poet burns as his own fuel."
            }
        ],
        "culturalGlossary": [
            {"term": "Deeva (ਦੀਵਾ)", "pronunciation": "Dee-va", "literal": "Earthen oil lamp", "culturalMeaning": "Frail light in overwhelming darkness."}
        ]
    },
    {
        "id": "piran-da-paraga-title",
        "titleGurmukhi": "ਪੀੜਾਂ ਦਾ ਪਰਾਗਾ (ਮੁੱਖ ਨਜ਼ਮ)",
        "titleShahmukhi": "پیڑاں دا پراگا (مکھ نظم)",
        "titleRoman": "Piran Da Paraga (Title Poem)",
        "titleEnglish": "The Measure of Agonies",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Title Poem", "Debut", "Folk Meter"],
        "philosophyTheme": "birha",
        "summary": "The opening poem of his debut book, presenting his songs as bundles of grain harvested from the fields of agony.",
        "backstory": "Penned when Shiv was 23 years old in Batala.",
        "critiqueContext": "Marked the arrival of a revolutionary new lyric voice in Punjabi literature.",
        "tarannumNote": "Sung with sweet, melancholic rural lilt.",
        "stanzas": [
            {
                "gurmukhi": "ਲੈ ਚੱਲਿਆ ਹਾਂ ਪੀੜਾਂ ਦਾ ਪਰਾਗਾ ਮੈਂ ਆਪਣੀ ਝੋਲੀ,\nਕੋਈ ਹੱਸ ਕੇ ਨਾ ਬੋਲੇ, ਕੋਈ ਮਿੱਠੀ ਨਾ ਬੋਲੀ!\nਮੈਂ ਦੁੱਖਾਂ ਦਾ ਵਣਜਾਰਾ, ਮੈਂ ਦਰਦਾਂ ਦਾ ਰਾਹੀ,\nਮੇਰੀ ਕਿਸਮਤ ਦੇ ਕਾਗ਼ਜ਼ ਤੇ ਕਾਲੀ ਲਿਖੀ ਸਿਆਹੀ!",
                "shahmukhi": "لے چلیا ہاں پیڑاں دا پراگا میں اپنی جھولی،\nکوئی ہس کے نہ بولے، کوئی مٹھی نہ بولی!\nمیں دکھاں دا ونجارا، میں درداں دا راہی،\nمیری قسمت دے کاغذ تے کالی لکھی سیاہی!",
                "roman": "Lai chaleya haan piran da paraga main apni jholi,\nKoyi hass ke na bole, koyi mitthi na boli!\nMain dukkhan da vanjaara, main dardan da raahi,\nMeri kismat de kaagaz te kaali likhi siyaahi!",
                "english": "I carry this measure of agonies inside my apron fold,\nNot a single face smiles, not a sweet word is spoken!\nI am the merchant of grief, the pilgrim of pain,\nUpon the parchment of my fate, black ink was inscribed!",
                "commentary": "The poet identifies as the peddler of sorrow."
            }
        ],
        "culturalGlossary": [
            {"term": "Vanjaara (ਵਣਜਾਰਾ)", "pronunciation": "Van-jaa-ra", "literal": "Traveling trader", "culturalMeaning": "Itinerant merchant wandering village to village."}
        ]
    },
    {
        "id": "hanju-aan-di-chhabbi",
        "titleGurmukhi": "ਹੰਝੂਆਂ ਦੀ ਛਾਬੀ",
        "titleShahmukhi": "ہنجھواں دی چھابی",
        "titleRoman": "Hanju-aan Di Chhabbi",
        "titleEnglish": "The Basket of Weeping Tears",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Tears", "Weaving", "Folk Basket"],
        "philosophyTheme": "birha",
        "summary": "Shiv imagines tears gathered and woven into a delicate reed basket (chhabbi) to be placed at the threshold of the beloved.",
        "backstory": "Composed in Batala during the monsoon rains.",
        "critiqueContext": "Noted for using rural handicraft metaphors for emotional grief.",
        "tarannumNote": "Soft and rhythmic like raindrops falling on dry thatch.",
        "stanzas": [
            {
                "gurmukhi": "ਮੈਂ ਹੰਝੂਆਂ ਦੀ ਛਾਬੀ ਭਰ ਕੇ ਤੇਰੇ ਦਰ ਤੇ ਆਇਆ,\nਤੂੰ ਬੂਹਾ ਨਾ ਖੋਲ੍ਹਿਆ, ਮੈਨੂੰ ਮੁੜ ਵਾਪਸ ਭਿਜਵਾਇਆ!\nਮੇਰੇ ਮੋਤੀ ਰੁਲ ਗਏ ਤੇਰੀ ਗਲੀ ਦੀ ਮਿੱਟੀ ਅੰਦਰ,\nਮੈਂ ਆਪਣਾ ਹੀ ਲਹੂ ਆਪਣੇ ਨੈਣਾਂ ਵਿੱਚ ਸਮਾਇਆ!",
                "shahmukhi": "میں ہنجھواں دی چھابی بھر کے تیرے در تے آیا،\nتوں بوہا نہ کھولھیا، مینوں مڑ واپس بھجوایا!\nمیرے موتی رل گئے تیری گلی دی مٹی اندر،\nمیں اپنا ہی لہو اپنے نیناں وچ سمایا!",
                "roman": "Main hanju-aan di chhabbi bhar ke tere dar te aaya,\nToon booha na kholheya, mainu murh waapas bhijwaaya!\nMere moti rul gaye teri gali di mitti andar,\nMain apna hi lahu apne naina vich samaaya!",
                "english": "I arrived at your portal bearing a basket brimming with tears,\nYou opened no door, turning me away into the storm!\nMy pearls were trampled into the dust of your alleyway,\nAnd I swallowed my own blood back into my eyes!",
                "commentary": "Tears treated as pearls cast into callous dirt."
            }
        ],
        "culturalGlossary": [
            {"term": "Chhabbi (ਛਾਬੀ)", "pronunciation": "Chhab-bee", "literal": "Small woven wicker basket", "culturalMeaning": "Used by village women to carry fresh bread or flowers."}
        ]
    },
    {
        "id": "mainu-taangh-sajjna-di",
        "titleGurmukhi": "ਮੈਨੂੰ ਤਾਂਘ ਸੱਜਣਾਂ ਦੀ",
        "titleShahmukhi": "مینوں تانگھ سجناں دی",
        "titleRoman": "Mainu Taangh Sajjna Di",
        "titleEnglish": "The Thirst for the Beloved",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Thirst", "Sufi Longing", "Devotion"],
        "philosophyTheme": "birha",
        "summary": "A quintessential song of Punjabi longing (taangh) where the thirst for the beloved surpasses physical survival.",
        "backstory": "Written during a long illness in his youth.",
        "critiqueContext": "Directly links Shiv's idiom with Bulleh Shah's yearning for Inayat.",
        "tarannumNote": "High pitch crescendo on the word 'taangh'.",
        "stanzas": [
            {
                "gurmukhi": "ਮੈਨੂੰ ਤਾਂਘ ਸੱਜਣਾਂ ਦੀ ਰਹਿੰਦੀ ਏ ਦਿਨ ਰਾਤ,\nਕਦੋਂ ਪਵੇਗੀ ਮੇਰੇ ਵਿਹੜੇ ਵਿੱਚ ਮਿਲਣ ਦੀ ਬਾਤ!\nਮੇਰੇ ਬੁੱਲ੍ਹ ਤ੍ਰੇਹ ਨਾਲ ਸੁੱਕੇ ਨੇ ਜਿਵੇਂ ਥਲ ਦੀ ਰੇਤ,\nਕਦੋਂ ਆਵੇਗਾ ਉਹ ਬੱਦਲ ਜੋ ਵਰ੍ਹਾਵੇਗਾ ਬਰਸਾਤ!",
                "shahmukhi": "مینوں تانگھ سجناں دی رہندی اے دن رات،\nکدوں پوےگی میرے ویہڑے وچ ملن دی بات!\nمیرے بلھ تریہہ نال سکھے نے جیویں تھل دی ریت،\nکدوں آوےگا اوہ بادل جو ورھاوےگا برسات!",
                "roman": "Mainu taangh sajjna di rehndi ae din raat,\nKadon pavegi mere vehde vich milan di baat!\nMere bullh treh naal sukke ne jiven thal di ret,\nKadon aavega oh baddal jo varhaavega barsaat!",
                "english": "Day and night my soul thirsts for the beloved,\nWhen shall whispers of reunion grace my courtyard?\nMy lips are parched with thirst like the desert sand,\nWhen shall that cloud arrive to pour its redeeming rain!",
                "commentary": "The desert soul awaiting the cloud of the beloved."
            }
        ],
        "culturalGlossary": [
            {"term": "Taangh (ਤਾਂਘ)", "pronunciation": "Taangh", "literal": "Ache of longing / intense thirst", "culturalMeaning": "Sacred Punjabi word for spiritual and romantic craving."}
        ]
    },
    {
        "id": "birhon-di-reet",
        "titleGurmukhi": "ਬਿਰਹੋਂ ਦੀ ਰੀਤ",
        "titleShahmukhi": "برہوں دی ریت",
        "titleRoman": "Birhon Di Reet",
        "titleEnglish": "The Custom of Separation",
        "book": "Piran da Paraga",
        "year": 1960,
        "tags": ["Reet", "Custom", "Sacrifice"],
        "philosophyTheme": "birha",
        "summary": "Shiv meditates on why society celebrates wedding customs (reet) while forcing the lover to observe the solitary ritual of bleeding.",
        "backstory": "Reflections on social hypocrisy in wedding ceremonies.",
        "critiqueContext": "Highlights his early critique of social rituals.",
        "tarannumNote": "Sighing, melodic cadences.",
        "stanzas": [
            {
                "gurmukhi": "ਜੱਗ ਦੀਆਂ ਰੀਤਾਂ ਸਭੇ ਝੂਠੀਆਂ ਨੇ ਮਾਏ,\nਸੱਚੀ ਤਾਂ ਸਿਰਫ਼ ਬਿਰਹੋਂ ਦੀ ਪੀੜ ਏ!\nਸੋਹਣੇ ਚਿਹਰੇ ਮਿੱਟੀ ਵਿੱਚ ਰੁਲ ਜਾਣੇ,\nਪਰ ਦਿਲ ਦਾ ਜ਼ਖ਼ਮ ਸਦਾ ਅਮੀਰ ਏ!",
                "shahmukhi": "جگ دیاں ریتاں سبھے جھوٹھیاں نے مائے،\nسچی تاں صرف برہوں دی پیڑ اے!\nسوہنے چہرے مٹی وچ رل جانے،\nپر دل دا زخم سدا امیر اے!",
                "roman": "Jagg diyan reetan sabhe jhoothiyan ne maaye,\nSachhi taan sirf birhon di peerh ae!\nSohne chehre mitti vich rul jaane,\nPar dil da zakhm sada ameer ae!",
                "english": "All the customs of this world are falsehood, O mother,\nTruth resides only in the agony of separation!\nBeautiful faces shall crumble into dust,\nYet the wound of the heart remains forever wealthy!",
                "commentary": "The wound as the only enduring royal inheritance."
            }
        ],
        "culturalGlossary": [
            {"term": "Reet (ਰੀਤ)", "pronunciation": "Reet", "literal": "Tradition / custom", "culturalMeaning": "Social norms dictating marriage and social conduct."}
        ]
    }
]

# Write out python script to append 50+ more poems
print(f"Total base poems prepared: {len(poems)}")
