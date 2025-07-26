init python:
    # Player & party stats
    player_hp = 100
    jaun_hp = 120
    marko_hp = 150
    alain_hp = 90

    # Enemy stats
    enemy_hp = 100
    enemy_attack_min = 10
    enemy_attack_max = 25

# Character Definitions
define w = Character("Little Witch(You)", color="#B69ACC")  # The Little Elf Witch (player)
define jaun = Character("Jaun", color="#C97C5D")
define alain = Character("Alain", color="#5DB1C9")
define marko = Character("Marko", color="#8FDA9F")

#Flag definition
default inn_clue = False
default well_clue = False
default house_clue = False


label start:

    scene bg forest_day with fade

    w "This forest's quiet... too quiet."

    w "Not the peaceful kind. The kind that makes you feel watched."

    w "Still, better than another lecture from the Elders."

    w "They said chasing demon kings was foolish. Reckless."

    w "Maybe they’re right. But sitting around while the world falls apart?"

    w "That’s not for me."

    scene bg path_forest with dissolve

    w "I’ve tracked the stories this far. Burned maps. Half-finished journal pages."

    w "Someone saw something out here... something big."

    w "Could be a lead. Could be a waste of time."

    w "But when you’re hunting demon kings, you don’t wait for certainty."

    scene bg campfire_night with fade

    w "Smoke! Someone’s camping nearby."

    show jaun normal at left

    "???" "What are you doing here, kid."

    w "I am here to find a demon king."

    "???" "Demon kings?"

    w "Yes. And who are you?"

    jaun "My name is Jaun. I am a swordsman of Crimsom Blade."

    jaun "Come on, I’ll introduce you."

    show marko normal at right

    marko "Hey Jaun! who is that kid with you."

    jaun "She is looking for demon kings, so I bring her here."

    jaun "He is Marko our tank."

    marko "You don’t look like a sellsword or a knight."

    w "I’m not. I’m a witch."

    marko "A little one, at that."

    w "(‘Little’ always sticks, doesn’t it?)"

    marko "She’s elf-blooded, no doubt. Look at her eyes."

    w "Is this a problem?"

    jaun "Not if you can burn a demon king from the inside out."

    show alain normal at right
    
    alain "So how strong are you?"

    w "And who are you?"

    alain "Alain. I keep them alive. When I can."

    w "A healer?"

    alain "A war-priest, technically. But yes."

    marko "We’ve been tracking a rumor. Demon king activity in the region."

    jaun "A village not far from here went quiet. Whole place just... vanished."

    w "You think it's a demon king?"

    marko "We’re sure of it. No bandits leave behind empty beds and warm food."

    alain "And we could use another set of sharp eyes. Magic eyes."

    w "You’re inviting me?"

    jaun "If you’ve got the guts for it. Crimson Blade doesn’t carry dead weight."

    w "I’m not here to be carried."

    alain "Then let’s see how long you can run with us, little witch."

    marko "We head out at first light. Get some rest—if you can sleep."

    w "I don’t sleep much."

    jaun "Good. Then you’ll fit right in."

    scene bg night_sky with fade

    w "(Crimson Blade. A strange name for a band of hunters, but it suits them.)"

    w "(Jaun is all steel and scars. Alain looks like he walked out of a cathedral. Marko talks little, but his gaze is sharp.)"

    w "(They’ve seen blood. And they’ve lived through it.)"

    w "(If a demon king is really nearby... then this is where I’m needed.)"

    jump village_investigation

label village_investigation:

    scene bg village_ruins_morning with fade

    w "So this is the village..."

    jaun "What’s left of it."

    marko "No signs of struggle. No blood. No bodies."

    alain "Which makes it worse."

    w "Let me look around. Maybe something’s still whispering."

    menu:
        "Where do you want to investigate first?"
        "The abandoned inn":
            jump inn_scene
        "The well in the center":
            jump well_scene
        "A house with an open door":
            jump house_scene

label inn_scene:

    scene bg inn_interior_dusty with dissolve

    w "This place still smells of food. Faint... but recent."

    w "Chairs are still tucked in. Cups half full. Like they just walked out."

    w "(Or were pulled out...)"

    w "Wait—this carving on the wall... it’s a warning rune. Broken, though."

    w "(Someone tried to protect this place.)"

    $ inn_clue = True

    jump return_to_menu

label well_scene:

    scene bg village_well with dissolve

    w "The well’s sealed. Wooden planks nailed shut."

    w "Too clean for an old village. Recent work."

    w "What were they trying to keep out? Or... keep in?"

    w "Something's scratched into the stone... 'Don’t listen to it.'"

    w "(Creepy. Noted.)"

    $ well_clue = True

    jump return_to_menu

