#!/usr/bin/env python3
"""
Generate the atomized prediction ledger for Unmitigated Wisdom.

Data model:
  groups: list of {
    year, date (display), datetime (ISO), subhead,
    sources: [(label, url), ...],
    items: [
      {prediction: str, audits: [{meta: str, url: str, text: str}, ...]}
    ]
  }

Sources are either Telegram post URLs (the originating channel post) or
report URLs (when a prediction was first stated in a report or when a
report explicitly cites the number). Multiple sources allowed per group.

Audits are responses/validations written later. They cite the source of
the update (a follow-up Telegram post or a subsequent report).
"""

import html as html_mod

TG = "https://t.me/unmitigated_wisdom"
def tg(n): return f"{TG}/{n}"

groups = []

# ============================================================
# 2020
# ============================================================

groups.append(dict(
    year="2020", date="13 March 2020", datetime="2020-03-13",
    subhead="COVID market trajectory — short, mid, long-term",
    sources=[("Telegram #6", tg(6))],
    items=[
        dict(
            prediction="<strong>Short term.</strong> Stock markets will experience another big sell-off if the US death toll rises similarly to Italy's, followed by partial recovery once case growth and fear subside.",
            audits=[
                dict(meta="9 May 2020 · #24", url=tg(24),
                     text="Accurate — major US market drops coinciding with case reports, followed by partial recoveries once statistics stabilised."),
            ],
        ),
        dict(
            prediction="<strong>Mid term.</strong> Further major sell-offs and market crashes will follow when IMF, ECB, China, and the US announce negative or near-zero quarterly GDP growth.",
            audits=[
                dict(meta="9 May 2020 · #24", url=tg(24),
                     text="Partially accurate — unemployment and oil prices point to a major depression looming; awaiting market reaction."),
            ],
        ),
        dict(
            prediction="<strong>Long term.</strong> Within 1–1.5 years it will be clear that doomsday scenarios didn't materialise, and stocks will fully recover the losses — possibly returning to the highs of one month ago.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2020", date="18 March 2020", datetime="2020-03-18",
    subhead="Global 2020 GDP forecast",
    sources=[("Telegram #9", tg(9))],
    items=[
        dict(
            prediction="<strong>World.</strong> Global GDP growth will be near-zero or negative for 2020.",
            audits=[
                dict(meta="25 Mar 2020 · #18", url=tg(18),
                     text="Gloomier update — now forecasting world GDP at −5% to −2%."),
                dict(meta="7 Jul 2020 · #41", url=tg(41),
                     text="European Commission validates a slow recovery — EU GDP −8.7% in 2020, +6.1% in 2021, still below pre-outbreak by end of 2021 even absent a second wave."),
            ],
        ),
        dict(
            prediction="<strong>Europe.</strong> European economies will be the hardest-hit, shrinking 2–5%.",
            audits=[
                dict(meta="25 Mar 2020 · #18", url=tg(18),
                     text="Revised steeper — Italy specifically −10% or worse; the hardest-hit regions (Veneto, Lombardy) account for ~40% of Italy's economy."),
            ],
        ),
        dict(
            prediction="<strong>East Asia.</strong> Far-eastern countries will be the best-performing economies in 2020.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2020", date="19 March 2020", datetime="2020-03-19",
    subhead="US COVID stimulus — bailout and market reaction",
    sources=[("Telegram #10", tg(10)), ("Follow-up #11", tg(11)), ("Follow-up #19", tg(19))],
    items=[
        dict(
            prediction="A US stimulus package will pass as a bailout for &ldquo;too big to fail&rdquo; corporations — Boeing, Exxon, and Chevron among them — and their stocks will immediately go up as a result.",
            audits=[
                dict(meta="24 Mar 2020 · #14", url=tg(14),
                     text="Confirmed — after the $2-trillion bailout was signed, the named companies hugely outperformed the indices. Screenshots at #16: Chevron +18.1%, Boeing +16.5%, Dow +9.0% on the day."),
                dict(meta="26 Mar 2020 · #20", url=tg(20),
                     text="Indices up 5% on signing expectation; airlines, planes, shale oil, post, and hotels all carved out and expected to outperform once signed."),
            ],
        ),
        dict(
            prediction="American Airlines will be bailed out, and its stock will surge back immediately.",
            audits=[
                dict(meta="24 Mar 2020 · #16", url=tg(16),
                     text="American Airlines +40.3% on the day of rebound."),
            ],
        ),
        dict(
            prediction="When the stimulus bill is actually signed, there will be a temporary market surge.",
            audits=[
                dict(meta="24 Mar 2020 · #14", url=tg(14),
                     text="Confirmed — indices surged after signing."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2020", date="20 March 2020", datetime="2020-03-20",
    subhead="Richard Burr",
    sources=[("Telegram #12", tg(12))],
    items=[
        dict(
            prediction="Senator Richard Burr will resign from his position.",
            audits=[
                dict(meta="14 May 2020 · #29", url=tg(29),
                     text="Partially — he stepped down from the Senate Intelligence chair and won't run for re-election, but is not resigning the seat early (a Democratic governor would appoint a temporary replacement)."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2020", date="29 March 2020", datetime="2020-03-29",
    subhead="Monday open — S&amp;P and Dow",
    sources=[("Telegram #22", tg(22))],
    items=[
        dict(
            prediction="S&amp;P 500 and Dow Jones will drop 5±3% on the Monday open — markets have absorbed the stimulus news, US case and death-toll growth over the weekend is raising red flags, and the administration's crisis management looks inconsistent.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2020", date="9 May 2020", datetime="2020-05-09",
    subhead="Oil &amp; gas — 1–2 year investment view",
    sources=[("Telegram #25", tg(25))],
    items=[
        dict(
            prediction="Oil and gas companies like Exxon will return 50–80% over a 1–2 year window — the world economy will need oil again soon, and accumulated technology in these companies won't disappear even through near-bankruptcy.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2020", date="11 May 2020", datetime="2020-05-11",
    subhead="Trump 2020 re-election",
    sources=[("Telegram #26", tg(26)), ("Follow-up #27", tg(27)), ("Follow-up #38–39", tg(38)), ("Follow-up #48", tg(48))],
    items=[
        dict(
            prediction="Trump's 2020 re-election chances are materially lower than widely believed — the 2016 win was razor-thin, Biden leads nationally and in the swing states, and the pandemic amplifies economic disaffection.",
            audits=[
                dict(meta="6 Jun 2020 · #34", url=tg(34),
                     text="George Floyd's death produces unprecedented consensus on racial injustice; Trump approval drops below 50%, further weakening re-election."),
                dict(meta="6 Jun 2020 · #35", url=tg(35),
                     text="Protests may have lasting electoral effect — if Trump loses the white working-class vote in Wisconsin, Michigan, Pennsylvania, he loses the election."),
                dict(meta="21 Jun 2020 · #36", url=tg(36),
                     text="Trump setbacks compounding — COVID mismanagement, Bolton book publishing despite legal battle, Biden's polling margin widening to ~9 points."),
                dict(meta="21 Jun 2020 · #37", url=tg(37),
                     text="Context: Clinton had a 3-point national margin and lost; a 6-point Biden margin is a guaranteed win, 7+ a landslide that retakes the Senate."),
                dict(meta="9 Jul 2020 · #42", url=tg(42),
                     text="Biden cracking 50% in polls; prediction markets give Biden 60%, Goldman Sachs rates Trump below 49%; Trump campaign ads in Republican strongholds like Georgia indicate narrowing map."),
                dict(meta="2 Nov 2020 · #47", url=tg(47),
                     text="The pandemic is the biggest wildcard and should hurt Trump; 10% chance of winning is non-zero but rare."),
            ],
        ),
        dict(
            prediction="Biden will win with a 6–10% popular-vote margin and 330–370 electoral college votes.",
            audits=[
                dict(meta="12 Nov 2020 · #49", url=tg(49),
                     text="Biden projected 306 EC votes and 4–5% popular-vote margin after all votes counted — outside predicted intervals, but not far off."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2020", date="14 May 2020", datetime="2020-05-14",
    subhead="Roche &mdash; Genentech mid/long-term",
    sources=[("Telegram #28", tg(28))],
    items=[
        dict(
            prediction="Roche is a good mid-to-long-term investment — Genentech, a Roche subsidiary, has hired two leading geneticists (Aviv Regev and Mark McCarthy) and announced COVID-19 human antibody trials with the UK government, indicating expanded R&amp;D.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2020", date="25 May 2020", datetime="2020-05-25",
    subhead="US unemployment recovery trajectory",
    sources=[("Telegram #30", tg(30))],
    items=[
        dict(
            prediction="About 90% of US unemployment statistics reflect temporary job loss; in the next 1–2 months many businesses will reopen, unemployment will drop substantially, and stock markets will follow — with the caveat that less-essential businesses may not survive the timeline.",
            audits=[
                dict(meta="5 Jun 2020 · #31", url=tg(31),
                     text="Confirmed — US unemployment dropped to 13% and markets reacted positively (WaPo)."),
                dict(meta="5 Jun 2020 · #33", url=tg(33),
                     text="Dow soars ~1,000 points as Wall Street closes in on pre-pandemic levels."),
                dict(meta="2 Jul 2020 · #40", url=tg(40),
                     text="US added 4.5M jobs in June, validating the sharp decline; most economists expect a slower 1–2 year second phase."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2020", date="10 July 2020", datetime="2020-07-10",
    subhead="Unemployment benefit extension &amp; markets",
    sources=[("Telegram #43", tg(43))],
    items=[
        dict(
            prediction="Without extension of the stimulus unemployment benefits, US economic recovery may be derailed — but looming elections make a deal only about 50/50 (Republicans dislike welfare, Democrats dislike tax cuts).",
            audits=[
                dict(meta="7 Aug 2020 · #44", url=tg(44),
                     text="Revised — the weekly household payments will mostly be extended; the deal is most likely reached within 1–2 weeks due to economic damage from delay. Markets will respond positively."),
                dict(meta="11 Aug 2020 · #46", url=tg(46),
                     text="Dow Jones nears record high on stimulus bets — investors wagering on a bipartisan deal. Validates the upturn prediction."),
            ],
        ),
    ],
))

# ============================================================
# 2021
# ============================================================

groups.append(dict(
    year="2021", date="22 February 2021", datetime="2021-02-22",
    subhead="Crypto correction",
    sources=[("Telegram #50", tg(50))],
    items=[
        dict(
            prediction="Bitcoin and other cryptocurrencies will experience a major short-to-mid-term correction before the next surge — the $2T market cap is still small enough to be manipulated by whales and governments; the new post-correction baseline could well be above the previous all-time high.",
            audits=[
                dict(meta="19 May 2021 · #51", url=tg(51),
                     text="Confirmed in direction — crypto market cap shrunk 35% since the post; Musk, the US, and China all contributing to volatility. Long-term positive, but investing now likely locks capital for 2–3 years."),
                dict(meta="19 May 2021 · #52", url=tg(52),
                     text="ETH2 implementation is the biggest wildcard — successful → new highs; botched → disaster; delayed → sideways. Long-term determinant is clean energy for Bitcoin mining."),
                dict(meta="25 Jun 2021 · #55", url=tg(55),
                     text="Fully confirmed — Bitcoin and others down ~50%. Still &ldquo;when, not if&rdquo; Bitcoin surpasses $100k (per JP Morgan's price targets)."),
                dict(meta="16 Jul 2021 · #56", url=tg(56),
                     text="Government crackdowns actually increase mining rewards for remaining miners (like drugs and law enforcement); the cycle only breaks if miners are few enough for double-spending or if dirty-mining backlash overrides supply limits."),
                dict(meta="17 Nov 2022 · #75", url=tg(75),
                     text="FTX collapse — crypto's only product was absorbing surplus liquidity (correlated with inflation, unlike gold). Market was overdue for this correction. Bitcoin as digital gold and Ethereum as transparent contracts can recover with sensible rather than sensational arguments."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2021", date="27 May 2021", datetime="2021-05-27",
    subhead="Energy transition — auto &amp; energy incumbents vs. renewables",
    sources=[("Telegram #53", tg(53))],
    items=[
        dict(
            prediction="The long-term trend is against incumbent auto and energy giants (matured, sluggish) and in favour of tech companies in the renewable energy sector — Exxon adding climate activists to its board and the Dutch court ruling against Shell are early signals.",
            audits=[
                dict(meta="30 Oct 2021 · #64", url=tg(64),
                     text="Confirmation — a new US spending deal (expected to be approved in a week) will invest $500B in renewable energy, solar, EVs, and climate-related sectors."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2021", date="17 June 2021", datetime="2021-06-17",
    subhead="Musk as &ldquo;smart Trump&rdquo; risk",
    sources=[("Telegram #54", tg(54))],
    items=[
        dict(
            prediction="Elon Musk dangerously approaches &ldquo;smart Trump&rdquo; territory — Twitter fights, cult of personality around his companies, ruthless self-serving style — but his intelligence and achievements set him apart from Trump; benefit of the doubt that he'll transition toward post-Microsoft Bill Gates.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2021", date="29 July 2021", datetime="2021-07-29",
    subhead="Infrastructure bill &mdash; stocks that will rise",
    sources=[("Telegram #57", tg(57))],
    items=[
        dict(
            prediction="The ~$1T US infrastructure bill will push up Astec Industries, Martin Marietta Materials, Construction Partners (roads), Caterpillar and Manitowoc (machinery); $50B for EV charging will also positively affect the electric-car sector.",
            audits=[
                dict(meta="16 Aug 2021 · #58", url=tg(58),
                     text="Validated — named companies up 4–23% since the post, largely outperforming indices (Dow +2%). Martin Marietta +9%."),
                dict(meta="16 Aug 2021 · #61", url=tg(61),
                     text="Manitowoc +22.9% in the past month."),
                dict(meta="16 Aug 2021 · #62", url=tg(62),
                     text="A sweeping $3.5T bill is likely to pass — $135B agriculture, $330B housing, $198B clean energy, $67B solar — further boosting industrial and clean-energy stocks."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2021", date="27 August 2021", datetime="2021-08-27",
    subhead="Democrats &amp; 2022 midterms",
    sources=[("Telegram #63", tg(63))],
    items=[
        dict(
            prediction="Democrats are heading into 2022/2024 as underdogs — the ISIS attack on US forces is a foreign-policy nightmare for Biden; gerrymandering and re-canvassing favour Republicans; vote-restricting bills make Georgia uphill. If they lose both chambers, they have nothing to show heading into the next cycle.",
            audits=[
                dict(meta="3 Nov 2021 · #65", url=tg(65),
                     text="Partial early validation — disastrous Democratic performance in Virginia and New Jersey; without Trump motivating the Democratic base, the enthusiasm gap is likely to persist."),
                dict(meta="25 Jun 2022 · #70", url=tg(70),
                     text="Dobbs overturning abortion rights is the biggest wildcard for Democrats, but unlikely to save them — national polls bias toward populous liberal states; Democrats are historically bad at converting sentiment into political ammunition; economy remains dominant."),
                dict(meta="6 Nov 2022 · #73", url=tg(73),
                     text="Restated — Democrats face disastrous midterms, House likely to flip Republican, Senate a 50-50 toss-up. Possible consequences: Biden impeachment, Ukraine aid hindered."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2021", date="3 November 2021", datetime="2021-11-03",
    subhead="JCPOA fate",
    sources=[("Telegram #66", tg(66))],
    items=[
        dict(
            prediction="The fate of JCPOA is indirectly tied to Democratic majorities — without a solid Senate majority, Biden's promises fall short of the legislative assurances needed for a new deal, and the window is closing. Without a deal, tensions spiral out of control.",
            audits=[
                dict(meta="19 Mar 2022 · #67", url=tg(67),
                     text="JCPOA fate hangs again — Russia is now the most likely obstructor (Iran's oil/gas would limit Russia-sanction damage). Still more likely than not (>50%) that a deal is reached in the coming days."),
                dict(meta="23 Aug 2022 · #71", url=tg(71),
                     text="A JCPOA deal looks closer than ever — if reached, oil prices plummet (Iran ~50% of Russian supply lost), indices a sure bet to rise; exceptions are direct oil beneficiaries like Aramco and Exxon."),
                dict(meta="23 Aug 2022 · #72", url=tg(72),
                     text="Limiting factors: companies hesitant to buy Iranian oil (sanctions could be reimposed); Iran–Russia partnership restrains Iran; underlying tensions are not subsiding. Full-capacity Iranian supply is unlikely."),
                dict(meta="6 Nov 2022 · #74", url=tg(74),
                     text="Falsified in timing — JCPOA negotiations nearly dead after Iran's protest crackdown; no real prospect of re-enactment in the near future, if ever."),
            ],
        ),
    ],
))

# ============================================================
# 2022
# ============================================================

groups.append(dict(
    year="2022", date="20 March 2022", datetime="2022-03-20",
    subhead="Trump 2024",
    sources=[("Telegram #68", tg(68))],
    items=[
        dict(
            prediction="Trump will very likely run for re-election in 2024 and will lose either the primary or the general. The main reason Biden won in 2020 was Trump himself; Trump's Russia stance, which is becoming a focal point in US politics, further hurts him.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2022", date="26 March 2022", datetime="2022-03-26",
    subhead="Russian invasion of Ukraine — world-economy ramifications",
    sources=[("Telegram #69", tg(69))],
    items=[
        dict(
            prediction="The Russian invasion of Ukraine will shake the world economy — energy-driven inflation and later recession (Russia supplies 11% of global energy), and famine (Russia &amp; Ukraine supply 25% of global wheat). Biden saying Putin &ldquo;cannot stay in power&rdquo; raises Putin's existential stakes and makes settlement harder.",
            audits=[],
        ),
    ],
))

# ============================================================
# 2024
# ============================================================

groups.append(dict(
    year="2024", date="30 July 2024", datetime="2024-07-30",
    subhead="Kamala Harris VP pick",
    sources=[("Telegram #77", tg(77))],
    items=[
        dict(
            prediction="The most likely VP for Kamala Harris is Josh Shapiro — highly liked governor of Pennsylvania, plays Biden's role as a figure who understands blue-collar middle-class voters. Mark Kelly could play a similar role for Arizona.",
            audits=[],
        ),
    ],
))

# ============================================================
# 2026 — Iran War (ordered roughly by prediction date)
# ============================================================

groups.append(dict(
    year="2026", date="1 March 2026", datetime="2026-03-01",
    subhead="Iran regime survival vs. bombing campaign",
    sources=[("Telegram #78", tg(78)),
             ("Telegram #79 — Bayesian priors", tg(79)),
             ("Bayesian 15-Expert Report", "posts/Bayesian_15Expert_Report.html"),
             ("Who Should We Believe About Iran", "posts/Who_Should_We_Believe_About_Iran.html")],
    items=[
        dict(
            prediction="<strong>Regime change is very unlikely from the bombing campaign alone</strong> — there have been zero instances of regime change by air campaign alone, and there is little appetite in the Trump administration for ground troops. The war has taught the IR and IRGC that they are in an existential fight; they will crack down harder on protests.",
            audits=[
                dict(meta="2 Mar 2026 · #79", url=tg(79),
                     text="Bayesian priors — Quick Win 9.2%, Quagmire 52.3%, Off-Ramp 21.9%, Catastrophe 16.6%. Combined >90% probability of regime surviving in some form."),
                dict(meta="9 Mar 2026 · #92", url=tg(92),
                     text="Day 10 update — Quick Win falls to 3–5%; Quagmire 42–46%, Catastrophe rises to 35–38%, Off-Ramp falls to 10–13%. Mojtaba confirmed as Supreme Leader (IRGC-backed continuity)."),
                dict(meta="11 Mar 2026 · #96", url=tg(96),
                     text="Day 13 update — Quick Win 2–4%, Quagmire 38–42%, Catastrophe 38–42% (parity first time), Off-Ramp 13–17%. Mines in Hormuz; IEA release ignored by markets."),
                dict(meta="13 Mar 2026 · #103", url=tg(103),
                     text="Day 14 update — Catastrophe 42% overtakes Quagmire 36% as modal scenario for the first time; Off-Ramp 15%, Quick Win 2%. Combined worst-case: 78%."),
                dict(meta="15 Mar 2026 · #105", url=tg(105),
                     text="Day 15 update — Catastrophe 45%, Quagmire 31%, Off-Ramp rises to 18% for the first time since Day 1, Quick Win 2%."),
            ],
        ),
        dict(
            prediction="<strong>Quagmire is the modal scenario</strong> (~52% initial prior) — IRGC cohesion holds through bombing; prolonged attrition is the most likely outcome.",
            audits=[
                dict(meta="9 Mar 2026 · #92", url=tg(92),
                     text="Day 10 — Quagmire holds at 42–46%, still modal. Primary driver: IRGC cohesion, Mojtaba continuity."),
                dict(meta="13 Mar 2026 · #103", url=tg(103),
                     text="Day 14 — Quagmire falls to 36%, overtaken by Catastrophe for the first time."),
                dict(meta="15 Mar 2026 · #105", url=tg(105),
                     text="Day 15 — Quagmire 31% (Kharg ultimatum forces a decision rather than continued attrition)."),
            ],
        ),
        dict(
            prediction="<strong>Catastrophic regional escalation is a real tail risk</strong> (~17% initial prior) — risk-of-wider-war scenario driven by oil shocks, Houthi Red Sea entry, or Israeli strikes on Iranian civilian infrastructure.",
            audits=[
                dict(meta="9 Mar 2026 · #92", url=tg(92),
                     text="Day 10 — Catastrophe rises to 35–38% (oil at $119, Iraq collapse, SF option)."),
                dict(meta="11 Mar 2026 · #96", url=tg(96),
                     text="Day 13 — Catastrophe reaches parity with Quagmire at 38–42% for the first time."),
                dict(meta="13 Mar 2026 · #103", url=tg(103),
                     text="Day 14 — Catastrophe 42% becomes modal for the first time."),
                dict(meta="15 Mar 2026 · #105", url=tg(105),
                     text="Day 15 — Catastrophe 45% (UAE port threat, Kharg ultimatum, KC-135 losses)."),
            ],
        ),
        dict(
            prediction="<strong>Diplomatic off-ramp / ceasefire is the second-most-likely outcome</strong> (~22% initial prior).",
            audits=[
                dict(meta="9 Mar 2026 · #92", url=tg(92),
                     text="Day 10 — Off-Ramp falls to 10–13% (Larijani says &ldquo;no talks&rdquo;)."),
                dict(meta="11 Mar 2026 · #96", url=tg(96),
                     text="Day 13 — Off-Ramp rises to 13–17% (US asks Israel to halt energy strikes; China/Russia/France contact Tehran)."),
                dict(meta="15 Mar 2026 · #105", url=tg(105),
                     text="Day 15 — Off-Ramp rises to 18% for the first time since Day 1 (Sacks internal pressure; Turkey Fidan backchannel; Kharg deal structure)."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2026", date="2 March 2026", datetime="2026-03-02",
    subhead="Oil prices &amp; global markets — 4-week outlook",
    sources=[("Telegram #81", tg(81))],
    items=[
        dict(
            prediction="Over the next four weeks, <strong>70% likelihood that oil prices continue rising and global indices continue falling</strong> — since Quagmire + Catastrophe jointly have ~70% probability and both imply major oil-supply disruption.",
            audits=[
                dict(meta="3 Mar 2026 · #82", url=tg(82),
                     text="Within 24 hours — crude oil +5.84%, Brent +5.63%, gasoline +4.39%, heating oil +10.75%, coal +8.61%. Driven by the official closure of the Strait of Hormuz."),
                dict(meta="3 Mar 2026 · #85", url=tg(85),
                     text="Asian markets all red — KOSPI −7.24%, Nikkei −3.06%, Shenzhen −3.07%. Asian dependence on Hormuz oil makes them the hardest hit; no quick war end in sight."),
                dict(meta="9 Mar 2026 · #90", url=tg(90),
                     text="Materialising — Asian markets hit hardest; no diplomatic off-ramp in sight; IR military defeat implausible near-term; war likely 3–4+ weeks."),
                dict(meta="9 Mar 2026 · #94", url=tg(94),
                     text="Oil-price surge spooks Trump — switches from &ldquo;as long as it takes&rdquo; to &ldquo;pretty quick&rdquo;. Trump likely to rely on a show of force as a face-saving measure. Calculation shifts toward off-ramp/ceasefire (not a peace deal)."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2026", date="3 March 2026", datetime="2026-03-03",
    subhead="Iran supreme leader succession",
    sources=[("Telegram #83", tg(83)),
             ("Iran Succession Bayesian Expert Report", "posts/Iran_Succession_Bayesian_Expert_Report_v2.html")],
    items=[
        dict(
            prediction="An accuracy-weighted consensus of 14 Iran specialists &mdash; 76 scored predictions stretching back to 2006 &mdash; ranks succession candidates by probability. The report produces a calibrated distribution over ten candidate outcomes (published in the linked report).",
            audits=[
                dict(meta="3 Mar 2026 · #87", url=tg(87),
                     text="Polymarket pushed Mojtaba's odds to 72% after an Iran International post. Track record of Iran International is ~50–70% accurate on similar articles, and they have been debunked on highly similar pieces. Correct estimate: <strong>Mojtaba at ~30%</strong> — buying &ldquo;no&rdquo; is the edge."),
                dict(meta="5 Mar 2026 · #88", url=tg(88),
                     text="Updated — NYT reports Mojtaba as &ldquo;front runner&rdquo;, Reuters reports Assembly of Experts pushback. Revised range: <strong>Mojtaba at 40–50%</strong>, which is where Polymarket is now."),
                dict(meta="9 Mar 2026 · #92", url=tg(92),
                     text="Mojtaba confirmed as Supreme Leader — IRGC-backed continuity rather than disruption."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2026", date="3 March 2026", datetime="2026-03-03",
    subhead="Polymarket Iran regime-fall mispricing",
    sources=[("Telegram #84", tg(84))],
    items=[
        dict(
            prediction="Polymarket &ldquo;Iranian regime falls by June 30&rdquo; has risen from ~50% to 54% — but the expert model puts the odds significantly lower (<strong>&lt;10%</strong>). Buying &ldquo;no&rdquo; is a safe bet.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="7 March 2026", datetime="2026-03-07",
    subhead="Long-term — MAGA, Tucker Carlson, and the Israeli lobby",
    sources=[("Telegram #89", tg(89))],
    items=[
        dict(
            prediction="If the Iran war turns longer, messier, and costlier, the Republican/MAGA base's support will dip. Tucker-Carlson-style anti-war Republican figures will benefit. With Democratic-left already critical of Israel, Republicans were the Israeli lobby's most secure backstop &mdash; so if the Tucker camp wins over Republicans, this spells serious trouble for Israel and the Israeli lobby in the years ahead.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="16 March 2026", datetime="2026-03-16",
    subhead="Israeli nuclear use",
    sources=[("Telegram #108", tg(108)),
             ("Nuclear Threshold Assessment — Day 15", "posts/Nuclear_Threshold_Assessment_Day15.html")],
    items=[
        dict(
            prediction="The probability of Israel using nuclear weapons as a direct consequence of failing to change Iran's regime is <strong>very low, but not zero</strong> &mdash; 13-expert Bayesian panel puts it at <strong>~3.1%</strong>, 90% credible interval [0.5%, 9.0%].",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="16 March 2026", datetime="2026-03-16",
    subhead="US ground forces in Iran",
    sources=[("Telegram #109–110", tg(109)),
             ("Ground Troops Probability Assessment", "posts/Ground_Troops_Iran_Probability_Assessment_v3.html")],
    items=[
        dict(
            prediction="<strong>Any US boots on the ground</strong> (SOF, island, or conventional) during Operation Epic Fury: <strong>~19%</strong>, 95% CI [9%, 33%]. Three independent evidence lines &mdash; expert-accuracy audit, first-principles political statements, Bayesian-discounted prediction markets &mdash; converge at this band.",
            audits=[
                dict(meta="26 Mar 2026 · #126", url=tg(126),
                     text="Revised upward — now <strong>&gt;50%</strong> likelihood of a US ground operation, though scale and aims uncertain. Strait cannot be opened by bombing alone; US is moving more forces to the region. Small-scale operation (paratroopers) more likely than large-scale, but nothing is off the table if Trump feels cornered."),
                dict(meta="2 Apr 2026 · #129", url=tg(129),
                     text="Structural forecast (64-expert panel) — Q2: Ground forces by June 30: <strong>68% Yes</strong>, resolves Yes."),
            ],
        ),
        dict(
            prediction="<strong>Full conventional invasion</strong> (Iraq-2003 scale): <strong>~4%</strong>, 95% CI [1%, 9%].",
            audits=[],
        ),
        dict(
            prediction="Occupying Kharg (or another Iranian southern island) will <strong>not serve any of the US strategic goals</strong> — neither opening the Strait nor controlling Iranian oil for the market. Iran never used Kharg to close the Strait; occupying it would prompt Iran to simply shut off the submarine pipelines (de-facto embargo), and GCC retaliation risk.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="19 March 2026", datetime="2026-03-19",
    subhead="Oil prices and the political red lines",
    sources=[("Telegram #115", tg(115)),
             ("Iran Oil Special Report", "posts/Iran_Oil_Special_Report.html")],
    items=[
        dict(
            prediction="US gas is $3.84/gal, diesel $5.04, Brent $109 — all three sides read the same price signal differently. US: unsustainable drain. Iran: most effective weapon, keep the Strait closed. Israel: countdown clock on American political will.",
            audits=[
                dict(meta="20 Mar 2026 · #117", url=tg(117),
                     text="Gas was $2.927 on Feb 28 and is $3.884 today — 96¢ / 33% in 20 days, sharpest increase in more than two decades. Every American sees the number at every corner. >$4.00 makes gas prices politically unsustainable. The strategic question: can Iran keep the Strait closed, or can the US open it militarily?"),
            ],
        ),
        dict(
            prediction="Four war-ending scenarios follow from four oil-price trajectories (published in the linked report). We are currently between the first two.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="21 March 2026", datetime="2026-03-21",
    subhead="Iran's ordnance firing rate &mdash; strategic rationing, not destruction",
    sources=[("Telegram #118–119", tg(118)),
             ("Iran Daily Ordnance Tracker", "posts/Iran_DailyCount_ByCountry_v8.html")],
    items=[
        dict(
            prediction="Iran's missile-and-drone firing rate over days 1–22 (1,466 missiles + 3,522 drones = 4,988 total, declining from ~540/day to ~80/day) is <strong>more consistent with strategic attritional rationing than with the &ldquo;&gt;80% of launchers destroyed&rdquo; narrative</strong>. Iran's firing capabilities have sustained the bombing so far.",
            audits=[
                dict(meta="6 Apr 2026 · #134", url=tg(134),
                     text="Fully validated over 38 days — <strong>1,725+ ballistic missiles fired in 38 days</strong>, sustained floor of 20+ BMs/day, 7-day average consistent with rationing. Iran's SRBM fleet (estimated 5,000–8,000 rounds pre-war) has remained largely intact. Iran has runway in months; GCC interceptor stocks do not. See the &ldquo;Missile That Wasn't Destroyed&rdquo; fact brief."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2026", date="24 March 2026", datetime="2026-03-24",
    subhead="How the war ends &mdash; aggregate model",
    sources=[("Telegram #122–123", tg(122)),
             ("How Does the Iran War End", "posts/747fd16f-2d22-4532-ad84-e0c5b816ea46.html")],
    items=[
        dict(
            prediction="<strong>Strategic outcome.</strong> Iran is favoured to win strategically with <strong>~47%</strong> likelihood; US/Israel-favoured <strong>~28%</strong>; stalemate <strong>~25%</strong> (64-expert accuracy-weighted model, τ=0.20, κ=5.0).",
            audits=[],
        ),
        dict(
            prediction="<strong>Trajectory.</strong> Likelihood of: war ending quickly <strong>24%</strong>; major ground invasion <strong>34%</strong>; Hormuz reopened by force <strong>22%</strong>; major civilian-infrastructure strikes <strong>47%</strong>.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="25 March 2026", datetime="2026-03-25",
    subhead="US–Iran negotiations &mdash; real or posturing?",
    sources=[("Telegram #124", tg(124))],
    items=[
        dict(
            prediction="There are <strong>no serious US–Iran negotiations underway</strong>, despite Trump's rhetoric. Iran is not interested — views talks as giving Trump time to re-arm; strategic calculation is that raising oil/gas prices forces US withdrawal. Meanwhile, US has quietly amassed ~50,000 troops including paratroopers in the region — actions signal digging in.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="26 March 2026", datetime="2026-03-26",
    subhead="War duration",
    sources=[("Telegram #125", tg(125))],
    items=[
        dict(
            prediction="The war is <strong>highly likely to last &gt;2 months</strong>, quite possibly much longer. Neither side can end it with a quick decisive victory; Iran is in survival mode with maximalist demands; even unilateral US cessation doesn't open Hormuz without humiliating US/GCC concessions; Israel would likely continue on its own by targeting civilian infrastructure.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="2 April 2026", datetime="2026-04-02",
    subhead="Structural forecast &mdash; five resolvable questions",
    sources=[("Telegram #128", tg(128)),
             ("Structural Forecast Briefing", "posts/da975520-bf35-4c71-a457-9289db15b22c.html")],
    items=[
        dict(
            prediction="<strong>Q1.</strong> Ceasefire by June 30: <strong>15% Yes</strong> &mdash; resolves No (cross-ideological consensus).",
            audits=[],
        ),
        dict(
            prediction="<strong>Q2.</strong> US ground forces by June 30: <strong>68% Yes</strong> &mdash; resolves Yes (mixed consensus).",
            audits=[],
        ),
        dict(
            prediction="<strong>Q3.</strong> Hormuz transits &ge; 50% of pre-war by Sept 30: <strong>48% Yes</strong> &mdash; toss-up, panel divergence.",
            audits=[],
        ),
        dict(
            prediction="<strong>Q4.</strong> Brent &gt; $150 by July 31: <strong>52% Yes</strong> &mdash; lean Yes, conditional.",
            audits=[],
        ),
        dict(
            prediction="<strong>Q5.</strong> Iranian regime survives through Dec 31: <strong>92% Yes</strong> &mdash; strongest consensus.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="4 April 2026", datetime="2026-04-04",
    subhead="Critical civilian infrastructure &mdash; by September 30",
    sources=[("Telegram #130–131", tg(130)),
             ("Critical Infrastructure Escalation Analysis", "posts/12024222-8ebc-4e9a-81fb-8db7598f4490.html")],
    items=[
        dict(
            prediction="<strong>Power &amp; grid.</strong> Strikes on the 400 kV national transmission backbone or thermal plants (≥ 500 MW) by Sept 30: <strong>85%</strong> — near-certain. Coalition forces have already severed power to neutralise underground nuclear/missile sites; expanding to civilian-linked nodes.",
            audits=[],
        ),
        dict(
            prediction="<strong>Oil &amp; gas.</strong> Strikes on Kharg Island or major refineries by Sept 30: <strong>45%</strong> — a coin flip held in tension. Iran's &ldquo;Symmetry Doctrine&rdquo; deters; Trump's ultimatum and the 95%-closed Strait create an escalating credibility trap.",
            audits=[],
        ),
        dict(
            prediction="<strong>Water.</strong> Strikes on Iranian dams or desalination plants by Sept 30: <strong>15%</strong> — the absolute red line; reciprocal annihilation of Gulf water infrastructure would follow.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="6 April 2026", datetime="2026-04-06",
    subhead="The April 7 escalation window &mdash; Power Plant Day",
    sources=[("Telegram #133", tg(133)),
             ("The Labyrinth of Bad Options", "posts/976fb517-fc7c-4449-afe0-014eb0533899.html")],
    items=[
        dict(
            prediction="<strong>Rung D &mdash; Postponement / stand-down: 48%.</strong> No new deliberate strikes on civilian infrastructure; strikes confined to military combatants.",
            audits=[],
        ),
        dict(
            prediction="<strong>Rung C &mdash; Transport-only escalation: 30%.</strong> Strikes on civilian transport (bridges, highways, rail) but no power/water/major oil-gas — the lowest civilian rung that still looks like follow-through.",
            audits=[],
        ),
        dict(
            prediction="<strong>Rung B &mdash; Domestic grid escalation: 14%.</strong> Strikes on Iranian power generation or municipal water infrastructure (the rung Trump's rhetoric explicitly points to).",
            audits=[],
        ),
        dict(
            prediction="<strong>Rung A &mdash; Global energy escalation: 8%.</strong> Strikes on major oil/gas/petrochemical infrastructure — refineries, Kharg, South Pars. &ldquo;The rung that detonates the world economy.&rdquo;",
            audits=[],
        ),
        dict(
            prediction="<strong>Combined forecast.</strong> For the narrow April 7–14 window, backing down or symbolic hits is more likely than literal energy/grid follow-through &mdash; the structural incentives still point away from Power Plant Day. Not contradictory with the longer-horizon 85% grid probability, since that runs through September 30.",
            audits=[],
        ),
    ],
))

# ============================================================
# HTML generator
# ============================================================

def render_source(label, url):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'

def render_sources(sources):
    links = "".join(render_source(l, u) for l, u in sources)
    return f'<span class="sources"><span class="label">sources</span>{links}</span>'

def render_audit(a):
    return (f'<p class="audit"><span class="audit-meta">'
            f'<a href="{a["url"]}" target="_blank" rel="noopener">{a["meta"]}</a>'
            f'</span>{a["text"]}</p>')

def render_audits(audits):
    if not audits:
        return ""
    return '<div class="audits">' + "".join(render_audit(a) for a in audits) + '</div>'

def render_item(item):
    return (f'<div class="pred-item">'
            f'<p class="prediction">{item["prediction"]}</p>'
            f'{render_audits(item["audits"])}'
            f'</div>')

def render_group(g):
    items = "".join(render_item(it) for it in g["items"])
    return (f'<section class="pred-group">'
            f'<header>'
            f'<h3>{g["subhead"]}</h3>'
            f'<p class="meta">'
            f'<time datetime="{g["datetime"]}">{g["date"]}</time>'
            f'{render_sources(g["sources"])}'
            f'</p>'
            f'</header>'
            f'{items}'
            f'</section>')

def build_body():
    out = []
    current_year = None
    for g in groups:
        if g["year"] != current_year:
            out.append(f'<h2 class="year">{g["year"]}</h2>')
            current_year = g["year"]
        out.append(render_group(g))
    return "\n".join(out)

# ============================================================
# Page shell
# ============================================================

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unmitigated Wisdom — Prediction Ledger</title>
<meta name="description" content="An atomized prediction ledger — every falsifiable forecast from the Unmitigated Wisdom channel and its reports, one claim per entry, sourced and audited in threads.">
<link rel="stylesheet" href="site.css">
</head>
<body>
<div class="wrap">

  <nav class="top">
    <a class="brand" href="index.html" aria-label="Unmitigated Wisdom">
      <img src="logos/07_strict_monotonic_site_accent_split.svg" alt="Unmitigated Wisdom">
    </a>
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="ledger.html" aria-current="page">Ledger</a></li>
      <li><a href="mixture-of-experts.html">Mixture of Experts</a></li>
      <li><a href="reports.html">Reports</a></li>
    </ul>
  </nav>

  <header class="masthead">
    <h1>Prediction Ledger</h1>
    <p class="tagline">One falsifiable forecast per entry, grouped under the post or report that made it, with audits of each forecast in its own thread.</p>
    <a class="channel-link" href="https://t.me/unmitigated_wisdom" target="_blank" rel="noopener">t.me/unmitigated_wisdom →</a>
  </header>

  <div class="ledger-intro">
    Every forecast with a source and an audit trail. A single post or report often contains several distinct predictions &mdash; each is listed as its own item under the originating date. Sources link to the Telegram message where the claim was first made, and to any report that published or refined it. Validations, revisions, and resolutions live in threads beneath the prediction they apply to.
  </div>

"""

FOOT = """
  <footer class="site">
    © 2020–2026 Unmitigated Wisdom · <em>only theoretical frameworks that predict the future can be taken seriously in describing the past.</em>
  </footer>

</div>
</body>
</html>
"""

if __name__ == "__main__":
    import sys
    out = HEAD + build_body() + FOOT
    path = "/Users/amirjoudaki/Codes/unmitigated-wisdom.github.io/ledger.html"
    with open(path, "w") as f:
        f.write(out)
    sys.stdout.write(f"wrote {path} ({len(out.splitlines())} lines, {len(groups)} groups, "
                     f"{sum(len(g['items']) for g in groups)} atomic predictions)\n")
