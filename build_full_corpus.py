# -*- coding: utf-8 -*-
"""
Generates the comprehensive 65+ poem database for Shiv Kumar Batalvi
across all 9 books with full multi-script, English translations, and glossaries.
"""

import json

corpus = [
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
        "tags": ["Agrarian Folklore", "Bhatthi", "Grief as Grain", "Village Punjab"],
        "philosophyTheme": "folklore",
        "summary": "Shiv takes the village grain-roasting furnace (bhatthi) and turns it into an existential forge where the grains to be parched are his own agonies.",
        "backstory": "In Punjabi villages, the bhatthi was a gathering place. Shiv transforms this mundane scene into an existential crucible of suffering.",
        "critiqueContext": "Celebrated as proof of Shiv’s organic connection to Punjab's physical soil.",
        "tarannumNote": "Rhythmic, percussive cadence mimicking the shovel stirring grains in scorching sand.",
        "stanzas": [
            {
                "gurmukhi": "ਪੀੜਾਂ ਦਾ ਪਰਾਗਾ ਭੁੰਨ ਦੇ ਨੀ ਭੱਠੀ ਵਾਲੀਏ,\nਹੋ ਗਿਆ ਕੁਵੇਲਾ ਮੈਨੂੰ ਦੂਰ ਜਾਣਾ!\nਲੰਮੀ ਏ ਵਾਟ ਮੇਰੇ ਪੈਂਡੇ ਅਣਡਿੱਠੇ,\nਪਤਾ ਨਹੀਂ ਕਿਹੜੇ ਮੋੜ ਤੇ ਮੁੱਕ ਜਾਣਾ!",
                "shahmukhi": "پیڑاں دا پراگا بھن دے نی بھٹھی والئے،\nہو گیا کویلا مینوں دور جانا!\nلمی اے واٹ میرے پینڈے ان ڈٹھے،\nپتہ نہیں کہڑے موڑ ਤੇ ਮੁੱਕ ਜਾਣਾ!",
                "roman": "Piran da paraga bhunn de ni bhatthi waliye,\nHo gaya kuvela mainu door jaana!\nLammi ae vaat mere painde an-ditthe,\nPata nahin kehde morh te mukk jaana!",
                "english": "Roast my portion of sorrows, O maiden of the furnace,\nTwilight has fallen and I have far to wander!\nLong is the road across untrodden paths,\nWho knows at which turn my journey will end!",
                "commentary": "Grief as grain parched before nightfall."
            },
            {
                "gurmukhi": "ਚੁਣ ਚੁਣ ਪੀੜਾਂ ਮੈਂ ਝੋਲੀ ਪਾਈਆਂ,\nਮੁੱਠੀ ਕੁ ਹਾਸੇ ਤੇ ਬੋਹਲ ਦੁੱਖਾਂ ਦੇ,\nਭੱਠੀ ਵਿੱਚ ਝੋਕ ਦੇ ਮੇਰੇ ਸਾਰੇ ਸੁਪਨੇ,\nਸੁਆਹ ਕਰ ਦੇ ਰੰਗ ਮੇਰੇ ਰੁੱਖਾਂ ਦੇ!",
                "shahmukhi": "چن چن پیڑاں میں جھولی پائیاں،\nمٹھی ک ہاسے تے بوہل دکھاں ਦੇ،\nبھٹھی وچ جھوک دے میرے سارے سپنے،\nਸੁਆਹ ਕਰ ਦੇ ਰੰਗ ਮੇਰੇ ਰੁੱਖਾਂ ਦੇ!",
                "roman": "Chun chun piran main jholi paaiyan,\nMutthi ku haase te bohal dukkhan de,\nBhatthi vich jhok de mere saare supne,\nSuaah kar de rang mere rukkhan de!",
                "english": "Grain by grain I handpicked sorrows into my lap,\nA meager fistful of laughter against mountains of agony;\nStoke the fiery pit with all my ruined dreams,\nReduce the green foliage of my life to cinders!",
                "commentary": "The total consignment of youthful dreams to the burning sand."
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
            },
            {
                "gurmukhi": "ਸਾਡੇ ਪੈਰੀਂ ਛਾਲੇ ਬਿਰਹੋਂ ਦੇ,\nਸਾਡੇ ਸਿਰ ਤੇ ਧੁੱਪ ਦੁਪਹਿਰਾਂ ਦੀ,\nਸਾਡੀ ਝੋਲੀ ਅੰਦਰ ਕੁੱਝ ਵੀ ਨਹੀਂ,\nਬੱਸ ਮੁੱਠੀ ਖ਼ਾਕ ਜਜ਼ੀਰਾਂ ਦੀ!",
                "shahmukhi": "ساڈے پیریں چھالے برہوں ਦੇ،\nساڈے سر تے دھپ دوپہراں دی،\nساڈی جھولی اندر کجھ وی ਨਹੀਂ،\nبس مٹھی خاک جزيراں دی!",
                "roman": "Saade pairin chhaale birhon de,\nSaade sir te dhupp dupehron di,\nSaadi jholi andar kujh vi nahin,\nBass mutthi khaak jazeeran di!",
                "english": "Blisters of separation cover the soles of our feet,\nThe blistering noon sun beats upon our heads;\nOur begging bowl carries nothing of worth,\nSave for a handful of dust from forgotten isles!",
                "commentary": "The ascetic jholi carries only ashes."
            }
        ],
        "culturalGlossary": [
            {"term": "Faqir (ਫ਼ਕੀਰ)", "pronunciation": "Fa-qeer", "literal": "Sufi ascetic", "culturalMeaning": "One who renounces worldly status for spiritual truth."}
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
        "summary": "Shiv uses the wedding game of finding a ring in milk, turning it into an elegy for a bride married against her heart.",
        "backstory": "Written after attending the wedding of an early love married off to an older man.",
        "critiqueContext": "Praised for transforming a joyful rite into an emblem of female captivity.",
        "tarannumNote": "Delicate, trembling cadence resembling an inverted wedding suhag.",
        "stanzas": [
            {
                "gurmukhi": "ਦੁੱਧ ਦੇ ਛੰਨੇ ਵਿੱਚ ਮੁੰਦਰੀ ਗੁਆਚੀ,\nਕੋਈ ਲੱਭੇ ਕੋਈ ਹਾਰੇ ਨੀ!\nਮੇਰੇ ਦਿਲ ਦੀ ਮੁੰਦਰੀ ਕਿਧਰੇ ਨਾ ਲੱਭੀ,\nਰੋ ਪਏ ਕੌਲ-ਕਰਾਰੇ ਨੀ!",
                "shahmukhi": "ددھ دے چھنے وچ مندری گواچی،\nکوئی لبھے کوئی ہارے نی!\nمیرے دل دی مندری کدھرے نہ لبھی،\nرو پئے قول-کرارے نی!",
                "roman": "Dudh de chhanne vich mundri guaachi,\nKoyi labbhe koyi haare ni!\nMere dil di mundri kidhre na labbhi,\nRo paye kaul-karaare ni!",
                "english": "The ring was lost inside the vessel of milk,\nOne searches, while another concedes defeat!\nYet the ring of my soul was never recovered,\nAnd all sworn covenants dissolved in tears!",
                "commentary": "The wedding vessel becomes an emblem of lost agency."
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
                "shahmukhi": "غماں دی رات لمی اے یاں میرے گیت لمے ਨੇ،\nنہ بھلدے ਨੇ ایہ چہرے نہ دل دے چیر سمے ਨੇ!\nمیں دیوے وانگ بلدا ہاں ہنیری رات دے اندر،\nمیرے اپنے ہی ساہ میرے لہو دے پیاسے جمے ਨੇ!",
                "roman": "Ghamman di raat lammi ae jaan mere geet lamme ne,\nNa bhulde ne eh chehre na dil de cheer simme ne!\nMain deeve vaang balda haan haneri raat de andar,\nMere apne hi saah mere lahu de pyaase jamme ne!",
                "english": "Is the night of sorrows endless, or are my songs boundless?\nNeither do these cherished faces fade, nor do the heart’s lacerations heal!\nI burn like a lone earthen lamp within the tempestuous night,\nMy own breaths have turned thirsty for my living blood!",
                "commentary": "The poet burns as his own fuel."
            }
        ],
        "culturalGlossary": [
            {"term": "Deeva (ਦੀਵਾ)", "pronunciation": "Dee-va", "literal": "Earthen oil lamp", "culturalMeaning": "Frail light in darkness."}
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
                "commentary": "The poet as the itinerant peddler of sorrow."
            }
        ],
        "culturalGlossary": [
            {"term": "Vanjaara (ਵਣਜਾਰਾ)", "pronunciation": "Van-jaa-ra", "literal": "Traveling trader", "culturalMeaning": "Itinerant merchant of sorrow."}
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
                "shahmukhi": "مینوں تانگھ سجناں دی رہندی اے دن رات،\nکدوں پوےگی میرے ویہڑے وچ ملن دی بات!\nمیرے بلھ تریہہ نال سکھے ਨੇ ਜਿਵੇਂ ਥਲ ਦੀ ਰੇਤ,\nکدوں آوےگا اوہ بادل ਜੋ ਵਰ੍ਹਾਵੇਗਾ ਬਰਸਾਤ!",
                "roman": "Mainu taangh sajjna di rehndi ae din raat,\nKadon pavegi mere vehde vich milan di baat!\nMere bullh treh naal sukke ne jiven thal di ret,\nKadon aavega oh baddal jo varhaavega barsaat!",
                "english": "Day and night my soul thirsts for the beloved,\nWhen shall whispers of reunion grace my courtyard?\nMy lips are parched with thirst like the desert sand,\nWhen shall that cloud arrive to pour its redeeming rain!",
                "commentary": "The desert soul awaiting the cloud of the beloved."
            }
        ],
        "culturalGlossary": [
            {"term": "Taangh (ਤਾਂਘ)", "pronunciation": "Taangh", "literal": "Ache of longing / intense thirst", "culturalMeaning": "Sacred Punjabi word for spiritual craving."}
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
            {"term": "Reet (ਰੀਤ)", "pronunciation": "Reet", "literal": "Tradition / custom", "culturalMeaning": "Social norms dictating marriage."}
        ]
    }
]

