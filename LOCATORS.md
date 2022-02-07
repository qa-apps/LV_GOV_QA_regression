# Latvija.gov.lv Locators Reference

## Header Section

### Logo
- `a[aria-label="Sākumlapa"]` - Main logo link

### Search
- `input[aria-label*="Meklēšanas ievadlauks"]` - Search input field
- `button:has-text("Meklēt rezultātus")` - Search button

### Language Switcher
- `a[aria-label="Pārslēgties uz angļu valodu"]` - Switch to English

### Accessibility
- `button:has-text("Teksta izmēra maiņa")` - Text size control
- `button:has-text("Vājredzīgo režīma maiņa")` - Vision impaired mode

### Login
- `a:has-text("Ienākt Mana Latvija.lv")` - Login link

## Main Navigation

### Menu Items
- `button:has-text("Pakalpojumi")` - Services menu
- `button:has-text("Ko darīt, ja...?")` - Life situations menu
- `button:has-text("Mana Latvija.lv")` - My Latvija menu
- `button:has-text("E-adrese")` - E-address menu
- `button:has-text("Par portālu")` - About portal menu

## Homepage Content

### Services Section (Visi pakalpojumi)
- `a:has-text("VSAA informācija un pakalpojumi")` - VSAA information
- `a:has-text("Dzīvesvietas deklarēšana vai norādīšana")` - Residence declaration
- `a:has-text("Slimības pabalsta piešķiršana (B lapa)")` - Sick leave benefit
- `a:has-text("Parakstu vākšana par tautas nobalsošanas un pašvaldību referenduma ierosināšanu")` - Petition signatures
- `a:has-text("Visi pakalpojumi")` - All services link

### Life Situations Section (Ko darīt, ja...?)
- `a:has-text("Bezdarbnieku pabalsts un darba meklēšana")` - Unemployment benefit
- `a:has-text("Gada ienākumu deklarācija")` - Annual income declaration
- `a:has-text("Bērna gaidīšana un piedzimšana")` - Child expectation and birth
- `a:has-text("Rīcība saslimšanas gadījumā")` - Actions in case of illness
- `a:has-text("Visas dzīves situācijas")` - All life situations link

### My Latvija Section (Mana Latvija.lv)
- `a:has-text("E-adreses pastkastīte")` - E-address mailbox
- `a:has-text("Sākt lietot e-adresi")` - Start using e-address
- `a:has-text("Manas darbības portālā")` - My activities on portal
- `a:has-text("Profila iestatījumi")` - Profile settings
- `a:has-text("Rakstīt e-adresē")` - Write in e-address

## Cookie Banner
- `button:has-text("Piekrist visam")` - Accept all cookies
- `button:has-text("Pārvaldīt")` - Manage cookies

## Footer Links
- `a:has-text("Apskatīt lapas karti")` - View site map
- `a:has-text("Kontakti un saziņa")` - Contacts
- `a:has-text("Par portālu")` - About portal
- `a:has-text("Piekļūstamības paziņojums")` - Accessibility statement
- `a:has-text("Atsauksme par Latvija.gov.lv")` - Feedback
- `a:has-text("Latvija.gov.lv mobilā lietotne")` - Mobile app
- `button:has-text("Mainīt sīkdatņu iestatījumus")` - Change cookie settings

## Social Media Links
- `a:has-text("Youtube")` - YouTube channel
- `a:has-text("Facebook")` - Facebook page
- `a:has-text("X")` - Twitter/X profile

## Best Practices

### Locator Selection Priority
1. Use `aria-label` attributes when available (most stable)
2. Use `role` attributes for semantic elements
3. Use visible text with `:has-text()` for links/buttons
4. Avoid generic selectors like `div`, `span` without context
5. Use `.first` when multiple elements might match

### Examples
```python
# Good - Specific and stable
page.locator('a[aria-label="Sākumlapa"]')

# Good - Semantic and text-based
page.locator('button:has-text("Pakalpojumi")')

# Avoid - Too generic
page.locator('a[href*="Home"]')  # Matches multiple elements

# Fix - Add .first or use more specific selector
page.locator('a[href*="Home"]').first
```


