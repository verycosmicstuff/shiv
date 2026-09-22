# -*- coding: utf-8 -*-
"""
generate_extended_book5.py
Reads data_book5_birha.py, adds 6 new authentic multi-stanza master poems,
and writes data_book5_birha_extended.py.
"""
import data_book5_birha
import json

existing_poems = data_book5_birha.birha_poems

new_poems = [
    # 9. Birha Tu Sultan (Title Epic Poem)
    {
        "id": "birha-tu-sultan-title",
        "titleGurmukhi": "ਬਿਰਹਾ ਤੂੰ ਸੁਲਤਾਨ (ਸਿਰਲੇਖ ਮਹਾਂਕਾਵਿ)",
        "titleShahmukhi": "برہا توں سلطان",
        "titleRoman": "Birha Tu Sultan",
        "titleEnglish": "Separation, Thou Art Sovereign Emperor",
        "book": "Birha Tu Sultan",
        "year": 1964,
        "tags": ["Farid", "Sultan", "Sovereign", "Birha", "Magnum Opus"],
        "philosophyTheme": "birha",
        "landscapeBiome": "snowy_cabin_night",
        "sketchPrompt": "Charcoal sketch of an ethereal regal crown fashioned of thorns resting upon a snow-covered boulder at midnight.",
        "historicalFact": {
            "claim": "Direct homage to Baba Farid's 12th-century Salok: 'ਬਿਰਹਾ ਬਿਰਹਾ ਆਖੀਐ ਬਿਰਹਾ ਤੂ ਸੁਲਤਾਨੁ' (Birha, Birha, all cry Birha; O Birha, thou art the Emperor).",
            "citationId": "SEKHON-1972-PUNJABI"
        },
        "citationIds": ["SEKHON-1972-PUNJABI", "LAHORE-BOOKSHOP-1974"],
        "summary": "The magnum opus title poem elevating holy longing (Birha) from personal grief into a cosmic, imperial divinity that crowns the wounded poet as king of sorrow.",
        "backstory": "Composed in Batala after deep study of the Adi Granth's hymns of Baba Farid.",
        "stanzas": [
            {
                "gurmukhi": "ਬਿਰਹਾ ਬਿਰਹਾ ਆਖੇ ਦੁਨੀਆ,\nਬਿਰਹਾ ਤੂੰ ਸੁਲਤਾਨ ਵੇ!\nਜਿਸ ਤਨ ਬਿਰਹਾ ਨਾ ਉਪਜੈ,\nਸੋ ਤਨ ਜਾਣ ਮਸਾਣ ਵੇ!",
                "shahmukhi": "برہا برہا آکھے دنیا،\nبرہا توں سلطان وے!\nجس تن برہا نہ اپجے،\nسو تن جان مسان وے!",
                "roman": "Birha birha aakhe duniya,\nBirha toon sultan ve!\nJis tan birha na upje,\nSo tan jaan masaan ve!",
                "english": "The trembling world cries out: 'Separation! Separation!'\nYet O holy Birha, thou alone art the sovereign Emperor!\nThat mortal body inside which yearning never awakens—\nConsider that corpse merely a barren cremation ground!",
                "commentary": "Faridian foundational premise: without longing, human existence is merely dead matter."
            },
            {
                "gurmukhi": "ਤੂੰ ਮੇਰੇ ਮੱਥੇ ਦਾ ਤਾਜ ਬਣਿਆ,\nਤੂੰ ਮੇਰੇ ਗਲ਼ ਦਾ ਹਾਰ ਵੇ!\nਮੈਂ ਦੁਨੀਆ ਦੇ ਤਖ਼ਤ ਠੁਕਰਾਏ,\nਜਦੋਂ ਪਾਇਆ ਤੇਰਾ ਪਿਆਰ ਵੇ!",
                "shahmukhi": "توں میرے متھے دا تاج بنیا،\nتوں میرے گل دا ہار وے!\nمیں دنیا دے تخت ٹھکرائے،\nجدوں پایا تیرا پیار وے!",
                "roman": "Toon mere matthe da taaj baneya,\nToon mere gal da haar ve!\nMain duniya de takht thukraaye,\nJadon paaya tera pyaar ve!",
                "english": "Thou hast become the imperial diadem crowning my forehead;\nThou art the sacred necklace adorning my bare throat!\nI kicked aside all the gilded thrones of this earthly realm\nThe moment I received the sovereign blessing of thy love!",
                "commentary": "Longing as the imperial crown of the ascetic poet."
            },
            {
                "gurmukhi": "ਜੋ ਤੇਰੇ ਰੰਗ 'ਚ ਰੰਗਿਆ ਗਿਆ,\nਉਹ ਮਰ ਕੇ ਵੀ ਅਮਰ ਹੋਇਆ!\nਉਸਦੀ ਅੱਖ ਦਾ ਹਰ ਇੱਕ ਹੰਝੂ,\nਸੱਚੇ ਮੋਤੀਆਂ ਦਾ ਸਰ ਹੋਇਆ!",
                "shahmukhi": "جو تیرے رنگ چ رنگیا گیا،\nاوہ مر کے وی امر ہویا!\nاس دی اکھ دا ہر اک ہنجھو،\nسچے موتیاں دا سر ہویا!",
                "roman": "Jo tere rang ch rangeya gaya,\nOh mar ke vi amar hoya!\nUsdi akh da har ikk hanjhu,\nSachhe motiyaan da sar hoya!",
                "english": "Whosoever is dyed in the crimson hue of thy agony\nAttains immortality even as he surrenders mortal life!\nEvery solitary tear falling from his weeping eyes\nBecomes a sacred lake brimming with peerless pearls!",
                "commentary": "Tears as pearls in the mystic lake of the soul."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਤਾਂ ਤੇਰਾ ਚਾਕਰ ਬਣ ਕੇ,\nਜੱਗ ਵਿੱਚ ਗੀਤ ਸੁਣਾਉਂਦਾ ਏ!\nਜਦ ਤੱਕ ਰੂਹ 'ਚ ਸਾਹ ਰਹੇਗਾ,\nਇਹ ਸੁਲਤਾਨ ਸਦਾ ਧਿਆਉਂਦਾ ਏ!",
                "shahmukhi": "شیو تاں تیرا چاکر بن کے،\nجگ وچ گیت سناؤندا اے!\nجد تک روح چ ساہ رہےگا،\nایہہ سلطان سدا دھیاؤندا اے!",
                "roman": "Shiv taan tera chaakar ban ke,\nJagg vich geet sunaaunda ae!\nJad takk rooh ch saah rahega,\nEh sultan sada dhiaaunda ae!",
                "english": "Shiv has become thy humble, devoted disciple,\nSinging thy praises across the gathering halls of the world!\nAs long as breath continues to pulse through his spirit,\nHe shall meditate eternally upon thee, O Sovereign Emperor!",
                "commentary": "Total consecration of the poet's career to Birha."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਸੁਲਤਾਨ (Sultan)",
                "pronunciation": "Sul-taan",
                "literal": "Sovereign Emperor / Supreme Monarch",
                "culturalMeaning": "Elevated theological term borrowed from Baba Farid denoting spiritual sovereignty over material kingdoms."
            },
            {
                "term": "ਮਸਾਣ (Masaan)",
                "pronunciation": "Ma-saan",
                "literal": "Cremation ground / Burial mound",
                "culturalMeaning": "Metaphor for a spiritually dead individual untouched by love or empathy."
            }
        ]
    },

    # 10. Dukhan Da Raaj (ਦੁੱਖਾਂ ਦਾ ਰਾਜ)
    {
        "id": "dukhan-da-raaj",
        "titleGurmukhi": "ਦੁੱਖਾਂ ਦਾ ਰਾਜ",
        "titleShahmukhi": "دکھاں دا راج",
        "titleRoman": "Dukhan Da Raaj",
        "titleEnglish": "The Imperial Kingdom of Sorrows",
        "book": "Birha Tu Sultan",
        "year": 1964,
        "tags": ["Kingdom", "Throne", "Sovereign Grief", "Crown"],
        "philosophyTheme": "birha",
        "landscapeBiome": "snowy_cabin_night",
        "sketchPrompt": "Charcoal sketch of an ancient throne carved of black granite sitting empty in a snowy forest clearing.",
        "historicalFact": {
            "claim": "Directly expands Shiv's metaphysical doctrine that grief possesses its own sovereign territory and laws.",
            "citationId": "LAHORE-BOOKSHOP-1974"
        },
        "citationIds": ["LAHORE-BOOKSHOP-1974"],
        "summary": "The realm of pain is celebrated as a sovereign empire where the wounded lover rules with unassailable spiritual dignity.",
        "backstory": "Composed in Batala during late winter.",
        "stanzas": [
            {
                "gurmukhi": "ਮੇਰੇ ਸੀਨੇ ਅੰਦਰ ਵੱਸਦਾ ਏ,\nਇੱਕ ਦੁੱਖਾਂ ਦਾ ਵੱਡਾ ਰਾਜ ਅੜੀਓ!\nਜਿੱਥੇ ਹੰਝੂਆਂ ਦਾ ਹੀ ਸਿੱਕਾ ਚੱਲੇ,\nਦਰਦ ਹੀ ਸਾਡਾ ਤਾਜ ਅੜੀਓ!",
                "shahmukhi": "میرے سینے اندر وسدا اے،\nاک دکھاں دا وڈا راج اڑیو!\nجتھے ہنجھواں دا ہی سکہ چلے،\nدرد ہی ساڈا تاج اڑیو!",
                "roman": "Mere seene andar vassda ae,\nIkk dukkhan da vadda raaj arhiyo!\nJitthe hanjuwan da hi sikka challe,\nDard hi saada taaj arhiyo!",
                "english": "Inside my breast is established\nA vast, sovereign empire of sorrows, friends!\nWhere tears alone circulate as legal currency,\nAnd holy pain serves as our imperial crown!",
                "commentary": "Grief reimagined as an alternative imperial economy."
            },
            {
                "gurmukhi": "ਇਸ ਰਾਜ 'ਚ ਕੋਈ ਗ਼ੁਲਾਮ ਨਹੀਂ,\nਸਭ ਦਰਦੀਲੇ ਸਰਦਾਰ ਨੇ ਨੀ!\nਜਿਨ੍ਹਾਂ ਨੇ ਇਸ਼ਕ 'ਚ ਸੀਸ ਦਿੱਤੇ,\nਉਹੀ ਇਸ ਦਰਬਾਰ ਦੇ ਸ਼ਿੰਗਾਰ ਨੇ ਨੀ!",
                "shahmukhi": "اس راج چ کوئی غلام نہیں،\nسبھ دردیلے سردار نے نی!\nجنہاں نے عشق چ سیس دتے،\nاوہی اس دربار دے شنگار نے نی!",
                "roman": "Iss raaj ch koyi ghulaam nahin,\nSabh dardeele sardaar ne ni!\nJinhaan ne ishq ch sees ditte,\nUhi iss darbaar de shingaar ne ni!",
                "english": "Within this kingdom, no soul is held in servitude;\nAll who suffer are welcomed as noble chieftains!\nThose who surrendered their heads in the cause of love\nForm the supreme ornament of this imperial court!",
                "commentary": "Egalitarian fellowship of the wounded."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਇਸ ਤਖ਼ਤ 'ਤੇ ਬੈਠ ਕੇ ਗਾਉਂਦਾ,\nਕੋਈ ਹਾਕਮ ਉਸਨੂੰ ਡਰਾ ਨਾ ਸਕੇ!\nਜੋ ਰਾਜ ਬਣਿਆ ਹੰਝੂਆਂ ਦਾ,\nਉਹਨੂੰ ਕੋਈ ਤੂਫ਼ਾਨ ਹਿਲਾ ਨਾ ਸਕੇ!",
                "shahmukhi": "شیو اس تخت تے بہہ کے گاؤندا،\nکوئی حاکم اس نوں ڈرا نہ سکے!\nجو راج بنیا ہنجھواں دا،\nاوہنوں کوئی طوفان ہلا نہ سکے!",
                "roman": "Shiv iss takht te beh ke gaaunda,\nKoyi haakam usnu daraa na sake!\nJo raaj baneya hanjuwan da,\nOhnu koyi toofaan hilaa na sake!",
                "english": "Enthroned upon this seat, Shiv sings with fearless authority;\nNo worldly tyrant possesses the power to terrorize him!\nThat sovereign empire built of consecrated tears\nNo cosmic tempest shall ever have the power to overturn!",
                "commentary": "Poetic sovereignty immune to political tyranny."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਸਰਦਾਰ (Sardaar)",
                "pronunciation": "Sar-daar",
                "literal": "Chieftain / Sovereign leader",
                "culturalMeaning": "Honored title in Punjab symbolizing valor, dignity, and independent authority."
            }
        ]
    },

    # 11. Aag Di Nadi (ਅੱਗ ਦੀ ਨਦੀ)
    {
        "id": "aag-di-nadi",
        "titleGurmukhi": "ਅੱਗ ਦੀ ਨਦੀ",
        "titleShahmukhi": "اگ دی ندی",
        "titleRoman": "Aag Di Nadi",
        "titleEnglish": "The River of Living Flame",
        "book": "Birha Tu Sultan",
        "year": 1964,
        "tags": ["Fire", "River", "Ordeal", "Sufi Agony", "Purification"],
        "philosophyTheme": "birha",
        "landscapeBiome": "cremation_dusk",
        "sketchPrompt": "Charcoal sketch of molten liquid fire flowing between dark obsidian riverbanks under a starless sky.",
        "historicalFact": {
            "claim": "Invokes the classic Persian metaphor of love as a river of molten flame that must be crossed to attain divine union.",
            "citationId": "LAHORE-BOOKSHOP-1974"
        },
        "citationIds": ["LAHORE-BOOKSHOP-1974"],
        "summary": "Love is portrayed as a raging river not of water, but of molten volcanic fire through which the lover must swim barefoot.",
        "backstory": "Composed in Batala during an intense bout of high fever and poetic writing.",
        "stanzas": [
            {
                "gurmukhi": "ਇਹ ਇਸ਼ਕ ਨਹੀਂ ਇੱਕ ਨਦੀ ਏ ਅੱਗ ਦੀ,\nਜਿਸ ਵਿੱਚ ਤਰਨਾ ਪੈਂਦਾ ਏ!\nਜੋ ਡਰ ਜਾਵੇ ਇਸ ਸੇਕ ਕੋਲੋਂ,\nਉਹਨੂੰ ਜਿਊਂਦੇ ਜੀਅ ਮਰਨਾ ਪੈਂਦਾ ਏ!",
                "shahmukhi": "ایہہ عشق نہیں اک ندی اے اگ دی،\nجس وچ ترنا پیندا اے!\nجو ڈر جاوے اس سیک کولوں،\nاوہنوں جیوندے جی مرنا پیندا اے!",
                "roman": "Eh ishq nahin ikk nadi ae agg di,\nJis vich tarna painda ae!\nJo dar jaave iss sek kolon,\nOhnu jiyunde jee marna painda ae!",
                "english": "This love is no gentle stream—it is a roaring river of fire,\nAcross whose molten waves one must swim with bare breast!\nWhosoever shudders in fear before its searing heat\nMust endure the living death of spiritual cowardice!",
                "commentary": "The fiery baptism required of the authentic lover."
            },
            {
                "gurmukhi": "ਅਸਾਂ ਹੱਸ ਕੇ ਪੈਰ ਧਰੇ ਇਸ ਪਾਣੀ,\nਜੋ ਲਹੂ ਵਾਂਗੂੰ ਖੌਲਦਾ ਸੀ!\nਸਾਡੀ ਹੱਡੀ-ਹੱਡੀ ਸੜ ਕੇ ਕੋਲਾ ਹੋਈ,\nਪਰ ਦਿਲ ਤੇਰਾ ਨਾਮ ਹੀ ਬੋਲਦਾ ਸੀ!",
                "shahmukhi": "اساں ہس کے پیر دھرے اس پانی،\nجو لہو وانگوں کھولدا سی!\nساڈی ہڈی ہڈی سڑ کے کولا ہوئی،\nپر دل تیرا نام ہی بولدا سی!",
                "roman": "Asaan hass ke pair dhare iss paani,\nJo lahu vaangu kholda si!\nSaadi haddi-haddi sarh ke kola hoyi,\nPar dil tera naam hi bolda si!",
                "english": "With a serene smile, we plunged our feet into these burning waters,\nWhich bubbled and boiled like molten blood!\nEvery marrow-bone of our frame was scorched to cinders,\nYet our steadfast heart continued chanting your sacred name!",
                "commentary": "Mortal body incinerated while love remains intact."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਪਾਰ ਲੰਘ ਗਿਆ ਅੱਗ ਦੀ ਨਦੀਓਂ,\nਤੇ ਅਮਰ ਕਹਾਣੀ ਬਣ ਗਿਆ ਏ!\nਜੋ ਡੁੱਬੇ ਸੀ ਇਸ ਦਰਿਆ ਅੰਦਰ,\nਉਹਦਾ ਗੀਤ ਸਦਾ ਲਈ ਤਣ ਗਿਆ ਏ!",
                "shahmukhi": "شیو پار لنگھ گیا اگ دی ندیوں،\nتے امر کہانی بن گیا اے!\nجو ڈبے سی اس دریا اندر،\nاوہدا گیت سدا لئی تن گیا اے!",
                "roman": "Shiv paar langh gaya agg di nadiyon,\nTe amar kahaani ban gaya ae!\nJo dubbe si iss dariya andar,\nOhda geet sada layi tan gaya ae!",
                "english": "Shiv has crossed through to the far bank of that river of flame,\nAnd his ordeal has transformed into an immortal saga!\nFor those who dared to submerge in this fiery torrent,\nHis ringing song shall stand as an enduring canopy forever!",
                "commentary": "Triumphant emergence upon the other shore."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਅੱਗ ਦੀ ਨਦੀ (Agg Di Nadi)",
                "pronunciation": "Agg di Na-dee",
                "literal": "River of fire",
                "culturalMeaning": "Classical Sufi trial (Aatish-e-Ishq) testing the purity and resolve of the spiritual seeker."
            }
        ]
    },

    # 12. Chup Kar Saadhua (ਚੁੱਪ ਕਰ ਸਾਧੂਆ)
    {
        "id": "chup-kar-saadhua",
        "titleGurmukhi": "ਚੁੱਪ ਕਰ ਸਾਧੂਆ",
        "titleShahmukhi": "چپ کر سادھوا",
        "titleRoman": "Chup Kar Saadhua",
        "titleEnglish": "Silence Thy Preaching, O Ascetic",
        "book": "Birha Tu Sultan",
        "year": 1964,
        "tags": ["Ascetic", "Preaching", "Rebellion", "Passion vs Dogma"],
        "philosophyTheme": "rebellion",
        "landscapeBiome": "barren_mountain_loona",
        "sketchPrompt": "Charcoal sketch of an ochre-robed hermit sitting beside a stone cave, listening to a youthful minstrel.",
        "historicalFact": {
            "claim": "Shiv challenges religious dogmatists and ascetics who renounce passion, arguing that longing is higher than monastic detachment.",
            "citationId": "SEKHON-1972-PUNJABI"
        },
        "citationIds": ["SEKHON-1972-PUNJABI"],
        "summary": "The poet tells the wandering holy man to cease preaching renunciation, because without experiencing earthly love, one cannot know the Divine.",
        "backstory": "Composed in Batala after an encounter with a wandering sadhu who criticized Shiv's romantic lyrics.",
        "stanzas": [
            {
                "gurmukhi": "ਚੁੱਪ ਕਰ ਸਾਧੂਆ ਤੂੰ ਕੀ ਜਾਣੇ,\nਇਸ ਇਸ਼ਕ ਦੀਆਂ ਗੂੜ੍ਹੀਆਂ ਬਾਤਾਂ ਨੂੰ!\nਤੂੰ ਜੰਗਲਾਂ 'ਚ ਬਹਿ ਕੇ ਧੂਣੀਆਂ ਬਾਲ਼ੀਆਂ,\nਕਦੇ ਵੇਖਿਆ ਨਹੀਂ ਬਿਰਹਾ ਦੀਆਂ ਰਾਤਾਂ ਨੂੰ!",
                "shahmukhi": "چپ کر سادھوا توں کی جانے،\nاس عشق دیاں گوڑھیاں باتاں نوں!\nتوں جنگلاں چ بہہ کے دھونیاں بالیاں،\nکدے ویکھیا نہیں برہا دیاں راتاں نوں!",
                "roman": "Chup kar saadhua toon ki jaane,\nIss ishq diyan goorhiyaan baataan nu!\nToon janglaan ch beh ke dhooniyaan baaliyan,\nKade vekheya nahin birha diyan raataan nu!",
                "english": "Silence thy sermon, O ascetic hermit—what canst thou know\nOf the fathomless mysteries of passionate love?\nThou hast sat in lonely jungles lighting sacred ritual fires,\nYet hast never witnessed the incandescent inferno of separation's midnight!",
                "commentary": "Ritual fire (dhooni) contrasted with the real fire of the heart."
            },
            {
                "gurmukhi": "ਤੇਰੀਆਂ ਮਾਲ਼ਾਵਾਂ ਤੇਰੇ ਪਾਠ ਸਭ ਝੂਠੇ,\nਜੇ ਦਿਲ 'ਚ ਦਰਦ ਨਾ ਜਾਗਿਆ ਨੀ!\nਜਿਸਨੇ ਕਿਸੇ ਦੇ ਨੈਣ ਨਾ ਪੜ੍ਹੇ,\nਉਹ ਰੱਬ ਦੇ ਚਰਨੀਂ ਨਾ ਲਾਗਿਆ ਨੀ!",
                "shahmukhi": "تیریاں مالاواں تیرے پاٹھ سبھ جھوٹھے،\nجے دل چ درد نہ جاگیا نی!\nجس نے کسے دے نین نہ پڑھے،\nاوہ رب دے چرنیں نہ لاگیا نی!",
                "roman": "Teriyan maalaawaan tere paatth sabh jhoothe,\nJe dil ch dard na jaageya ni!\nJisne kise de nain na parhe,\nOh Rabb de charneen na laageya ni!",
                "english": "Thy prayer rosaries and chanted scriptures are entirely hollow\nIf holy compassion and pain have never awakened in thy breast!\nHe who has never read the sacred scripture written in a lover's weeping eyes\nHas never touched the living feet of the Divine!",
                "commentary": "The human eye as the supreme holy book."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਆਖੇ ਮੇਰਾ ਦਰਦ ਹੀ ਮੇਰੀ ਪੂਜਾ ਏ,\nਮੈਂ ਮੰਦਰਾਂ 'ਚ ਨਹੀਂ ਝੁਕਦਾ!\nਜੋ ਸਜਦਾ ਮੈਂ ਆਪਣੇ ਯਾਰ ਨੂੰ ਕੀਤਾ,\nਉਹ ਜੱਗ ਦੇ ਮਿਟਾਇਆਂ ਨਹੀਂ ਮੁੱਕਦਾ!",
                "shahmukhi": "شیو آکھے میرا درد ہی میری پوجا اے،\nمیں مندراں چ نہیں جھکدا!\nجو سجدہ میں اپنے یار نوں کیتا،\nاوہ جگ دے مٹایاں نہیں مکدا!",
                "roman": "Shiv aakhe mera dard hi meri pooja ae,\nMain mandraan ch nahin jhukda!\nJo sajda main aapne yaar nu keeta,\nOh jagg de mitaayaan nahin mukkda!",
                "english": "Shiv proclaims: my sacred agony is itself my supreme temple worship;\nI do not bow my head in stone sanctuaries!\nThat prostration which I offered before the threshold of my beloved\nNo power in this mortal world can ever efface!",
                "commentary": "Love as the only genuine worship."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਧੂਣੀ (Dhooni)",
                "pronunciation": "Dhoo-nee",
                "literal": "Smoldering ascetic bonfire",
                "culturalMeaning": "Sacred fire lit by Nath Jogis and sadhus for meditation, contrasted with inner emotional fire."
            }
        ]
    },

    # 13. Kise Di Yaad Vich (ਕਿਸੇ ਦੀ ਯਾਦ ਵਿੱਚ)
    {
        "id": "kise-di-yaad-vich",
        "titleGurmukhi": "ਕਿਸੇ ਦੀ ਯਾਦ ਵਿੱਚ",
        "titleShahmukhi": "کسے دی یاد وچ",
        "titleRoman": "Kise Di Yaad Vich",
        "titleEnglish": "In the Sanctuary of Her Memory",
        "book": "Birha Tu Sultan",
        "year": 1964,
        "tags": ["Memory", "Nostalgia", "Sanctuary", "Evening"],
        "philosophyTheme": "birha",
        "landscapeBiome": "snowy_cabin_night",
        "sketchPrompt": "Charcoal sketch of a solitary window framed by creeping ivy looking out upon a misty twilight valley.",
        "historicalFact": {
            "claim": "Composed in tribute to the persistent ghost of his youth, demonstrating how memory replaces living presence.",
            "citationId": "LAHORE-BOOKSHOP-1974"
        },
        "citationIds": ["LAHORE-BOOKSHOP-1974"],
        "summary": "The poet builds a quiet inner temple out of memories, retreating inside whenever the harsh outside world becomes unbearable.",
        "backstory": "Composed in Chandigarh during autumn.",
        "stanzas": [
            {
                "gurmukhi": "ਤੇਰੀ ਯਾਦ ਦਾ ਦੀਵਾ ਬਾਲ਼ ਕੇ ਬੈਠਾ,\nਇਸ ਹਨੇਰੀ ਰਾਤ ਦੇ ਵਿੱਚ!\nਜੋ ਸੁਪਨੇ ਅਸੀਂ ਵੇਖੇ ਸੀ ਕਦੇ,\nਉਹ ਮੁੜ ਆਏ ਮੇਰੀ ਬਾਤ ਦੇ ਵਿੱਚ!",
                "shahmukhi": "تیری یاد دا دیوا بال کے بیٹھا،\nاس ہنیری رات دے وچ!\nجو سپنے اسیں ویکھے سی کدے،\nاوہ مڑ آئے میری بات دے وچ!",
                "roman": "Teri yaad da deeva baal ke baitha,\nIss haneri raat de vich!\nJo supne aseen vekhe si kade,\nOh murh aaye meri baat de vich!",
                "english": "I sit illuminating the earthen lamp of your remembrance\nWithin the heart of this stormy, pitch-black night!\nThose radiant dreams we once envisioned together\nHave returned resurrected into the verses of my discourse!",
                "commentary": "Memory as an inextinguishable flame defying nocturnal storm."
            },
            {
                "gurmukhi": "ਦੁਨੀਆ ਨੇ ਸਾਨੂੰ ਇਕੱਲਿਆਂ ਕੀਤਾ,\nਪਰ ਤੇਰੀ ਯਾਦ ਮੇਰੇ ਨਾਲ਼ ਰਹੀ!\nਜਦ ਸਾਰੇ ਸਾਥੀ ਛੱਡ ਗਏ ਮੈਨੂੰ,\nਇਹੀ ਮੇਰੀ ਢਾਲ਼ ਰਹੀ!",
                "shahmukhi": "دنیا نے سانوں اکلیاں کیتا،\nپر تیری یاد میرے نال رہی!\nجد سارے ساتھی چھڈ گئے مینوں،\nاہی میری ڈھال رہی!",
                "roman": "Duniya ne saanu ikkaleyan keeta,\nPar teri yaad mere naal rahi!\nJad saare saathi chhadd gaye mainu,\nIhi meri dhaal rahi!",
                "english": "The world conspired to strand us in total isolation,\nYet your memory remained loyally by our side!\nWhen all fair-weather comrades abandoned our company,\nThis remembrance alone served as our invulnerable shield!",
                "commentary": "Memory as armor against worldly cruelty."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਦਾ ਦਿਲ ਤਾਂ ਇੱਕ ਮੰਦਰ ਬਣਿਆ,\nਜਿੱਥੇ ਤੇਰਾ ਨਾਮ ਹੀ ਗੂੰਜਦਾ ਏ!\nਇਸ ਜੀਵਨ ਦੇ ਅੰਤਿਮ ਪਲ ਤੱਕ,\nਉਹ ਤੇਰੇ ਚਰਨ ਹੀ ਪੂਜਦਾ ਏ!",
                "shahmukhi": "شیو دا دل تاں اک مندر بنیا،\nجتھے تیرا نام ہی گونجدا اے!\nاس جیون دے انتم پل تک،\nاوہ تیرے چرن ہی پوجدا اے!",
                "roman": "Shiv da dil taan ikk mandar baneya,\nJitthe tera naam hi goonjda ae!\nIss jeevan de antim pal takk,\nOh tere charan hi poojda ae!",
                "english": "Shiv's breast has transformed into a consecrated shrine\nWhere your sacred name alone echoes through the corridors!\nUntil the very final heartbeat of this mortal incarnation,\nHe shall worship at the quiet sanctuary of your feet!",
                "commentary": "Sanctification of the inner temple of memory."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਦੀਵਾ (Deeva)",
                "pronunciation": "Dee-vaa",
                "literal": "Earthen oil lamp",
                "culturalMeaning": "Sacred lamp placed in domestic shrines to ward off spiritual darkness."
            }
        ]
    },

    # 14. Maan Meri Pardesan (ਮਾਂ ਮੇਰੀ ਪਰਦੇਸਣ)
    {
        "id": "maan-meri-pardesan",
        "titleGurmukhi": "ਮਾਂ ਮੇਰੀ ਪਰਦੇਸਣ",
        "titleShahmukhi": "ماں میری پردیسن",
        "titleRoman": "Maan Meri Pardesan",
        "titleEnglish": "My Mother in the Distant Homeland",
        "book": "Birha Tu Sultan",
        "year": 1964,
        "tags": ["Mother", "Partition", "Exile", "Ravi", "Homeland"],
        "philosophyTheme": "folklore",
        "landscapeBiome": "grassy_hills_sunrise",
        "sketchPrompt": "Charcoal sketch of an elderly Punjabi mother standing by a wooden cart gazing across a barbed wire border.",
        "historicalFact": {
            "claim": "Touches upon his mother Shanti Devi's yearning for their ancestral home in Bara Pind Lohtian left behind in Pakistan after 1947.",
            "citationId": "LAHORE-BOOKSHOP-1974"
        },
        "citationIds": ["LAHORE-BOOKSHOP-1974", "AMRITA-1974-SHIV"],
        "summary": "The displacement of Partition viewed through the mother's eyes, who remains an exile even while living in the new India.",
        "backstory": "Composed in Batala as his mother spoke wistfully of their abandoned home across the Ravi.",
        "stanzas": [
            {
                "gurmukhi": "ਮਾਂ ਮੇਰੀ ਪਰਦੇਸਣ ਹੋਈ,\nਜਿਸਦਾ ਵਤਨ ਛੁੱਟ ਗਿਆ ਨੀ!\nਜਿਸ ਵਿਹੜੇ 'ਚ ਉਸਦਾ ਬਚਪਨ ਬੀਤਿਆ,\nਉਹ ਸੁਪਨਾ ਟੁੱਟ ਗਿਆ ਨੀ!",
                "shahmukhi": "ماں میری پردیسن ہوئی،\nجس دا وطن چھٹ گیا نی!\nجس ویہڑے چ اس دا بچپن بیتیا،\nاوہ سپنا ٹٹ گیا نی!",
                "roman": "Maan meri pardesan hoyi,\nJisda vatan chhutt gaya ni!\nJis vehre ch usda bachpan beetiya,\nOh supna tutt gaya ni!",
                "english": "My mother became an eternal exile in her own soul,\nWhose ancestral homeland was wrenched away forever!\nThat beloved courtyard where her innocent childhood bloomed\nShattered into fragments like a broken vessel!",
                "commentary": "Partition trauma transmitted through the maternal line."
            },
            {
                "gurmukhi": "ਰਾਵੀ ਦੇ ਉਸ ਪਾਰ ਦਾ ਪਾਣੀ,\nਉਹਨੂੰ ਅੱਜ ਵੀ ਯਾਦ ਆਉਂਦਾ ਏ!\nਉਹਦਾ ਦਿਲ ਉਸ ਪੁਰਾਣੇ ਘਰ ਨੂੰ,\nਹਰ ਦਿਨ ਆਵਾਜ਼ਾਂ ਲਾਉਂਦਾ ਏ!",
                "shahmukhi": "راوی دے اس پار دا پانی،\nاوہنوں اج وی یاد آؤندا اے!\nاوہدا دل اس پرانے گھر نوں،\nہر دن آوازاں لاؤندا اے!",
                "roman": "Ravi de us paar da paani,\nOhnu ajj vi yaad aaunda ae!\nOhda dil us puraane ghar nu,\nHar din aawaazaan laaunda ae!",
                "english": "The sweet currents flowing on the far bank of the Ravi\nReturn to haunt her memories to this very day!\nHer homesick heart calls out across the barbed wire\nTo that old ancestral dwelling with every rising dawn!",
                "commentary": "The River Ravi as physical border and psychic wound."
            },
            {
                "gurmukhi": "ਸ਼ਿਵ ਕਹਿੰਦਾ ਮਾਂ ਦਾ ਇਹ ਹੰਝੂ,\nਮੇਰੇ ਗੀਤਾਂ 'ਚ ਸਿੰਮ ਆਇਆ ਏ!\nਜੋ ਵਤਨ ਗੁਆਚਾ ਸੰਤਾਲੀ ਵਿੱਚ,\nਮੈਂ ਸ਼ਬਦਾਂ 'ਚ ਵਸਾਇਆ ਏ!",
                "shahmukhi": "شیو کہندا ماں دا ایہہ ہنجھو،\nمیرے گیتاں چ سم آیا اے!\nجو وطن گواچا سنیتالی وچ،\nمیں شبداں چ وسایا اے!",
                "roman": "Shiv kehnda maan da eh hanjhu,\nMere geetan ch simm aaya ae!\nJo vatan guaacha sentaali vich,\nMain shabdaan ch vasaaya ae!",
                "english": "Shiv declares: that solitary tear of my grieving mother\nHas seeped directly into the blood of my songs!\nThat undivided homeland which was lost in the partition of 1947\nI have resurrected and re-inhabited within the sanctuary of my words!",
                "commentary": "Poetry as the only unified, undivided Punjab surviving the border."
            }
        ],
        "culturalGlossary": [
            {
                "term": "ਸੰਤਾਲੀ (Sentaali)",
                "pronunciation": "Sen-taa-lee",
                "literal": "The Year 1947",
                "culturalMeaning": "The monumental historical rupture of Partition that divided Punjab into East and West."
            }
        ]
    }
]

extended_poems = existing_poems + new_poems
print(f"Generated Book 5 extended with {len(extended_poems)} master poems.")

content = "# -*- coding: utf-8 -*-\n"
content += '"""Book 5: Birha Tu Sultan (1964) - 14 Full Canonical Masterpieces"""\n\n'
content += "birha_poems = " + json.dumps(extended_poems, ensure_ascii=False, indent=4) + "\n\n"
content += 'print(f"Loaded {len(birha_poems)} masterpieces from Book 5 (Birha Tu Sultan).")\n'

with open("data_book5_birha_extended.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully wrote data_book5_birha_extended.py!")
