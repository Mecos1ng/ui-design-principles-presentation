# -*- coding: utf-8 -*-
"""Content of the YMH213 presentation: slides, speaker scripts, sources.

Used by build_presentation.py to fill the course template and to write
Kaynak_Rehberi.md (Turkish source guide).
"""

TITLE = "User Interface Design for Mobile Applications"

# IEEE references. Write {key} in the text; numbers [n] are assigned
# automatically in order of first citation (see the bottom of this file).
REFERENCES = {
    'adipat': 'B. Adipat and D. Zhang, "Interface design for mobile applications," in Proc. 11th Americas Conf. Inf. Syst. (AMCIS), Omaha, NE, USA, Aug. 2005, pp. 2281–2290.',
    'hick': 'W. E. Hick, "On the rate of gain of information," Quart. J. Exp. Psychol., vol. 4, no. 1, pp. 11–26, 1952.',
    'figmaui': 'Figma, "Seven essential UI design principles + how to use them," Figma Resource Library. Accessed: Nov. 8, 2026. [Online]. Available: https://www.figma.com/resource-library/ui-design-principles/',
    'hoober': 'S. Hoober, "How do users really hold mobile devices?," UXmatters, Feb. 18, 2013. Accessed: Nov. 8, 2026. [Online]. Available: https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php',
    'figmafitts': 'Figma, "Fitts\' law: What is it + how does it apply to UI design?," Figma Resource Library. Accessed: Nov. 8, 2026. [Online]. Available: https://www.figma.com/resource-library/fitts-law/',
    'fitts': 'P. M. Fitts, "The information capacity of the human motor system in controlling the amplitude of movement," J. Exp. Psychol., vol. 47, no. 6, pp. 381–391, 1954.',
    'apple': 'Apple Inc., "Accessibility," Human Interface Guidelines. Accessed: Nov. 8, 2026. [Online]. Available: https://developer.apple.com/design/human-interface-guidelines/accessibility',
    'm3touch': 'Google, "Accessibility designing: Structure," Material Design 3. Accessed: Nov. 8, 2026. [Online]. Available: https://m3.material.io/foundations/designing/structure',
    'm3nav': 'Google, "Navigation bar: Guidelines," Material Design 3. Accessed: Nov. 8, 2026. [Online]. Available: https://m3.material.io/components/navigation-bar/guidelines',
    'wcag': 'W3C, "Web Content Accessibility Guidelines (WCAG) 2.1," W3C Recommendation, Jun. 5, 2018. Accessed: Nov. 8, 2026. [Online]. Available: https://www.w3.org/TR/WCAG21/',
    'nnheur': 'J. Nielsen, "10 usability heuristics for user interface design," Nielsen Norman Group, Apr. 24, 1994. Accessed: Nov. 8, 2026. [Online]. Available: https://www.nngroup.com/articles/ten-usability-heuristics/',
    'nnresp': 'J. Nielsen, "Response times: The 3 important limits," Nielsen Norman Group, Jan. 1, 1993. Accessed: Nov. 8, 2026. [Online]. Available: https://www.nngroup.com/articles/response-times-3-important-limits/',
    'who': 'World Health Organization, Global Report on Health Equity for Persons With Disabilities. Geneva, Switzerland: WHO, 2022. Accessed: Nov. 8, 2026. [Online]. Available: https://www.who.int/publications/i/item/9789240063600',
    'nl': 'J. Nielsen and T. K. Landauer, "A mathematical model of the finding of usability problems," in Proc. INTERCHI \'93 Conf. Human Factors Comput. Syst., Amsterdam, The Netherlands, Apr. 1993, pp. 206–213.',
}

OUTLINE = [
    (0, "Why mobile interfaces are difficult  (Presenter 1)"),
    (0, "The framework {adipat}, cognitive load and clarity  (Presenter 1)"),
    (0, "Information presentation, layout, navigation and text  (Presenter 2)"),
    (0, "Data entry, context, feedback and accessibility  (Presenter 3)"),
    (0, "Testing, conclusion and questions  (Presenter 3)"),
]

