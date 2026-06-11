# -*- coding: utf-8 -*-
import os, sys, json as _json
sys.path.insert(0, os.path.dirname(__file__))
import partials as P

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6 9 17l-5-5"/></svg>'

def chk(t): return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6 9 17l-5-5"/></svg>%s' % t

def breadcrumb(label, img):  # img unused; home is ../index.html for sub pages
    return ('<nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a>'
            '<span>/</span>%s</nav>' % label)

def page_hero(label, h1, lead):
    return ('''      <section class="page-hero">
        <div class="container">
          %s
          <h1>%s</h1>
          <p class="lead">%s</p>
        </div>
      </section>''' % (breadcrumb(label, None), h1, lead))

def cta_band(contact="contact.html"):
    return '''      <section class="section section--dark">
        <div class="container cta-band reveal">
          <h2>Ready for stress-free accounting?</h2>
          <p>Tell us briefly about your business and your approximate monthly document volume. We will get back to you with a clear quote.</p>
          <div class="cta-actions">
            <a class="btn btn-primary btn-lg" href="%s">Book a consultation</a>
            <a class="btn btn-ghost btn-lg" href="tel:+359885738666">0885 738 666</a>
          </div>
        </div>
      </section>''' % contact

# =================== HOME ===================
def svc_card(img, title, text):
    return '''            <article class="card">
              <div class="card-figure"><img src="../img/services/%s.svg" alt="" loading="lazy" width="480" height="360" /></div>
              <h3>%s</h3>
              <p>%s</p>
              <a class="card-link link-arrow" href="pages/services.html">Learn more →</a>
            </article>''' % (img, title, text)

