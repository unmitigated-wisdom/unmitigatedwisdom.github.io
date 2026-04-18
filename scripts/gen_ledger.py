#!/usr/bin/env python3
"""
Generate the atomized prediction ledger for Unmitigated Wisdom.

Each item is one falsifiable forecast. The `prediction` sentence carries
the subject + claim + metric inline wherever possible. An optional
`resolution` field spells out the explicit test criterion for cases
where the check is non-obvious or multi-part.
"""

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
            prediction="<strong>Short term.</strong> US equity markets will experience further major sell-offs (single-day declines of roughly 5%+) during the weeks in which daily US COVID-19 case growth continues to rise in the Italy-like way, followed by partial recoveries once daily case growth stabilises.",
            resolution="Compare S&amp;P 500 and Dow Jones daily returns against US daily case-growth inflections, March–May 2020.",
            audits=[
                dict(meta="9 May 2020 · #24", url=tg(24),
                     text="Accurate — major US market drops coincided with case reports, followed by partial recoveries once statistics stabilised."),
            ],
        ),
        dict(
            prediction="<strong>Mid term.</strong> Each time a major authority (IMF, ECB, the US, or China) publishes a negative or near-zero Q1/Q2 2020 GDP print, US equity markets will see a further major sell-off (roughly 5%+ single-day drop, or comparable drawdown across the week of release).",
            resolution="S&amp;P 500 / Dow Jones behaviour on or within the week of each major Q1/Q2 2020 GDP release.",
            audits=[
                dict(meta="9 May 2020 · #24", url=tg(24),
                     text="Partially accurate — unemployment and oil prices point to a major depression looming; awaiting full market reaction."),
            ],
        ),
        dict(
            prediction="<strong>Long term.</strong> Within 12–18 months (by late 2021), doomsday macro scenarios will have failed to materialise and US equity indices will have fully recovered to their February 2020 pre-COVID highs, possibly eclipsing them.",
            resolution="S&amp;P 500 / Dow Jones closing levels between September 2021 and March 2022 vs. the Feb 2020 peak.",
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
            prediction="<strong>World.</strong> Global real GDP growth for calendar year 2020 will come in at or below 0.5% (i.e. effectively zero or negative).",
            resolution="IMF World Economic Outlook or World Bank final 2020 real world GDP growth figure.",
            audits=[
                dict(meta="25 Mar 2020 · #18", url=tg(18),
                     text="Gloomier update — now forecasting world GDP at −5% to −2%."),
                dict(meta="7 Jul 2020 · #41", url=tg(41),
                     text="European Commission validates a slow recovery — EU GDP −8.7% in 2020, +6.1% in 2021, still below pre-outbreak by end of 2021 even absent a second wave."),
            ],
        ),
        dict(
            prediction="<strong>Europe.</strong> European economies will be the hardest-hit major region in 2020, with full-year 2020 real GDP contracting by 2–5% (Euro Area or EU-27 aggregate).",
            resolution="Eurostat / IMF Euro Area and EU-27 real GDP growth for CY2020.",
            audits=[
                dict(meta="25 Mar 2020 · #18", url=tg(18),
                     text="Revised steeper — Italy specifically −10% or worse; the hardest-hit regions (Veneto, Lombardy) account for ~40% of Italy's economy."),
            ],
        ),
        dict(
            prediction="<strong>East Asia.</strong> Far-eastern economies (China, Japan, South Korea, Taiwan, Vietnam) will be the best-performing major region in 2020, measured by aggregate or median real GDP growth.",
            resolution="IMF 2020 real GDP growth for East Asian majors vs. other world regions.",
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
            prediction="A US federal stimulus will pass in the coming weeks with bailout provisions covering &ldquo;too big to fail&rdquo; corporates including Boeing (BA), Exxon (XOM), and Chevron (CVX), and those three stocks will rise immediately on signing.",
            resolution="Passage of CARES Act or equivalent; BA/XOM/CVX single-day return on signing day.",
            audits=[
                dict(meta="24 Mar 2020 · #14", url=tg(14),
                     text="Confirmed — after the $2-trillion bailout was signed, the named companies hugely outperformed the indices. Screenshots at #16: Chevron +18.1%, Boeing +16.5%, Dow +9.0% on the day."),
                dict(meta="26 Mar 2020 · #20", url=tg(20),
                     text="Indices up 5% on signing expectation; airlines, planes, shale oil, post, and hotels all carved out and expected to outperform once signed."),
            ],
        ),
        dict(
            prediction="American Airlines (AAL) will receive federal bailout funding in the coming stimulus, and its stock will surge on or immediately after signing.",
            resolution="Federal funding directed at AAL; AAL single-day return on signing day.",
            audits=[
                dict(meta="24 Mar 2020 · #16", url=tg(16),
                     text="Confirmed — American Airlines +40.3% on the day of the rebound."),
            ],
        ),
        dict(
            prediction="On the day the US stimulus bill is signed into law, the major US equity indices will post a temporary surge (single-day gain of 5%+).",
            resolution="S&amp;P 500 / Dow Jones single-day return on CARES Act signing day.",
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
            prediction="Senator Richard Burr (R-NC) will resign from his Senate seat before his term ends in January 2023.",
            resolution="Formal Senate resignation record for Richard Burr by 3 January 2023.",
            audits=[
                dict(meta="14 May 2020 · #29", url=tg(29),
                     text="Revised — he stepped down from the Senate Intelligence chair and won't run for re-election, but is not resigning the seat early (a Democratic governor would appoint a temporary replacement)."),
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
            prediction="On Monday 30 March 2020 (the next market open), the S&amp;P 500 and Dow Jones will drop 5 ± 3% (between 2% and 8% intraday).",
            resolution="S&amp;P 500 and Dow Jones open-to-close return on 30 March 2020.",
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
            prediction="Oil and gas majors such as Exxon (XOM) will return 50–80% over the 1–2 year window from 9 May 2020.",
            resolution="XOM total return (price + dividends) from 9 May 2020 to a date between 9 May 2021 and 9 May 2022.",
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
            prediction="Trump will lose the November 2020 US presidential election to the Democratic nominee.",
            resolution="Certified 2020 US presidential election outcome.",
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
            prediction="Biden will win the 2020 election with a 6–10% popular-vote margin and 330–370 electoral-college votes.",
            resolution="Certified 2020 popular-vote margin and EC vote count.",
            audits=[
                dict(meta="12 Nov 2020 · #49", url=tg(49),
                     text="Biden projected 306 EC votes and 4–5% popular-vote margin after all votes counted — outside predicted intervals, but not far off."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2020", date="14 May 2020", datetime="2020-05-14",
    subhead="Roche — Genentech mid/long-term",
    sources=[("Telegram #28", tg(28))],
    items=[
        dict(
            prediction="Roche Holding (RHHBY / ROG.SW) will outperform the STOXX Europe 600 Health Care index on a total-return basis over the 1–5 year window from 14 May 2020 — driven by Genentech's senior-geneticist hires (Aviv Regev, Mark McCarthy) and its UK-government COVID-19 antibody partnership.",
            resolution="Roche total return vs. STOXX Europe 600 Health Care from 14 May 2020 over 1Y, 3Y, and 5Y.",
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
            prediction="US unemployment will fall substantially over the next 1–2 months as roughly 90% of the reported job losses were temporary and many businesses reopen, and US equity indices will rise in sympathy. Less-essential businesses face worse recovery odds, including bankruptcy risk.",
            resolution="BLS monthly unemployment rate for May–July 2020; S&amp;P 500 / Dow Jones returns over the same window.",
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
            prediction="Probability that US Congress passes a stimulus bill extending pandemic unemployment benefits before end-August 2020: roughly 50% — Republicans dislike welfare, Democrats dislike tax cuts, election pressure cuts both ways.",
            resolution="Enactment of any federal COVID unemployment-benefit extension between 10 Jul and 31 Aug 2020.",
            audits=[
                dict(meta="7 Aug 2020 · #44", url=tg(44),
                     text="Revised up — weekly household payments will mostly be extended; deal likely within 1–2 weeks due to economic damage from delay. Markets will respond positively."),
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
            prediction="Bitcoin and the broader crypto market will experience a peak-to-trough drawdown of at least 30% within the next 3–9 months (i.e. by late 2021), before resuming an upward trend whose subsequent all-time high may exceed the pre-correction peak.",
            resolution="Bitcoin price and total crypto market-cap peak-to-trough drawdown during 22 Feb 2021 – 31 Dec 2021.",
            audits=[
                dict(meta="19 May 2021 · #51", url=tg(51),
                     text="Confirmed in direction — crypto market cap shrunk 35% since the post; Musk, the US, and China all contributing to volatility. Long-term positive, but investing now likely locks capital for 2–3 years."),
                dict(meta="19 May 2021 · #52", url=tg(52),
                     text="ETH2 implementation is the biggest wildcard — successful → new highs; botched → disaster; delayed → sideways. Long-term determinant is clean energy for Bitcoin mining."),
                dict(meta="25 Jun 2021 · #55", url=tg(55),
                     text="Fully confirmed — Bitcoin and others down ~50%. Still &ldquo;when, not if&rdquo; Bitcoin surpasses $100k (per JP Morgan's price targets)."),
                dict(meta="16 Jul 2021 · #56", url=tg(56),
                     text="Government crackdowns actually increase mining rewards for remaining miners; the cycle only breaks if miners are few enough for double-spending or if dirty-mining backlash overrides supply limits."),
                dict(meta="17 Nov 2022 · #75", url=tg(75),
                     text="FTX collapse — crypto's only product was absorbing surplus liquidity (correlated with inflation, unlike gold). Market was overdue for this correction."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2021", date="27 May 2021", datetime="2021-05-27",
    subhead="Energy transition — incumbents vs. renewables",
    sources=[("Telegram #53", tg(53))],
    items=[
        dict(
            prediction="Over the 2021–2031 horizon, incumbent auto and fossil-fuel energy majors (market-cap-weighted index) will underperform a market-cap-weighted basket of pure-play renewable-energy and EV tech companies on a total-return basis.",
            resolution="Compare XLE (energy sector) and legacy automakers vs. ICLN / TAN / LIT / QCLN over 2021–2031.",
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
            prediction="Elon Musk will display an increasingly Trump-adjacent political-media style (Twitter/X combat, cult of personality, self-serving use of platforms) over the next 2–5 years, increasing his net political footprint. His intelligence and engineering track record keep open the alternative that he transitions to a post-Microsoft Bill Gates role instead.",
            resolution="Musk's X posting pattern, endorsements and political spending, and role in US politics through 2026.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2021", date="29 July 2021", datetime="2021-07-29",
    subhead="Infrastructure bill — stocks that will rise",
    sources=[("Telegram #57", tg(57))],
    items=[
        dict(
            prediction="Astec Industries (ASTE), Martin Marietta (MLM), Construction Partners (ROAD), Caterpillar (CAT), and Manitowoc (MTW) will outperform the Dow Jones Industrial Average over the 3–6 months following passage of the ~$1T US infrastructure bill.",
            resolution="Named tickers' total return vs. DJIA from 29 Jul 2021 over 3M and 6M windows.",
            audits=[
                dict(meta="16 Aug 2021 · #58", url=tg(58),
                     text="Validated early — named companies up 4–23% since the post, largely outperforming indices (Dow +2%). Martin Marietta +9%."),
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
            prediction="Democrats will lose the US House majority in the November 2022 midterms. The Senate will be a 50-50 toss-up. The Georgia Senate race will be particularly uphill. Downstream: if both chambers flip, real prospect of Biden impeachment proceedings and obstruction of Ukraine aid.",
            resolution="Composition of the 118th Congress; presence of formal impeachment proceedings against Biden; Ukraine aid legislation outcomes through 2023.",
            audits=[
                dict(meta="3 Nov 2021 · #65", url=tg(65),
                     text="Partial early validation — disastrous Democratic performance in Virginia and New Jersey; enthusiasm gap likely to persist."),
                dict(meta="25 Jun 2022 · #70", url=tg(70),
                     text="Dobbs unlikely to rescue Democrats — national polls bias liberal; Democrats historically bad at converting sentiment into political ammunition; economy remains dominant."),
                dict(meta="6 Nov 2022 · #73", url=tg(73),
                     text="Restated — Democrats face disastrous midterms; House likely to flip; Senate a 50-50 toss-up; possible consequences include Biden impeachment and Ukraine aid hindered."),
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
            prediction="The JCPOA will not be re-enacted or replaced by an equivalent US–Iran nuclear agreement during Biden's first term (through 20 January 2025); without a durable Senate majority Biden cannot provide the legislative assurances Tehran requires, the window closes, and US–Iran tensions escalate.",
            resolution="Status of any US–Iran nuclear agreement on 20 January 2025.",
            audits=[
                dict(meta="19 Mar 2022 · #67", url=tg(67),
                     text="JCPOA fate hangs again — Russia is now the most likely obstructor (Iran's oil/gas would limit Russia-sanction damage). Still more likely than not (>50%) that a deal is reached in the coming days."),
                dict(meta="23 Aug 2022 · #71", url=tg(71),
                     text="A JCPOA deal looks closer than ever — if reached, oil prices plummet; indices a sure bet to rise; exceptions are oil beneficiaries like Aramco and Exxon."),
                dict(meta="23 Aug 2022 · #72", url=tg(72),
                     text="Limiting factors: companies hesitant to buy Iranian oil; Iran–Russia partnership restrains Iran; underlying tensions not subsiding."),
                dict(meta="6 Nov 2022 · #74", url=tg(74),
                     text="Confirmed — JCPOA negotiations nearly dead after Iran's protest crackdown; no real prospect of re-enactment in the near future, if ever."),
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
            prediction="Trump will run in the 2024 US presidential election and will lose &mdash; either the Republican primary or the general. The main reason Biden won in 2020 was Trump himself; Trump's Russia stance, now a focal point in US politics, further hurts him.",
            resolution="Trump's 2024 candidacy status + certified 2024 presidential election outcome.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2022", date="26 March 2022", datetime="2022-03-26",
    subhead="Russia–Ukraine — world-economy ramifications",
    sources=[("Telegram #69", tg(69))],
    items=[
        dict(
            prediction="The Russian invasion of Ukraine will drive sustained global energy- and food-price inflation through 2023, pushing major economies into recession or near-recession — primarily because Russia supplies ~11% of global energy and Russia + Ukraine supply ~25% of global wheat. Biden's &ldquo;cannot stay in power&rdquo; rhetoric raises Putin's existential stakes and makes settlement harder, so the war extends.",
            resolution="G20-weighted CPI inflation 2022–2023, G7 recession indicators, and status of war as of end-2023.",
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
            prediction="Kamala Harris's most likely 2024 VP pick is Josh Shapiro (D-PA) — high-approval governor of a swing state, fills the Biden-style blue-collar middle-class role. Mark Kelly (D-AZ) is a secondary possibility.",
            resolution="Harris's announced VP selection in August 2024.",
            audits=[],
        ),
    ],
))

# ============================================================
# 2026 — Iran War
# ============================================================

groups.append(dict(
    year="2026", date="1 March 2026", datetime="2026-03-01",
    subhead="Iran regime survival vs. the bombing campaign",
    sources=[("Telegram #78", tg(78)),
             ("Telegram #79 — Bayesian priors", tg(79)),
             ("Bayesian 15-Expert Report", "posts/Bayesian_15Expert_Report.html"),
             ("Who Should We Believe About Iran", "posts/Who_Should_We_Believe_About_Iran.html")],
    items=[
        dict(
            prediction="<strong>Regime change.</strong> The Islamic Republic's governing structure (Supreme Leader + IRGC + Guardian Council) will survive the 2026 US/Israel bombing campaign. Probability of regime change strictly from air campaign alone: &lt; 10%. The IRGC is being forced into existential-survival mode; protest crackdowns will intensify rather than crumble the state.",
            resolution="Existence of the Islamic Republic as the ruling government of Iran on 31 December 2026 (no successor state, no collapse of central authority).",
            audits=[
                dict(meta="2 Mar 2026 · #79", url=tg(79),
                     text="Bayesian priors — Quick Win 9.2%, Quagmire 52.3%, Off-Ramp 21.9%, Catastrophe 16.6%. Combined >90% probability of regime surviving in some form."),
                dict(meta="9 Mar 2026 · #92", url=tg(92),
                     text="Day 10 — Quick Win falls to 3–5%; Quagmire 42–46%, Catastrophe 35–38%, Off-Ramp 10–13%. Mojtaba confirmed as Supreme Leader (IRGC continuity)."),
                dict(meta="11 Mar 2026 · #96", url=tg(96),
                     text="Day 13 — Quick Win 2–4%, Quagmire 38–42%, Catastrophe 38–42% (parity for first time), Off-Ramp 13–17%."),
                dict(meta="13 Mar 2026 · #103", url=tg(103),
                     text="Day 14 — Catastrophe 42% overtakes Quagmire 36% as modal scenario for the first time; Off-Ramp 15%, Quick Win 2%."),
                dict(meta="15 Mar 2026 · #105", url=tg(105),
                     text="Day 15 — Catastrophe 45%, Quagmire 31%, Off-Ramp rises to 18% (first time since Day 1), Quick Win 2%."),
            ],
        ),
        dict(
            prediction="<strong>Quagmire scenario.</strong> The war will drag into prolonged attrition (lasting &gt; 90 days without decisive military or diplomatic resolution) — modal outcome at ~52% initial probability, driven by IRGC cohesion and Mojtaba continuity.",
            resolution="War still active on Day 90 without a formal ceasefire or a decisive military outcome.",
            audits=[
                dict(meta="9 Mar 2026 · #92", url=tg(92), text="Day 10 — Quagmire 42–46%, still modal."),
                dict(meta="13 Mar 2026 · #103", url=tg(103), text="Day 14 — Quagmire falls to 36%, overtaken by Catastrophe."),
                dict(meta="15 Mar 2026 · #105", url=tg(105), text="Day 15 — Quagmire 31% as Kharg ultimatum forces a decision."),
            ],
        ),
        dict(
            prediction="<strong>Catastrophic regional escalation.</strong> The war will escalate into wider regional catastrophe — defined as any of: (a) deliberate strikes on major Iranian oil/gas infrastructure (Kharg, South Pars, major refineries), (b) Houthi active entry into the Red Sea theatre with sustained anti-shipping operations, or (c) Israeli strikes on Iranian civilian infrastructure producing mass civilian casualties. Initial probability ~17%.",
            resolution="Occurrence of any of (a)/(b)/(c) by end of the war or 31 December 2026.",
            audits=[
                dict(meta="9 Mar 2026 · #92", url=tg(92), text="Day 10 — Catastrophe 35–38% (oil at $119, Iraq collapse, SF option)."),
                dict(meta="11 Mar 2026 · #96", url=tg(96), text="Day 13 — Catastrophe reaches parity with Quagmire at 38–42%."),
                dict(meta="13 Mar 2026 · #103", url=tg(103), text="Day 14 — Catastrophe 42% becomes modal."),
                dict(meta="15 Mar 2026 · #105", url=tg(105), text="Day 15 — Catastrophe 45% (UAE port threat, Kharg ultimatum, KC-135 losses)."),
            ],
        ),
        dict(
            prediction="<strong>Diplomatic off-ramp / ceasefire.</strong> A formal ceasefire or de-escalation agreement will be reached within the first 90 days of the war. Initial probability ~22%.",
            resolution="Formal ceasefire or equivalent de-escalation agreement signed or announced by Day 90 of the war.",
            audits=[
                dict(meta="9 Mar 2026 · #92", url=tg(92), text="Day 10 — Off-Ramp falls to 10–13% (Larijani: &ldquo;no talks&rdquo;)."),
                dict(meta="11 Mar 2026 · #96", url=tg(96), text="Day 13 — Off-Ramp rises to 13–17% (US asks Israel to halt energy strikes; China/Russia/France contact Tehran)."),
                dict(meta="15 Mar 2026 · #105", url=tg(105), text="Day 15 — Off-Ramp rises to 18% for the first time since Day 1 (Sacks pressure; Turkey Fidan backchannel; Kharg deal structure)."),
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
            prediction="Over the next four weeks (through 30 March 2026), there is a ~70% probability that Brent crude continues to rise and major global equity indices (S&amp;P, Euro Stoxx, Nikkei, Hang Seng) continue to fall — because Quagmire + Catastrophe jointly have ~70% probability and both imply sustained oil-supply disruption.",
            resolution="Brent crude and major global index net moves from 2 Mar to 30 Mar 2026.",
            audits=[
                dict(meta="3 Mar 2026 · #82", url=tg(82),
                     text="Within 24 hours — crude oil +5.84%, Brent +5.63%, gasoline +4.39%, heating oil +10.75%, coal +8.61%. Driven by official closure of the Strait of Hormuz."),
                dict(meta="3 Mar 2026 · #85", url=tg(85),
                     text="Asian markets all red — KOSPI −7.24%, Nikkei −3.06%, Shenzhen −3.07%. Asian dependence on Hormuz oil makes them hardest hit."),
                dict(meta="9 Mar 2026 · #90", url=tg(90),
                     text="Materialising — Asian markets hit hardest; no diplomatic off-ramp in sight; war likely 3–4+ weeks."),
                dict(meta="9 Mar 2026 · #94", url=tg(94),
                     text="Oil-price surge spooks Trump — switches from &ldquo;as long as it takes&rdquo; to &ldquo;pretty quick&rdquo;. Calculation shifts toward off-ramp/ceasefire (not peace deal)."),
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
            prediction="Accuracy-weighted consensus of 14 Iran specialists (76 scored predictions back to 2006, 100,000 Monte Carlo draws) produces a calibrated probability distribution over 10 candidate outcomes for Khamenei's successor — published in the linked report.",
            resolution="Compare published per-candidate probabilities vs. the actual Supreme Leader after Khamenei's death or succession event.",
            audits=[
                dict(meta="3 Mar 2026 · #87", url=tg(87),
                     text="Polymarket pushed Mojtaba's odds to 72% after an Iran International post. Track record of Iran International ~50–70% on similar articles; they have been debunked on highly similar pieces. Correct estimate: <strong>Mojtaba at ~30%</strong> — buying &ldquo;no&rdquo; is the edge."),
                dict(meta="5 Mar 2026 · #88", url=tg(88),
                     text="Updated — NYT reports Mojtaba as &ldquo;front runner&rdquo;; Reuters reports Assembly of Experts pushback. Revised range: <strong>Mojtaba at 40–50%</strong>, which is where Polymarket now is."),
                dict(meta="9 Mar 2026 · #92", url=tg(92),
                     text="Mojtaba confirmed as Supreme Leader — IRGC-backed continuity."),
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
            prediction="The Polymarket contract &ldquo;Iranian regime falls by June 30 2026&rdquo; is mispriced at 54% — the expert-panel probability is below 10%. Buying &ldquo;no&rdquo; (shorting regime fall) has positive expected value.",
            resolution="Whether the Islamic Republic's central government is overthrown or dissolved by 30 June 2026.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="7 March 2026", datetime="2026-03-07",
    subhead="Long-term — MAGA, Tucker Carlson, and the Israel lobby",
    sources=[("Telegram #89", tg(89))],
    items=[
        dict(
            prediction="If the 2026 Iran war extends beyond 6–8 weeks and/or produces significant US casualties or economic damage, the Republican/MAGA base's support for the war will noticeably decline — and Tucker-Carlson-aligned anti-war Republican figures will capture a larger share of Republican media, primary support, and 2028 positioning. Consequence: the Israel lobby loses its most reliable political backstop, with visible policy effects (reduced aid, more conditional military support) emerging in 2027–2028.",
            resolution="Republican primary polling and 2028 candidate lineup; US public support for Israel among Republicans (Pew, Gallup) 2027–2028; US aid-to-Israel legislation 2027–2028.",
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
            prediction="Probability that Israel will use nuclear weapons against Iran as a direct consequence of failing to change Iran's regime via the 2026 campaign: <strong>~3.1%</strong>, 90% credible interval [0.5%, 9.0%] (13-expert Bayesian panel).",
            resolution="Any confirmed Israeli nuclear-weapon use against Iranian targets between 1 Mar 2026 and 31 Dec 2026.",
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
            prediction="Probability of <strong>any</strong> US ground forces operating inside Iranian territory during Operation Epic Fury (SOF, island seizure, or larger): <strong>~19%</strong>, 95% CI [9%, 33%]. Three independent evidence lines — expert-accuracy audit, first-principles extraction from political statements, Bayesian-discounted prediction markets — converge on this band.",
            resolution="Any confirmed US ground-forces presence inside Iranian territory during the war.",
            audits=[
                dict(meta="26 Mar 2026 · #126", url=tg(126),
                     text="Revised upward to <strong>&gt;50%</strong> given that the Strait cannot be opened by bombing alone and US forces are being moved in. Small-scale (paratroopers) more likely than large-scale, but nothing is off the table if Trump is cornered."),
                dict(meta="2 Apr 2026 · #129", url=tg(129),
                     text="Structural forecast (64-expert panel) — Q2: Ground forces by June 30: <strong>68% Yes</strong>, resolves Yes."),
            ],
        ),
        dict(
            prediction="Probability of a <strong>full conventional US invasion</strong> of Iran (Iraq-2003 scale, &gt;100,000 troops): <strong>~4%</strong>, 95% CI [1%, 9%].",
            resolution="Any US deployment &gt; 100,000 troops inside Iran during the war.",
            audits=[],
        ),
        dict(
            prediction="Occupying Kharg Island (or any single Iranian southern island) will <strong>not achieve</strong> either of the US's strategic goals: (1) it cannot reopen the Strait of Hormuz because Iran has never used Kharg to close it; (2) it cannot give the US control of Iranian oil, because occupying Kharg lets Iran shut off the submarine pipelines (de-facto embargo) and invites retaliation on GCC infrastructure. If attempted, oil prices and regional escalation will rise, not fall.",
            resolution="If a Kharg-occupation operation is mounted, compare post-operation Hormuz throughput and Iranian-oil-on-market volumes vs. pre-operation levels.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="19 March 2026", datetime="2026-03-19",
    subhead="Oil prices &amp; the political red lines",
    sources=[("Telegram #115", tg(115)),
             ("Iran Oil Special Report", "posts/Iran_Oil_Special_Report.html")],
    items=[
        dict(
            prediction="At current energy prices (US gas $3.84/gal, diesel $5.04, Brent $109) the three belligerents read the signal differently: the US as an unsustainable political-economic drain, Iran as its most effective weapon, Israel as a countdown clock on American political will. This divergence will drive near-term strategic behaviour more than any other single variable.",
            resolution="Public statements and operational behaviour from the three sides over the 2–6 weeks following 19 Mar 2026.",
            audits=[
                dict(meta="20 Mar 2026 · #117", url=tg(117),
                     text="Gas was $2.927 on Feb 28 and is $3.884 today — 96¢ / 33% in 20 days, the sharpest rise in over two decades. &gt;$4.00 makes gas prices politically unsustainable."),
            ],
        ),
        dict(
            prediction="The war will end via one of four oil-price-driven scenarios (full analysis in the linked report). As of 19 March, the trajectory sits between the first two. Brent will determine which scenario realises.",
            resolution="Identify which of the four linked scenarios the war actually resolves into, with Brent trajectory as the primary driver.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="21 March 2026", datetime="2026-03-21",
    subhead="Iran's ordnance firing rate — rationing, not destruction",
    sources=[("Telegram #118–119", tg(118)),
             ("Iran Daily Ordnance Tracker", "posts/Iran_DailyCount_ByCountry_v8.html")],
    items=[
        dict(
            prediction="Iran's missile-and-drone firing trajectory over days 1–22 (1,466 missiles + 3,522 drones; declining from ~540/day to ~80/day) is consistent with <strong>strategic rationing</strong> of a still-intact stockpile, not with the &ldquo;&gt;80% of launchers destroyed&rdquo; Western narrative. Prediction: Iran will continue to fire a sustained floor of &gt; 20 ballistic missiles per day for at least the next 30 days.",
            resolution="Daily ballistic-missile count from target-country MoDs vs. 20/day floor, March–April 2026.",
            audits=[
                dict(meta="6 Apr 2026 · #134", url=tg(134),
                     text="Fully validated over 38 days — 1,725+ ballistic missiles fired, sustained floor of 20+ BMs/day, 7-day average consistent with rationing. Iran's SRBM fleet (5,000–8,000 rounds pre-war) remained largely intact."),
            ],
        ),
    ],
))

groups.append(dict(
    year="2026", date="24 March 2026", datetime="2026-03-24",
    subhead="How the war ends — aggregate model",
    sources=[("Telegram #122–123", tg(122)),
             ("How Does the Iran War End", "posts/747fd16f-2d22-4532-ad84-e0c5b816ea46.html")],
    items=[
        dict(
            prediction="<strong>Strategic outcome.</strong> Probabilities of war-end outcome (64-expert accuracy-weighted panel, τ=0.20, κ=5.0): Iran-favoured <strong>~47%</strong>, US/Israel-favoured <strong>~28%</strong>, stalemate <strong>~25%</strong>.",
            resolution="Classify the actual war-end outcome (see report for definitions) once the war concludes.",
            audits=[],
        ),
        dict(
            prediction="<strong>Trajectory forecasts.</strong> Within the remainder of the war: quick end <strong>24%</strong>; major US ground invasion <strong>34%</strong>; Hormuz reopened by force <strong>22%</strong>; major civilian-infrastructure strikes <strong>47%</strong>.",
            resolution="Resolve each item against the observed trajectory through the end of the war.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="25 March 2026", datetime="2026-03-25",
    subhead="US–Iran negotiations — real or posturing?",
    sources=[("Telegram #124", tg(124))],
    items=[
        dict(
            prediction="Despite Trump's rhetoric, there are <strong>no serious US–Iran negotiations</strong> underway as of 25 March 2026. Iran views talks as giving Trump re-arm time; its strategic bet is that sustained high oil/gas prices force US withdrawal. The US, meanwhile, has quietly amassed ~50,000 troops including paratroopers in the region — signalling digging in, not diplomacy.",
            resolution="Any formal or back-channel US–Iran negotiating track during 25 March – 30 April 2026 (media reports, Swiss/Qatari/Omani intermediaries, official readouts).",
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
            prediction="The 2026 Iran war will last <strong>more than two months</strong> from its start (i.e. still active past end-April 2026), and plausibly much longer — neither side can deliver a quick decisive victory, Iran's maximalist demands preclude early settlement, and even unilateral US cessation would not reopen Hormuz without humiliating US/GCC concessions. Israel would likely continue independently.",
            resolution="Status of the war on 30 April 2026.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="2 April 2026", datetime="2026-04-02",
    subhead="Structural forecast — five resolvable questions",
    sources=[("Telegram #128", tg(128)),
             ("Structural Forecast Briefing", "posts/da975520-bf35-4c71-a457-9289db15b22c.html")],
    items=[
        dict(
            prediction="<strong>Q1 — Ceasefire by 30 June 2026: 15% Yes.</strong> The panel resolves No.",
            resolution="Formal ceasefire or equivalent agreement by 30 June 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Q2 — US ground forces inside Iran by 30 June 2026: 68% Yes.</strong> Panel resolves Yes (mixed consensus).",
            resolution="Any confirmed US ground-forces presence inside Iran by 30 June 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Q3 — Strait of Hormuz transits at ≥ 50% of pre-war volume by 30 September 2026: 48% Yes.</strong> Toss-up with panel divergence.",
            resolution="Hormuz tanker-transit count or tonnage for September 2026 vs. Feb 2026 baseline.",
            audits=[],
        ),
        dict(
            prediction="<strong>Q4 — Brent crude closes above $150/bbl at any point before 31 July 2026: 52% Yes.</strong> Lean Yes, conditional on continued Hormuz disruption.",
            resolution="Brent front-month close &gt; $150 on any day 2 Apr – 31 Jul 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Q5 — Iranian regime remains in power through 31 December 2026: 92% Yes.</strong> Strongest cross-ideological consensus.",
            resolution="Islamic Republic remains the ruling government of Iran on 31 December 2026.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="4 April 2026", datetime="2026-04-04",
    subhead="Critical civilian infrastructure — by 30 September 2026",
    sources=[("Telegram #130–131", tg(130)),
             ("Critical Infrastructure Escalation Analysis", "posts/12024222-8ebc-4e9a-81fb-8db7598f4490.html")],
    items=[
        dict(
            prediction="<strong>Power &amp; grid: 85%.</strong> Deliberate US/Israeli kinetic strikes on Iran's 400 kV national transmission backbone or thermal plants ≥ 500 MW will occur at least once before 30 September 2026.",
            resolution="Confirmed kinetic strike on Iranian grid backbone or ≥500 MW thermal plant by 30 Sep 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Oil &amp; gas: 45%.</strong> Deliberate strikes on Kharg Island or major Iranian refineries will occur at least once before 30 September 2026. Coin flip — Iran's &ldquo;Symmetry Doctrine&rdquo; deters, Trump's ultimatum and 95%-closed Strait create a credibility trap.",
            resolution="Confirmed kinetic strike on Kharg or major Iranian refinery by 30 Sep 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Water: 15%.</strong> Deliberate strikes on Iranian dams or desalination plants will occur at least once before 30 September 2026. The absolute red line — would trigger reciprocal annihilation of Gulf water infrastructure.",
            resolution="Confirmed kinetic strike on Iranian dam or desalination plant by 30 Sep 2026.",
            audits=[],
        ),
    ],
))

groups.append(dict(
    year="2026", date="6 April 2026", datetime="2026-04-06",
    subhead="The April 7 escalation window — Power Plant Day",
    sources=[("Telegram #133", tg(133)),
             ("The Labyrinth of Bad Options", "posts/976fb517-fc7c-4449-afe0-014eb0533899.html")],
    items=[
        dict(
            prediction="<strong>Rung D — Postponement / stand-down: 48%.</strong> In the April 7–14 window, no new deliberate strikes on civilian infrastructure; strikes confined to military combatants (air defences, missile launchers, radars, bases).",
            resolution="Target type of any US/coalition strikes during 7–14 April 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Rung C — Transport-only escalation: 30%.</strong> In the April 7–14 window, deliberate strikes on Iranian civilian transport (bridges, highways, rail) — the lowest civilian rung that still reads as follow-through.",
            resolution="Any confirmed US/coalition strike on Iranian transport infrastructure during 7–14 April 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Rung B — Domestic grid escalation: 14%.</strong> In the April 7–14 window, deliberate strikes on Iranian power generation or municipal water infrastructure (the rung Trump's rhetoric explicitly points toward).",
            resolution="Any confirmed US/coalition strike on Iranian power or water infrastructure during 7–14 April 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Rung A — Global energy escalation: 8%.</strong> In the April 7–14 window, strikes on major Iranian oil/gas/petrochemical infrastructure — refineries, Kharg, South Pars. &ldquo;The rung that detonates the world economy.&rdquo;",
            resolution="Any confirmed US/coalition strike on Iranian oil/gas infrastructure during 7–14 April 2026.",
            audits=[],
        ),
        dict(
            prediction="<strong>Combined forecast.</strong> For the narrow April 7–14 window, backing down or symbolic hits is more likely than literal energy/grid follow-through (Rungs C+D together: ~78%). Not contradictory with the longer-horizon 85% grid probability, which runs through 30 September.",
            resolution="Which rung materialised during 7–14 April 2026.",
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

def render_resolution(item):
    res = item.get("resolution")
    if not res:
        return ""
    return f'<p class="resolution">{res}</p>'

def render_item(item):
    return (f'<div class="pred-item">'
            f'<p class="prediction">{item["prediction"]}</p>'
            f'{render_resolution(item)}'
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
    Every forecast with a source, an explicit test criterion, and an audit trail. A single post or report often contains several distinct predictions &mdash; each is listed as its own item under the originating date. Sources link to the Telegram message where the claim was first made, and to any report that published or refined it. The <em>Resolves</em> line on each entry spells out the observable that decides whether the forecast hit. Validations, revisions, and resolutions live in threads beneath the prediction they apply to.
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
    total_preds = sum(len(g['items']) for g in groups)
    with_res = sum(1 for g in groups for it in g['items'] if it.get('resolution'))
    sys.stdout.write(f"wrote {path} ({len(out.splitlines())} lines, "
                     f"{len(groups)} groups, {total_preds} atomic predictions, "
                     f"{with_res} with explicit resolution)\n")
