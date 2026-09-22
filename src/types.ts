export type ScriptMode = 'gurmukhi' | 'shahmukhi' | 'roman' | 'english' | 'bilingual';

export interface PoemStanza {
  gurmukhi: string;
  shahmukhi: string;
  roman: string;
  english: string;
  commentary?: string;
}

export interface GlossaryItem {
  term: string;
  pronunciation: string;
  literal: string;
  culturalMeaning: string;
}

export type LandscapeBiome = 
  | 'grassy_hills_sunrise' 
  | 'snowy_cabin_night' 
  | 'river_chenab_mist' 
  | 'cremation_dusk' 
  | 'barren_mountain_loona'
  | 'tavern_midnight'
  | 'village_monsoon'
  | 'ancestral_village'
  | 'barren_dune'
  | 'abandoned_haveli';

export interface Citation {
  id: string;
  author: string;
  sourceTitle: string;
  publicationYear: number;
  publisher?: string;
  pageOrTimestamp?: string;
  contextExcerpt: string;
  archiveType: 'Primary Memoir' | 'Archival Broadcast' | 'Literary Criticism' | 'Institutional Record' | 'Newspaper/Periodical';
  url?: string;
}

export interface Poem {
  id: string;
  titleGurmukhi: string;
  titleShahmukhi: string;
  titleRoman: string;
  titleEnglish: string;
  book: string;
  year: number;
  tags: string[];
  philosophyTheme: 'birha' | 'mortality' | 'feminism' | 'folklore' | 'modernism' | 'rebellion' | 'solitude';
  landscapeBiome?: LandscapeBiome;
  sketchPrompt?: string;
  historicalFact?: {
    claim: string;
    citationId: string;
  };
  summary: string;
  backstory: string;
  critiqueContext?: string;
  tarannumNote?: string;
  stanzas: PoemStanza[];
  culturalGlossary: GlossaryItem[];
  relatedPoemIds?: string[];
  citationIds?: string[];
}

export interface TimelineEvent {
  id: string;
  year: number;
  period: string;
  title: string;
  category: 'personal' | 'literary' | 'political_context' | 'controversy';
  location: string;
  summary: string;
  deepNarrative: string;
  impactOnPoetry: string;
  relatedPoemIds: string[];
  citationIds?: string[];
  keyQuote?: {
    text: string;
    source: string;
  };
}

export interface EssaySection {
  id: string;
  heading: string;
  subheading?: string;
  paragraphs: string[];
  citationIds?: string[];
  callout?: {
    type: 'quote' | 'alert' | 'historical_fact';
    content: string;
    attribution?: string;
    citationId?: string;
  };
}

export interface EssayChapter {
  id: string;
  number: string;
  title: string;
  subtitle: string;
  coverLabel: string;
  readTime: string;
  sections: EssaySection[];
}

export interface ArchiveInvestigation {
  id: string;
  title: string;
  theMyth: string;
  theReality: string;
  evidence: string[];
  citationIds?: string[];
  verdict: 'Confirmed Myth' | 'Institutional Neglect' | 'Documented Loss' | 'Ideological Boycott';
  historicalDetails: string;
}

export interface LoonaActAnalysis {
  act: number;
  title: string;
  classicalMyth: string;
  shivSubversion: string;
  philosophicalConflict: string;
  citationIds?: string[];
  keyDialogue: {
    speaker: string;
    gurmukhi: string;
    shahmukhi: string;
    roman: string;
    english: string;
    exegesis: string;
  }[];
}