# Each slide: title, bullets [(level, text)], speaker, script (said aloud),
# sources (shown in notes), tr (Turkish explanation for the source guide).
SLIDES = [
# ---------------------------------------------------------------- SPEAKER 1
dict(
 speaker=1,
 title="Why Are Mobile Interfaces Difficult?",
 bullets=[
  (0, "Small screen, low resolution and slow data entry {adipat}"),
  (0, "Users are often walking, talking or doing another task {adipat}"),
  (0, "Four typical problems {adipat}:"),
  (1, "Too much information on a small screen"),
  (1, "Remembering what icons and labels mean"),
  (1, "Getting lost while navigating"),
  (1, "Typing on tiny keyboards"),
  (0, "Desktop design rules do not simply work on phones {adipat}"),
 ],
 script="""Good morning everyone, and thank you for being here. Our topic today is user interface design for mobile applications. My name is [Name 1], and I am here with [Name 2] and [Name 3]. Each of us will speak for about five minutes.

How many times did you look at your phone today? Probably more times than you can count, and every time you used a user interface.

Our main source is a paper by Boonlit Adipat and Dongsong Zhang from the AMCIS conference in 2005. Phones looked very different back then, but many of its ideas are still true today.

The authors say that mobile design is hard because of the device itself. Screens were small, the resolution was low, and typing was slow. People also use their phones while walking or talking, so their attention is divided.

The paper lists four typical problems. First, too much information for a small screen. Second, users have to remember what icons and labels mean. Third, people get lost while navigating. And fourth, small keyboards need a lot of attention. So, design rules for desktop computers cannot just be copied to phones.""",
 sources=["{adipat} p. 2281 (Introduction): small screen, low resolution, inefficient data entry; the four problems (information overload, limited memory, navigation loss, cumbersome input); users distracted by other tasks such as talking and walking; desktop guidelines may not be directly applicable."],
 tr="Bu slayttaki her şey makalenin 'Introduction' bölümünden (s. 2281), kendi cümlelerimizle anlatıldı. Dört problem makalede numaralı olarak geçiyor: information overload, limited memory, navigation loss, cumbersome input. 'Telefona bugün kaç kez baktınız?' sorusu ise bizim açılış sorumuz, bir kaynağa dayanmıyor.",
),
dict(
 speaker=1,
 title="A Framework for Mobile Interface Design",
 bullets=[
  (0, "Adipat and Zhang suggest four parts to think about {adipat}:"),
  (1, "User: who is using the app?"),
  (1, "Context: where, and in what situation?"),
  (1, "Information presentation: how is content shown?"),
  (1, "Data entry: how does the user type, write or speak?"),
  (0, "Our talk follows these four parts"),
 ],
 script="""To deal with these problems, the authors propose a framework with four parts. The first part is the user. Different people have different needs, preferences and abilities. The second part is context. This means the place and the situation, for example a noisy street or a dark room. The third part is information presentation, which means how we show content on a small screen. And the fourth part is data entry, which means how people give input, for example with a keyboard or with their voice.

We built our presentation on this framework. In my part, I will talk about the user. [Name 2] will talk about information presentation, layout and readable text. Then [Name 3] will cover data entry, context, feedback and accessibility.""",
 sources=["{adipat} p. 2282, Figure 1 ('A framework of interface design for mobile applications'): user, context, information presentation, data entry methods. Also repeated in the Conclusion, p. 2288."],
 tr="Dört bileşenli çerçeve makalenin ana katkısı: s. 2282'deki Şekil 1'de çiziliyor, s. 2288'deki Sonuç bölümünde de tekrar ediliyor. Hoca 'framework nereden?' diye sorarsa 'Adipat ve Zhang, Figure 1' deyin.",
),
dict(
 speaker=1,
 title="The User: Reduce Cognitive Load",
 bullets=[
  (0, "Working memory is limited {adipat}"),
  (0, "Mobile users often do two things at once {adipat}"),
  (0, "What designers can do {adipat}:"),
  (1, "Group information in a clear hierarchy"),
  (1, "Put the most important content at the top"),
  (1, "Guide attention to one part of the screen"),
  (1, "Add a search function"),
  (0, "More choices mean slower decisions (Hick's Law) {hick}"),
 ],
 script="""Let me begin with the user and cognitive load, which means the mental effort a person needs. Our working memory is small. The paper says a good interface lets people use their memory for their task, not for the interface. On a phone this matters even more, because users often do something else at the same time, like reading a map while driving.

The authors give practical advice. Organise information in a hierarchy, so users go deeper only when they want. Put the most important information near the top. Help users focus on one part of the screen. And give them a search function.

This idea connects to Hick's Law from psychology. In 1952, William Hick showed that people need more time to make a decision when they have more choices. So we should show the main options first and move the others to a second screen.""",
 sources=["{adipat} p. 2284, section 'Cognitive Load' and Table 2: limited working memory; multiple tasks (map while driving); hierarchical structure, important information near top, focus on one part of the screen, search functions.",
          "{hick} Hick (1952): decision time increases with the number of choices."],
 tr="Bilişsel yük (cognitive load) kısmı makalenin s. 2284'teki 'Cognitive Load' başlığı ve Tablo 2'den alındı. 'Haritaya bakarken araba kullanma' örneği de makalenin kendi örneği. Hick Yasası makalede geçmiyor; biz ekledik. Kaynağı Hick'in 1952 tarihli psikoloji makalesi ({hick}).",
),
dict(
 speaker=1,
 title="Clarity, Simplicity and Visual Hierarchy",
 bullets=[
  (0, "Clarity: Where am I? What can I do? What happens next?"),
  (0, "Use short and meaningful labels {adipat}"),
  (0, "Simplicity: show only what is needed, step by step {figmaui}"),
  (0, "Visual hierarchy: font size, contrast and spacing {figmaui}"),
  (0, "Important content goes near the top {adipat}"),
  (0, "Example: the camera app has one big shutter button"),
 ],
 script="""From these ideas, we can take three simple principles. The first is clarity. A clear screen answers three questions: where am I, what can I do here, and what happens next? For example, a button that says "Pay now" is clearer than a small picture alone. The paper also says that labels should be short and meaningful.

The second principle is simplicity. Every button and every line of text should have a reason to be there. If the user does not need something on this screen, we should remove it. Figma's design guide calls a related idea progressive disclosure: show information step by step, so the screen never feels too full.

The third principle is visual hierarchy. Important things should look important. Figma's guide says we can show this with font size, contrast and spacing, and the paper also suggests putting important content near the top. Think about the camera app on your phone. The shutter button is big and in the middle, and everything else is small. You understand the screen in one second.

To sum up my part, a good mobile screen respects the user's limited attention. Now I would like to hand over to [Name 2], who will talk about information presentation and layout.""",
 sources=["{adipat} p. 2286, Table 5: 'use succinct and meaningful labels'; 'important content should be placed near the top of the hierarchy'; 'allow users to know where they are'.",
          "{figmaui} Figma, Principle 1 Hierarchy (font size and weight, contrast, spacing) and Principle 2 Progressive disclosure.",
          "Clarity questions and the camera-app example are our own summary and example."],
 tr="Kısa ve anlamlı etiketler ile önemli içeriğin üstte olması makalenin s. 2286'daki Tablo 5'inden geliyor. 'Adım adım göster' (progressive disclosure) ve 'yazı boyutu, kontrast, boşluk ile hiyerarşi' Figma'nın UI tasarım ilkeleri yazısından {figmaui}: Principle 1 ve 2. 'Neredeyim, ne yapabilirim, sonra ne olacak?' soruları ve kamera uygulaması örneği bizim kendi özetimiz ve örneğimiz. Hoca sorarsa: 'Bu, makaledeki kuralları bildiğimiz bir uygulamayla açıklamak için verdiğimiz kendi örneğimiz' deyin.",
),
# ---------------------------------------------------------------- SPEAKER 2
dict(
 speaker=2,
 title="Presenting Information on a Small Screen",
 bullets=[
  (0, "Avoid horizontal scrolling {adipat}"),
  (0, "Keep menus shallow: fewer levels, more items per level {adipat}"),
  (0, "Design the shortest path to each page {adipat}"),
  (0, "Always show users where they are {adipat}"),
  (0, "Maps and images: overview first, then zoom in {adipat}"),
 ],
 script="""Thank you, [Name 1]. Hello everyone, I am [Name 2]. My part is about the third component of the framework, information presentation. After that, I will talk about layout, navigation and readable text.

The main problem is simple: there is a lot of information, but very little space. Adipat and Zhang collect several guidelines from earlier studies. First, avoid horizontal scrolling. People are used to scrolling up and down, but scrolling left and right is easy to miss. Second, keep the menu structure shallow. It is better to have more items on one level than many levels inside each other. Third, design the shortest path to each page, so users can finish a task with only a few taps. Fourth, always show users where they are, for example by highlighting the current page. And for maps and pictures, the paper suggests giving an overview first and then letting people zoom in for more detail.""",
 sources=["{adipat} p. 2286, Table 5 (1-dimensional content): avoid horizontal scrolling; limit the depth of the menu hierarchy but expand the breadth; design for shortest path; let users know where they are. Table 5 (2-dimensional content): overview + zooming. Same page (presentation optimization): users 'simply scroll up/down (while ignore left/right scrolling)'; 'easy to miss' is our wording."],
 tr="Bu slaytın tamamı makalenin s. 2286'daki Tablo 5'inden geliyor (bilgi sunumu kuralları). Tabloda 'Limit the depth ... but expand the breadth' ifadesi var; biz bunu 'menüleri sığ tut' diye özetledik.",
),
dict(
 speaker=2,
 title="Layout: Thumb Zone and Touch Targets",
 bullets=[
  (0, "49% of people touching their phone used only one hand {hoober}"),
  (0, "Thumb zone: put frequent actions where the thumb can reach {figmafitts}"),
  (0, "Big, close targets are faster to hit (Fitts's Law) {fitts}"),
  (0, "Touch target size:"),
  (1, "Apple: 44 × 44 pt default control size {apple}"),
  (1, "Google: at least 48 × 48 dp {m3touch}"),
  (0, "Leave enough space between buttons {figmafitts}"),
 ],
 script="""Now, layout. How do people actually hold their phones? In 2013, Steven Hoober watched people using their phones in streets, airports and cafés more than a thousand times. Of the people who were touching the screen, forty-nine percent used only one hand. So the thumb does most of the work. Figma's guide on Fitts's Law calls the easy area the thumb zone. On most phones, it is the lower middle part of the screen. That is why we should put frequent actions there, and put dangerous actions, like "Delete account", in places that are harder to reach.

This is connected to Fitts's Law. In 1954, Paul Fitts showed that big targets that are close to us are faster to hit. A finger is much less exact than a mouse pointer, so buttons need to be big enough. Apple's guidelines give a default size of forty-four by forty-four points for controls on the iPhone. Google's Material Design says touch targets should be at least forty-eight by forty-eight density-independent pixels. Figma also reminds us to leave enough space between buttons, or people will tap the wrong one.""",
 sources=["{hoober} Hoober (2013): 1,333 observations; of 780 observations of people touching the screen, 49% one-handed, 36% cradled, 15% two-handed.",
          "{fitts} Fitts (1954): movement time depends on target size and distance.",
          "{apple} Apple HIG, Accessibility > Mobility table: iOS/iPadOS default control size 44x44 pt (minimum 28x28 pt).",
          "{m3touch} Material Design 3, Accessibility designing > Structure: 'consider making touch targets at least 48 x 48dp'.",
          "{figmafitts} Figma, Fitts' law article: 'thumb zone' (Touchscreen interactions) and spacing between buttons to avoid misclicks (Pro tips).",
          "'Delete account' example: our own example."],
 tr="%49 tek el bilgisi Hoober'ın 2013 gözlem çalışmasından {hoober}. Fitts Yasası 1954 tarihli makaleden {fitts}. Apple 44×44 pt değerini 'varsayılan (default) kontrol boyutu' olarak veriyor; minimum ise 28×28 pt {apple}. Google 'en az 48×48 dp' diyor {m3touch}. 'Thumb zone' terimi ve butonlar arasında boşluk bırakma önerisi Figma'nın Fitts Yasası yazısından {figmafitts}. 'Delete account' ise bizim örneğimiz.",
),
dict(
 speaker=2,
 title="Navigation and Consistency",
 bullets=[
  (0, "Bottom navigation bar: three to five main destinations {m3nav}"),
  (0, "Hamburger menu saves space, but hides the options"),
  (0, "The back button must work as users expect"),
  (0, "Highlight the current page or section {adipat}"),
  (0, "Same buttons, layout and menu names everywhere {adipat}, {figmaui}"),
 ],
 script="""Next, navigation. Good navigation answers two questions: where am I, and how can I go somewhere else? The most common pattern today is the bottom navigation bar, like in Instagram or YouTube. Google's Material Design says to use it for three to five main destinations. It is always visible and easy to reach with the thumb. The hamburger menu saves space, but the options are hidden, so many people forget that they are there. And the back button should always do what users expect.

Here the paper gives a very important rule: use consistent buttons, layout and menu names in the whole application. If a page is called "Profile" on one screen, do not call it "Account" on another screen. Figma's guide explains why: when a button looks and works the same everywhere, users stop thinking about the interface and focus on their task.""",
 sources=["{m3nav} Material Design 3, Navigation bar guidelines: 'Navigation bars provide access to three to five destinations'.",
          "{adipat} p. 2286, Table 5: 'use consistent buttons, layout, and menu naming for an entire application'; show current position.",
          "{figmaui} Figma, Principle 3 Consistency: consistent patterns let users focus on their tasks.",
          "Hamburger menu and back-button points: our own observation / common practice."],
 tr="3–5 hedef bilgisi Material Design 3'ün 'Navigation bar' sayfasından {m3nav}. Tutarlılık kuralı makalenin s. 2286'daki Tablo 5'inden, birebir: 'consistent buttons, layout, and menu naming'. Figma'nın UI ilkeleri yazısındaki 3. ilke (Consistency) de aynı şeyi söylüyor {figmaui}. Hamburger menü ve geri tuşu yorumları bizim gözlemimiz.",
),
dict(
 speaker=2,
 title="Readable Text and Colour",
 bullets=[
  (0, "Use simple, readable fonts"),
  (0, "Minimum contrast ratio {wcag}:"),
  (1, "4.5 : 1 for normal text"),
  (1, "3 : 1 for large text"),
  (0, "Do not use colour as the only signal {adipat}, {wcag}"),
  (0, "Add an icon or a word next to the colour"),
 ],
 script="""My last topic is readable text. Use a simple font that is easy to read, and do not mix too many font styles in one app.

Contrast is very important. Contrast is the difference between the text colour and the background colour. The Web Content Accessibility Guidelines, or WCAG, ask for a contrast ratio of at least four point five to one for normal text, and three to one for large text.

Both WCAG and the paper by Adipat and Zhang give the same advice about colour: do not use colour as the only way to give information. Some people cannot see some colours clearly. So, an error should have an icon or a short message, not only a red colour.

To summarise my part: show less but clearer information, put actions where the thumb can reach, keep navigation consistent, and make text easy to read. Now [Name 3] will talk about data entry, context and feedback. Thank you.""",
 sources=["{wcag} WCAG 2.1, Success Criterion 1.4.3 Contrast (Minimum): 4.5:1, large text 3:1; SC 1.4.1 Use of Color.",
          "{adipat} p. 2284, Table 3 (Color blind): 'Do not rely on color'; 'use black-and-white or very contrast colors'."],
 tr="4.5:1 ve 3:1 değerleri WCAG 2.1'in 1.4.3 numaralı başarı kriterinden; 'sadece renge güvenme' kuralı ise 1.4.1'den {wcag}. Makale de s. 2284'teki Tablo 3'te renk körleri için aynı şeyi söylüyor {adipat}. Font tavsiyesi genel bir tasarım pratiği.",
),
# ---------------------------------------------------------------- SPEAKER 3
dict(
 speaker=3,
 title="Data Entry: Typing, Writing and Speaking",
 bullets=[
  (0, "Soft keyboard: needs full visual attention {adipat}"),
  (0, "Handwriting: natural, but recognition makes errors {adipat}"),
  (0, "Voice: hands-free and fast, but {adipat}:"),
  (1, "less accurate"),
  (1, "not good in noisy or public places"),
  (0, "Multimodal: voice, touch and keys together {adipat}"),
  (0, "Choose by task, device and environment {adipat}"),
 ],
 script="""Thank you, [Name 2]. Hi everyone, I am [Name 3]. I will talk about data entry and context, then feedback, accessibility and testing.

The paper compares several input methods. A soft keyboard on the touch screen is flexible, but it needs your full visual attention. Handwriting feels natural, but recognition makes mistakes. Voice is hands-free and fast, but in 2005 it was not very accurate. It is also a bad choice in noisy places or when privacy matters.

The authors see multimodal input as the most promising: voice, touch and keys together. Today you can type a message or just speak it. The lesson is to choose the input method by task, device and environment.""",
 sources=["{adipat} p. 2288, section 'Data entry methods' and Table 8: soft keyboard (high visual attention), handwriting (recognition errors), voice (hands-free, faster, low accuracy; not for noisy/public places, privacy), multimodal access (Lai, 2004: users prefer multimodal).",
          "{adipat} p. 2282 (Related Work): choose input mode by task, physical device and environment (Larson, 2003)."],
 tr="Giriş yöntemleri makalenin s. 2288'deki 'Data entry methods' bölümü ve Tablo 8'den. 'Kullanıcılar çok kipli (multimodal) girişi tercih ediyor' bilgisini makale Lai (2004) çalışmasına dayandırıyor; biz makale üzerinden aktarıyoruz. 'Görev, cihaz, ortam' ayrımı s. 2282'deki 'Related Work' bölümünde geçiyor.",
),
dict(
 speaker=3,
 title="Context: Where Is the User?",
 bullets=[
  (0, "Context: location, people nearby, noise, light {adipat}"),
  (0, "Context-aware apps adapt, e.g. a brighter screen in the dark {adipat}"),
  (0, "But users must stay in control {adipat}:"),
  (1, "let them turn the feature on or off"),
  (1, "tell them before the interface changes"),
  (0, "Send information only when users need it {adipat}"),
 ],
 script="""The second part is context. Context means the user's situation: where they are, who is nearby, and how noisy or dark it is. Context-aware apps change their behaviour based on this information. The example in the paper is an app that makes the font bigger or the screen brighter in a dark place. Today, automatic brightness and dark mode at night work in a very similar way.

But if the app changes things by itself, users can feel they have lost control. So the authors say: let users turn these features off, tell them before the interface changes, and do not send messages they did not ask for, like an advertisement every time you walk past a shopping mall.""",
 sources=["{adipat} p. 2285, section 'Context' (definition by Dey et al., 2001; dark-environment example) and Table 4: turn services on/off, inform users before changing settings, provide context-aware information only when users need it (mall advertisement example).",
          "Automatic brightness / dark mode: our own modern example."],
 tr="Bağlam (context) tanımı ve karanlıkta ekranın parlaklaşması örneği makalenin s. 2285'inden. Kontrol kullanıcıda olmalı kuralları Tablo 4'ten. AVM reklamı örneği de makalenin kendi örneği. Otomatik parlaklık ve karanlık mod ise bugünden verdiğimiz kendi örneğimiz.",
),
dict(
 speaker=3,
 title="Feedback: Tell Users What Is Happening",
 bullets=[
  (0, "Visibility of system status {nnheur}"),
  (0, "Feedback can be visual, sound or vibration {adipat}"),
  (0, "Response time limits {nnresp}:"),
  (1, "0.1 s feels instant"),
  (1, "1 s keeps the flow of thought"),
  (1, "10 s: users start to lose attention"),
  (0, "Clear error messages that help users recover {adipat}, {nnheur}"),
 ],
 script="""Now, feedback. Imagine you press a button and nothing happens. Is the app working, or is it broken? You press again, and again. Jakob Nielsen calls the solution "visibility of system status". This means the system should always tell users what is going on. Adipat and Zhang add that on a phone, feedback does not have to be visual. It can be a sound, or a vibration, which is very useful in a meeting or when your eyes are busy.

Speed is also part of feedback. Nielsen describes three limits. If the response comes in less than one tenth of a second, it feels instant. Within one second, the user's flow of thought is not broken. After about ten seconds, users start to lose their attention. So, when something takes time, we should show a loading indicator or a progress bar.

And when mistakes happen, the paper says error messages must be clear and meaningful. "Error 404" does not help anyone. "We could not find this page. Please check your connection" is much better.""",
 sources=["{nnheur} Nielsen's heuristics #1 'Visibility of system status' and #9 'Help users recognize, diagnose, and recover from errors'.",
          "{adipat} p. 2287, Table 7: visual, audio and tactile (vibration) display; p. 2286, Table 5: 'provide clear and meaningful error messages'.",
          "{nnresp} Nielsen (1993): 0.1 s / 1.0 s / 10 s response-time limits.",
          "'Error 404' example and loading indicator advice: our own example / common practice."],
 tr="'Visibility of system status' Nielsen'in 10 sezgisel kuralının birincisi, hata mesajları ise dokuzuncusu {nnheur}. Görsel, ses ve titreşim geri bildirimi makalenin s. 2287'deki Tablo 7'sinden. 0.1, 1 ve 10 saniye sınırları Nielsen'in 1993 makalesinden {nnresp}. 'Net hata mesajı' kuralı makalede de geçiyor (s. 2286, Tablo 5). 'Error 404' örneği bizim örneğimiz.",
),
dict(
 speaker=3,
 title="Accessibility: Design for Everyone",
 bullets=[
  (0, "About 1.3 billion people (1 in 6) have a significant disability {who}"),
  (0, "Blind users: audio, vibration, sound confirmation {adipat}"),
  (0, "Colour-blind users: do not rely on colour, use strong contrast {adipat}"),
  (0, "Deaf users: visual information and vibration alerts {adipat}"),
  (0, "Support screen readers and bigger text sizes"),
 ],
 script="""Next, accessibility. In 2022, the World Health Organization reported that about one point three billion people, around one in six people in the world, live with a significant disability.

Adipat and Zhang give guidelines for different groups of users. For blind users, use audio and vibration, and give a sound confirmation every time the user starts a function. For colour-blind users, do not rely on colour; use bold text, size and strong contrast instead. For deaf users, show information visually and use vibration for alerts. Today, phones have screen readers like VoiceOver on iPhone and TalkBack on Android. So we should add clear labels to every button and image, and let users make the text bigger.""",
 sources=["{who} WHO (2022): an estimated 1.3 billion people, 16% of the world population (about 1 in 6), experience significant disability.",
          "{adipat} p. 2284, Table 3 'Mobile interface design guidelines for disabled users' (blind, color blind, deaf/hearing impaired, mobility impaired).",
          "VoiceOver / TalkBack: names of the built-in screen readers on iOS and Android (general knowledge)."],
 tr="1.3 milyar kişi ve %16 (yaklaşık 6'da 1) rakamı Dünya Sağlık Örgütü'nün 2022 raporundan {who}. Engelli kullanıcılar için kurallar makalenin s. 2284'teki Tablo 3'ünden. VoiceOver ve TalkBack telefonlardaki ekran okuyucuların isimleri, genel bilgi.",
),
dict(
 speaker=3,
 title="Testing and Conclusion",
 bullets=[
  (0, "Designers are not users, so test with real people"),
  (0, "A small test with about 5 users finds most big problems {nl}"),
  (0, "Test, improve, test again {figmaui}"),
  (0, "Remember the four parts: user, context, information, data entry {adipat}"),
  (0, "A good mobile interface is clear, simple, consistent and friendly"),
 ],
 script="""Finally, testing. Designers know their own app too well, so they often cannot see its problems. In 1993, Nielsen and Landauer showed with a mathematical model that a small test with about five users can find most of the usability problems. Figma's guide agrees: watch real people use your design. So, test with a few people, improve it, and test again.

To summarise: [Name 1] introduced the four-part framework and the user. [Name 2] explained information presentation, layout, navigation and readable text. And I covered data entry, context, feedback and accessibility. The basic problem has not changed since 2005: small screens and busy people. If I had to say it in one sentence: a great mobile interface is clear, simple, consistent and friendly to the user. Thank you very much for listening. We are happy to answer your questions.""",
 sources=["{nl} Nielsen & Landauer (1993): Poisson model of problem discovery; a few test users find most problems.",
          "{adipat} p. 2288, Conclusion: four perspectives (information presentation, data entry, user, context).",
          "{figmaui} Figma, pro tip 'Conduct testing': watch how people use your interface.",
          "Final sentence: our own conclusion."],
 tr="'Yaklaşık 5 kullanıcı' bilgisi Nielsen ve Landauer'ın 1993 tarihli matematiksel modelinden geliyor {nl}. Dikkat: bu bir yasa değil, planlama tahmini. Hoca sorarsa 'yaklaşık' deyin. Özet makalenin Sonuç bölümünden (s. 2288). 'Test et, iyileştir, tekrar test et' önerisi Figma'nın yazısındaki 'Conduct testing' ipucuyla da destekleniyor {figmaui}. Son cümle bizim kendi sonucumuz.",
),
]