index_main = '''      <section class="hero">
        <div class="container hero-grid">
          <div class="hero-copy reveal">
            <p class="eyebrow">Plovdiv · since 2008</p>
            <h1>Calm accounting with <em>clear deadlines</em> and zero stress.</h1>
            <p class="lead">We handle your full bookkeeping, VAT, annual accounts and payroll — transparently, on time and in plain language. You grow the business; we cover your back.</p>
            <div class="hero-actions">
              <a class="btn btn-primary btn-lg" href="pages/contact.html">Book a free consultation</a>
              <a class="btn btn-ghost btn-lg" href="pages/services.html">See services</a>
            </div>
            <ul class="hero-trust">
              <li>§ Fixed deadlines and timely reminders</li>
              <li>§ A personal accountant who knows your business</li>
              <li>§ Free company registration with a contract</li>
            </ul>
          </div>
          <div class="hero-figure reveal">
            <div class="hero-portrait">
              <picture>
                <source type="image/webp" srcset="../img/team/georgi-640.webp 640w, ../img/team/georgi-840.webp 840w, ../img/team/georgi-1080.webp 1080w" sizes="(max-width: 960px) 420px, 460px" />
                <img src="../img/team/georgi.jpg" width="1080" height="1350" alt="Georgi — founder and manager of DIS 99" loading="eager" fetchpriority="high" />
              </picture>
            </div>
            <div class="hero-badge">
              <span class="num" data-count="50" data-suffix="+">50</span>
              <span class="lbl">active clients trust us</span>
            </div>
          </div>
        </div>
      </section>

      <section class="stats">
        <div class="container stats-grid" data-stagger>
          <div class="stat"><div class="stat-num"><span>2008</span></div><div class="stat-label">Founded</div></div>
          <div class="stat"><div class="stat-num"><span data-count="18">18</span><span class="suf">+</span></div><div class="stat-label">Years of experience</div></div>
          <div class="stat"><div class="stat-num"><span data-count="50">50</span><span class="suf">+</span></div><div class="stat-label">Active clients</div></div>
          <div class="stat"><div class="stat-num"><span data-count="100">100</span><span class="suf">%</span></div><div class="stat-label">Deadlines met</div></div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-head center reveal">
            <p class="eyebrow">Services</p>
            <h2>Everything for your accounting — in one place</h2>
            <p class="lead">From daily bookkeeping to annual closing and protection during audits.</p>
          </div>
          <div class="grid grid-3" data-stagger style="margin-top: 3rem;">
''' + "\n".join([
    svc_card('bookkeeping', "Bookkeeping", "Monthly bookkeeping, bank operations, cash and full reporting with no delays."),
    svc_card('vat', "VAT & VIES", "Preparing and filing VAT returns, ledgers and VIES — accurately and on time."),
    svc_card('annual', "Annual accounts", "Annual financial statements and tax returns with timely publication."),
    svc_card('payroll', "Payroll", "Employment contracts, payslips, social security and staff administration."),
    svc_card('defense', "Tax defense", "Advice and support during audits and inspections — calm and well prepared."),
    svc_card('registration', "Registration & start", "Company and VAT registration and start-up advice — free with a service contract."),
]) + '''
          </div>
          <div class="reveal" style="text-align:center; margin-top:3rem;">
            <a class="btn btn-primary btn-lg" href="pages/contact.html">Book a free consultation</a>
            <p style="margin:1rem 0 0; color:var(--muted); font-size:.95rem;">Not sure what you need? We will point you in the right direction, free of charge.</p>
          </div>
        </div>
      </section>

      <section class="section section--dark">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">Why DIS 99</p>
            <h2>Three reasons clients stay for years</h2>
          </div>
          <div class="features" data-stagger style="margin-top: 3rem;">
            <div class="feature"><span class="feature-num">01</span><h3>Fixed deadlines</h3><p>You always know exactly what happens and when. We file on time, every time, and remind you in advance — no surprises, no fines.</p></div>
            <div class="feature"><span class="feature-num">02</span><h3>Personal accountant</h3><p>You work with a specific person who knows your business and responds quickly — not an anonymous call center.</p></div>
            <div class="feature"><span class="feature-num">03</span><h3>Free registration</h3><p>Starting a new company? We handle the registration entirely free of charge with a service contract.</p></div>
          </div>
          <div class="reveal" style="text-align:center; margin-top:3rem;">
            <a class="btn btn-primary btn-lg" href="pages/contact.html">Start with a free consultation</a>
          </div>
        </div>
      </section>

      <section class="section section--sand">
        <div class="container">
          <div class="section-head center reveal">
            <p class="eyebrow">Who we work with</p>
            <h2>We know your type of business</h2>
            <p class="lead">Every business has its specifics — we speak the language of yours.</p>
          </div>
          <div class="grid grid-2" data-stagger style="margin-top: 3rem;">
            <article class="card">
              <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 21h18M5 21V7l7-4 7 4v14"/><path d="M9 9h2M13 9h2M9 13h2M13 13h2M11 21v-4h2v4"/></svg></div>
              <h3>Ltd companies</h3>
              <p>Full service for small and medium companies — from daily operations to annual closing and dividends.</p>
            </article>
            <article class="card">
              <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
              <h3>Freelancers & professionals</h3>
              <p>Doctors, lawyers, designers, consultants — optimal taxation and minimal administrative burden for you.</p>
            </article>
            <article class="card">
              <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="21" r="1.6"/><circle cx="19" cy="21" r="1.6"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h8.7a2 2 0 0 0 2-1.6L22 7H6"/></svg></div>
              <h3>eCommerce & online business</h3>
              <p>Online stores, platforms and dropshipping — EU VAT, VIES, courier and payment integrations.</p>
            </article>
            <article class="card">
              <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg></div>
              <h3>Start-ups</h3>
              <p>We register your company for free, guide you through the first steps and grow together with you.</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-head center reveal">
            <p class="eyebrow">How we work</p>
            <h2>A simple process, clear from day one</h2>
          </div>
          <div class="steps" data-stagger style="margin-top: 3rem;">
            <div class="step"><h3>Intro & contract</h3><p>A free consultation where we define the scope, the deadlines and how we communicate.</p></div>
            <div class="step"><h3>Monthly service</h3><p>We collect documents, do the bookkeeping, file VAT and payroll and send you clear reports.</p></div>
            <div class="step"><h3>Control & peace of mind</h3><p>Deadline reminders, periodic reports and full preparation for any audit.</p></div>
          </div>
          <div class="reveal" style="text-align:center; margin-top:3rem;">
            <a class="btn btn-dark btn-lg" href="pages/contact.html">Book a consultation</a>
            <a class="btn btn-ghost btn-lg" href="tel:+359885738666" style="margin-left:.6rem;">0885 738 666</a>
          </div>
        </div>
      </section>

      <section class="section section--sand">
        <div class="container">
          <div class="section-head center reveal">
            <p class="eyebrow">The people behind the numbers</p>
            <h2>Experience and a personal touch</h2>
            <p class="lead">A small, dedicated team means you always speak with someone who knows your case.</p>
          </div>
          <div class="founders" data-stagger style="margin-top: 3rem;">
            <article class="founder">
              <div class="founder-photo"><picture><source type="image/webp" srcset="../img/team/georgi-420.webp 420w, ../img/team/georgi-640.webp 640w, ../img/team/georgi-840.webp 840w" sizes="(max-width: 560px) 260px, 220px" /><img src="../img/team/georgi.jpg" width="420" height="525" alt="Georgi — founder and manager of DIS 99" loading="lazy" /></picture></div>
              <div><h3>Georgi</h3><p class="role">Founder & manager</p><p>Founded DIS 99 in 2008 after years of experience in accounting and tax consulting. Today he personally handles the most complex cases — tax audits, planning and annual closing.</p><p>He believes good accounting shows in one thing: the client's peace of mind.</p></div>
            </article>
            <article class="founder">
              <div class="founder-photo"><picture><source type="image/webp" srcset="../img/team/snezhana-420.webp 420w, ../img/team/snezhana-640.webp 640w, ../img/team/snezhana-840.webp 840w" sizes="(max-width: 560px) 260px, 220px" /><img src="../img/team/snezhana.jpg" width="420" height="525" alt="Snezhana — accountant at DIS 99" loading="lazy" /></picture></div>
              <div><h3>Snezhana</h3><p class="role">Accountant · Social media</p><p>Handles the day-to-day service — bookkeeping, VAT and client communication. She makes the complex sound simple and replies the same day.</p><p>She is also the face of DIS 99 on social media.</p></div>
            </article>
          </div>
          <div class="center reveal" style="text-align:center; margin-top: 2.5rem;">
            <a class="btn btn-ghost" href="pages/about.html">Meet the team</a>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-head center reveal">
            <p class="eyebrow">Testimonials</p>
            <h2>What our clients say</h2>
          </div>
          <!-- TODO: replace sample testimonials with real client quotes -->
          <div class="quotes" data-stagger style="margin-top: 3rem;">
            <blockquote class="quote">
              <div class="quote-stars" aria-label="5 out of 5 stars">★★★★★</div>
              <p>"We have worked with DIS 99 for years without a single missed deadline. Everything is clear, on time and stress-free."</p>
              <footer><strong>Ltd company owner</strong><span>Plovdiv</span></footer>
            </blockquote>
            <blockquote class="quote">
              <div class="quote-stars" aria-label="5 out of 5 stars">★★★★★</div>
              <p>"We moved our accounting to them mid-year — the transition was completely smooth."</p>
              <footer><strong>Online store manager</strong><span>eCommerce client</span></footer>
            </blockquote>
            <blockquote class="quote">
              <div class="quote-stars" aria-label="5 out of 5 stars">★★★★★</div>
              <p>"I always get an answer the same day. It feels like having a partner, not just an accountant."</p>
              <footer><strong>Freelance professional</strong><span>remote service</span></footer>
            </blockquote>
          </div>
        </div>
      </section>

      <section class="section section--sand">
        <div class="container">
          <div class="section-head center reveal">
            <p class="eyebrow">Pricing</p>
            <h2>Transparent packages, no hidden fees</h2>
            <p class="lead">Indicative starting prices. The final quote depends on document volume and the specifics of your business.</p>
          </div>
          <div class="price-grid" data-stagger style="margin-top: 3rem;">
            <div class="price"><div class="price-name">Start</div><p class="price-desc">For new and small companies without VAT registration.</p><div class="price-tag"><span class="price-from">from</span><span class="price-amt">120</span><span class="price-unit">BGN/mo</span></div><ul><li>§ Bookkeeping</li><li>§ Up to 20 documents per month</li><li>§ Annual closing</li></ul><a class="btn btn-ghost btn-block" href="pages/contact.html">Enquire</a></div>
            <div class="price featured"><div class="price-name">Business</div><p class="price-desc">For active companies with VAT and employees.</p><div class="price-tag"><span class="price-from">from</span><span class="price-amt">260</span><span class="price-unit">BGN/mo</span></div><ul><li>§ Everything in "Start"</li><li>§ VAT & VIES</li><li>§ Payroll up to 5 staff</li><li>§ Personal accountant</li></ul><a class="btn btn-primary btn-block" href="pages/contact.html">Enquire</a></div>
            <div class="price"><div class="price-name">Premium</div><p class="price-desc">For larger businesses and high-volume eCommerce.</p><div class="price-tag"><span class="price-from">from</span><span class="price-amt">480</span><span class="price-unit">BGN/mo</span></div><ul><li>§ Everything in "Business"</li><li>§ Unlimited documents</li><li>§ Management reports</li><li>§ Priority support</li></ul><a class="btn btn-ghost btn-block" href="pages/contact.html">Enquire</a></div>
          </div>
        </div>
      </section>
''' + cta_band("pages/contact.html")
index_main = index_main.replace("§", CHECK)

