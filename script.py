import yaml
import sys

def write_line(f, title, author, summary, link):
    line = ""
    line += "<details>\n"
    if len(sys.argv) > 1 and link is not None:
        line += "<summary>" + "[" + title + " - " + author + "](" + link + ")" + "</summary>\n"
    else:
        line += "<summary>" + title + " - " + author + "</summary>\n"
    line += "\t> " + summary + "\n"
    line += "</details>\n"
    line += "</br>\n"
    f.write(line)
    return

def check(item, section, subsection):
    return item.get("h2") == section and item.get("h3") == subsection

PHILOSOPHY = [
    "Kantian",
    "Ethics",
    "Legal and Political Philosophy",
    "Epistemology and Metaphysics"
]

LITERATURE = [
    "Poetry",
    "Novels"
]

HEADER_TWO = [
    {"Philosophy": PHILOSOPHY },
    {"Literature": LITERATURE }
]

with open("data.yml", 'r') as f:
    data = yaml.safe_load(f)
    
    f = open("output.md", "w")
    f.write("# Test\n")
    f.write("![](../_assets/books.jpg)\n")
    for section in HEADER_TWO:
        section_text = list(section.keys())[0]
        f.write("## " + section_text + "\n")
        for sub in section.get(section_text):
            f.write("### " + sub + "\n")
            for item in data.get("items"):
                if check(item, section_text, sub):
                    write_line(f, item.get("title"), item.get("author"),
                            item.get("summary"), item.get("link"))

        