QA = [
    ("Why did you choose a paper from 2005?",
     "Because it gives a clear framework with four parts, and the problems are still the same today: small screens and busy users. We also added newer sources, like WCAG 2.1, Material Design 3 and the WHO report from 2022, to update the numbers."),
    ("What are the four parts of the framework?",
     "User, context, information presentation and data entry. They are shown in Figure 1 of the paper by Adipat and Zhang."),
    ("Where does the 44 points come from?",
     "From Apple's Human Interface Guidelines, in the Accessibility section. Forty-four by forty-four points is the default control size for iPhone. The minimum is twenty-eight points."),
    ("Is five users always enough for testing?",
     "Not always. Nielsen and Landauer's model says a small test finds most problems, but it is an estimate. It works best if you test several times and improve the design between the tests."),
    ("What is cognitive load?",
     "It is the mental effort a person needs to use something. The paper says a good interface lets users spend their memory on their task, not on the interface."),
    ("What is a context-aware application?",
     "It is an app that changes its behaviour based on the situation, for example a brighter screen in a dark place. The paper says users must be able to turn this off."),
    ("What is the difference between UI and UX?",
     "UI is what you see and touch, like buttons and text. UX is the whole experience of using the product. A beautiful UI can still give a bad experience if it is confusing."),
    ("Which input method is the best?",
     "There is no single best method. The paper says it depends on the task, the device and the environment. That is why multimodal input, using voice and touch together, is so useful."),
]