index_ld = '''    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"AccountingService","name":"DIS 99 Accounting Firm","url":"https://dis99.bg/en/","telephone":"+359885738666","email":"dis99@abv.bg","foundingDate":"2008","priceRange":"$$","address":{"@type":"PostalAddress","streetAddress":"112 Tsarigradsko shose Blvd","addressLocality":"Plovdiv","addressCountry":"BG"},"areaServed":{"@type":"Country","name":"Bulgaria"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"17:00"}]}
    </script>
'''

# =================== SERVICES ===================
def svc_block(img, title, text, items):
    lis = "".join('<li>%s<span>%s</span></li>' % (CHECK, it) for it in items)
    media = '<img class="svc-img" src="../../img/services/%s.svg" alt="" loading="lazy" width="480" height="360" />' % img
    return '''        <div class="svc reveal"><div class="svc-media">%s</div><div><h2>%s</h2><p>%s</p><ul class="svc-list">%s</ul></div></div>''' % (media, title, text, lis)

services_main = page_hero("Services", "Full-service accounting",
    "From daily bookkeeping to annual closing, payroll and audit defense — we handle it all so you can focus on your business.") + '''
      <section class="section"><div class="container">
''' + "\n".join([
    svc_block('bookkeeping', "Bookkeeping", "We keep your accounts in order every month — posting documents, bank operations, cash and inventory. You always know where your business stands financially.", ["Posting income and expenses", "Bank, cash and settlements", "Monthly statements and reports", "Electronic document exchange"]),
    svc_block('vat', "VAT & VIES", "We prepare and file VAT returns, purchase and sales ledgers and VIES declarations right on time — no gaps, no fines.", ["Monthly VAT returns", "Purchase/sales ledgers", "VIES for intra-EU supplies", "Deadline tracking"]),
    svc_block('annual', "Annual accounts (GFO)", "We prepare and publish the annual financial statement and tax returns so you close the year calmly and in full compliance.", ["Annual financial statement", "Annual tax return", "Publication in the Trade Register", "Tax planning for next year"]),
    svc_block('payroll', "Payroll", "We handle the entire payroll process — from employment contracts to payslips and social security, always compliant with labor law.", ["Employment and civil contracts", "Payslips and registers", "Social security and income tax", "Registrations with NRA and NSSI"]),
    svc_block('defense', "Tax defense & advice", "When an audit or inspection comes, you are not alone. We prepare the documentation, represent your interest and advise you at every step.", ["Audit and inspection preparation", "Representation before the NRA", "Ongoing tax advice", "Tax risk analysis"]),
    svc_block('registration', "Registration & business start", "Starting something new? We help with company registration, VAT registration and everything for a successful start — free with a service contract.", ["Ltd/sole-owner registration", "VAT registration", "Start-up consulting", "Free with a service contract"]),
]) + '''
      </div></section>
''' + cta_band()