label house_scene:

    scene bg house_dark with fade

    w "This house looks untouched... but the door was open."

    w "Strange. No footprints, no signs of struggle."

    w "Just a chair, a table... and that chest over there."

    w "Too obvious."

    show mimic closed at center

    w "Let’s test a theory."

    w "..."

    w "Alright, chest. Let’s see what you’re really hiding."

    # Mimic opens
    show mimic open with dissolve
    play sound "mimic_roar.wav"

    "mimic" "S̷̛̟̺̖͗̍o̷̦̯̹͍͗̏͆́̒̐ ̴̰͚̔͒h̷̢̤̠̖̓͐̋͊͝͝ȗ̸͙̍̆͛́̋̓n̵̳̘̲̱̓͆̇ǧ̷̛̘̎̏r̴̞̯̬̤͌̋̒̀͐͝y̷̡̢̜̹̖̋͐́́͘͠..."

    w "Called it."

    "mimic" "F̸̛̯o̶̖̒ǫ̸̈́d̶̽͜.̴͕̐ ̸̰͑F̴̡̿o̵̞̒o̸̯̽d̸̍ͅ!̸̞́"

    w "You’re not getting a bite of me."

    menu:
        "What do you do?"

        "Cast a fire spell":
            w "Burn!"
            play sound "fire_blast.wav"
            "The mimic screeches as flames consume its false wooden shell."
            w "Next time, pick a less flammable disguise."
            $ house_clue = True
            jump return_to_menu

        "Dodge and strike with a blade":
            w "Too slow, chest-for-brains!"
            play sound "slash.wav"
            "You roll past its snapping jaws and slash its mimic tongue clean off."
            w "Disgusting... but effective."
            $ house_clue = True
            jump return_to_menu

        "Try to trap it with magic chains":
            w "Let’s hold that appetite of yours."
            play sound "chain_bind.wav"
            "Arcane chains whip forward and pin the mimic in place as it thrashes."
            w "Hope the others appreciate gift-wrapped nightmares."
            $ house_clue = True
            jump return_to_menu

label return_to_menu:

    menu:
        "The abandoned inn" if not inn_clue:
            jump inn_scene
        "The well in the center" if not well_clue:
            jump well_scene
        "A house with an open door" if not house_clue:
            jump house_scene
        "I'm done investigating":
            jump end_investigation

label end_investigation:

    scene bg village_ruins_morning with fade

    w "(Something’s wrong here. But where’s the demon king?)"

    alain "Find anything useful?"

    if inn_clue and well_clue and house_clue:
        w "Everything points to something *pretending* to be normal. A presence that mimics routine... before striking."
    elif inn_clue and house_clue:
        w "People vanished mid-meal. Something unnatural passed through—quietly."
    elif well_clue:
        w "They tried to seal something in the well. Or keep something from coming out."
    else:
        w "Not much, but enough to know this wasn’t natural."

    marko "Everyone disappeared too cleanly."

    jaun "Let's head back for now."

    jump after_investigation

label after_investigation:

    scene bg campfire_night with fade

    show jaun normal at left
    show marko normal at right
    show alain normal at center

    w "That village was cursed. Not just abandoned."

    marko "We found claw marks. Too large for a beast, too erratic for a man."

    alain "The well reeked of death. Something was thrown down there... or crawled up."

    jaun "We saw movement near the inn. It fled before we could strike."

    w "I ran into a mimic disguised as a chest. Almost took my head off."

    alain "A mimic? They don’t wander. Something placed it there—like bait."

    marko "Which means something smarter is behind this."

    w "There’s a pattern in the decay. Something feeding, growing. Testing how far it can push."

    jaun "Then we’re on the right trail."

    w "But are you ready to face a demon king. Not yet."

    marko "One more village like that and we won't have a choice."

    alain "We rest tonight. But tomorrow... we follow the corruption."

    jaun "Little Witch. You handled yourself well."

    w "Thanks. You’re not so bad either—for mercenaries."

    marko "She's got a mouth. I like that."

    alain "Let’s see if her fire holds when we face the real thing."

    w "(The Crimson Blade fights like they’ve seen the end of the world—and survived it.)"

    w "(I just hope I’m not too late to stop it from ending again.)"

    scene bg night_sky with fade

    w "(Tomorrow, the real hunt begins.)"

    scene bg morning_forest with fade

    jump forest_ruins

