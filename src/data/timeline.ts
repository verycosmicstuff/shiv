import { TimelineEvent } from '../types';

export const timelineDatabase: TimelineEvent[] = [
  {
    id: 'tl-1936-birth',
    year: 1936,
    period: 'October 23, 1936',
    title: 'Birth in Bara Pind Lohtian',
    category: 'personal',
    location: 'Bara Pind Lohtian, Shakargarh (now Pakistan)',
    summary: 'Born to Pandit Krishan Gopal (a village tehsildar/patwari) and Shanti Devi in rural undivided Punjab.',
    deepNarrative: 'Shiv grew up immersed in the fertile folk rhythms of rural Punjab—listening to women parching grains at the bhatthi, wandering through mustard fields, and absorbing the musical meters of Waris Shah, Bulleh Shah, and Qadir Yar. This agrarian childhood became the eternal reservoir of his imagery.',
    impactOnPoetry: 'Supplied the indelible pastoral metaphors: the clay furnace, wild thorns (thohar), desert mirages, and village seasonal rites.',
    relatedPoemIds: ['bhatthi-waliye'],
    citationIds: ['SHARMA-1979-SOLITARY'],
    keyQuote: {
      text: 'My childhood was not spent in towns, but in the lap of the soil where every wind sang in Heer’s meter.',
      source: 'Recollection recorded by contemporaries'
    }
  },
  {
    id: 'tl-1947-partition',
    year: 1947,
    period: 'August 1947',
    title: 'The Wound of Partition: Flight to Batala',
    category: 'political_context',
    location: 'Bara Pind to Batala (Gurdaspur, East Punjab)',
    summary: 'At age 11, Shiv and his family were uprooted in the bloodbath of Partition, fleeing across the newly drawn border to settle in Batala.',
    deepNarrative: 'The trauma of Partition was not celebrated with patriotic anthems in Shiv’s work; instead, it lived inside him as a quiet, incurable ache of homelessness. The loss of ancestral soil and the visceral horror of communal carnage permanently shattered his childhood innocence, embedding the motif of permanent exile in his soul.',
    impactOnPoetry: 'Transformed separation from mere personal heartbreak into a generational, existential condition of dislocation.',
    relatedPoemIds: ['kee-puchhde-o-haal'],
    citationIds: ['SHARMA-1979-SOLITARY', 'GARGI-1979-SURME'],
    keyQuote: {
      text: 'When borders were sliced through our fields, a part of our living flesh was left behind on the other side of the river.',
      source: 'Conversations with Balwant Gargi'
    }
  },
  {
    id: 'tl-1953-bohemianism',
    year: 1953,
    period: '1953 – 1957',
    title: 'Refusal of Conformity: The Wandering Rebel',
    category: 'personal',
    location: 'Batala, Nabha, Chandigarh',
    summary: 'Failed his F.Sc examinations and abandoned engineering and patwari school, refusing to enter a predictable bureaucratic career.',
    deepNarrative: 'His father, deeply practical and anxious for family honor, pressured Shiv to become a village revenue clerk (patwari). Shiv detested land deeds and ledgers. He spent nights sleeping under banyan trees, frequenting teahouses, and writing verses on loose scraps and cigarette packs, earning the family reputation of a wayward failure.',
    impactOnPoetry: 'Gave rise to his self-identification as a "faqir" and a wandering mendicant outside the bounds of polite middle-class society.',
    relatedPoemIds: ['kee-puchhde-o-haal'],
    citationIds: ['GARGI-1979-SURME', 'SHARMA-1979-SOLITARY'],
    keyQuote: {
      text: 'I cannot measure land in kanals and marlas when the sky itself has no boundary.',
      source: 'Letter to a friend'
    }
  },
  {
    id: 'tl-1960-piran-da-paraga',
    year: 1960,
    period: '1960',
    title: 'Publication of "Piran da Paraga": The Phenomenon Begins',
    category: 'literary',
    location: 'Batala / Amritsar',
    summary: 'Publishes his first poetry anthology, "Piran da Paraga" (A Handful of Sorrows), taking the Punjabi literary world by storm.',
    deepNarrative: 'At age 24, Shiv performed at the All India Baisakhi Kavi Darbar in Jalandhar. When he began reciting his verses in his distinctive, piercing musical chant (tarannum), legendary poets like Mohan Singh and Amrita Pritam were spellbound. Overnight, a penniless young man from Batala became the voice of Punjabi youth.',
    impactOnPoetry: 'Established the iconic motif of grief roasted in the kiln of time, blending folk melody with modern pathos.',
    relatedPoemIds: ['bhatthi-waliye', 'kee-puchhde-o-haal'],
    citationIds: ['AMRITA-1974-NAGMANI', 'LAHORE-BOOKSHOP-1974'],
    keyQuote: {
      text: 'Shiv did not merely recite; he sang with the voice of a wounded nightingale bleeding upon a thorn.',
      source: 'Amrita Pritam in "Nagmani"'
    }
  },
  {
    id: 'tl-1964-birha-tu-sultan',
    year: 1964,
    period: '1964',
    title: '"Birha tu Sultan" & The Clashes with Leftist Critics',
    category: 'controversy',
    location: 'Chandigarh / Indian Coffee House',
    summary: 'Releases "Birha tu Sultan". As youth idolize him, the Marxist Progressive Writers’ Movement launches an offensive against his "defeatist escapism".',
    deepNarrative: 'In Chandigarh’s Sector 17 Indian Coffee House, ideological battles raged. Marxist critics like Kishan Singh and followers of Sant Singh Sekhon condemned his songs of death and sorrow as "bourgeois indulgence" and "poison for the youth." Shiv defiantly answered that human suffering transcends political party manifestos.',
    impactOnPoetry: 'Shiv hardened his resolve, penning "Asan Taan Joban Rutte Marna" and "Main Ek Shikra Yaar Banaya" as badges of unbending defiance.',
    relatedPoemIds: ['shikra-yaar', 'joban-rutte-marna', 'ikk-kudi', 'maye-ni-maye'],
    citationIds: ['SEKHON-1972-PUNJABI-KAVI', 'PAASH-1973-SIARH', 'KISHAN-SINGH-1971'],
    keyQuote: {
      text: 'They want me to write about the redness of the flag; I can only write about the redness of the wound.',
      source: 'Shiv Kumar Batalvi to contemporaries'
    }
  },
  {
    id: 'tl-1965-loona',
    year: 1965,
    period: '1965',
    title: 'The Masterpiece: "Loona" Subverts 1,000 Years of Patriarchy',
    category: 'literary',
    location: 'Chandigarh',
    summary: 'Publishes his magnum opus, the epic verse play "Loona", rewriting the sacred legend of Puran Bhagat from the stepmother’s perspective.',
    deepNarrative: 'Shiv committed what traditionalists considered cultural heresy: he took Loona, the reviled symbol of lust and deceit, and revealed her as an exploited, low-caste young girl forced into marriage with an old king. Loona became Punjab’s first truly modern, radical feminist heroine, sparking both immense acclaim and moral outrage.',
    impactOnPoetry: 'Elevated Shiv from a lyric balladist to a titan of blank verse drama and philosophical courage.',
    relatedPoemIds: ['loona-act4'],
    citationIds: ['QADIR-YAR-1840', 'SAHITYA-1967-LOONA'],
    keyQuote: {
      text: 'If an old king buys a girl with gold, the world calls it holy marriage; if that girl desires love, the world calls her a harlot.',
      source: 'Shiv Kumar Batalvi, Preface to "Loona"'
    }
  },
  {
    id: 'tl-1967-sahitya-akademi',
    year: 1967,
    period: '1967',
    title: 'Sahitya Akademi Award at 31: Envy & Marital Anchor',
    category: 'controversy',
    location: 'New Delhi / Gurdaspur',
    summary: 'Becomes the youngest ever recipient of the Sahitya Akademi Award for "Loona", igniting literary jealousy. Marries Aruna.',
    deepNarrative: 'Winning India’s highest literary honor at age 31 stunned the literary establishment. Older academics and party-affiliated writers were infuriated that this "drunken bohemian" had outpaced them. In the same year, he married Aruna in Gurdaspur, who attempted to bring order to his increasingly chaotic lifestyle.',
    impactOnPoetry: 'Struggled between the demands of bourgeois domesticity, his job at the State Bank of India in Chandigarh, and his untameable artistic daemon.',
    relatedPoemIds: ['loona-act4'],
    citationIds: ['SAHITYA-1967-LOONA', 'GARGI-1979-SURME'],
    keyQuote: {
      text: 'At 31, he held the highest crown of Indian literature, yet inside, he felt more alone than ever.',
      source: 'Balwant Gargi, "Surme Wali Akh"'
    }
  },
  {
    id: 'tl-1970-main-te-main',
    year: 1970,
    period: '1970',
    title: 'Modern Alienation: "Main te Main" and the Naxalite Surge',
    category: 'literary',
    location: 'Chandigarh',
    summary: 'Publishes "Main te Main" as the Naxalite movement grips Punjab; dialogue and tension with radical poets like Paash intensify.',
    deepNarrative: 'While Naxalite poets like Paash, Lal Singh Dil, and Sant Ram Udasi wrote poetry of armed peasant insurrection, Shiv retreated into the fractures of the modern urban psyche. In "Main te Main", he exposed the neurosis of modern Chandigarh—a city of clean concrete lines masking hollow, divided souls.',
    impactOnPoetry: 'Broke away from folk rhyme into fractured, psychoanalytic free verse depicting self-loathing and social alienation.',
    relatedPoemIds: ['main-te-main'],
    citationIds: ['PAASH-1973-SIARH', 'SEKHON-1972-PUNJABI-KAVI'],
    keyQuote: {
      text: 'Shiv was torn between two worlds: the village that had vanished and the city that had no soul.',
      source: 'Dr. Attar Singh, Critical Essays'
    }
  },
  {
    id: 'tl-1972-london-tour',
    year: 1972,
    period: 'May – September 1972',
    title: 'The UK Exile: Adulation, Alienation, and Physical Decline',
    category: 'personal',
    location: 'London, Birmingham, UK',
    summary: 'Travels to England on the invitation of the Punjabi diaspora. Adored by fans, but overwhelmed by loneliness and alcohol.',
    deepNarrative: 'In Britain, Shiv was mobbed like a rockstar at Heathrow and Southall. Yet away from Punjab’s soil, he felt profoundly alienated in the damp, grey industrial climate. He was hosted at endless parties where liquor flowed without pause. During this trip, he gave his historic, sole surviving BBC interview with Mahendra Kaul, looking thin, luminous, and haunted.',
    impactOnPoetry: 'Wrote somber reflections on the commercialization of his grief and the cold loneliness of the immigrant experience.',
    relatedPoemIds: ['aarti', 'kee-puchhde-o-haal'],
    citationIds: ['BBC-1972-KAUL', 'BRITISH-LIBRARY-1972'],
    keyQuote: {
      text: 'A poet is not a contractor for a political manifesto. Pain has its own dignity; it does not need a political slogan to justify its tears.',
      source: 'BBC Interview with Mahendra Kaul, London 1972'
    }
  },
  {
    id: 'tl-1973-death',
    year: 1973,
    period: 'May 6–7, 1973',
    title: 'The Prophecy Fulfilled: Death at 36 in Kir Mangyal',
    category: 'personal',
    location: 'Kir Mangyal, Pathankot, Punjab',
    summary: 'Collapses from advanced liver cirrhosis and exhaustion, passing away in his in-laws’ village at age 36.',
    deepNarrative: 'After returning from England emaciated and critically ill, Shiv was admitted to hospitals in Chandigarh and Amritsar. Sensed his approaching end, he asked to be taken to his wife’s maternal village of Kir Mangyal near Pathankot. In the early morning hours of May 7, 1973, the Sultan of Birha passed into legend at the age of 36, exactly as he had prophesied a decade earlier.',
    impactOnPoetry: 'Crystallized his status as Punjab’s immortal martyr of passion, beauty, and authentic grief.',
    relatedPoemIds: ['joban-rutte-marna', 'shikra-yaar'],
    citationIds: ['CIVIL-HOSPITAL-1973', 'AMRITA-1974-NAGMANI', 'BATALVI-ARUNA-1988'],
    keyQuote: {
      text: 'Asan taan joban rutte marna... (We shall die in the springtime of our years).',
      source: 'His eternal epitaph'
    }
  },
  {
    id: 'tl-posthumous-loss',
    year: 1974,
    period: '1973 – Present',
    title: 'The Lost Archives: Discarded Papers, Wiped Tapes & Immortality',
    category: 'controversy',
    location: 'Chandigarh, Jalandhar, Global Diaspora',
    summary: 'Rooms cleared out, loose manuscripts lost, and Akashvani/Doordarshan tapes erased; yet his songs achieve global immortality.',
    deepNarrative: 'In the aftermath of his death, controversies arose over his estate. Boxes of papers left in rented accommodations were discarded. Institutional neglect at state broadcasters led to tape overwriting. Yet through legendary singers—Nusrat Fateh Ali Khan, Jagjit Singh, Hans Raj Hans, and modern cinema—his poetry became an unshakeable bedrock of Punjabi identity.',
    impactOnPoetry: 'Transcendence: Shiv lives not in institutional archives, but on the lips of millions across borders and generations.',
    relatedPoemIds: ['shikra-yaar', 'ikk-kudi', 'loona-act4'],
    citationIds: ['BATALVI-ARUNA-1988', 'AIR-ARCHIVES-JALANDHAR', 'GARGI-1979-SURME'],
    keyQuote: {
      text: 'Shiv cannot be erased by wiping a tape; he is written into the Punjabi language itself.',
      source: 'Gurbhajan Gill, Punjabi Sahit Akademi'
    }
  }
];
