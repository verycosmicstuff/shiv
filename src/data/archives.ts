import { ArchiveInvestigation } from '../types';

export const archiveInvestigations: ArchiveInvestigation[] = [
  {
    id: 'inv-burned-diaries',
    title: 'The Burned Diaries & Lost Manuscripts: Ideological Plot or Tragic Neglect?',
    verdict: 'Documented Loss',
    citationIds: ['GARGI-1979-SURME', 'AMRITA-1974-NAGMANI', 'BATALVI-ARUNA-1988'],
    theMyth: 'In popular culture, online articles (e.g. TFIPost), and viral social media threads, it is frequently claimed that organized leftist cliques, enraged by Shiv’s popularity, raided his quarters and burnt his private diaries and unpublished poetry to cleanse his "bourgeois" influence from Punjab.',
    theReality: 'While no formal, organized book-burning by political decree occurred, massive amounts of Shiv’s unpublished writing were genuinely incinerated, lost, or discarded in the chaotic months following his death.',
    evidence: [
      'Contemporaries Balwant Gargi (in "Surme Wali Akh") and Amrita Pritam document that Shiv had no archival discipline; he routinely penned masterpiece stanzas on the foil backs of Scissors and Gold Flake cigarette packets, tea stall napkins, and deposit chits at the State Bank of India in Chandigarh.',
      'Dozens of acquaintances, drinking companions, and bar patrons walked away with original handwritten poems that were never cataloged.',
      'Following his collapse and death in 1973 in Kir Mangyal, rented rooms where he had stayed in Batala and Chandigarh were cleared out by landlords and uncomprehending relatives. Crates of loose papers, draft notebooks, and letters were discarded and burned as waste scrap.',
      'The literary establishment did not need to light matches—they practiced intellectual ostracization by refusing to publish, archive, or critically engage with his late notebooks in state-funded academies.'
    ],
    historicalDetails: 'The tragedy is not that an armed mob burnt his diaries in the town square, but that the society that adored his voice treated his living documents with heartbreaking carelessness until it was too late.'
  },
  {
    id: 'inv-erased-tapes',
    title: 'The Wiped Audio & Video Reels of Akashvani (AIR) and Doordarshan',
    verdict: 'Institutional Neglect',
    citationIds: ['AIR-ARCHIVES-JALANDHAR', 'BBC-1972-KAUL'],
    theMyth: 'Leftist cultural officers at All India Radio (Akashvani Jalandhar) and Doordarshan deliberately deleted, de-magnetized, and destroyed all master tapes of Shiv Kumar Batalvi’s recitations to erase his memory from the state airwaves.',
    theReality: 'A systemic institutional catastrophe: Doordarshan and All India Radio suffered from catastrophic resource constraints and systematically erased thousands of hours of historical cultural programming by reusing 2-inch quadruplex videotapes and magnetic audio spools for daily bulletins.',
    evidence: [
      'In the 1960s and 1970s, magnetic recording tape had to be imported with scarce foreign exchange. Standard operating procedure in Indian state broadcasting was to overwrite existing reels with daily news, agricultural broadcasts, and ministerial speeches.',
      'Shiv was not the only victim: master broadcast recordings of Ustad Bade Ghulam Ali Khan, Begum Akhtar, and dozens of historic theatrical productions were wiped clean in the same administrative routine.',
      'However, there was an ideological bias in what was preserved: state academies and cultural boards dominated by progressive intellectuals made deliberate efforts to preserve political symposia and progressive seminars while showing complete indifference to preserving the all-night mushaira performances of romantic and folk poets.',
      'Consequently, decades of Shiv’s mesmerizing "tarannum" recitations in Jalandhar, Delhi, and Chandigarh vanished forever into silence.'
    ],
    historicalDetails: 'Bureaucratic philistinism, coupled with ideological disdain from cultural gatekeepers, accomplished the exact same result as active censorship: the near-total erasure of an audio-visual record of India’s most charismatic modern poet.'
  },
  {
    id: 'inv-surviving-bbc',
    title: 'The Sole Surviving Visual Artifact: The 1972 BBC London Interview',
    verdict: 'Institutional Neglect',
    citationIds: ['BBC-1972-KAUL', 'BRITISH-LIBRARY-1972'],
    theMyth: 'Shiv Kumar Batalvi left behind no moving footage or live interviews before his untimely death at 36.',
    theReality: 'A single, priceless visual document survived: the May 1972 BBC television interview conducted in London by legendary broadcaster Mahendra Kaul.',
    evidence: [
      'Recorded during Shiv’s first and only tour of England in May 1972, hosted by the diaspora community.',
      'In the interview, a visibly frail, luminous Shiv discusses his philosophy of suffering, his contempt for political slogans in poetry, and his loneliness in London.',
      'He performs a legendary recitation of "Kee Puchhde O Haal Fakiran Da" in his authentic, unadorned speaking voice, offering the only high-fidelity visual and vocal record of his living presence.',
      'Preserved in the BBC World Service archives in London, it was later digitized and released by BBC News Punjabi, becoming the definitive audiovisual monument of his life.'
    ],
    historicalDetails: 'It is a tragic irony of modern Punjabi history that the only surviving television record of Punjab’s greatest 20th-century poet was preserved not in Chandigarh, Jalandhar, or Delhi, but in the archives of a British public broadcaster.'
  },
  {
    id: 'inv-rescued-verses',
    title: 'Posthumous Recovery: The Battle for His Estate & "Chup Di Awaaz"',
    verdict: 'Documented Loss',
    citationIds: ['BATALVI-ARUNA-1988', 'LAHORE-BOOKSHOP-1974'],
    theMyth: 'All of Shiv’s posthumous work was lost forever.',
    theReality: 'Through the dedicated stewardship of his widow Aruna Batalvi and their son Meharban, surviving fragments, uncollected nazms, and personal letters were painstakingly gathered and published decades after his death.',
    evidence: [
      'Aruna Batalvi spent decades fielding inquiries, fighting unauthorized pirated editions, and gathering handwritten sheets from friends and collectors across Punjab.',
      'Posthumous volumes including "Alvida" (Farewell, 1974) and later "Chup Di Awaaz" (The Voice of Silence) brought previously uncollected and unfinished works to the public.',
      'Independent scholars and admirers in Pakistan (West Punjab) also played a vital role, transcribing his works into Shahmukhi and keeping his flame alive across the Radcliffe Line.'
    ],
    historicalDetails: 'His legacy was saved not by institutions or academies, but by family devotion and the stubborn love of ordinary Punjabi readers across the world.'
  }
];
