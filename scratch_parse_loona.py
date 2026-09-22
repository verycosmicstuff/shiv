# -*- coding: utf-8 -*-
import urllib.request
import re
import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.punjabi-kavita.com/LoonaShivKumarBatalvi.php'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# The main content is inside <div class="list">
# Acts are demarcated by <h1>ਲੂਣਾ : [ਅੰਕ]</h1>
splits = re.split(r'<h1>\s*ਲੂਣਾ\s*:\s*', html)
print(f"Total splits found: {len(splits)}")

acts_data = []

act_names_english = [
    "Act I: Dhanwanti te Uhde Paharan de Naa (The Mountains of Chamba)",
    "Act II: Baroo di Haveli (Baroo's Courtyard & Loona's Youth)",
    "Act III: Sialkot da Mehal (Salwan's Return & The Wedding)",
    "Act IV: Loona da Virlaap (Loona's Soliloquy - The Cry of Living Flesh)",
    "Act V: Puran te Loona da Takraar (The Confrontation & Refusal)",
    "Act VI: Ichhran da Shraap (Mother Ichhran & The Broken Crown)",
    "Act VII: Puran nu Dand (The Severing of Hands in the Well)",
    "Act VIII: Loona di Aakhri Cheek (The Epilogue - The Curse of Sialkot)"
]

for idx in range(1, len(splits)):
    chunk = splits[idx]
    # Header is before </h1>
    header_part, body_part = chunk.split('</h1>', 1)
    act_title_gurmukhi = header_part.strip()
    
    # Clean up tail if this is the last act (remove footer, scripts, etc.)
    if idx == len(splits) - 1:
        # Find closing divs or footer
        footer_pos = body_part.find('</div></div>')
        if footer_pos != -1:
            body_part = body_part[:footer_pos]
        footer_pos2 = body_part.find('<footer>')
        if footer_pos2 != -1:
            body_part = body_part[:footer_pos2]

    # Convert HTML to clean markdown formatting
    # Speaker headers: <h3 align=left>Speaker</h3> or <h3 ...>
    # Paragraphs: <p> ... <br/>
    
    # Process tokens
    # Replace <h3[^>]*>(.*?)</h3> with ### \1\n\n
    def h3_repl(m):
        content = m.group(1).strip()
        return f"\n\n### 🎭 {content}\n\n"
    
    clean_body = re.sub(r'<h3[^>]*>(.*?)</h3>', h3_repl, body_part, flags=re.DOTALL | re.IGNORECASE)
    
    # Replace <p> with empty or newline
    clean_body = re.sub(r'<p[^>]*>', '\n', clean_body, flags=re.IGNORECASE)
    clean_body = re.sub(r'</p>', '\n', clean_body, flags=re.IGNORECASE)
    
    # Replace <br\s*/?> with newline
    clean_body = re.sub(r'<br\s*/?>', '\n', clean_body, flags=re.IGNORECASE)
    
    # Remove remaining HTML tags
    clean_body = re.sub(r'<[^>]+>', '', clean_body)
    
    # Clean up lines
    lines = clean_body.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        cleaned_lines.append(stripped)
    
    # Join into coherent text
    formatted_text = '\n'.join(cleaned_lines)
    # Deduplicate excessive empty lines
    formatted_text = re.sub(r'\n{3,}', '\n\n', formatted_text).strip()
    
    eng_name = act_names_english[idx - 1] if idx - 1 < len(act_names_english) else f"Act {idx}"
    
    act_obj = {
        "actNumber": idx,
        "titleGurmukhi": f"ਲੂਣਾ : {act_title_gurmukhi}",
        "titleEnglish": eng_name,
        "rawLineCount": len([l for l in formatted_text.split('\n') if l.strip() and not l.startswith('#')]),
        "fullText": formatted_text
    }
    acts_data.append(act_obj)
    print(f"Parsed Act {idx}: {act_obj['titleGurmukhi']} ({act_obj['rawLineCount']} lines)")

print(f"\nAll {len(acts_data)} acts parsed successfully!")
total_lines = sum(a['rawLineCount'] for a in acts_data)
print(f"Total verse lines in complete play: {total_lines}")

# Save JSON for programmatic access
os.makedirs("books/07_loona_1965", exist_ok=True)
with open("books/07_loona_1965/LOONA_UNABRIDGED_PARSED.json", "w", encoding="utf-8") as f:
    json.dump(acts_data, f, ensure_ascii=False, indent=2)

print("Saved books/07_loona_1965/LOONA_UNABRIDGED_PARSED.json")