label forest_ruins:

    scene bg forest_path_dark with fade

    w "(The air’s thicker here. Like it’s choking on something old and angry.)"

    marko "We’re not far now. That ridge ahead… there’s something behind it."

    alain "That corruption we felt in the village—it’s stronger here."

    jaun "Weapons out. No jokes. No stumbles."

    w "Wait…"

    scene bg ruins_gate with dissolve

    w "That’s an elven barrier sigil. Broken, but still faintly glowing."

    marko "You sure?"

    w "It’s old magic. Very old. We used these to seal places touched by the abyss."

    alain "You’re saying someone already tried to contain what’s in there?"

    w "Yes. And they failed."

    jaun "Then we finish what they couldn’t."

    show jaun normal at left
    show marko normal at right
    show alain normal at center

    menu:
        "Enter the ruins cautiously.":
            $ approach_method = "cautious"
            w "Let’s move slow. If this place was sealed, it’s for a reason."

        "Break through boldly.":
            $ approach_method = "bold"
            w "No point wasting time. Let’s break whatever’s left and go in."

    scene bg ruins_inside with fade

    w "(Stone corridors swallowed by roots. Walls cracked with time… and blood.)"

    alain "There’s a stink in the air. Like burning metal and rot."

    marko "Shh…"

    "..."

    w "(I feel it. Something’s awake. And it’s waiting.)"

    jaun "We’re not alone."

    show enemy_shadow with dissolve

    "???" "Thieves... meddlers..."

    w "It speaks?"

    "???" "This place was buried for a reason. And now you’ve come to bleed."

    alain "It’s not a demon king… but it’s something touched by one."

    marko "A guardian. Or a prisoner."

    w "Either way—"

    jaun "We fight."

    scene bg battle_flash with fade

    play music "battle_theme.ogg"

    label demon_fight:

    scene bg battle_field with fade
    play music "battle_theme.ogg"

    w "It’s coming…!"

    "The corrupted guardian snarls and charges toward you."

    label battle_loop:

        if enemy_hp <= 0:
            jump victory

        if player_hp <= 0 and jaun_hp <= 0 and marko_hp <= 0 and alain_hp <= 0:
            jump game_over

        "Your turn"

        menu:
            "Fire Sigil (Deals 25 damage)":
                $ enemy_hp -= 25
                w "Take this!"
            "Focus Magic (+10 HP regen)":
                $ player_hp = min(player_hp + 10, 100)
                w "(Steady… breathe…)"
    
    jump enemy_phase

    label enemy_phase:

    if 'stunned' in globals() and stunned:
        "The enemy flinches, stunned by Marko’s blow!"
        $ stunned = False
        jump battle_loop

    "The guardian attacks!"

    $ import random
    $ target = renpy.random.choice(["player", "jaun", "marko", "alain"])
    $ dmg = random.randint(enemy_attack_min, enemy_attack_max)

    if target == "player":
        $ player_hp -= dmg
        "The guardian claws at you! (-[dmg] HP)"
    elif target == "jaun":
        $ jaun_hp -= dmg
        "Jaun takes a savage hit! (-[dmg] HP)"
    elif target == "marko":
        $ marko_hp -= dmg
        "Marko blocks part of the blow, but still takes damage. (-[dmg] HP)"
    elif target == "alain":
        $ alain_hp -= dmg
        "Alain stumbles, wounded by dark energy! (-[dmg] HP)"

    jump battle_loop

label game_over:
    stop music fadeout 1.5
    scene bg black with fade

    "Your party falls. The ruins echo with silence… and hunger."

    return

label victory:
    stop music fadeout 1.5
    scene bg ruins_inside with fade

    "The guardian screeches and collapses, crumbling into ash."

    w "It’s over… for now."

    show enemy_shadow defeated with dissolve

    stop music fadeout 2.0

    scene bg ruins_inside_dim with fade

    jaun "That wasn’t even the main threat, was it?"

    w "No. Just a gatekeeper. The deeper chamber is still sealed."

    alain "There’s another door. Symbols all over it. Looks like a trial."

    marko "And we just rang the bell announcing ourselves."

    w "Then we go in. Together."

    jaun "Crimson Blade doesn’t run."

    w "Neither does the witch."

    return





label demon_king_fragment_battle:

    scene bg ritual_circle with flash
    play music "ominous_theme.ogg" fadein 1.5

    w "The seal... it’s breaking. That thing—it's not whole, but it's waking up!"

    marko "Everyone, form up! We hold it here!"

    alain "By the light, what even is that thing?"

    jaun "It’s a piece of a Demon King. Be ready for anything!"

    show demon_king_fragment with dissolve

    demon "Foolish... mortals..."

    w "It speaks?! Even fractured, it has will!"

    # Begin battle loop (simplified for narrative VN)
    menu:
        "Cast a barrier spell to protect the team":
            $ player_action = "barrier"
            w "Shielding us now!"
            "A shimmering light surrounds the group as the fragment's tendrils lash out."

        "Attack with focused fire magic":
            $ player_action = "attack"
            w "Let’s see how you like this!"
            "A searing blaze erupts from your staff, pushing the fragment back."

        "Distract it so Crimson Blade can flank":
            $ player_action = "distract"
            w "Hey! Over here, you ugly shadow!"
            "The fragment turns toward you, allowing Jaun and Marko to strike."

    if player_action == "barrier":
        marko "The barrier held! We’re alive!"
    elif player_action == "attack":
        alain "That actually hurt it!"
    elif player_action == "distract":
        jaun "Nice move, witch! That gave us an opening!"

    demon "You... meddling insects... I will—"

    w "You’ll do nothing!"

    "With a final coordinated strike, the fragment is banished back into the seal, its echoing scream fading into silence."

    scene bg forest_day with fade
    stop music fadeout 2.0

    w "(That was just a fragment... and it nearly killed us.)"
    w "(What kind of nightmare waits when we face the real one?)"

    marko "You alright, little witch?"

    w "Yeah. I’m fine. Just... shaken."

    jaun "We need answers. And I think this seal is older than anything in the village."

    alain "There are more fragments. And worse."

    w "Then we keep moving. This world won’t save itself."

    jump next_chapter_intro