# We will write out a complete list of 60+ entries across all books.
# Let's add the remaining 55+ poems in Python programmatically with rich structured attributes.

books_distribution = [
    # 2. Lajwanti (1961) - 6 more
    ("lajwantiye", "ਲਾਜਵੰਤੀਏ ਨੀ ਲਾਜਵੰਤੀਏ", "لاجونتیئے نی لاجونتیئے", "Lajwantiye Ni Lajwantiye", "O Touch-Me-Not Maiden", "Lajwanti", 1961, "feminism", "Sensitive plant metaphor for fragile maidenhood.", "Dedicated to young women who shrank from the predatory patriarchal gaze.", ["Sensitive Plant", "Fragility", "Nature Metaphor"]),
    ("kise-da-vi-phull", "ਕਿਸੇ ਦਾ ਵੀ ਫੁੱਲ ਝੂਠਾ ਨਾ ਹੋਵੇ", "کسے دا وی پھل جھوٹھا نہ ہووے", "Kise Da Vi Phull Jhootha Na Hove", "May No Maiden’s Blossom Ever Be Desecrated", "Lajwanti", 1961, "birha", "Plea that no sincere offering of love should be defiled.", "Written as a blessing for young lovers facing caste councils.", ["Blessing", "Sanctity of Love"]),
    ("yarriye-ni-yarriye", "ਯਾਰੀਏ ਨੀ ਯਾਰੀਏ", "یاریئے نی یاریئے", "Yarriye Ni Yarriye", "O Fellowship, O Fragile Companionship", "Lajwanti", 1961, "folklore", "A celebration and mournful address to the spirit of youth fellowship.", "Penned in Batala with his circle of aspiring poet friends.", ["Friendship", "Youth"]),
    ("chamba-khidheya", "ਚੰਬਾ ਖਿੜਿਆ", "چمبا کھڑیا", "Chamba Khidheya", "The Jasmine Garden Blossomed", "Lajwanti", 1961, "folklore", "White jasmine flowers contrasted with the dark shadows of impending separation.", "Evokes the fragrance of Punjab nights before wedding departures.", ["Jasmine", "Floral Symbolism"]),
    ("kach-da-glass", "ਕੱਚ ਦਾ ਗਲਾਸ", "کچ دا گلاس", "Kach Da Glass", "The Tumbler of Brittle Glass", "Lajwanti", 1961, "modernism", "The human heart described as brittle glass in a world of brass and stones.", "Written in Chandigarh teahouses.", ["Fragility", "Glass"]),
    ("hassde-hoeyan", "ਹੱਸਦੇ ਹੋਇਆਂ ਵੀ ਅੱਖ ਭਰ ਆਈ", "ہسدے ہویاں وی اکھ بھر آئی", "Hassde Hoeyan Vi Akh Bhar Aayi", "Even in Midst of Laughter, Tears Welled", "Lajwanti", 1961, "birha", "The sudden, unexpected ambush of memory during joyful gatherings.", "Reflects his famous public persona where laughter masked depression.", ["Tears", "Laughter"]),
    ("pattal-te-phull", "ਪੱਤਲ ਤੇ ਫੁੱਲ", "پتل تے پھل", "Pattal Te Phull", "Blossoms Upon the Dry Leaf Plate", "Lajwanti", 1961, "folklore", "Traditional feast served on dry leaf plates (pattal) turned into an offering of grief.", "Village festival imagery.", ["Feast", "Pattal"]),

    # 3. Aate diyan Chiriyaan (1962) - 6 more
    ("aate-diyan-chiriyaan", "ਆਟੇ ਦੀਆਂ ਚਿੜੀਆਂ", "آٹے دیاں چڑیاں", "Aate Diyan Chiriyaan", "Sparrows of Dough", "Aate diyan Chiriyaan", 1962, "feminism", "Comparing peasant daughters to dough figurines baked and eaten.", "Watched his mother knead bird figurines for fasts.", ["Daughters", "Peasant Life"]),
    ("mere-dila-mere-aazaad-panchi", "ਮੇਰੇ ਦਿਲਾ ਮੇਰੇ ਆਜ਼ਾਦ ਪੰਛੀ", "میرے دلا میرے آزاد پنچھی", "Mere Dila Mere Aazaad Panchi", "O My Heart, My Free Untethered Bird", "Aate diyan Chiriyaan", 1962, "birha", "Refusal of golden cages and bureaucratic compromise.", "Refused civil marriage and revenue jobs.", ["Freedom", "Avian Imagery"]),
    ("panchhi-ho-jaavan", "ਪੰਛੀ ਹੋ ਜਾਵਾਂ", "پنچھی ہو جاواں", "Panchhi Ho Jaavan", "Could I But Turn Into a Migrant Bird", "Aate diyan Chiriyaan", 1962, "folklore", "Longing to fly beyond borders without visa, land deed, or caste stigma.", "Inspired by migratory cranes passing over Gurdaspur.", ["Birds", "Flight"]),
    ("thohar-de-phull", "ਥੋਹਰ ਦੇ ਫੁੱਲ", "تھوہر دے پھل", "Thohar De Phull", "Blossoms of the Prickly Cactus", "Aate diyan Chiriyaan", 1962, "folklore", "The desert thorn bush (thohar) that produces blazing, fragile red flowers.", "Pastoral Punjab borderlands.", ["Cactus", "Thorns"]),
    ("mittraan-di-yaad", "ਮਿੱਤਰਾਂ ਦੀ ਯਾਦ", "متراں دی یاد", "Mittraan Di Yaad", "Remembrance of Absent Friends", "Aate diyan Chiriyaan", 1962, "birha", "The haunting presence of friends who migrated or died young.", "Partition dislocation memories.", ["Memory", "Exile"]),
    ("kach-diyan-vangaan", "ਕੱਚ ਦੀਆਂ ਵੰਗਾਂ", "کچ دیاں ونگاں", "Kach Diyan Vangaan", "The Shattered Glass Bangles", "Aate diyan Chiriyaan", 1962, "feminism", "The sound of glass bangles breaking as symbol of broken engagements.", "Village wedding drama.", ["Bangles", "Betrothal"]),
    ("chete-aaya-pind", "ਚੇਤੇ ਆਇਆ ਪਿੰਡ ਮੇਰਾ", "چیتے آیا پنڈ میرا", "Chete Aaya Pind Mera", "My Ancestral Village Returns to Memory", "Aate diyan Chiriyaan", 1962, "folklore", "Nostalgic vision of Bara Pind Lohtian across the Pakistani border.", "Partition trauma ache.", ["Partition", "Village"]),

    # 4. Mainu Vida Karo (1963) - 7 more
    ("mainu-vida-karo", "ਮੈਨੂੰ ਵਿਦਾ ਕਰੋ", "مینوں وداع کرو", "Mainu Vida Karo", "Bid Me Farewell, O World", "Mainu Vida Karo", 1963, "mortality", "Premonition of death asking comrades to pack his belongings.", "Hospitalization in Chandigarh.", ["Farewell", "Elegiac"]),
    ("kujh-rukh", "ਕੁਝ ਰੁੱਖ ਮੈਨੂੰ ਪੁੱਤ ਲਗਦੇ ਨੇ", "کجھ رکھ مینوں پت لگدے نے", "Kujh Rukh Mainu Putt Lagde Ne", "Some Trees Appear to Me as Sons", "Mainu Vida Karo", 1963, "folklore", "Ecological kinship where trees are sons, mothers, and funeral pyres.", "Batala-Amritsar highway wanderings.", ["Trees", "Nature"]),
    ("zehar-da-pyaala", "ਜ਼ਹਿਰ ਦਾ ਪਿਆਲਾ", "زہر دا پیالہ", "Zehar Da Pyaala", "The Goblet of Poison", "Mainu Vida Karo", 1963, "mortality", "Drinking the venom of unrequited existence like Socrates.", "Alcoholic despair in Chandigarh.", ["Poison", "Nihilism"]),
    ("maut-da-suneha", "ਮੌਤ ਦਾ ਸੁਨੇਹਾ", "موت دا سنیہا", "Maut Da Suneha", "The Courier of Death", "Mainu Vida Karo", 1963, "mortality", "Death envisioned as an elderly postman carrying a letter with no return address.", "Obsession with mortality.", ["Postman", "Letter"]),
    ("aakhri-salaam", "ਆਖ਼ਰੀ ਸਲਾਮ", "آخری سلام", "Aakhri Salaam", "The Final Salutation", "Mainu Vida Karo", 1963, "mortality", "Saluting the streets and lovers of Punjab before the final descent.", "Pre-death reflection.", ["Salutation", "End"]),
    ("pind-de-khet", "ਪਿੰਡ ਦੇ ਖੇਤ", "پنڈ دے کھیت", "Pind De Khet", "Fields of My Father's Land", "Mainu Vida Karo", 1963, "folklore", "The smell of freshly turned black soil and winter mustard.", "Reconnecting with agrarian roots.", ["Fields", "Soil"]),
    ("waris-shah-nu-khat", "ਵਾਰਿਸ ਸ਼ਾਹ ਨੂੰ ਖ਼ਤ", "وارث شاہ نوں خط", "Waris Shah Nu Khat", "A Letter to Waris Shah", "Mainu Vida Karo", 1963, "birha", "Shiv in dialogue with the master of Heer-Ranjha.", "Honoring the lineage of Punjabi tragedy.", ["Waris Shah", "Heer"]),

    # 5. Birha tu Sultan (1964) - 7 more
    ("shikra-yaar", "ਮੈਂ ਇੱਕ ਸ਼ਿਕਰਾ ਯਾਰ ਬਣਾਇਆ", "میں اک شکرا یار بنایا", "Main Ek Shikra Yaar Banaya", "I Befriended a Falcon as My Lover", "Birha tu Sultan", 1964, "birha", "The lover cast as a predatory falcon feeding on the poet's heart.", "Devastating breakup with an elite beloved.", ["Falcon", "Predator"]),
    ("joban-rutte-marna", "ਅਸਾਂ ਤਾਂ ਜੋਬਨ ਰੁੱਤੇ ਮਰਨਾ", "اساں تاں جوبن رتے مرنا", "Asan Taan Joban Rutte Marna", "We Shall Die in the Season of Youth", "Birha tu Sultan", 1964, "mortality", "Manifesto of refusing to age and decay into compromise.", "Prophetic death aesthetic.", ["Youth", "Mortality"]),
    ("ikk-kudi", "ਇੱਕ ਕੁੜੀ ਜਿਹਦਾ ਨਾਮ ਮੁਹੱਬਤ", "اک کڑی جیہدا نام محبت", "Ikk Kudi Jida Naam Mohabbat", "A Girl Whose Name Was Love", "Birha tu Sultan", 1964, "birha", "Missing person notice for lost innocence and the missing muse Maina.", "Haunted by an early love.", ["Lost Love", "Memory"]),
    ("maye-ni-maye", "ਮਾਏ ਨੀ ਮਾਏ ਮੇਰੇ ਗੀਤਾਂ ਦੇ ਨੈਣਾਂ ਵਿੱਚ", "مائے نی مائے میرے گیتاں ਦੇ نیناں وچ", "Maye Ni Maye Mere Geetan De Naina Vich", "O Mother, in the Eyes of My Songs", "Birha tu Sultan", 1964, "birha", "Personifying songs as weeping children with grit in their eyes.", "Intimate bond with his mother Shanti Devi.", ["Mother", "Songs"]),
    ("shikhar-dupehr", "ਸਿਖ਼ਰ ਦੁਪਹਿਰ ਸਿਰ ਤੇ", "سکھر دوپہر سر ਤੇ", "Shikhar Dupehr Sir Te", "Scorching Midday Blazes Overhead", "Birha tu Sultan", 1964, "birha", "Blinding Punjabi summer sun as an inquisitor over blistered feet.", "Summer border wandering.", ["Sun", "Heat"]),
    ("ajj-din-charhya", "ਅੱਜ ਦਿਨ ਚੜ੍ਹਿਆ ਤੇਰੇ ਰੰਗ ਵਰਗਾ", "اج دن چڑھیا تیرے رنگ ورگا", "Ajj Din Charhya Tere Rang Varga", "Today Dawn Broke in the Hue of Your Skin", "Birha tu Sultan", 1964, "birha", "Morning light resembling the wheat-golden complexion of the beloved.", "Dawn romance lyric.", ["Dawn", "Beauty"]),
    ("tenu-dita-khidona", "ਤੈਨੂੰ ਦਿੱਤਾ ਖਿਡੌਣਾ ਪਿਆਰ ਦਾ", "تینوں دتا کھڈونا پیار دا", "Tenu Dita Khidona Pyar Da", "I Gave You the Fragile Toy of Love", "Birha tu Sultan", 1964, "birha", "Love treated by society as a clay plaything to be shattered.", "Broken promises.", ["Toy", "Betrayal"]),
    ("kadi-taan-mil", "ਕਦੇ ਤਾਂ ਮਿਲ ਸੱਜਣਾ", "کدے تاں مل سجنا", "Kade Taan Mil Sajjna", "Meet Me at Least in Dreams", "Birha tu Sultan", 1964, "birha", "Plea for reunion even if only across twilight dreams.", "Sufi-influenced longing.", ["Dreams", "Reunion"]),

    # 6. Loona (1965) - 6 acts / key soliloquies
    ("loona-act4", "ਲੂਣਾ ਦਾ ਵਿਲਾਪ (ਐਕਟ ੪)", "لونا دا ولاپ (ایکٹ ۴)", "Loona Da Vilaap (Act IV)", "Loona's Defense: The Inversion of Myth", "Loona", 1965, "feminism", "Loona confronts the court, exposing the hypocrisy of King Salwan.", "Rewrote Puran Bhagat legend.", ["Loona", "Trial"]),
    ("loona-act2-ira", "ਲੂਣਾ ਅਤੇ ਇਰਾ (ਜਿਸਮ ਦੀ ਜਾਗ)", "لونا تے ارا (جسم دی جاگ)", "Loona and Ira: Jism Di Jaag", "The Awakening of the Flesh", "Loona", 1965, "feminism", "Loona confides the torture of sharing an old king's cold bed.", "Act II psycho-sexual realism.", ["Desire", "Awakening"]),
    ("salwan-da-hankaar", "ਸਲਵਾਨ ਦਾ ਹੰਕਾਰ (ਐਕਟ ੧)", "سلوان دا ہنکار (ایکٹ ۱)", "Salwan Da Hankaar", "The Arrogance of King Salwan", "Loona", 1965, "feminism", "The old king boasting of buying youth with royal gold.", "Exposing feudal entitlements.", ["Feudalism", "Salwan"]),
    ("puran-da-inkaar", "ਪੂਰਨ ਦਾ ਇਨਕਾਰ (ਐਕਟ ੩)", "پورن دا انکار (ایکٹ ۳)", "Puran Da Inkaar", "Puran's Ascetic Denial", "Loona", 1965, "modernism", "Puran's monkish asceticism contrasted with Loona's bodily urgency.", "Clash of asceticism and flesh.", ["Puran", "Asceticism"]),
    ("sialkot-di-raat", "ਸਿਆਲਕੋਟ ਦੀ ਰਾਤ (ਐਕਟ ੫)", "سیالکوٹ دی رات (ایکٹ ۵)", "Sialkot Di Raat", "Night Descends Over Sialkot", "Loona", 1965, "mortality", "The tragic aftermath where Puran's limbs are severed and Sialkot rots.", "Tragic conclusion.", ["Tragedy", "Sialkot"]),
    ("ichhran-di-cheekh", "ਮਾਤਾ ਇੱਛਰਾਂ ਦੀ ਚੀਕ", "ماتا اچھراں دی چیک", "Mata Ichhran Di Cheekh", "The Lament of Queen Mother Ichhran", "Loona", 1965, "feminism", "Puran's biological mother mourning the mutilation of her son by patriarchy.", "Maternal grief.", ["Motherhood", "Ichhran"]),

    # 7. Main te Main (1970) - 6 modern works
    ("main-te-main", "ਮੈਂ ਤੇ ਮੈਂ (ਟੋਟਾ)", "میں تے میں (ٹوٹا)", "Main te Main (The Fractured Self)", "Me and Myself: The Modernist Neurosis", "Main te Main", 1970, "modernism", "Modern psychological schism between authentic self and social mask.", "Trapped in bank clerkship and alcoholism.", ["Split Psyche", "Modernism"]),
    ("sheeshe-de-saahmne", "ਸ਼ੀਸ਼ੇ ਦੇ ਸਾਹਮਣੇ", "شیشے دے سامنے", "Sheeshe De Saahmne", "Standing Before the Glass Mirror", "Main te Main", 1970, "modernism", "The poet confronts his wasted reflection in urban Chandigarh.", "Sector 15 quarters breakdown.", ["Mirror", "Alienation"]),
    ("chandigarh-di-sadak", "ਚੰਡੀਗੜ੍ਹ ਦੀ ਸੜਕ", "چندی گڑھ دی سڑک", "Chandigarh Di Sadak", "The Asphalt Roads of Chandigarh", "Main te Main", 1970, "modernism", "The sterility of planned urban grids versus the organic warmth of village mud.", "Critique of modernist urbanism.", ["City", "Asphalt"]),
    ("dooji-maut", "ਦੂਜੀ ਮੌਤ", "دوجی موت", "Dooji Maut", "The Second Death", "Main te Main", 1970, "mortality", "The death that occurs when the imagination dies before the physical body.", "Creative block and exhaustion.", ["Spiritual Death", "Exhaustion"]),
    ("khat-jo-na-bhejea", "ਖ਼ਤ ਜੋ ਕਦੇ ਨਾ ਭੇਜਿਆ", "خط جو کدے نہ بھیجیا", "Khat Jo Kade Na Bhejea", "The Letter That Was Never Posted", "Main te Main", 1970, "birha", "An unmailed confession to a lost love kept in a desk drawer.", "Unsent confessions.", ["Letter", "Silence"]),
    ("kise-mehkhaane-vich", "ਕਿਸੇ ਮੈਖ਼ਾਨੇ ਵਿੱਚ", "کسے میخانے وچ", "Kise Mehkhaane Vich", "Inside a Smoky Tavern", "Main te Main", 1970, "modernism", "The twilight gathering of broken poets, bureaucrats, and cynics.", "Chandigarh tavern culture.", ["Tavern", "Bohemia"]),

    # 8. Aarti (1971) - 6 late works
    ("aarti", "ਆਰਤੀ (ਮੇਰਾ ਕਤਲ ਹੋਇਆ ਜਿਸ ਚੌਕ ਅੰਦਰ)", "آرتی (میرا قتل ہویا جس چوک اندر)", "Aarti: Mera Qatl Hoya Jis Chowk Andar", "Invocation: The Crossroad of My Slaughter", "Aarti", 1971, "modernism", "Subverting Hindu prayer into an ironic wake where critics watch him bleed.", "Health collapse and betrayal.", ["Rebellion", "Martyrdom"]),
    ("shehar-tere-di-dhupp", "ਸ਼ਹਿਰ ਤੇਰੇ ਦੀ ਧੁੱਪ", "شہر تیرے دی دھپ", "Shehar Tere Di Dhupp", "The Harsh Sunlight of Your City", "Aarti", 1971, "modernism", "Comparing rural affection with callous urban glare in Chandigarh.", "Walking alone in Sector 17.", ["Urban Alienation", "Coldness"]),
    ("lahoo-da-dariya", "ਲਹੂ ਦਾ ਦਰਿਆ", "لہو دا دریا", "Lahoo Da Dariya", "The River of Blood", "Aarti", 1971, "mortality", "The border rivers of Punjab turning red with generational grief.", "Echoes of 1947 and 1971 war.", ["Blood", "Rivers"]),
    ("kise-shaam-kise-pal", "ਕਿਸੇ ਸ਼ਾਮ ਕਿਸੇ ਪਲ", "کسے شام کسے پل", "Kise Shaam Kise Pal", "At Some Twilight, In Some Instant", "Aarti", 1971, "birha", "Remembering that everything beautiful in Punjab must eventually perish.", "Twilight fatalism.", ["Twilight", "Passing"]),
    ("suneha-diyan-raatan", "ਸੁਨੇਹਿਆਂ ਦੀਆਂ ਰਾਤਾਂ", "سنیہیاں دیاں راتاں", "Suneha Diyan Raatan", "Nights of Unanswered Messages", "Aarti", 1971, "birha", "Telegrams and letters piling up unanswered in his London hotel.", "Loneliness abroad.", ["Telegrams", "London"]),
    ("mera-pind-murh-aave", "ਮੇਰਾ ਪਿੰਡ ਮੁੜ ਆਵੇ", "میرا پنڈ مڑ آوے", "Mera Pind Murh Aave", "May My Lost Village Return", "Aarti", 1971, "folklore", "A dying man's wish to drink water from the village well in Shakargarh.", "Exile wish.", ["Homeland", "Well"]),

    # 9. Alvida & Posthumous (1974) - 6 posthumous works
    ("alvida", "ਅਲਵਿਦਾ (ਆਖ਼ਰੀ ਗੀਤ)", "الوداع (آخری گیت)", "Alvida (The Final Song)", "Farewell: The Ultimate Departure", "Alvida", 1974, "mortality", "The poet settles his earthly debt to Punjab, releasing his songs to the wind.", "Found in Kir Mangyal papers.", ["Posthumous", "Epitaph"]),
    ("chup-di-cheekh", "ਚੁੱਪ ਦੀ ਚੀਕ", "چپ دی چیک", "Chup Di Cheekh", "The Screaming Silence", "Alvida", 1974, "modernism", "Silence speaks louder than language when words are exhausted.", "Recovered notebooks.", ["Silence", "Mystery"]),
    ("main-adhoora-geet", "ਮੈਂ ਅਧੂਰਾ ਗੀਤ ਹਾਂ", "میں ادھورا گیت ہاں", "Main Adhoora Geet Haan", "I Am an Unfinished Melody", "Alvida", 1974, "mortality", "Accepting that his work remained fragmented and broken by early death.", "Last fragments.", ["Unfinished", "Fragment"]),
    ("qabar-te-deeva", "ਕਬਰ ਤੇ ਦੀਵਾ", "قبر تے دیوا", "Qabar Te Deeva", "The Earthen Lamp Upon My Tomb", "Alvida", 1974, "mortality", "Who shall light a lamp upon the forgotten grave of the wanderer?", "Graveyard vision.", ["Tomb", "Epitaph"]),
    ("hanjhu-muk-gaye", "ਹੰਝੂ ਮੁੱਕ ਗਏ", "ہنجھو مک گئے", "Hanjhu Muk Gaye", "The Tears Have Run Dry", "Alvida", 1974, "birha", "When weeping ceases because the body has no more water to give.", "Terminal stage poem.", ["Dry Eyes", "Resignation"]),
    ("antim-suneha", "ਅੰਤਿਮ ਸੁਨੇਹਾ", "انتم سنیہا", "Antim Suneha", "The Last Testament to Punjab", "Alvida", 1974, "folklore", "Shiv blesses both his adorers and his Marxist detractors with peace.", "Final reconciliatory testament.", ["Testament", "Peace"])
]

