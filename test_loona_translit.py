# -*- coding: utf-8 -*-
"""
build_loona_verbatim_extended.py
Builds authentic, verbatim 8-act Loona data module (data_book7_loona_extended.py)
in strict chronological order (Act 1 -> Act 8) with complete character speeches,
accurate Gurmukhi, Shahmukhi, Romanization, and poetic English translations.
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Helper functions for Gurmukhi to Shahmukhi and Roman transliteration

G2S_MAP = {
    'ੳ': 'او', 'ਉ': 'او', 'ਊ': 'او',
    'ਅ': 'ا', 'ਆ': 'آ', 'ਇ': 'ای', 'ਈ': 'ای',
    'ਏ': 'اے', 'ਐ': 'اے', 'ਓ': 'او', 'ਔ': 'او',
    'ੲ': 'ای',
    'ਕ': 'ک', 'ਖ': 'کھ', 'ਗ': 'گ', 'ਘ': 'گھ', 'ਙ': 'ن',
    'ਚ': 'چ', 'ਛ': 'چھ', 'ਜ': 'ج', 'ਝ': 'جھ', 'ਞ': 'ن',
    'ਟ': 'ٹ', 'ਠ': 'ٹھ', 'ਡ': 'ڈ', 'ਢ': 'ڈھ', 'ਣ': 'ݨ',
    'ਤ': 'ت', 'ਥ': 'تھ', 'ਦ': 'د', 'ਧ': 'دھ', 'ਨ': 'ن',
    'ਪ': 'پ', 'ਫ': 'پھ', 'ਬ': 'ب', 'ਭ': 'بھ', 'ਮ': 'م',
    'ਯ': 'ی', 'ਰ': 'ر', 'ਲ': 'ل', 'ਵ': 'و', 'ੜ': 'ڑ',
    'ਸ਼': 'ش', 'ਜ਼': 'ز', 'ਖ਼': 'خ', 'ਗ਼': 'غ', 'ਫ਼': 'ف', 'ਲ਼': 'ل',
    'ਾ': 'ا', 'ਿ': '', 'ੀ': 'ی', 'ੁ': '', 'ੂ': 'و',
    'ੇ': 'ے', 'ੈ': 'ے', 'ੋ': 'و', 'ੌ': 'و',
    'ਂ': 'ں', 'ੰ': 'ن', 'ੱ': '', '੍': '',
    '।': '۔', ',': '،', '?': '؟'
}

G2R_MAP = {
    'ੳ': 'u', 'ਉ': 'u', 'ਊ': 'oo',
    'ਅ': 'a', 'ਆ': 'aa', 'ਇ': 'i', 'ਈ': 'ee',
    'ਏ': 'e', 'ਐ': 'ai', 'ਓ': 'o', 'ਔ': 'au',
    'ੲ': 'i',
    'ਕ': 'k', 'ਖ': 'kh', 'ਗ': 'g', 'ਘ': 'gh', 'ਙ': 'ng',
    'ਚ': 'ch', 'ਛ': 'chh', 'ਜ': 'j', 'ਝ': 'jh', 'ਞ': 'ny',
    'ਟ': 't', 'ਠ': 'th', 'ਡ': 'd', 'ਢ': 'dh', 'ਣ': 'n',
    'ਤ': 't', 'ਥ': 'th', 'ਦ': 'd', 'ਧ': 'dh', 'ਨ': 'n',
    'ਪ': 'p', 'ਫ': 'ph', 'ਬ': 'b', 'ਭ': 'bh', 'ਮ': 'm',
    'ਯ': 'y', 'ਰ': 'r', 'ਲ': 'l', 'ਵ': 'v', 'ੜ': 'rh',
    'ਸ਼': 'sh', 'ਜ਼': 'z', 'ਖ਼': 'kh', 'ਗ਼': 'gh', 'ਫ਼': 'f', 'ਲ਼': 'l',
    'ਾ': 'aa', 'ਿ': 'i', 'ੀ': 'ee', 'ੁ': 'u', 'ੂ': 'oo',
    'ੇ': 'e', 'ੈ': 'ai', 'ੋ': 'o', 'ੌ': 'au',
    'ਂ': 'n', 'ੰ': 'n', 'ੱ': '', '੍': '',
    '।': '.', ',': ',', '?': '?'
}

def gurmukhi_to_shahmukhi(text):
    # Word replacements for common Punjabi literary terms
    word_dict = {
        "ਲੂਣਾ": "لونا", "ਪੂਰਨ": "پورن", "ਸਲਵਾਨ": "سلوان", "ਇੱਛਰਾਂ": "اچھراں",
        "ਨਟੀ": "نٹی", "ਸੂਤਰਧਾਰ": "سوتردھار", "ਵਰਮਨ": "ورمن", "ਬਾਰੂ": "بارو",
        "ਈਰਾ": "ارا", "ਇਰਾ": "ارا", "ਗੋਲੀ": "گولی", "ਚੌਧਲ": "چودھل",
        "ਜੱਲਾਦ": "جلاد", "ਚੰਬਾ": "چمبا", "ਸਿਆਲਕੋਟ": "سیالکوٹ", "ਮਹਿਲ": "محل",
        "ਅੱਗ": "اگ", "ਲਹੂ": "لہو", "ਧਰਤ": "دھرتی", "ਸੂਰਜ": "سورج", "ਚੰਨ": "چن",
        "ਦਰਿਆ": "دریا", "ਪਾਣੀ": "پانی", "ਹਵਾ": "ہوا", "ਰਾਤ": "رات", "ਦਿਨ": "دن",
        "ਮੌਤ": "موت", "ਜੀਵਨ": "جیون", "ਜ਼ਿੰਦਗੀ": "زندگی", "ਦਰਦ": "درد", "ਦੁੱਖ": "دکھ",
        "ਬਿਰਹਾ": "برہا", "ਗੀਤ": "گیت", "ਪੰਛੀ": "پنچھی", "ਫੁੱਲ": "پھل", "ਰੁੱਖ": "رکھ",
        "ਬਾਬਲ": "بابل", "ਮਾਂ": "ماں", "ਧੀ": "دھی", "ਪੁੱਤਰ": "پتر", "ਪਿਓ": "پیو",
        "ਰਾਜਾ": "راجا", "ਰਾਣੀ": "رانی", "ਰੂਪ": "روپ", "ਜਵਾਨੀ": "جوانی", "ਸੁਪਨਾ": "سپنا",
        "ਸੱਚ": "سچ", "ਝੂਠ": "جھوٹ", "ਕਬਰ": "قبر", "ਸਿਵੇ": "سوے", "ਚਿਖਾ": "چکھا",
        "ਕੰਧ": "کندھ", "ਬੂਹਾ": "بوہا", "ਵੇਹੜਾ": "ویہڑا", "ਸ਼ਹਿਰ": "شہر", "ਪਿੰਡ": "پنڈ",
        "ਅੰਬਰ": "امبر", "ਤਾਰੇ": "تارے", "ਹੰਝੂ": "ہنجھو", "ਅੱਖੀਆਂ": "اکھیاں",
        "ਸੀਨਾ": "سینہ", "ਦਿਲ": "دل", "ਸਾਹ": "ساہ", "ਦੇਹ": "دیہہ", "ਜਿਸਮ": "جسم",
        "ਮੇਰੇ": "میرے", "ਤੇਰੇ": "تیرے", "ਸਾਡੇ": "ساڈے", "ਤੁਹਾਡੇ": "تہاڈੇ",
        "ਹੈ": "اے", "ਹਨ": "نے", "ਸੀ": "سی", "ਕੀ": "کی", "ਕਿਉਂ": "کیوں",
        "ਜੇ": "جے", "ਤਾਂ": "تاں", "ਪਰ": "پر", "ਨਾਲ਼": "نال", "ਵਿੱਚ": "وچ",
        "ਉੱਤੇ": "اتے", "ਕੋਲ਼": "کول", "ਬਾਝੋਂ": "باجھوں", "ਮੂਹਰੇ": "موہرے"
    }
    
    words = text.split()
    translated_words = []
    for w in words:
        # Strip punctuation
        clean_w = re.sub(r'[^\w\u0A00-\u0A7F]', '', w)
        if clean_w in word_dict:
            res = word_dict[clean_w]
            # re-attach punctuation
            if w.endswith(':'): res += ':'
            if w.endswith('।') or w.endswith('.'): res += '۔'
            if w.endswith(','): res += '،'
            if w.endswith('!'): res += '!'
            if w.endswith('?'): res += '؟'
            translated_words.append(res)
        else:
            # character by character mapping
            out = []
            for ch in w:
                out.append(G2S_MAP.get(ch, ch))
            translated_words.append(''.join(out))
    
    return ' '.join(translated_words)

def gurmukhi_to_roman(text):
    word_dict = {
        "ਲੂਣਾ": "Loona", "ਪੂਰਨ": "Puran", "ਸਲਵਾਨ": "Salwan", "ਇੱਛਰਾਂ": "Ichhran",
        "ਨਟੀ": "Nati", "ਸੂਤਰਧਾਰ": "Sutradhar", "ਵਰਮਨ": "Varman", "ਬਾਰੂ": "Baroo",
        "ਈਰਾ": "Ira", "ਇਰਾ": "Ira", "ਗੋਲੀ": "Goli", "ਚੌਧਲ": "Chaudhal",
        "ਜੱਲਾਦ": "Jallaad", "ਚੰਬਾ": "Chamba", "ਸਿਆਲਕੋਟ": "Sialkot", "ਮਹਿਲ": "Mehal",
        "ਅੱਗ": "Agg", "ਲਹੂ": "Lahu", "ਧਰਤ": "Dharat", "ਸੂਰਜ": "Suraj", "ਚੰਨ": "Chann",
        "ਦਰਿਆ": "Dariya", "ਪਾਣੀ": "Paani", "ਹਵਾ": "Havaa", "ਰਾਤ": "Raat", "ਦਿਨ": "Din",
        "ਮੌਤ": "Maut", "ਜੀਵਨ": "Jeevan", "ਜ਼ਿੰਦਗੀ": "Zindagi", "ਦਰਦ": "Dard", "ਦੁੱਖ": "Dukh",
        "ਬਿਰਹਾ": "Birha", "ਗੀਤ": "Geet", "ਪੰਛੀ": "Panchhi", "ਫੁੱਲ": "Phull", "ਰੁੱਖ": "Rukkh",
        "ਬਾਬਲ": "Babul", "ਮਾਂ": "Maan", "ਧੀ": "Dhee", "ਪੁੱਤਰ": "Puttar", "ਪਿਓ": "Peyo",
        "ਰਾਜਾ": "Raja", "ਰਾਣੀ": "Rani", "ਰੂਪ": "Roop", "ਜਵਾਨੀ": "Javaani", "ਸੁਪਨਾ": "Supna"
    }
    
    lines = text.split('\n')
    roman_lines = []
    for line in lines:
        words = line.split()
        r_words = []
        for w in words:
            clean_w = re.sub(r'[^\w\u0A00-\u0A7F]', '', w)
            if clean_w in word_dict:
                res = word_dict[clean_w]
                if w.endswith(':'): res += ':'
                if w.endswith(','): res += ','
                if w.endswith('!'): res += '!'
                if w.endswith('?'): res += '?'
                r_words.append(res)
            else:
                out = []
                for ch in w:
                    out.append(G2R_MAP.get(ch, ch))
                r_words.append(''.join(out))
        roman_lines.append(' '.join(r_words))
    return '\n'.join(roman_lines)

print("Transliteration engine ready.")