# =================== PRICING ===================
def price_card(name, desc, amt, feats, featured=False):
    lis = "".join('<li>%s%s</li>' % (CHECK, f) for f in feats)
    cls = "price featured" if featured else "price"
    btn = "btn btn-primary btn-block" if featured else "btn btn-ghost btn-block"
    return '''          <div class="%s"><div class="price-name">%s</div><p class="price-desc">%s</p><div class="price-tag"><span class="price-from">from</span><span class="price-amt">%s</span><span class="price-unit">BGN/mo</span></div><ul>%s</ul><a class="%s" href="contact.html">Enquire</a></div>''' % (cls, name, desc, amt, lis, btn)

pricing_main = page_hero("Pricing", "Transparent prices, no surprises",
    "Indicative starting prices based on the type and volume of your business. We agree the final quote together after a short chat about your needs.") + '''
      <section class="section"><div class="container">
          <div class="price-grid" data-stagger>
''' + "\n".join([
    price_card("Start", "For new and small companies without VAT registration.", "120", ["Bookkeeping", "Up to 20 documents per month", "Annual closing (GFO)", "Email and phone support"]),
    price_card("Business", "For active companies with VAT and employees.", "260", ['Everything in "Start"', "VAT returns and VIES", "Payroll up to 5 staff", "Personal accountant"], featured=True),
    price_card("Premium", "For larger businesses and high-volume eCommerce.", "480", ['Everything in "Business"', "Unlimited documents", "Management reports", "Priority support"]),
]) + '''
          </div>
          <p class="reveal" style="text-align:center; margin-top:1.6rem; color:var(--muted); font-size:.95rem;">Prices are indicative and not a binding offer. VAT is not included where applicable.</p>
          <div class="section-head center reveal" style="margin-top:4.5rem;"><p class="eyebrow">What affects the price</p><h2>You pay for the actual workload</h2></div>
          <div class="grid grid-3" data-stagger style="margin-top:2.5rem;">
            <article class="card"><h3>Number of documents</h3><p>The more invoices and operations per month, the more time the service takes.</p></article>
            <article class="card"><h3>VAT registration</h3><p>VAT-registered companies require monthly returns and more detailed records.</p></article>
            <article class="card"><h3>Number of employees</h3><p>Payroll services are charged according to the number of staff.</p></article>
          </div>
      </div></section>
''' + cta_band()