# ---------------------------------------------------------------------------
# Resolve {key} citations to IEEE numbers in order of first appearance on the
# slides (outline, then each slide's bullets), then in notes/guide text.
def _resolve():
    import re
    global REFERENCES
    order = []
    def scan(text):
        for k in re.findall(r"\{(\w+)\}", text):
            if k not in order:
                order.append(k)
    for _, t in OUTLINE:
        scan(t)
    for d in SLIDES:
        scan(d["title"])
        for _, t in d["bullets"]:
            scan(t)
    for d in SLIDES:
        for x in d["sources"] + [d["tr"]]:
            scan(x)
    missing = [k for k in REFERENCES if k not in order]
    assert not missing, f"references never cited: {missing}"
    num = {k: i for i, k in enumerate(order, 1)}
    fix = lambda t: re.sub(r"\{(\w+)\}", lambda m: f"[{num[m.group(1)]}]", t)
    OUTLINE[:] = [(l, fix(t)) for l, t in OUTLINE]
    for d in SLIDES:
        d["bullets"] = [(l, fix(t)) for l, t in d["bullets"]]
        d["sources"] = [fix(x) for x in d["sources"]]
        d["tr"] = fix(d["tr"])
        d["script"] = fix(d["script"])
    REFERENCES = [REFERENCES[k] for k in order]


_resolve()
