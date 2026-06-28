css = """

/* --- Contact Card Styles --- */
.contact-card {
  max-width: 520px;
  padding: 36px 42px;
  background: #1f4da8;
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 12px;
  color: #ffffff;
  margin: 0 auto;
}
.contact-card h2 {
  margin: 0;
  color: #ffc928;
  font-size: 25px;
  line-height: 1.25;
  font-weight: 800;
}
.contact-card .abbr {
  margin: 4px 0 26px;
  color: #ffc928;
  font-size: 22px;
  font-weight: 700;
}
.contact-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.contact-row {
  display: grid;
  grid-template-columns: 110px 1fr;
  column-gap: 18px;
  align-items: start;
}
.contact-row .label {
  color: #c9dcff;
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.contact-row .value {
  color: #ffffff;
  font-size: 16px;
  line-height: 1.55;
  font-weight: 500;
}
.contact-row a {
  color: #ffc928;
  font-weight: 700;
  text-decoration: none;
}
.contact-row a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .contact-card {
    padding: 24px 28px;
  }
  .contact-row {
    grid-template-columns: 1fr;
    gap: 4px;
  }
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Contact card CSS appended successfully.")