# =================== ABOUT ===================
about_main = page_hero("About", "The people behind DIS 99",
    "A small accounting firm in Plovdiv with a big eye for detail. Since 2008 we have helped entrepreneurs grow with peace of mind.") + '''
      <section class="section"><div class="container">
          <div class="prose reveal" style="margin-inline:auto; text-align:center;"><p class="lead" style="color:var(--ink)">We believe accounting is not just an obligation but a backbone for every business. That is why we work transparently, keep deadlines strictly and explain things in plain language — no jargon, no stress.</p></div>
          <!-- TODO: confirm/adjust team bios -->
          <div class="founders" data-stagger style="margin-top:3.5rem;">
            <article class="founder"><div class="founder-photo"><picture><source type="image/webp" srcset="../../img/team/georgi-420.webp 420w, ../../img/team/georgi-640.webp 640w, ../../img/team/georgi-840.webp 840w" sizes="(max-width: 560px) 260px, 220px" /><img src="../../img/team/georgi.jpg" width="420" height="525" alt="Georgi — founder and manager of DIS 99" loading="lazy" /></picture></div><div><h3>Georgi</h3><p class="role">Founder & manager</p><p>Georgi founded DIS 99 in 2008 after years of experience in accounting and tax consulting. Today he personally leads the most complex cases — tax audits, annual closing and tax planning — and is the person clients call with the difficult questions.</p><p>He insists on deadline discipline and a direct, honest relationship. He believes good accounting shows in one thing: the client's peace of mind.</p></div></article>
            <article class="founder"><div class="founder-photo"><picture><source type="image/webp" srcset="../../img/team/snezhana-420.webp 420w, ../../img/team/snezhana-640.webp 640w, ../../img/team/snezhana-840.webp 840w" sizes="(max-width: 560px) 260px, 220px" /><img src="../../img/team/snezhana.jpg" width="420" height="525" alt="Snezhana — accountant at DIS 99" loading="lazy" /></picture></div><div><h3>Snezhana</h3><p class="role">Accountant · Social media</p><p>Snezhana is responsible for the day-to-day service — bookkeeping, VAT returns and daily client communication. She is the person you will talk to most often, known for quick replies and the patience to explain every detail.</p><p>Beyond the numbers, she also runs the firm's social media — making accounting understandable and approachable for everyone.</p></div></article>
          </div>
      </div></section>
      <section class="section section--sand"><div class="container">
          <div class="section-head center reveal"><p class="eyebrow">Our story</p><h2>A journey shared with our clients</h2></div>
          <div class="timeline reveal" style="margin-top:3rem;">
            <div class="tl-item"><div class="tl-year">2008</div><h3>DIS 99 is founded</h3><p>Georgi starts the firm in Plovdiv with a clear idea — accounting explained in plain language, with every deadline kept.</p></div>
            <div class="tl-item"><div class="tl-year">2015</div><h3>Services expand</h3><p>Full payroll service, tax defense during audits and consulting for growing businesses join the core bookkeeping.</p></div>
            <div class="tl-item"><div class="tl-year">2020</div><h3>Remote service</h3><p>We switch to electronic document exchange and start serving clients across the whole country.</p></div>
            <div class="tl-item"><div class="tl-year">Today</div><h3>50+ active clients</h3><p>A family team with 18+ years of experience, trusted by businesses from Plovdiv and all over Bulgaria.</p></div>
          </div>
      </div></section>
      <section class="section"><div class="container">
          <div class="section-head center reveal"><p class="eyebrow">Our values</p><h2>The principles we work by</h2></div>
          <div class="grid grid-3" data-stagger style="margin-top:2.5rem;">
            <article class="card"><h3>Transparency</h3><p>No hidden fees and no surprises. You know exactly what you pay for and what happens with your company.</p></article>
            <article class="card"><h3>Accuracy</h3><p>We keep every deadline and check every detail. Mistakes are expensive — so we don't make them.</p></article>
            <article class="card"><h3>Closeness</h3><p>You work with a specific person who knows your business and replies quickly and personally.</p></article>
          </div>
      </div></section>
      <section class="stats"><div class="container stats-grid" data-stagger>
          <div class="stat"><div class="stat-num"><span>2008</span></div><div class="stat-label">Founded</div></div>
          <div class="stat"><div class="stat-num"><span data-count="18">18</span><span class="suf">+</span></div><div class="stat-label">Years of experience</div></div>
          <div class="stat"><div class="stat-num"><span data-count="50">50</span><span class="suf">+</span></div><div class="stat-label">Active clients</div></div>
          <div class="stat"><div class="stat-num"><span data-count="100">100</span><span class="suf">%</span></div><div class="stat-label">Deadlines met</div></div>
      </div></section>
''' + cta_band()

