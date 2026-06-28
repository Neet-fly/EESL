import re

with open('d:\\hompage\\pi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Work Experience
html = html.replace(
    '<h3 class="history-title">Work Experience</h3>',
    '<div class="history-block work-experience">\n                            <h3 class="history-title">Work Experience</h3>'
)
# We need to close the div after the first timeline ul.
# The first ul ends before <h3 class="history-title mt-4">Research Area</h3>
html = html.replace(
    '</ul>\n                        \n                        <h3 class="history-title mt-4">Research Area</h3>',
    '</ul>\n                        </div>\n                        \n                        <div class="history-block research-area">\n                            <h3 class="history-title mt-4">Research Area</h3>'
)
# Close Research Area div before <!-- Right Column -->
html = html.replace(
    '</ul>\n                    </div>\n                    \n                    <!-- Right Column -->',
    '</ul>\n                        </div>\n                    </div>\n                    \n                    <!-- Right Column -->'
)

# Education div
html = html.replace(
    '<h3 class="history-title">Education</h3>',
    '<div class="history-block education">\n                            <h3 class="history-title">Education</h3>'
)

# Close Education div before </div> </div>
html = html.replace(
    '</ul>\n                    </div>\n                </div>',
    '</ul>\n                        </div>\n                    </div>\n                </div>'
)

with open('d:\\hompage\\pi.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("pi.html updated")

with open('d:\\hompage\\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
@media (max-width: 768px) {
    .history-col {
        display: contents;
    }
    .history-grid {
        display: flex;
        flex-direction: column;
    }
    .history-block.work-experience {
        order: 1;
    }
    .history-block.education {
        order: 2;
    }
    .history-block.research-area {
        order: 3;
    }
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("style.css updated")
