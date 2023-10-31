from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import SearchForm  # Import your SearchForm

# Create your views here.
json = {
    "category":[{

        "series":[
            {
                "name":"one piece",
                "img":"AnimePlayApp/images/category/one_piece.jpg",
                "aired": "Date aired : Oct 20, 1999 to ?",
                "studios": "Toei Animation",
                "description": "The Pirate King, Gol D. Roger, was renowned as the mightiest and most infamous sailor to navigate the Grand Line. The World Government's apprehension and subsequent execution of Roger prompted a global shift. His final words disclosed the existence of One Piece, the greatest treasure in the world. As a result, the Grand Age of Pirates emerged, with swashbucklers yearning for One Piece's vast riches, fame, and the vaunted title of Pirate King. Monkey D. Luffy, a 17-year-old atypical pirate, enters the fray. Unlike the stereotypical marauder—grizzled, wicked, and ruthless—Luffy seeks pure adventure, relishing the prospect of meeting diverse characters, embarking on wild escapades, and ultimately obtaining the promised treasure. Inspired by his childhood idol, Luffy and his team navigate the Grand Line, encountering strange phenomena, unraveling enigmatic puzzles, and battling formidable foes in their quest for One Piece, the most coveted of all treasures.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Black Clover",
                "img":"AnimePlayApp/images/category/Black_Clover.jpg",
                "aired": "Date aired : Oct 03, 2017 to Mar 30, 2021",
                "studios": "Pierrot",
                "description": "Asta and Yuno were both abandoned as infants at a church, growing up together and dreaming of becoming the Wizard King - the most powerful mage in their kingdom. However, as they matured, their differences became more apparent; Yuno was a natural with magic, while Asta struggled to find the power within himself. At the age of 15, Yuno is given a stunning Grimoire, while Asta is left without. When a stranger named Lebuty targets Yuno to obtain his Grimoire, Asta valiantly attempts to defend his friend, but is overpowered. In the moment of despair, hearing Yuno's voice gives Asta the courage to summon a five-leaf Grimoire, known as the Black Clover, and finally defeat Lebuty. With newfound strength and determination, Asta and Yuno embark on a quest to become the Wizard King.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Naruto: Shippuden",
                "img":"AnimePlayApp/images/category/Naruto_Shippuden.jpg",
                "aired": "Date aired : Feb 15, 2007 to Mar 23, 2017",
                "studios": "Pierrot",
                "description": "Naruto Uzumaki left the Hidden Leaf Village for intense training after an event that fueled his desire to become stronger. Now, two and a half years later, the elite rogue ninja organization Akatsuki is threatening the safety of the shinobi world with their grand plan. Despite the impending danger, Naruto's personality remains largely unchanged, still his rambunctious and childish self, but now more confident and determined to protect his loved ones and home. He will continue to fight for what's important to him, even if it means sacrificing his own body, as his journey to become Hokage continues.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Boruto: Naruto Next Generations",
                "img":"AnimePlayApp/images/category/Boruto_Naruto.jpg",
                "aired": "Date aired : Apr 05, 2017 to Mar 26, 2023",
                "studios": "Pierrot",
                "description": "After the Fourth Shinobi World War came to a successful end, Konohagakure has been relishing in a peaceful era of prosperity and remarkable technological progress. The credit for this goes to the joint efforts of the Allied Shinobi Forces and Naruto Uzumaki, Konohagakure's seasoned Seventh Hokage. With an appearance akin to a modern metropolis, Konohagakure has undergone a significant change, especially for its shinobi. The city's new generation of ninjas is being groomed under the vigilant supervision of Naruto and his old companions. Boruto Uzumaki, the Seventh Hokage's son, draws a lot of attention due to his lineage. Despite inheriting Naruto's dynamic and stubborn personality, Boruto is regarded as a gifted individual who can develop his full potential with the guidance of his loving friends and family. Regrettably, this has also exacerbated his conceit, propelling him to outdo his father, causing friction in their relationship, owing to Naruto's hectic schedule. However, trouble brewing within the village may jeopardize Boruto's carefree life. As a new chapter unfolds, fresh faces and familiar acquaintances join Boruto.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"JUJUTSU KAISEN",
                "img":"AnimePlayApp/images/category/JUJUTSU_KAISEN_series.jpg",
                "aired": "Date aired : Oct 03, 2020 to Mar 27, 2021",
                "studios": "MAPPA",
                "description": "Yuuji Itadori, a high schooler, spends his days indulging in frivolous paranormal activities with the Occult Club while also visiting his sick grandfather at the hospital. However, his leisurely lifestyle takes a strange twist when he unknowingly comes across a cursed object that triggers a series of supernatural events. After swallowing the cursed item, it turns out to be Sukuna Ryoumen's finger, causing him to enter the fearful world of Curses. Yuuji experiences the dangerous nature of these Curses firsthand and gains newfound powers, making him a Jujutsu sorcerer. He finds himself on a path he cannot turn back from at the Tokyo Metropolitan Jujutsu Technical High School.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Attack on Titan",
                "img":"AnimePlayApp/images/category/Attack_Titan.jpg",
                "aired": "Date aired : Dec 07, 2020 to Mar 29, 2021",
                "studios": "MAPPA",
                "description": "The Scout Regiment has now been on the shoreline for four years, and the world has undergone significant changes. The destiny of the regiment and the individuals of Paradis is now at stake as tension escalates. Unfortunately, Eren is nowhere to be found. Could his reappearance prevent an inevitable war between Marleyans and Eldians, which has been brewing for generations?",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Bleach",
                "img":"AnimePlayApp/images/category/Bleach.jpg",
                "aired": "Date aired : Oct 05, 2004 to Mar 27, 2012",
                "studios": "Pierrot",
                "description": "Despite being an ordinary high school student, Ichigo Kurosaki possesses a unique gift - the power to sense ghosts. This talent had no impact on his life until he encounters Kuchiki Rukia, a Shinigami who saves his family from a twisted spirit known as a Hollow, which devours souls. While battling the creature, Rukia is injured and has no choice but to transfer her Shinigami abilities to Ichigo, enabling him to defeat the beast. Temporarily taking on the role of substitute Shinigami until Rukia heals, Ichigo embarks on a quest to eradicate the Hollows that plague his hometown.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Hunter_Hunter",
                "img":"AnimePlayApp/images/category/Hunter_Hunter.jpg",
                "aired": "Date aired : Oct 02, 2011 to Sep 24, 2014",
                "studios": "Madhouse",
                "description": "From traversing uncharted territories to searching for rare items and battling monsters, Hunters risk their lives to complete dangerous tasks. Only those who pass the Hunter Examination, a grueling selection process where most don't make it out alive, can become a Hunter. For 12-year-old Gon Freecss, the desire to find his father and fellow Hunter, Ging, fuels his ambition to pass the exam. Alongside his newfound friends - medical student Leorio Paladiknight, vengeful Kurapika, and former assassin Killua Zoldyck - they unite with a shared mission to navigate the treacherous world of a Hunter. Although their reasons for undertaking this journey may differ, they continue on together towards their common goal.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"My Hero Academia Season 5",
                "img":"AnimePlayApp/images/category/Hero_Academia.jpg",
                "aired": "Date aired : Mar 27, 2021 to Sep 25, 2021",
                "studios": "Bones",
                "description": "The rivalry between Class 1-A and Class 1-B heats up with a joint training battle. Shinso, a specialist in brainwashing, eagerly takes part on both teams in hopes of making it into the hero course. As weaknesses are exposed and new strengths revealed, the result of the conflict is up in the air.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Akame ga Kill",
                "img":"AnimePlayApp/images/category/Akame_ga_Kill.jpg",
                "aired": "Date aired : Jul 07, 2014 to Dec 15, 2014",
                "studios": "White Fox",
                "description": "The Revolutionary Army's covert assassination branch, Night Raid, is committed to bringing down Prime Minister Honest. This power-hungry ruler orchestrated the nation's descent into poverty and ruin by manipulating the young emperor. Night Raid's members possess deadly skills, but remain wary of the consequences of taking lives, as it contradicts their values and may trigger retribution. Tatsumi, a young man hailing from a destitute village, joins Night Raid with the goal of aiding his community. He is inspired by the group's principles and unyielding dedication to their cause. Akame ga Kill! sees Tatsumi confronting the Empire's formidable weapons, competing assassins, and ethical dilemmas that challenge his beliefs. Throughout this, he learns the true purpose and significance of his role as an assassin.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            }
            
        ],
        "movies":[
            {
                "name":"Your Name",
                "img":"AnimePlayApp/images/category/Your_Name.jpg",
                "aired": "Date aired : Aug 26, 2016",
                "studios": "CoMix Wave Films",
                "description": "Mitsuha Miyamizu, a high school student from the countryside, yearns to experience life as a boy in the bustling city of Tokyo. On the other hand, Taki Tachibana is a busy student in Tokyo with a part-time job and dreams of becoming an architect. One fateful day, Mitsuha wakes up in a foreign room, inside Taki's body, living the life she always dreamed of. Meanwhile, Taki wakes up in Mitsuha's life in the humble countryside. As they try to uncover the reason behind this strange occurrence, they embark on a journey to find each other. Kimi no Na wa., a tale of fate and circumstance, follows the dramatic impact of Mitsuha and Taki's actions on each other's lives, weaving them into a tapestry of interconnectedness.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"A Silent Voice",
                "img":"AnimePlayApp/images/category/A_Silent_Voice.jpg",
                "aired": "Date aired : Sep 17, 2016",
                "studios": "Kyoto Animation",
                "description": "Shouya Ishida was a disruptive elementary school student who went to great lengths to combat boredom. When deaf student Shouko Nishimiya arrived in their class, Shouya and his peers cruelly tormented her for amusement. Once the school was notified by Shouko's mother, Shouya was blamed for all the mistreatment and Shouko was forced to leave the school. Shouya was subsequently shunned by his classmates and endured this throughout elementary and middle school, with no teacher intervention. Now attending his third year of high school, Shouya remains tormented by his past actions. Determined to make amends, he seeks out Shouko in an attempt to reconcile. Koe no Katachi details Shouya's journey of redemption as he faces the lingering consequences of his misconduct. Despite being incessantly plagued by his past, Shouya reunites with Shouko, genuinely seeking to make things right.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train",
                "img":"AnimePlayApp/images/category/Demon_Slayer_movie.jpg",
                "aired": "Date aired : Oct 16, 2020",
                "studios": "ufotable",
                "description": "A series of enigmatic vanishing acts begins to afflict a train, with the Demon Slayer Corps' several attempts to tackle the problem being unsuccessful. The Flame Pillar, Kyoujurou Rengoku, decides to take matters into his own hands to avoid further loss of lives. Accompanying him are some of the Corps' most promising novices: Tanjirou Kamado, Zenitsu Agatsuma, and Inosuke Hashibira, who are keen to witness the remarkable skills of this exceptional demon hunter. However, unbeknownst to them, the demonic entity behind the disappearances has already set its malevolent scheme in motion. In the face of this diabolical presence, the team must summon their utmost courage and wield their weapons to save the two hundred passengers on board. Kimetsu no Yaiba Movie: Mugen Ressha-hen probes the deepest corners of Tanjirou's psyche, testing his resolve and commitment to his duties.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"JUJUTSU KAISEN 0",
                "img":"AnimePlayApp/images/category/JUJUTSU_KAISEN_0.jpg",
                "aired": "Date aired : Dec 24, 2021",
                "studios": "MAPPA",
                "description": "Yuta Okkotsu, an anxious high schooler, is plagued with a grave issue - his childhood companion Rika has transformed into a curse and refuses to cease bothering him. As Rika is not an ordinary curse, Satoru Gojo, an instructor at Jujutsu High, a renowned institute where budding exorcists are trained to battle curses, acknowledges his predicament. Persuading Yuta to register, Gojo poses the question, can he grasp the necessary knowledge quickly enough to combat the curse that lingers over him",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"I Want to Eat Your Pancreas",
                "img":"AnimePlayApp/images/category/I_Want_to_Eat_Your_Pancreas.jpg",
                "aired": "Date aired : Sep 01, 2018",
                "studios": "Studio VOLN",
                "description": "Spring time in April and the last of the cherry blossoms are still in bloom. The usually aloof bookworm with no interest in others comes across a book in a hospital waiting room. Handwritten on the cover are the words: Living with Dying. He soon discovers that it is a diary kept by his very popular and genuinely cheerful classmate, Sakura Yamauchi, who reveals to him that she is secretly suffering from a pancreatic illness and only has a limited time left. It is at this moment that she gains just one more person to share her secret. Trying to maintain a normal life as much as possible, Sakura is determined to live her life to the fullest until the very last day. As her free spirit and unpredictable actions throw him for a loop, his heart begins to gradually change.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Weathering With You",
                "img":"AnimePlayApp/images/category/Weathering_With_You.jpg",
                "aired": "Date aired : Jul 19, 2019",
                "studios": "CoMix Wave Films",
                "description": "Due to rainy weather, the daily routines of Tokyo locals have been negatively affected, causing a great deal of hardship for high school runaway Hodaka Morishima who is struggling to make ends meet. In search of work to support her younger brother, orphan Hina Amano crosses paths with Hodaka when he rescues her from a group of questionable individuals. Together they decide to run away. Hodaka soon discovers Hina's extraordinary ability to bring forth the sun through prayer, which could prove to be beneficial considering Tokyo's unpredictable climate. Hodaka's proposal for Hina to become a sunshine girl seems like a promising solution, but they soon realize the heavy burden that comes with possessing such unique powers.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Spirited Away",
                "img":"AnimePlayApp/images/category/Spirited_Away.jpg",
                "aired": "Date aired : Jul 20, 2001",
                "studios": "Studio Ghibli",
                "description": "As Chihiro Ogino's family journeys to their new residence, they come across an abandoned amusement park. Intrigued, they wander the park, unaware that it is actually home to spirits who only awaken at night. After Chihiro's parents consume food from a restaurant, angry spirits transform them into pigs, and a vast ocean separates her from the human world, leaving her trapped in the spirit realm. Thankfully, Haku, a mysterious boy who claims to know her, comes to her aid. He instructs her to find work at the bathhouse where he is employed. Armed with newfound friends and inner strength, Chihiro sets out to return her parents to their human form and escape the eerie land of spirits.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name": "Sword Art Online the Movie: Ordinal Scale",
                "img": "AnimePlayApp/images/category/Sword_Art_Online_movie.jpg",
                "aired": "Date aired : Feb 18, 2017",
                "studios": "A-1 Pictures",
                "description": "The year 2022 marked a major shift in the virtual reality landscape with the emergence of NerveGear, a groundbreaking innovation from the brilliant programmer Akihiko Kayaba. This revolutionary technology introduced boundless potential to VRMMORPGs as the first full-dive system. Fast forward to 2026, a new contender called Augma was created to compete with NerveGear and its successor, Amusphere. Augma, a next-gen wearable device, utilized Augmented Reality to immerse players in the game without the full-dive feature of its predecessors. Its safety, user-friendliness, and ability to enable conscious gameplay propelled it to instant success upon its release. The platform's most sought-after title was Ordinal Scale, an ARMMORPG exclusively crafted for the Augma. Asuna and her group had already been enjoying Ordinal Scale for some time when Kirito decided to join them. Little did they know that the game was not all about entertainment, and they were about to find themselves facing a more significant challenge.The year 2022 marked a major shift in the virtual reality landscape with the emergence of NerveGear, a groundbreaking innovation from the brilliant programmer Akihiko Kayaba. This revolutionary technology introduced boundless potential to VRMMORPGs as the first full-dive system. Fast forward to 2026, a new contender called Augma was created to compete with NerveGear and its successor, Amusphere. Augma, a next-gen wearable device, utilized Augmented Reality to immerse players in the game without the full-dive feature of its predecessors. Its safety, user-friendliness, and ability to enable conscious gameplay propelled it to instant success upon its release. The platform's most sought-after title was Ordinal Scale, an ARMMORPG exclusively crafted for the Augma. Asuna and her group had already been enjoying Ordinal Scale  for some time when Kirito decided to join them. Little did they know that the game was not all about entertainment, and they were about to find themselves facing a more significant challenge.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"KONOSUBA",
                "img":"AnimePlayApp/images/category/KONOSUBA.jpg",
                "aired": "Date aired : Aug 30, 2019",
                "studios": "J.C.Staff",
                "description": "The Crimson Demons, a clan housing Megumin and Yunyun, are an impressive and intimidating group, wielding advanced and overpowering magic that even rivals the Demon Lord's army. Yunyun urgently notifies Kazuma Satou and the gang upon receiving a letter warning of danger in her village, and they set out on a journey. Despite comedic mishaps, they discover the letter was a joke from a demon with literary aspirations. Nonetheless, Megumin remains worried for her loved ones' well-being and persuades her comrades to join her in visiting her homeland. They reach the Crimson Demons' settlement and take in the surroundings, but soon realize the prank letter may have contained some authenticity.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"5 Centimeters per Second",
                "img":"AnimePlayApp/images/category/5_Centimeters_per_Second.jpg",
                "aired": "Date aired : Mar 03, 2007",
                "studios": "CoMix Wave Films",
                "description": "Even though Takaki Toono and Akari Shinohara share a deep love, fate seems to have other plans for their relationship. Despite being childhood friends, circumstances beyond their control lead to their separation. Regardless of the distance between them growing with time, their memories of each other remain ever-present, and they vow to stay in touch. Byousoku 5 Centimeter explores the pain and struggles that come with long-distance relationships, with Takaki and Akari unable to move on from the past and make new memories. As a result, they find themselves living half-hearted lives, causing pain not only to themselves but to those around them.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            }

        ],
        "recent":[
            {
                "name":"Hells Paradise",
                "img":"AnimePlayApp/images/category/Hells_Paradise.jpg",
                "aired": "Date aired : Apr 01, 2023 to Jul 01, 2023",
                "studios": "MAPPA",
                "description": "Gabimaru the Hollow, a ninja from Iwagakure Village recognized for his unemotional demeanor and devoid of any warmth, finds himself on death row after being plotted against by his fellow comrades. He has grown exhausted of living a life of killing and treachery and desires nothing more than to depart from this world. Nevertheless, despite his seemingly impassive facade, Gabimaru secretly harbors a reason to exist – his beloved wife, the very person who caused him to soften and become ineffective in his line of work. With the hope of reuniting with her, Gabimaru refuses to succumb to death, frustrating all attempts of execution. Asaemon the Decapitator, a renowned executioner, comes across Gabimaru's plight and devises an offer. She agrees to secure a full pardon from the Shogunate for Gabimaru in exchange for his participation in an expedition to a southern Japanese island, where they seek the elixir of life that is rumored to be found there. However, this island is no ordinary land; it is believed to be Paradise. Nonetheless, the expedition team, consisting of members who are all marked for death, discovers that this island is shrouded in mystery, and they may not be entirely equipped to handle what they encounter during their expedition.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Tokyo Ghoul",
                "img":"AnimePlayApp/images/category/Tokyo_Ghoul.jpg",
                "aired": "Date aired : Jul 04, 2014 to Sep 19, 2014",
                "studios": "Pierrot",
                "description": "Tokyo is being terrorized by a menacing threat: ghouls who resemble humans and blend in with the populace while feasting on flesh. Ken Kaneki, a shy college student who is more interested in reading books than following current events, is thrust into the fray when he meets Rize Kamishiro, an attractive woman who boldly asks him out on a date. As he walks Rize home, Kaneki discovers that she is not as kind as she seems and has nefarious motives. In a tragic altercation, he is left hospitalized, having received life-saving organ transplants from Rize. However, Kaneki's body begins to undergo terrifying changes and he morphs into a hybrid of human and ghoul. As he navigates this new and frightening existence, Kaneki desperately clings to his humanity in a violent battle between the government agents hunting the ghouls and these new monsters who threaten society.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"One Punch Man",
                "img":"AnimePlayApp/images/category/One_Punch_Man.jpg",
                "aired": "Date aired : Oct 05, 2015 to Dec 21, 2015",
                "studios": "Madhouse",
                "description": "Saitama, a seemingly unimpressive man, has an unusual hobby: being a hero. He had relentlessly trained for three years to pursue his childhood dream, losing all of his hair in the process. Saitama's unparalleled strength makes him capable of defeating any enemy with just one punch. However, his boredom has increased since there's no one who can match his power. One day, Genos, a 19-year-old cyborg, seeks to become Saitama's apprentice after witnessing his incredible strength. Genos proposes that they join the Hero Association to obtain recognition for their heroic deeds. Saitama, surprised that he was relatively unknown, agrees to join the association. He accepts the offer to combat new enemies and make new allies, embarking on a new journey as a Hero Association member to rekindle the excitement of battle that he once had.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"That Time I Got Reincarnated as a Slime",
                "img":"AnimePlayApp/images/category/That_Time_I_Got_Reincarnated_as_a_Slime.jpg",
                "aired": "Date aired : Oct 02, 2018 to Mar 19, 2019",
                "studios": "8bit",
                "description": "Satoru Mikami, a desolate 37-year-old man, is trapped in a dreary job, dissatisfied with his tedious existence, but a fatal altercation with a thief leads him to be reincarnated in a remarkable realm...as a slime creature! While he adjusts to his gelatinous form, his interactions with fellow monsters initiate a series of incidents that will revolutionize his strange world!",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Demon Slayer",
                "img":"AnimePlayApp/images/category/Demon_Slayer.jpg",
                "aired": "Date aired : Apr 09, 2023 to Jun 18, 2023",
                "studios": "ufotable",
                "description": "Following the death of his father, Tanjirou Kamado bears the weight of providing for his family. Despite residing in poverty on a remote mountain, the Kamado family manages to maintain a peaceful and contented existence. Seeking to earn a modest income selling charcoal, Tanjirou embarks on a journey to the nearby village. However, as dusk descends, he finds himself compelled to take refuge in a stranger's home. The host cautions him of the existence of flesh-eating demons lurking in the woods at night. Upon returning home the next day, Tanjirou is greeted by a nightmare: his entire family has been brutally murdered. The only survivor is his sister Nezuko, now cursed as a bloodthirsty demon. Fueled by wrath and hatred, Tanjirou swears to avenge his family and care for Nezuko. Allying with the enigmatic Demon Slayer Corps, he vows to raze the demons and safeguard his sister's remaining humanity at all costs.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Sword Art Online",
                "img":"AnimePlayApp/images/category/Sword_Art_Online.jpg",
                "aired": "Date aired : Jul 08, 2012 to Dec 23, 2012",
                "studios": "A-1 Pictures",
                "description": "Sword Art Online, a Virtual Reality Massive Multiplayer Online Role-Playing Game (VRMMORPG), has hit the market. It's unique in that players use a device called Nerve Gear to operate their avatars through physical movement. However, the game takes a dark turn when players learn that they cannot exit the game. The creator has taken them hostage and demands that they reach the 100th floor of the tower and defeat the final boss. The catch is that dying in the game means dying in real life. The players are now forced to fight for survival.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Tokyo Revengers",
                "img":"AnimePlayApp/images/category/Tokyo_Revengers.jpg",
                "aired": "Date aired : Apr 11, 2021 to Sep 19, 2021",
                "studios": "LIDENFILMS",
                "description": "Having hit rock bottom in his life, Takemichi Hanagaki is a freelancer struggling to stay afloat. One day, he discovers that Hinata Tachibana, his middle school girlfriend and the only one he ever had, was brutally murdered by the Tokyo Manji Gang. Overcome with grief and despair, Takemichi finds himself on a train station platform the next day, only to be pushed onto the tracks by a swarm of people. As he braces for the end, his eyes close shut. But when he opens them again, he's traveled back in time by 12 years – to the best days of his life. With a newfound determination to set things right, Takemichi embarks on a mission to save his lost love and become the person he always wanted to be.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"The Rising of the Shield Hero",
                "img":"AnimePlayApp/images/category/The_Rising_of_the_Shield_Hero.jpg",
                "aired": "Date aired : Jan 09, 2019 to Jun 26, 2019",
                "studios": "Kinema Citrus",
                "description": "A collection of average men from modern-day Japan, known as the Four Cardinal Heroes, were summoned to the kingdom of Melromarc to save it from the recurrent Waves of Catastrophe that have been plaguing and devastating the land for ages. Each of the four heroes was granted a weapon, such as a sword, spear, bow, or shield, to combat these destructive Waves. Naofumi Iwatani, an enthusiastic otaku, was burdened with the role of being the Shield Hero, equipped with a weak shield. His companions and the populace of Melromarc relentlessly scorned him due to his minimal offensive potential and unimpressive character. After acquiring resources and companions to train with, Naofumi partnered with Malty Melromarc, the only person willing to collaborate with him. Unfortunately, Malty's treachery resulted in Naofumi being falsely implicated for taking advantage of her. He suffered from extreme discrimination and animosity from the people of Melromarc due to the unjust accusations. Fueled by anguish and suspicion, Naofumi began a quest to better himself and his reputation. However, the burden of traveling alone began to weigh on him, prompting him to buy a demi-human slave named Raphtalia, who was on the brink of death, to be his traveling companion. As the Waves approached Melromarc, Naofumi and Raphtalia were responsible for safeguarding the kingdom and its residents from their ominous future.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Overlord",
                "img":"AnimePlayApp/images/category/Overlord.jpg",
                "aired": "Date aired : Jul 07, 2015 to Sep 29, 2015",
                "studios": "Madhouse",
                "description": "At the stroke of midnight, the beloved virtual reality game Yggdrasil comes to a close. However, Momonga, the skilled sorcerer and leader of the notorious dark guild, Ainz Ooal Gown, chooses to linger within the game until the very last moment. To his astonishment, Momonga remains fully cognizant as the servers begin their shutdown protocol. In a most unexpected twist, the game's non-playable characters exhibit individual personas! Derailed by this bizarre event, Momonga rallies his loyal followers to investigate this peculiar phenomenon and conquer this newfound realm. His mission is twofold: to uncover the root of this inexplicable situation and ascertain if other players are likewise impacted.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Classroom of the Elite",
                "img":"AnimePlayApp/images/category/Classroom_of_the_Elite.jpg",
                "aired": "Date aired : Jul 12, 2017 to Sep 27, 2017",
                "studios": "Lerche",
                "description": "Koudo Ikusei Senior High School may seem like a utopia on the surface, with its students enjoying exceptional freedom and a high rank in Japan. However, the reality is far from perfect. The school divides its students into four classes, A through D, based on merit, only granting favorable treatment to the top classes. Kiyotaka Ayanokouji is a student in the lowest-ranked Class D, where the school places its worst students. He meets Suzune Horikita, a withdrawn student who thinks she ended up in Class D due to an error and wants to climb up to Class A. Also, Kikyou Kushida, the friendly class queen, aims to make as many friends as possible. Although class association is a constant, students in lower-ranked classes can rise in standing by scoring better than those in the top groups. Furthermore, Class D puts no restrictions on the methods one can use to advance. Will they overcome the obstacles in this challenging school and climb to the top?",
                "video": "AnimePlayApp/video/One_piece.mp4"
            }
        ],
        "recommendations":[
            {
                "name":"Samurai Giants",
                "img":"AnimePlayApp/images/category/Samurai_Giants.jpg",
                "aired": "Date aired : Oct 06, 1973 to Sep 14, 1974",
                "studios": "Madhouse, Tokyo Movie Shinsha",
                "description": "Ban Banjou is an insolent wild boy who was raised on the rough sea in Tosa, southern Japan. He joined the Tokyo Yomiuri Giants in Japanese pro baseball league such a baseball pitcher noted for the blazing fastball and the worst control. He fights hard battles against his rival batters, developing his incredible pitching magics.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Grunge",
                "img":"AnimePlayApp/images/category/Grunge.jpg",
                "aired": "Date aired : Sep 08, 2023 to ?",
                "studios": "MontBlanc Pictures",
                "description": "The fourth season of FLCL, and sequel to FLCL Alternative. It centers on three teenagers who graduated and have started working. The CGI anime will have a theme of the feeling of being an adult.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Semi wa Magic Cube",
                "img":"AnimePlayApp/images/category/Semi_wa_Magic_Cube.jpg",
                "aired": "Date aired : Mar 29, 2020 to May 22, 2020",
                "studios": "Durufix",
                "description": "The story revolves around Semi, a girl who travels back in time to prevent evil forces from using the magic cube.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Bakugan",
                "img":"AnimePlayApp/images/category/Bakugan.jpg",
                "aired": "Date aired : Aug 31, 2023 to ?",
                "studios": "TMS Entertainment",
                "description": "In the exciting new season of Bakugan, the VESTROIAN star system is made up of six planets each home to a different species of Bakugan (Avian, Dragon, Insect, Mammal, Aquatic and Dino). Constantly at WAR with one another, the use of experimental weaponry causes the Bakugan to be inadvertently transported to EARTH. Baku-Balls rain down from the sky like meteors and crash into cities, forests, and oceans. And when the balls unroll, humans meet the 10 FEET TALL Bakugan for the very first time. Thankfully, humanity welcomes these displaced creatures, embraces their culture, and particularly falls in love with their long-standing tradition of BRAWLING. That is until kids start PAIRING with Bakugan and miraculously give them the ability to grow to giant KAIJU size.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Little Lulu",
                "img":"AnimePlayApp/images/category/Little_Lulu.jpg",
                "aired": "Date aired : Oct 03, 1976 to Apr 03, 1977",
                "studios": "Nippon Animation",
                "description": "The adventures of Little Lulu and her friends. The series is based on the famous character from comic strips and comic books.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"The Mischevious Twins",
                "img":"AnimePlayApp/images/category/The_Mischevious_Twins.jpg",
                "aired": "Date aired : Jan 05, 1991 to Nov 02, 1991",
                "studios": "TMS Entertainment",
                "description": "Patricia and Isabel O'Sullivan arrives at the St. Claire, a college for girls, to study and live in the new home. In there place, they meet to Alison, Wella, Catherine and Doris, who live too in the St. Claire, and join with their in the team spirit. All together, the girls play games and fun long time, living in harmony until appears Winfred, a sulky rude and antisocial girl that no will doubt in to create all kind of troubles for the O'Sullivan twins and their friends.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"The Misfit of Demon King Academy",
                "img":"AnimePlayApp/images/category/The_Misfit_of_Demon_King_Academy.jpg",
                "aired": "Date aired : Jan 08, 2023 to Sep 24, 2023",
                "studios": "Silver Link",
                "description": "After peace returns to the demon realm, Anos Voldigoad longs to give up his title as the Demon King of Tyranny and return to his misfit ways at the prestigious Demon King Academy. Sadly, peaceful times are short-lived. Sinister demons, kings, and deities plot against Anos in the shadows. Rumors are in the air about the Child of God, a powerful being that could rival Anos. To uncover the truth and neutralize the potential threat, Anos must journey into the spirit world, but its mysteries can only be unlocked after facing a series of taxing trials. With unmatched power and confidence, Anos prepares to take on various opponents with grandiose titles. Yet, with the help of his trusted allies, he barely breaks a sweat as the ultimate Demon King of Tyranny.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"The Eminence in Shadow",
                "img":"AnimePlayApp/images/category/The_Eminence_in_Shadow.jpg",
                "aired": "Date aired : Oct 05, 2022 to Feb 15, 2023",
                "studios": "Nexus",
                "description": "Not everyone possesses the disposition to portray a showy, outspoken hero or a diabolical villain with exaggerated flair. Some prefer to work covertly, using their ingenuity and sagacity to manipulate society. This is precisely the role that Cid yearns to embody upon finding himself in a new world. With his gift for storytelling, he emerges as an improbable leader of the subterranean Shadow Garden organization, engaged in combat against a threatening cult (which he fabricated from thin air). Unexpectedly, Cid's overactive imagination becomes his undoing as the cult he believed to be a figment of his creativity is revealed to be real, and infuriated that his escapist delusions have impeded their nefarious agenda.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Death Note",
                "img":"AnimePlayApp/images/category/Death_Note.jpg",
                "aired": "Date aired : Oct 04, 2006 to Jun 27, 2007",
                "studios": "Madhouse",
                "description": "The human realm is plagued with atrocious acts such as brutal homicides, minor theft, and senseless violence. Meanwhile, the land of death gods is nothing but a dreary gambling den, devoid of any eventful happenings. Both Light Yagami, a 17-year-old intelligent and savvy Japanese student, and the harsh god of death, Ryuk, are of the same opinion: their domains have been corrupted. Ryuk, for his amusement, drops his Death Note in the human world, which is then stumbled upon by Light. Disregarding the first rule that states whoever has their name written in the book will die, Light is overwhelmed by temptation and experiments on a criminal by inscribing his name. Surprisingly, the wrongdoer perishes, and Light commits his first murder. With the colossal power that has been bestowed upon him, Light assumes the name Kira and embarks on a misguided mission to obliterate all the malevolent people in the world, motivated by his warped sense of justice. However, the astute detective L has already started pursuing Kira's trail, and as Light's shrewdness matches that of L, the chase escalates into a strenuous intellectual battle, and the eventual triumph is only achieved when one of them bites the dust.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            },
            {
                "name":"Chainsaw Man",
                "img":"AnimePlayApp/images/category/Chainsaw_Man.jpg",
                "aired": "Date aired : Oct 12, 2022 to Dec 28, 2022",
                "studios": "MAPPA",
                "description": "Denji's teenage years are stolen from him as he is burdened with the overwhelming debt left behind by his deadbeat father. His only trusted companion is Pochita, the chainsaw devil, whom he works with to slay demons for money that's ultimately claimed by the yakuza. Despite facing numerous challenges, Denji daydreams of a simple life filled with mouth-watering cuisine and a stunning girlfriend. However, his hopes are dashed by a dreadful act of treachery by the yakuza, leading to his unfortunate demise. In an astonishing turn of fate, Pochita's ability to meld with the deceased unleashes devil powers in Denji, transforming him into a hybrid capable of morphing his body parts into chainsaws. Since Denji's newfound abilities pose a significant threat to society, he's taken in by the Public Safety Bureau's top devil hunter, Makima. On the condition that he obeys her every command, Denji is given the opportunity to live and pursue his aspiration of settling down with a lovely lady. With aspirations as pure as they are naive, Denji endeavors to make his dreams a reality, exuding all his efforts into the cause.",
                "video": "AnimePlayApp/video/One_piece.mp4"
            }
            

        ]
    }
    ]
}


def index(request):
    user = request.user.is_authenticated
    context = {
        'jsonObjects': json
    }
    return render(request, 'AnimePlayApp/index.html', context)

def movies(request):
    subcategory_data = json['category'][0]['movies']
    return render(request, 'AnimePlayApp/category.html', {'subcategory_data': subcategory_data, 'subcategory': 'movies'})

def series(request):
    subcategory_data = json['category'][0]['series']
    return render(request, 'AnimePlayApp/category.html', {'subcategory_data': subcategory_data, 'subcategory': 'series'})


def recom(request):
    subcategory_data = json['category'][0]['recommendations']
    return render(request, 'AnimePlayApp/category.html', {'subcategory_data': subcategory_data, 'subcategory': 'recommendations'})


def recent(request):
    subcategory_data = json['category'][0]['recent']
    return render(request, 'AnimePlayApp/category.html', {'subcategory_data': subcategory_data, 'subcategory': 'recent'})


def watchlist(request):
    
    subcategory_data = json['category'][0]['recommendations']
    return render(request, 'AnimePlayApp/watchlist.html', {'subcategory_data': subcategory_data, 'subcategory': 'recommendations'})

    
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            search_results = []
            for subcategory, items in json['category'][0].items():
                for item in items:
                    if search_query in item['name']:
                        search_results.append((subcategory, item))
            return render(request, 'AnimePlayApp/detail.html', {'search_results': search_results , 'search_query': search_query })

    else:
        form = SearchForm()
        return render(request, 'AnimePlayApp/detail.html',{})
    
def detail_id(request, search_query):
    search_results = []
    for subcategory, items in json['category'][0].items():
        for item in items:
            if search_query in item['name']:
                search_results.append((subcategory, item))
    return render(request, 'AnimePlayApp/detail.html', {'search_results': search_results , 'search_query': search_query })
    