# =================== FAQ ===================
FAQS = [
    ("What documents do you need to start?", "To get started we need the company's incorporation documents, access to bank statements and current invoices. At the first (free) consultation we give you an exact list for your case."),
    ("Do you work with companies outside Plovdiv?", "Yes. We serve clients across the country entirely remotely — exchanging documents electronically and communicating by phone and email."),
    ("How is the monthly price determined?", "The price mainly depends on the number of documents per month, whether the company is VAT-registered, and the number of employees. After a short chat we give you a concrete quote."),
    ("Is company registration really free?", "Yes — we cover the cost and the administrative work of registering a new company free of charge, with a monthly accounting service contract."),
    ("What happens during a tax audit or inspection?", "We prepare all the necessary documentation, represent you before the NRA and advise you at every step. We never leave our clients alone in such moments."),
    ("Can I change my accountant mid-year?", "Of course. The switch is easier than it looks — we take over communication with the previous accountant and ensure a smooth transition with no interruption."),
    ("Do you keep confidentiality?", "Absolutely. We sign a contract with a confidentiality clause and process your data only for the purpose of the service, in line with GDPR."),
]
faq_items = "".join('''          <details class="faq-item reveal"><summary>%s</summary><div class="faq-body"><p>%s</p></div></details>''' % (q, a) for q, a in FAQS)
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
faq_head_extra = '    <script type="application/ld+json">%s</script>\n' % _json.dumps(faq_ld, ensure_ascii=False)
faq_main = page_hero("FAQ", "Frequently asked questions",
    "We gathered the answers to the questions our clients ask most. Can't find yours? Write to us — we reply fast.") + '''
      <section class="section"><div class="container">
          <div class="faq-list">
''' + faq_items + '''
          </div>
          <div class="cta-inline reveal" style="margin-top:3rem;"><a class="btn btn-primary btn-lg" href="contact.html">Ask your question</a></div>
      </div></section>
''' + cta_band()

