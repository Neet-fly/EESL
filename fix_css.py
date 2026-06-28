with open('d:\\hompage\\style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We need to drop lines 1002 and 1003 since they are:
# 1002: }
# 1003: \n
lines = lines[:1001]

css = """

/* --- New Logo Container Styles --- */
.logo-container {
    display: flex;
    align-items: center;
    gap: 15px;
    text-decoration: none;
}
.header-logo-img {
    height: 52px; 
    width: auto;
}
.logo-text-group {
    display: flex;
    flex-direction: column;
    justify-content: center;
    line-height: 1.25;
}
.logo-main-text {
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--primary-color, #003399);
    letter-spacing: 0.5px;
}
.logo-sub-text {
    font-size: 0.85rem;
    font-weight: 500;
    color: #444444;
    white-space: nowrap; 
    line-height: 1.25;
}

@media (max-width: 768px) {
    .logo-sub-text {
        display: none;
    }
}
"""

with open('d:\\hompage\\style.css', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    f.write(css)