label next_chapter_intro:

    scene bg forest_clearing with fade
    play music "adventure_theme.ogg" fadein 1.5

    w "The fragment is gone... but its scream still echoes in my mind."

    marko "We should rest. But I fear the real Demon King is watching."

    alain "The barrier sigils... they were part of a larger network."

    jaun "We need to find the heart of this corruption. Fast."

    w "There’s a ruined shrine to the east. Maybe its archives hold clues."

    scene bg travel_forest with dissolve

    w "(We travel deeper into the wilds, under a sky half-lit by that blood-green moon.)"

    # Transition to shrine scene
    jump shrine_ruins

label shrine_ruins:

    scene bg shrine_exterior with fade

    w "This shrine... once a place of healing. Now it bleeds shadow."

    marko "Look at those runes. They’ve been carved in haste."

    alain "We might try restoring them."

    menu:
            "Attempt to cleanse the runes":
                jump cleanse_runes
            "Search inside for a hidden archive":
                jump search_archive

label cleanse_runes:

    w "Light of Eld’Aran, guide my hand..."

    play sound "magic_pulse.wav"
    scene bg shrine_exterior_light with flash
    "The runes glow and crackle, pushing back tendrils of darkness."

    w "The path forward should be clear."

    jump shrine_interior

label search_archive:

    scene bg shrine_interior_dusty with dissolve

    w "Shelves of scrolls... but most are ruined."

    w "Wait—this tome survived."

    show image tome_open at center
    w "It speaks of a Demon King born from ancient pride, sealed here by our forebears."

    jump shrine_interior

label shrine_interior:

    scene bg shrine_interior with fade

    jaun "Door ahead, engraved with a single word: 'Pride.'"

    w "This is our target. The Demon King of Pride."

    marko "Brace yourselves."

    # Final boss confrontation
    jump final_boss_battle

label final_boss_battle:

    scene bg throne_room with fade
    play music "boss_theme.ogg" fadein 1.5

    w "So... you are the source of all this."

    demon_king "Foolish witch. You think you can undo my dominion?"

    menu:
            "Invoke the purified runes' power":
                $ action = "runes"
                w "By the light of the old shrine, I cast you out!"
            "Strike with all your allies":
                $ action = "strike"
                w "Crimson Blade, now!"
            "Speak to the Demon King":
                $ action = "speak"
                w "Why do you corrupt this world?"

    if action == "runes":
        play sound "rune_blast.wav"
        "A wave of pure magic crashes into the Demon King, shattering his dark form."
        demon_king "No... this cannot be..."
    elif action == "strike":
        play sound "battle_clash.wav"
        "Jaun, Marko, and Alain join in, their combined assault overwhelming the Demon King."
        demon_king "Argh... united... power..."
    elif action == "speak":
        demon_king "I am the world's sorrow made flesh. I reflect your own pride."
        w "Then I cast away all fears... and slay you."
        play sound "final_strike.wav"
        "A single stroke severs the Demon King’s essence."

    scene bg throne_room_destroyed with fade
    stop music fadeout 2.0

    demon_king "You... have freed... yourselves..."

    w "(His words fade with the ruin of his throne.)"

    # Epilogue
    jump epilogue

label epilogue:

    scene bg forest_dawn with fade
    play music "peace_theme.ogg" fadein 1.5

    w "The world breathes again."

    alain "The corruption recedes with the first light."

    marko "Villages will wake. Life returns."

    jaun "Crimson Blade stands victorious."

    w "But every victory... demands a choice."

    menu:
            "I record the end, and a beginning":
                w "(I write of ending darkness, and the dawn it brings.)"
            "I vow to watch over this world":
                w "(I vow to guard against pride ever rising again.)"
            "I lay down my blade and rest":
                w "(At last, I rest. Tomorrow, a new story begins.)"

    scene bg credits with fade
    show text "Thank you for playing
Chronicles Beneath the Blood-Green Moon" with dissolve

    return