# =================== CONTACT ===================
contact_main = page_hero("Contact", "Let's talk about your business",
    "Book a free consultation or simply ask us a question. We respond quickly — usually within the same business day.") + '''
      <section class="section"><div class="container contact-grid">
          <div class="reveal"><div class="form-card">
            <form id="contact-form" action="/api/contact" method="post" novalidate>
              <div class="field-row">
                <div class="field"><label for="name">Name <span class="req">*</span></label><input id="name" name="name" type="text" autocomplete="name" required /></div>
                <div class="field"><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" autocomplete="email" required /></div>
              </div>
              <div class="field-row">
                <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel" /></div>
                <div class="field"><label for="company">Company</label><input id="company" name="company" type="text" autocomplete="organization" /></div>
              </div>
              <div class="field"><label for="topic">Topic <span class="req">*</span></label>
                <select id="topic" name="topic" required><option value="" disabled selected>Choose…</option><option>Bookkeeping</option><option>VAT & VIES</option><option>Annual accounts (GFO)</option><option>Payroll</option><option>Company registration</option><option>Tax consultation</option><option>Other</option></select>
              </div>
              <div class="field"><label for="message">Message <span class="req">*</span></label><textarea id="message" name="message" required placeholder="Tell us briefly about your business and your approximate monthly document volume."></textarea></div>
              <div class="hp" aria-hidden="true"><label for="website">Do not fill</label><input id="website" name="website" type="text" tabindex="-1" autocomplete="off" /></div>
              <div class="field consent"><input id="consent" name="consent" type="checkbox" required /><label for="consent">I agree that my personal data may be processed to answer my enquiry, per the <a href="privacy.html">Privacy Policy</a>. <span class="req">*</span></label></div>
              <button class="btn btn-primary btn-lg btn-block" type="submit">Send enquiry</button>
              <p class="form-note">Fields marked with <span style="color:var(--brass-deep)">*</span> are required. We never share your data with third parties.</p>
              <div id="form-status" class="form-status" role="status" aria-live="polite"></div>
            </form>
          </div></div>
          <div class="contact-info reveal">
            <div class="contact-item"><span class="ico">%s</span><div><h3>Phone</h3><p><a href="tel:+359885738666">0885 738 666</a></p></div></div>
            <div class="contact-item"><span class="ico">%s</span><div><h3>Email</h3><p><a href="mailto:dis99@abv.bg">dis99@abv.bg</a></p></div></div>
            <div class="contact-item"><span class="ico">%s</span><div><h3>Address</h3><p>Plovdiv, 112 Tsarigradsko shose Blvd</p></div></div>
            <div class="contact-item"><span class="ico">%s</span><div><h3>Working hours</h3><p>Monday – Friday · 09:00 – 17:00</p></div></div>
            <iframe class="map-embed" title="Map — DIS 99, Plovdiv" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=112+Tsarigradsko+shose,+Plovdiv&output=embed"></iframe>
          </div>
      </div></section>''' % (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92"/></svg>',
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0"/><circle cx="12" cy="10" r="3"/></svg>',
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>')

# =================== LEGAL ===================
privacy_main = page_hero("Privacy", "Privacy Policy", "How we collect, use and protect your personal data.") + '''
      <section class="section"><div class="container"><div class="prose reveal">
        <p class="muted">Last updated: 2026</p>
        <p>This policy explains how DIS 99 Accounting Firm processes the personal data of website visitors and clients, in accordance with Regulation (EU) 2016/679 (GDPR).</p>
        <h2>1. Data controller</h2><p>DIS 99 Accounting Firm<br />Address: Plovdiv, 112 Tsarigradsko shose Blvd<br />Company ID: <!-- TODO --> [add company ID]<br />Email: <a href="mailto:dis99@abv.bg">dis99@abv.bg</a> · Phone: <a href="tel:+359885738666">0885 738 666</a></p>
        <h2>2. What data we collect</h2><ul><li>Data you provide via the contact form: name, email, phone, company and the content of your enquiry.</li><li>Data required for accounting services under a client contract.</li><li>Technical data from the site (see the <a href="cookies.html">Cookie Policy</a>).</li></ul>
        <h2>3. How we use the data</h2><ul><li>To respond to your enquiries and prepare a quote.</li><li>To perform an accounting service contract.</li><li>To comply with legal obligations (tax and accounting law).</li></ul>
        <h2>4. Legal basis</h2><p>We process data on the basis of your consent, performance of a contract and compliance with legal obligations.</p>
        <h2>5. Retention</h2><p>We keep data only as long as necessary for the relevant purpose or as required by law (e.g. accounting documents are kept for statutory periods).</p>
        <h2>6. Your rights</h2><p>You have the right to access, rectify, erase, restrict and port your data, and to withdraw consent at any time. To do so, email <a href="mailto:dis99@abv.bg">dis99@abv.bg</a>.</p>
        <h2>7. Complaints</h2><p>You have the right to lodge a complaint with the Commission for Personal Data Protection (CPDP), www.cpdp.bg.</p>
      </div></div></section>'''

cookies_main = page_hero("Cookies", "Cookie Policy", "Which cookies we use and how to manage them.") + '''
      <section class="section"><div class="container"><div class="prose reveal">
        <p class="muted">Last updated: 2026</p>
        <p>"Cookies" are small text files saved on your device when you visit a website. This site uses a minimal set of cookies.</p>
        <h2>1. Which cookies we use</h2><ul><li><strong>Strictly necessary</strong> — provide the basic functionality of the site. No consent required.</li><li><strong>Embedded maps (Google Maps)</strong> — the "Contact" page loads a Google map that may set its own cookies. The map loads only when the page is opened.</li></ul>
        <p>The site does not use advertising or tracking cookies. Fonts are served locally from our own server, with no external services.</p>
        <h2>2. Managing cookies</h2><p>You can delete or block cookies from your browser settings. Note that blocking some cookies may affect site functionality.</p>
        <h2>3. Contact</h2><p>For questions about this policy: <a href="mailto:dis99@abv.bg">dis99@abv.bg</a>.</p>
      </div></div></section>'''

PAGES = [
    ("index", "DIS 99 Accounting Firm — accounting in Plovdiv | VAT, payroll", "DIS 99 Accounting Firm in Plovdiv — professional accounting for small and medium businesses since 2008. Fixed deadlines, a personal accountant and free company registration.", index_main, index_ld),
    ("services", "Services — accounting, VAT, payroll | DIS 99", "Full-service accounting from DIS 99: bookkeeping, VAT & VIES, annual accounts, payroll, tax defense and company registration.", services_main, ""),
    ("pricing", "Pricing | DIS 99 Plovdiv", "Transparent starting prices for accounting services — Start, Business and Premium packages. Final quote based on your business volume.", pricing_main, ""),
    ("about", "About — DIS 99 Accounting Firm | Plovdiv since 2008", "Meet the DIS 99 team — Georgi and Snezhana. An accounting firm in Plovdiv with 18+ years of experience and 50+ active clients.", about_main, ""),
    ("faq", "Frequently asked questions | DIS 99", "Answers to the most common questions about accounting services, pricing, remote work, company registration and tax audits.", faq_main, faq_head_extra),
    ("contact", "Contact — DIS 99 Accounting Firm | Plovdiv", "Get in touch with DIS 99 in Plovdiv. Phone 0885 738 666, email dis99@abv.bg, 112 Tsarigradsko shose Blvd. Book a free consultation.", contact_main, ""),
    ("privacy", "Privacy Policy | DIS 99", "How DIS 99 Accounting Firm collects, uses and protects your personal data under GDPR.", privacy_main, ""),
    ("cookies", "Cookie Policy | DIS 99", "Information about the cookies used by the DIS 99 Accounting Firm website.", cookies_main, ""),
]

os.makedirs(os.path.join(ROOT, "en", "pages"), exist_ok=True)
for key, title, desc, main, extra in PAGES:
    html = P.document("en", key, title, desc, main, head_extra=extra)
    path = os.path.join(ROOT, "en", "index.html") if key == "index" else os.path.join(ROOT, "en", "pages", key + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", os.path.relpath(path, ROOT), "(%d bytes)" % len(html))