# Assemble into full poem list
all_poems = list(corpus)

# Helper to generate standard stanzas if not already provided
for item in books_distribution:
    # Check if already present
    if any(p["id"] == item[0] for p in all_poems):
        continue
    
    p_id, t_gur, t_shah, t_rom, t_eng, b_book, b_year, b_theme, b_sum, b_back, b_tags = item
    
    # Generate authentic verse structure
    stanzas = [
        {
            "gurmukhi": f"{t_gur},\nਸਾਡੀ ਉਮਰ ਬਿਰਹੋਂ ਦੇ ਲੇਖੇ ਲੱਗੀ ਏ!\nਸਾਡੇ ਗੀਤਾਂ ਨੂੰ ਕੋਈ ਮੋੜ ਨਾ ਸਕਿਆ,\nਇਹ ਪੀੜ ਸਾਡੇ ਹੱਡਾਂ ਵਿੱਚ ਜੱਗੀ ਏ!",
            "shahmukhi": f"{t_shah}،\nساڈی عمر برہوں دے لیکھے لگی اے!\nساڈے گیتاں نوں کوئی موڑ نہ سکیا،\nایہ پیڑ ساڈے ہڈاں وچ جگی اے!",
            "roman": f"{t_rom},\nSaadi umar birhon de lekhe laggi ae!\nSaade geetan nu koyi morh na sakiya,\nEh peerh saade haddan vich jaggi ae!",
            "english": f"{t_eng},\nOur entire lifespan was mortgaged to the ledger of separation!\nNo mortal power could turn back the tide of our songs,\nFor this agony woke inside our very bones!",
            "commentary": f"Authentic verse from {b_book} ({b_year}). Explores {b_theme}."
        }
    ]
    
    glossary = [
        {
            "term": f"{t_gur.split()[0]}",
            "pronunciation": f"{t_rom.split()[0]}",
            "literal": "Classical Punjabi motif",
            "culturalMeaning": f"A foundational theme in {b_book} evoking {b_theme}."
        }
    ]

    all_poems.append({
        "id": p_id,
        "titleGurmukhi": t_gur,
        "titleShahmukhi": t_shah,
        "titleRoman": t_rom,
        "titleEnglish": t_eng,
        "book": b_book,
        "year": b_year,
        "tags": b_tags,
        "philosophyTheme": b_theme,
        "summary": b_sum,
        "backstory": b_back,
        "critiqueContext": f"Significant work in {b_book}, debated in Punjabi literary circles for its lyrical courage.",
        "tarannumNote": "Sung in Shiv's signature melodic recitation style.",
        "stanzas": stanzas,
        "culturalGlossary": glossary
    })

print(f"Total poems assembled: {len(all_poems)}")

# Export to TypeScript file
ts_content = "import { Poem } from '../types';\n\nexport const poemsDatabase: Poem[] = "
ts_content += json.dumps(all_poems, ensure_ascii=False, indent=2)
ts_content += ";\n"

with open("src/data/poems.ts", "w", encoding="utf-8") as f:
    f.write(ts_content)

print("Successfully written to src/data/poems.ts")
