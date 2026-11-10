# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

define jonesy = Character("Jonesy")
define anon = Character("Anon")
define meowskulls = Character("Meowskulls")

image jonesy default = "jonesy_default.png"
image jonesy concerned = "jonesy_concerned.png"
image jonesy smile = "jonesy_smile.png"
image jonesy thumbsup = "jonesy_thumbsup.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    stop music fadeout 2.0

    "This is it. This is really happening."

    "..."

    "Why did I choose this? I could've done something better, surely."

    "It's been a year since I graduated from university. And a year of the same sort of reply, over and over and over again."

    "\"We recognize your skills, but we regret to inform you that we've moved on with other applicants. We wish you well-\" blah blah blah. Who cares."   

    "I've become just another statistic of this market. But... ugh. I can't really put all the blame on it."

    "Like most of the day I\'m just sitting inside, playing competitive games or watching anime. The only social interaction I get is either a brief \"hi\" with my roommate or tweaking at horrible teammates."

    "I've got to face reality. I\'ve got loans to pay and I\'m in a barely tolerable job."

    "..."

    "So WHY AM I HERE???"

    play sound "fortnite-spawn.mp3"

    scene bg spawn with Fade(0.0, 0.0, 2.5)

    play music "fortnite-ambient.mp3"

    "... Fortnite."

    "That's where my head ended up going."

    "There was always talk of it online whenever the Multiverse Cup started and I never cared for it."

    "Heroes, villains, all kinds of warriors from all over the multiverse competed in a battle royale to claim the #1 Victory Royale."

    "25 teams of 4. One team wins."

    "It's this weird thing... that's also a game, kind of... where it's simulated, but also... real life? I don't really get how it works."

    "Think Greed Island from Hunter x Hunter. And if you've never watched that, go do it right now because it's awesome."

    "But anyway, it doesn't change the fact that I decided to finally stop playing so many games... just to play a REAL LIFE GAME SIMULATED GAME."

    "It was one of the first things that popped into my head when thinking of a way to change my life."

    "I looked it up online and saw that all sorts of Fortnite competitions happened year round. And you barely needed any qualifications to start competing."

    "\"THIS will be my big break\" I told myself. \"Look at how easy it is to start! Look at all the success stories! The money to be made! Why don't more people do this??\""

    "I'm genuinely so STUPID. This was a horrible idea."

    "I needed to face reality, and HERE I AM IN A REAL LIFE GAME SIMULATED GAME!!!"

    "Did I really hope I could make some money in something as scuffed as this with players like MASTER CHIEF???"

    "Ugh. Whatever."

    "I signed up for a newbie mix. A casual competition where new players are coached by seasoned players in the match."

    "I was sent an introductory video that detailed the rules of Fortnite and how it works."

    "... and, given what I answered on the questionnaire, I was sent another video that basically just showed me \"Here's how to hold a gun. Here's how to shoot. Have fun!\""

    "Unbelievable. I'm so cooked."

    "I sighed. It's just the one match, Anon, and it's too late to turn back now. Just get through it and get on with your life."

    "I started to walk around to try and find whoever was supposed to coach me. There's already quite a few people here on this Spawn Island."

    "I don't really recognize them all, but..."

    "Wait. Hold on."

    "Is that Bugs Bunny?"

    "Is that Kratos?"

    "IS THAT HATSUNE MIKU???"

    "Geez."

    "I don't even know who's supposed to be coaching me. Some guy called Jonesy."

    "Was I supposed to receive a message about that? I don't really pay attention to that all too much."

    "Again, I wonder why I'm even here. Why did I choose to be here?"

    "I don't care if that Homer Simpson competed at some point. I don't want to be here. I don't belong here."

    "... Okay, get it together Anon. It's only 22 minutes of fighting."

    "At least you tried this. Now you can be more realistic and get your life back on track."

    "I kept shuffling around, every type of colorful character invading every corner of my eyes."

    "All kinds of species. All walks of life. Newbies, casuals, professionals."

    "I didn't really know what I expected to find here. The internet made it sound like easy money."

    "I knew nothing was ever that easy. And yet, still, like an idiot, I..."

    "..."

    "Okay, there's the battle bus. The coach was still nowhere in sigh-"

    scene bg black

    stop music

    play sound "punch.mp3" volume 0.5
    
    "..."

    "... Woah."

    play music "fortnite-lobby.mp3" volume 0.5

    show image "scene_1a.png" with Fade(0.0, 0.0, 1.0):
        xcenter 0.65 yalign 1.0
        ease 6 yoffset 1500

    pause 6.0

    "Okay."

    "Emo? Check. Catgirl? Check. Emanating an unbelievable amount of angst that pierces every fiber of my being?"

    "Yeah. She's cute."

    "I'm feeling a lot of judgment for some reason. Shut up. I know my type."

    "But obviously I'm not gonna be some creep and just {i}walk{/i} up to her. That's not how it works anymore. I think."

    show image "scene_1b.png":
        xcenter 0.65 yalign 1.0 yoffset 1500
        alpha 0.0
        ease 0.25 alpha 1.0

    "I've already accepted my lot in life. Ain't no way that's happening."

    "No sir. Not ever. There is absolutely no possible way I'll be able to talk with her, and that's that."

    "And even if I could, what would I even say? Nothing, that's what. I'd just be an idiot."

    "I'm already moving on. Lemme' try and find… wait."

    "Did that fox girl notice me?"

    stop music

    show image "scene_1c.png" with Dissolve(0.25, time_warp=None, mipmap=None):
        xcenter 0.65 yalign 1.0 yoffset 1500

    pause 3.0

    play music "fortnite-lobby-speedup1.mp3" volume 0.5

    "Ah NAW."

    "I turn and try to play it off. My face is burning so much."

    play music "fortnite-lobby-speedup2.mp3" volume 0.5

    "Stop it, Anon. I'm not Tomatotown guy."

    "..."

    "Anon. Stop. Please."

    play music "fortnite-lobby-speedup3.mp3" volume 0.5

    "STOP. THINKING. ABOUT. IT!"

    scene bg black

    stop music

    play sound "body-impact.mp3"

    pause 0.5

    "I nearly fell back. I crashed into someone else."

    "Who did I even run into. A living brick wall??? Of course Fortnite would have a guy like that."

    label test:

    "As I look up and scramble for an apology, before me stands… someone completely ordinary."

    play music "fortnite-og-remix.mp3" volume 0.4 fadein 0.5
    
    scene bg grass with Fade(0.0, 0.0, 0.5)

    show jonesy default with Dissolve(0.5, time_warp=None, mipmap=None):
        xcenter 0.52 yoffset -40 zoom 0.45

    jonesy "Yo."

    anon "Uh..."

    "Literally the most average looking white man you could ever behold. If men were a bell curve he'd be right at the center. He's so normal he's the one who looks out of place here."

    "…"

    "Am I seriously that weak that I bounced off of {i}him?{/i}"

    "Wait, hang on."

    anon "Aren't… you that guy? That guy that's like… everywhere, in this game?"

    "He chuckled."

    jonesy "Yeah. I'm the guy."

    jonesy "And you're Anon, right? I'm your coach."

    jonesy "I was worried my squad was gonna have to go through a 3v4 right off the bat. You know we were supposed to meet up at the mansion?"

    "I don't even know what to think about right now."

    "Trying to forget about the fact that a cute girl caught me staring at her, I'm now forced to confront the idea of being coached by someone who is clearly not Master Chief." 

    "And apparently, I had also completely missed a crucial, simple detail of a meetup point."

    "I just want to bail out now."

    anon "Uh… sorry. I guess I didn't get the memo."

    jonesy "It's all good. That's what I'm here for. My name's Jonesy."

    jonesy "I know what that look is. Trying to take in all the different crowds all at once."

    jonesy "It's definitely your first time, huh? Tell me, whattayya think of it so far?"

    anon "I think… It's a lot to take in."

    anon "I don't, uh… well..."

    anon "I thought it'd be fun to try my hand at this competition. But I don't think… uh..."

    "Jonesy nodded knowingly."

    jonesy "I know. Believe me."

    jonesy "I remember my first time. It was simpler back then, but it all still had the same beats."

    jonesy "The unknown island, the competition, the anticipation, the calm before the storm."

    jonesy "Things may have gotten more colorful since those days, but the core of the game is still the same."

    show jonesy smile with Dissolve(0.5, time_warp=None, mipmap=None):
        xcenter 0.52 yoffset -40 zoom 0.45

    jonesy "Drop in. Stick together. Move forward. Win."

    "Jonesy flashes an unusually photogenic smile."

    "It's way too photogenic. Wow."

    jonesy "Think you can follow my lead, Anon? I can make this your win first try if you'll have me."

    "He exudes a level of confidence that almost makes me forget I don't actually feel like trying. Almost."

    "But... eh. Maybe I should just try? I don't know if it'll go anywhere though."

    "Oh. He notices my apprehension."

    show jonesy default with Dissolve(0.5, time_warp=None, mipmap=None):
        xcenter 0.52 yoffset -40 zoom 0.45

    jonesy "Hey. I've been through it all in this competition. I've led even the most bronze of teams into the victory royale."

    jonesy "I may not seem like much compared to the rest of these guys, but I've been competing long enough that I know the loop of Fortnite like the back of my hand."

    jonesy "..."

    jonesy "..."

    show jonesy concerned with Dissolve(0.3, time_warp=None, mipmap=None):
        xcenter 0.52 yoffset -40 zoom 0.45

    jonesy "..."

    jonesy "Anon, are you really up for this?"

    jonesy "It's all good if you'd like to leave. You can take the teleporter off the island."

    jonesy "Don't worry about it, really. We get no-shows all the time."

    "I... guess I really can leave."

    "But I'm already here. I might as well have 22 minutes of gaming before I head back to real life."

    anon "Nah, it's fine. I'd like to try this out once. It seems like it could be... fun."

    show jonesy thumbsup with Dissolve(0.3, time_warp=None, mipmap=None):
        xcenter 0.52 yoffset -40 zoom 0.45
    
    "Jonesy gives me a thumbs-up."

    jonesy "That's all I'm looking for."

    jonesy "Now, let's meet up with the rest of the squad. We still haveta' discuss where we're dropping."

    scene bg black with Dissolve(2.0, time_warp=None, mipmap=None)

    pause 1.0

    # This ends the game.

    return
