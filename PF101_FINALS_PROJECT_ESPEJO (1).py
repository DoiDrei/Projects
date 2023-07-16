
class ZooKeeper:          
                       
    def __init__(self,LoA):
        self.LoA = LoA

    def displayanimals(self):
        for each_animal in self.LoA:
            print("►►",each_animal)

    def addanimal(self):
            animal_Name = input("What animal would you like to add : ")
            self.LoA.append(animal_Name) 

    def deleteanimal(self):
            animal_Name = input("What animal would you like to rehome : ")
            self.LoA.remove(animal_Name)
            print("animal rehomed :)")


if __name__ == "__main__":
    General = ZooKeeper(["Crocodile","Snake","Lizard","Turtle","Chameleon","Komodo dragon","Gecko","Monitor lizard","Alligator","Iguana","Boa constrictor","Cobra","Garter snake",
    "Anaconda","Sea turtle","Frilled lizard","Galapagos tortoise","Green sea turtle","Horned lizard","King cobra","Leatherback sea turtle","Rattlesnake","Saltwater crocodile","Lion","Elephant","Giraffe","Kangaroo","Zebra","Rhino","Gorilla","Dolphin","Bat","Squirrel",
    "Panda","Koala","Wolf","Hedgehog","Fox","Raccoon","Otter","Kangaroo Rat","Armadillo","Platypus","Pangolin","Eagle","Hummingbird","Ostrich","Penguin","Flamingo","Swan","Owl","Peacock","Kiwi","Parrot","Pelican","Seagull","Cardinal",
    "Toucan","Albatross","Pigeon","Hawk","Raven","Stork","Emu","Dove","Canary","Vulture","Kingfisher","Blue Jay","Clownfish","Angelfish","Betta fish","Pufferfish","Discus fish","Guppy","Rainbow fish","Swordtail","Goldfish","Tetra","Cichlid","Eel",
    "Lionfish","Mackerel","Salmon","Tuna","Seahorse","Barracuda","Clown triggerfish","Grouper","Wrasse","Flounder","Herring","Manta ray","Shark"])
    General2 = ZooKeeper({"Crocodile": "a large, semi-aquatic reptile with a long snout, powerful jaws, and tough armored skin, known for its strength and aggression",
    "Snake": "a long, legless reptile with a flexible body and the ability to constrict its prey or inject venom with its fangs, found in a variety of habitats",
    "Lizard": "a reptile with scaly skin, a long tail, and the ability to shed its tail for protection, known for its diverse range of species and habitats",
    "Turtle": "a reptile with a hard shell that covers its body, a beaked mouth, and the ability to retract its head and legs inside its shell for protection",
    "Chameleon": "a lizard known for its ability to change color to match its surroundings and its long, sticky tongue used for catching prey",
    "Komodo dragon": "a large, venomous lizard with a powerful bite, found only on a few Indonesian islands and known for its ability to hunt prey much larger than itself",
    "Gecko": "a small, agile lizard with sticky pads on its feet for climbing and a unique vocalization often described as a 'chirp' or 'click' sound",
    "Monitor lizard": "a large, carnivorous lizard with a long tail and sharp claws, found in Africa, Asia, and Australia and known for its intelligence and predatory skills",
    "Alligator": "a large, semi-aquatic reptile with a broad snout, powerful jaws, and armored skin, found in the southeastern United States and China and known for its ability to hunt both on land and in water",
    "Iguana": "a large, herbivorous lizard with a distinctive dewlap and known for its long lifespan and docile temperament as a pet",
    "Boa constrictor": "a large, non-venomous snake known for its ability to constrict and suffocate its prey, found in Central and South America",
    "Cobra": "a venomous snake with a hood on its neck that can be expanded when threatened, found in Africa and Asia",
    "Garter snake": "a small, non-venomous snake with a distinctive striped pattern, found in North and Central America",
    "Anaconda": "a large, non-venomous snake found in South America that is known for its size and ability to constrict its prey",
    "Sea turtle": "a large, aquatic turtle with flippers and a streamlined shell for swimming, found in oceans around the world",
    "Frilled lizard": "a lizard with a distinctive frill around its neck that expands when threatened, found in Australia and New Guinea",
    "Galapagos tortoise": "a large, herbivorous turtle found only on the Galapagos Islands and known for its long lifespan and unique saddleback shell",
    "Green sea turtle": "a large, herbivorous turtle with a smooth shell and paddle-like flippers for swimming, found in tropical and subtropical oceans around the world",
    "Horned lizard": "a small, spiny lizard with a distinctive crown of horns on its head, found in North and Central America",
    "King cobra": "a highly venomous snake found in Southeast Asia and known for its size and deadly bite",
    "Leatherback sea turtle": "a large, endangered turtle with a soft, leathery shell and the ability to dive deeper than any other sea turtle, found in oceans around the world",
    "Rattlesnake": "a venomous snake with a distinctive rattle on its tail used to warn potential threats, found in North and South America",
    "Saltwater crocodile": "a large, aggressive crocodile found in Australia, Southeast Asia, and parts of India, known for its ability",
    "Lion": "a large, powerful carnivorous mammal with a distinctive mane and known for its roar",
    "Elephant": "a massive mammal with a long trunk, ivory tusks, and large ears used for cooling",
    "Giraffe": "a tall mammal with a long neck and distinctive spotted pattern on its fur",
    "Kangaroo": "a marsupial mammal native to Australia with powerful hind legs and a pouch for carrying its young",
    "Zebra": "a mammal with distinctive black and white striped fur and known for its agility and speed",
    "Rhino": "a large mammal with a distinctive horn on its nose and a tough, armored hide",
    "Gorilla": "a large, powerful primate known for its strength and intelligence",
    "Dolphin": "a highly intelligent mammal that lives in the water and is known for its playful behavior and communication skills",
    "Bat": "a mammal that can fly and is known for its echolocation abilities",
    "Squirrel": "a small, agile mammal with a bushy tail and known for its ability to climb trees and gather nuts",
    "Panda": "a mammal with distinctive black and white fur and known for its peaceful nature and love of bamboo",
    "Koala": "a marsupial mammal native to Australia with a distinctive round face and known for its love of eucalyptus leaves",
    "Wolf": "a carnivorous mammal known for its pack mentality and distinctive howl",
    "Hedgehog": "a small, spiny mammal known for rolling into a ball for protection",
    "Fox": "a small carnivorous mammal with a bushy tail and known for its cunning and adaptability",
    "Raccoon": "a mammal with distinctive black and white fur and a mask-like pattern around its eyes, known for its intelligence and dexterity with its hands",
    "Otter": "a playful mammal that lives in the water and is known for its sleek fur and ability to use tools",
    "Kangaroo Rat": "a small rodent with long back legs and a kangaroo-like hopping gait, found in arid regions of North America",
    "Armadillo": "a mammal with a bony armor shell and known for its digging ability and curling into a ball for protection",
    "Platypus": "a unique mammal that lays eggs and has a duck-like bill, beaver-like tail, and webbed feet, native to Australia",
    "Pangolin": "a mammal covered in scales and known for its ability to roll into a ball for protection, found in Africa and Asia",
    "Eagle": "a large bird of prey with a hooked beak, sharp talons, and impressive eyesight","Hummingbird": "a tiny bird known for its ability to hover in mid-air and its brightly-colored feathers",
    "Ostrich": "a flightless bird with a long neck, powerful legs, and the ability to run up to 43 miles per hour",
    "Penguin": "a bird that is adapted to life in cold environments and is known for its distinctive waddling gait",
    "Flamingo": "a tall, pink bird with a long, thin neck and distinctive curved beak",
    "Swan": "a large, graceful bird with a long, curved neck and distinctive white plumage",
    "Owl": "a nocturnal bird of prey with large, forward-facing eyes and the ability to rotate its head up to 270 degrees",
    "Peacock": "a large bird known for its colorful plumage and impressive courtship display",
    "Kiwi": "a flightless bird native to New Zealand with distinctive hair-like feathers and a long, curved beak",
    "Parrot": "a highly intelligent bird known for its ability to mimic human speech and for its brightly-colored plumage",
    "Pelican": "a large water bird with a distinctive pouch-like bill used for catching and carrying fish",
    "Seagull": "a common coastal bird with white and grey plumage and a distinctive squawking call",
    "Cardinal": "a small, brightly-colored bird with a distinctive crest and a sweet, musical song",
    "Toucan": "a brightly-colored bird with a large, curved bill that is native to the forests of Central and South America",
    "Albatross": "a large seabird with a long wingspan and the ability to fly for hours without landing",
    "Pigeon": "a common bird found in cities and other urban areas with a distinctive cooing call",
    "Hawk": "a bird of prey known for its sharp talons and keen eyesight",
    "Raven": "a large, black bird with a distinctive croaking call and a reputation for being intelligent and mysterious",
    "Stork": "a large bird with a long, thin beak and distinctive black and white plumage",
    "Emu": "a flightless bird native to Australia with distinctive shaggy feathers and powerful legs",
    "Dove": "a small, gentle bird known for its cooing call and symbolic association with peace",
    "Canary": "a small, brightly-colored bird known for its beautiful song and its popularity as a pet",
    "Vulture": "a large bird of prey that feeds on the carcasses of dead animals",
    "Kingfisher": "a small, brightly-colored bird with a distinctive long, pointed beak that is used for catching fish",
    "Blue Jay": "a small, noisy bird with blue and white plumage and a distinctive crest on its head",
    "Clownfish": "a small, brightly-colored fish with distinctive orange and white stripes,",
    "Angelfish": "a popular aquarium fish known for its unique shape and striking colors,",
    "Betta fish": "also known as Siamese fighting fish, a beautiful and territorial species with long, flowing fins,",
    "Pufferfish": "a spiky, round fish that can inflate its body to deter predators,",
    "Discus fish": "a colorful and graceful species that is highly prized by aquarium enthusiasts,",
    "Guppy": "a small, easy-to-care-for fish with a variety of colors and patterns,",
    "Rainbow fish": "a beautiful species known for its iridescent scales and peaceful nature,",
    "Swordtail": "a popular livebearer fish with a distinctive, sword-like tail fin,",
    "Goldfish": "a classic aquarium fish that comes in many different varieties, including fantails, orandas, and comets,",
    "Tetra": "a family of small, colorful fish that are well-suited for community aquariums,",
    "Cichlid": "a family of fish known for its many different shapes, sizes, and colors, as well as its aggressive behavior,",
    "Eel": "a long, snake-like fish that can be found in both fresh and saltwater environments,",
    "Lionfish": "a venomous species known for its striking appearance and impressive hunting skills,",
    "Mackerel": "a fast-swimming, predatory fish that is often used for food,",
    "Salmon": "a popular game fish that is known for its rich, flavorful flesh,",
    "Tuna": "a large, powerful fish that is prized for its meat, which is used in sushi and other dishes,",
    "Seahorse": "a small, slow-moving fish that is known for its unique appearance and fascinating breeding habits,",
    "Barracuda": "a predatory fish that is found in tropical and subtropical waters around the world,",
    "Clown triggerfish": "a brightly-colored species known for its distinctive, polka-dotted appearance,",
    "Grouper": "a large, slow-moving fish that can be found in warm waters around the world,",
    "Wrasse": "a family of fish that includes many different species known for their striking colors and patterns,",
    "Flounder": "a flat, bottom-dwelling fish that can change color to blend in with its surroundings,",
    "Herring": "a small, oily fish that is often used for food and forage,",
    "Manta ray": "a large, graceful fish that is found in tropical and subtropical waters around the world,",
    "Shark": "a powerful, predatory fish that is feared and respected by humans and other marine creatures alike,"})

    Gen = ["Crocodile","Snake","Lizard","Turtle","Chameleon","Komodo dragon","Gecko","Monitor lizard","Alligator","Iguana","Boa constrictor","Cobra","Garter snake",
    "Anaconda","Sea turtle","Frilled lizard","Galapagos tortoise","Green sea turtle","Horned lizard","King cobra","Leatherback sea turtle","Rattlesnake","Saltwater crocodile","Lion","Elephant","Giraffe","Kangaroo","Zebra","Rhino","Gorilla","Dolphin","Bat","Squirrel",
    "Panda","Koala","Wolf","Hedgehog","Fox","Raccoon","Otter","Kangaroo Rat","Armadillo","Platypus","Pangolin","Eagle","Hummingbird","Ostrich","Penguin","Flamingo","Swan","Owl","Peacock","Kiwi","Parrot","Pelican","Seagull","Cardinal",
    "Toucan","Albatross","Pigeon","Hawk","Raven","Stork","Emu","Dove","Canary","Vulture","Kingfisher","Blue Jay","Clownfish","Angelfish","Betta fish","Pufferfish","Discus fish","Guppy","Rainbow fish","Swordtail","Goldfish","Tetra","Cichlid","Eel",
    "Lionfish","Mackerel","Salmon","Tuna","Seahorse","Barracuda","Clown triggerfish","Grouper","Wrasse","Flounder","Herring","Manta ray","Shark"]
    Gen2 = {"Crocodile": "a large, semi-aquatic reptile with a long snout, powerful jaws, and tough armored skin, known for its strength and aggression",
    "Snake": "a long, legless reptile with a flexible body and the ability to constrict its prey or inject venom with its fangs, found in a variety of habitats",
    "Lizard": "a reptile with scaly skin, a long tail, and the ability to shed its tail for protection, known for its diverse range of species and habitats",
    "Turtle": "a reptile with a hard shell that covers its body, a beaked mouth, and the ability to retract its head and legs inside its shell for protection",
    "Chameleon": "a lizard known for its ability to change color to match its surroundings and its long, sticky tongue used for catching prey",
    "Komodo dragon": "a large, venomous lizard with a powerful bite, found only on a few Indonesian islands and known for its ability to hunt prey much larger than itself",
    "Gecko": "a small, agile lizard with sticky pads on its feet for climbing and a unique vocalization often described as a 'chirp' or 'click' sound",
    "Monitor lizard": "a large, carnivorous lizard with a long tail and sharp claws, found in Africa, Asia, and Australia and known for its intelligence and predatory skills",
    "Alligator": "a large, semi-aquatic reptile with a broad snout, powerful jaws, and armored skin, found in the southeastern United States and China and known for its ability to hunt both on land and in water",
    "Iguana": "a large, herbivorous lizard with a distinctive dewlap and known for its long lifespan and docile temperament as a pet",
    "Boa constrictor": "a large, non-venomous snake known for its ability to constrict and suffocate its prey, found in Central and South America",
    "Cobra": "a venomous snake with a hood on its neck that can be expanded when threatened, found in Africa and Asia",
    "Garter snake": "a small, non-venomous snake with a distinctive striped pattern, found in North and Central America",
    "Anaconda": "a large, non-venomous snake found in South America that is known for its size and ability to constrict its prey",
    "Sea turtle": "a large, aquatic turtle with flippers and a streamlined shell for swimming, found in oceans around the world",
    "Frilled lizard": "a lizard with a distinctive frill around its neck that expands when threatened, found in Australia and New Guinea",
    "Galapagos tortoise": "a large, herbivorous turtle found only on the Galapagos Islands and known for its long lifespan and unique saddleback shell",
    "Green sea turtle": "a large, herbivorous turtle with a smooth shell and paddle-like flippers for swimming, found in tropical and subtropical oceans around the world",
    "Horned lizard": "a small, spiny lizard with a distinctive crown of horns on its head, found in North and Central America",
    "King cobra": "a highly venomous snake found in Southeast Asia and known for its size and deadly bite",
    "Leatherback sea turtle": "a large, endangered turtle with a soft, leathery shell and the ability to dive deeper than any other sea turtle, found in oceans around the world",
    "Rattlesnake": "a venomous snake with a distinctive rattle on its tail used to warn potential threats, found in North and South America",
    "Saltwater crocodile": "a large, aggressive crocodile found in Australia, Southeast Asia, and parts of India, known for its ability",
    "Lion": "a large, powerful carnivorous mammal with a distinctive mane and known for its roar",
    "Elephant": "a massive mammal with a long trunk, ivory tusks, and large ears used for cooling",
    "Giraffe": "a tall mammal with a long neck and distinctive spotted pattern on its fur",
    "Kangaroo": "a marsupial mammal native to Australia with powerful hind legs and a pouch for carrying its young",
    "Zebra": "a mammal with distinctive black and white striped fur and known for its agility and speed",
    "Rhino": "a large mammal with a distinctive horn on its nose and a tough, armored hide",
    "Gorilla": "a large, powerful primate known for its strength and intelligence",
    "Dolphin": "a highly intelligent mammal that lives in the water and is known for its playful behavior and communication skills",
    "Bat": "a mammal that can fly and is known for its echolocation abilities",
    "Squirrel": "a small, agile mammal with a bushy tail and known for its ability to climb trees and gather nuts",
    "Panda": "a mammal with distinctive black and white fur and known for its peaceful nature and love of bamboo",
    "Koala": "a marsupial mammal native to Australia with a distinctive round face and known for its love of eucalyptus leaves",
    "Wolf": "a carnivorous mammal known for its pack mentality and distinctive howl",
    "Hedgehog": "a small, spiny mammal known for rolling into a ball for protection",
    "Fox": "a small carnivorous mammal with a bushy tail and known for its cunning and adaptability",
    "Raccoon": "a mammal with distinctive black and white fur and a mask-like pattern around its eyes, known for its intelligence and dexterity with its hands",
    "Otter": "a playful mammal that lives in the water and is known for its sleek fur and ability to use tools",
    "Kangaroo Rat": "a small rodent with long back legs and a kangaroo-like hopping gait, found in arid regions of North America",
    "Armadillo": "a mammal with a bony armor shell and known for its digging ability and curling into a ball for protection",
    "Platypus": "a unique mammal that lays eggs and has a duck-like bill, beaver-like tail, and webbed feet, native to Australia",
    "Pangolin": "a mammal covered in scales and known for its ability to roll into a ball for protection, found in Africa and Asia",
    "Eagle": "a large bird of prey with a hooked beak, sharp talons, and impressive eyesight","Hummingbird": "a tiny bird known for its ability to hover in mid-air and its brightly-colored feathers",
    "Ostrich": "a flightless bird with a long neck, powerful legs, and the ability to run up to 43 miles per hour",
    "Penguin": "a bird that is adapted to life in cold environments and is known for its distinctive waddling gait",
    "Flamingo": "a tall, pink bird with a long, thin neck and distinctive curved beak",
    "Swan": "a large, graceful bird with a long, curved neck and distinctive white plumage",
    "Owl": "a nocturnal bird of prey with large, forward-facing eyes and the ability to rotate its head up to 270 degrees",
    "Peacock": "a large bird known for its colorful plumage and impressive courtship display",
    "Kiwi": "a flightless bird native to New Zealand with distinctive hair-like feathers and a long, curved beak",
    "Parrot": "a highly intelligent bird known for its ability to mimic human speech and for its brightly-colored plumage",
    "Pelican": "a large water bird with a distinctive pouch-like bill used for catching and carrying fish",
    "Seagull": "a common coastal bird with white and grey plumage and a distinctive squawking call",
    "Cardinal": "a small, brightly-colored bird with a distinctive crest and a sweet, musical song",
    "Toucan": "a brightly-colored bird with a large, curved bill that is native to the forests of Central and South America",
    "Albatross": "a large seabird with a long wingspan and the ability to fly for hours without landing",
    "Pigeon": "a common bird found in cities and other urban areas with a distinctive cooing call",
    "Hawk": "a bird of prey known for its sharp talons and keen eyesight",
    "Raven": "a large, black bird with a distinctive croaking call and a reputation for being intelligent and mysterious",
    "Stork": "a large bird with a long, thin beak and distinctive black and white plumage",
    "Emu": "a flightless bird native to Australia with distinctive shaggy feathers and powerful legs",
    "Dove": "a small, gentle bird known for its cooing call and symbolic association with peace",
    "Canary": "a small, brightly-colored bird known for its beautiful song and its popularity as a pet",
    "Vulture": "a large bird of prey that feeds on the carcasses of dead animals",
    "Kingfisher": "a small, brightly-colored bird with a distinctive long, pointed beak that is used for catching fish",
    "Blue Jay": "a small, noisy bird with blue and white plumage and a distinctive crest on its head",
    "Clownfish": "a small, brightly-colored fish with distinctive orange and white stripes,",
    "Angelfish": "a popular aquarium fish known for its unique shape and striking colors,",
    "Betta fish": "also known as Siamese fighting fish, a beautiful and territorial species with long, flowing fins,",
    "Pufferfish": "a spiky, round fish that can inflate its body to deter predators,",
    "Discus fish": "a colorful and graceful species that is highly prized by aquarium enthusiasts,",
    "Guppy": "a small, easy-to-care-for fish with a variety of colors and patterns,",
    "Rainbow fish": "a beautiful species known for its iridescent scales and peaceful nature,",
    "Swordtail": "a popular livebearer fish with a distinctive, sword-like tail fin,",
    "Goldfish": "a classic aquarium fish that comes in many different varieties, including fantails, orandas, and comets,",
    "Tetra": "a family of small, colorful fish that are well-suited for community aquariums,",
    "Cichlid": "a family of fish known for its many different shapes, sizes, and colors, as well as its aggressive behavior,",
    "Eel": "a long, snake-like fish that can be found in both fresh and saltwater environments,",
    "Lionfish": "a venomous species known for its striking appearance and impressive hunting skills,",
    "Mackerel": "a fast-swimming, predatory fish that is often used for food,",
    "Salmon": "a popular game fish that is known for its rich, flavorful flesh,",
    "Tuna": "a large, powerful fish that is prized for its meat, which is used in sushi and other dishes,",
    "Seahorse": "a small, slow-moving fish that is known for its unique appearance and fascinating breeding habits,",
    "Barracuda": "a predatory fish that is found in tropical and subtropical waters around the world,",
    "Clown triggerfish": "a brightly-colored species known for its distinctive, polka-dotted appearance,",
    "Grouper": "a large, slow-moving fish that can be found in warm waters around the world,",
    "Wrasse": "a family of fish that includes many different species known for their striking colors and patterns,",
    "Flounder": "a flat, bottom-dwelling fish that can change color to blend in with its surroundings,",
    "Herring": "a small, oily fish that is often used for food and forage,",
    "Manta ray": "a large, graceful fish that is found in tropical and subtropical waters around the world,",
    "Shark": "a powerful, predatory fish that is feared and respected by humans and other marine creatures alike,"}

    Reptiles1 = ["Crocodile","Snake","Lizard","Turtle","Chameleon","Komodo dragon","Gecko","Monitor lizard","Alligator","Iguana","Boa constrictor","Cobra","Garter snake",
    "Anaconda","Sea turtle","Frilled lizard","Galapagos tortoise","Green sea turtle","Horned lizard","King cobra","Leatherback sea turtle","Rattlesnake","Saltwater crocodile"]
    Reptiles2 = {"Crocodile": "a large, semi-aquatic reptile with a long snout, powerful jaws, and tough armored skin, known for its strength and aggression",
    "Snake": "a long, legless reptile with a flexible body and the ability to constrict its prey or inject venom with its fangs, found in a variety of habitats",
    "Lizard": "a reptile with scaly skin, a long tail, and the ability to shed its tail for protection, known for its diverse range of species and habitats",
    "Turtle": "a reptile with a hard shell that covers its body, a beaked mouth, and the ability to retract its head and legs inside its shell for protection",
    "Chameleon": "a lizard known for its ability to change color to match its surroundings and its long, sticky tongue used for catching prey",
    "Komodo dragon": "a large, venomous lizard with a powerful bite, found only on a few Indonesian islands and known for its ability to hunt prey much larger than itself",
    "Gecko": "a small, agile lizard with sticky pads on its feet for climbing and a unique vocalization often described as a 'chirp' or 'click' sound",
    "Monitor lizard": "a large, carnivorous lizard with a long tail and sharp claws, found in Africa, Asia, and Australia and known for its intelligence and predatory skills",
    "Alligator": "a large, semi-aquatic reptile with a broad snout, powerful jaws, and armored skin, found in the southeastern United States and China and known for its ability to hunt both on land and in water",
    "Iguana": "a large, herbivorous lizard with a distinctive dewlap and known for its long lifespan and docile temperament as a pet",
    "Boa constrictor": "a large, non-venomous snake known for its ability to constrict and suffocate its prey, found in Central and South America",
    "Cobra": "a venomous snake with a hood on its neck that can be expanded when threatened, found in Africa and Asia",
    "Garter snake": "a small, non-venomous snake with a distinctive striped pattern, found in North and Central America",
    "Anaconda": "a large, non-venomous snake found in South America that is known for its size and ability to constrict its prey",
    "Sea turtle": "a large, aquatic turtle with flippers and a streamlined shell for swimming, found in oceans around the world",
    "Frilled lizard": "a lizard with a distinctive frill around its neck that expands when threatened, found in Australia and New Guinea",
    "Galapagos tortoise": "a large, herbivorous turtle found only on the Galapagos Islands and known for its long lifespan and unique saddleback shell",
    "Green sea turtle": "a large, herbivorous turtle with a smooth shell and paddle-like flippers for swimming, found in tropical and subtropical oceans around the world",
    "Horned lizard": "a small, spiny lizard with a distinctive crown of horns on its head, found in North and Central America",
    "King cobra": "a highly venomous snake found in Southeast Asia and known for its size and deadly bite",
    "Leatherback sea turtle": "a large, endangered turtle with a soft, leathery shell and the ability to dive deeper than any other sea turtle, found in oceans around the world",
    "Rattlesnake": "a venomous snake with a distinctive rattle on its tail used to warn potential threats, found in North and South America",
    "Saltwater crocodile": "a large, aggressive crocodile found in Australia, Southeast Asia, and parts of India, known for its ability"}

    Mammals1 = ["Lion","Elephant","Giraffe","Kangaroo","Zebra","Rhino","Gorilla","Dolphin","Bat","Squirrel",
    "Panda","Koala","Wolf","Hedgehog","Fox","Raccoon","Otter","Kangaroo Rat","Armadillo","Platypus","Pangolin",]
    Mammals2 = {"Lion": "a large, powerful carnivorous mammal with a distinctive mane and known for its roar",
    "Elephant": "a massive mammal with a long trunk, ivory tusks, and large ears used for cooling",
    "Giraffe": "a tall mammal with a long neck and distinctive spotted pattern on its fur",
    "Kangaroo": "a marsupial mammal native to Australia with powerful hind legs and a pouch for carrying its young",
    "Zebra": "a mammal with distinctive black and white striped fur and known for its agility and speed",
    "Rhino": "a large mammal with a distinctive horn on its nose and a tough, armored hide",
    "Gorilla": "a large, powerful primate known for its strength and intelligence",
    "Dolphin": "a highly intelligent mammal that lives in the water and is known for its playful behavior and communication skills",
    "Bat": "a mammal that can fly and is known for its echolocation abilities",
    "Squirrel": "a small, agile mammal with a bushy tail and known for its ability to climb trees and gather nuts",
    "Panda": "a mammal with distinctive black and white fur and known for its peaceful nature and love of bamboo",
    "Koala": "a marsupial mammal native to Australia with a distinctive round face and known for its love of eucalyptus leaves",
    "Wolf": "a carnivorous mammal known for its pack mentality and distinctive howl",
    "Hedgehog": "a small, spiny mammal known for rolling into a ball for protection",
    "Fox": "a small carnivorous mammal with a bushy tail and known for its cunning and adaptability",
    "Raccoon": "a mammal with distinctive black and white fur and a mask-like pattern around its eyes, known for its intelligence and dexterity with its hands",
    "Otter": "a playful mammal that lives in the water and is known for its sleek fur and ability to use tools",
    "Kangaroo Rat": "a small rodent with long back legs and a kangaroo-like hopping gait, found in arid regions of North America",
    "Armadillo": "a mammal with a bony armor shell and known for its digging ability and curling into a ball for protection",
    "Platypus": "a unique mammal that lays eggs and has a duck-like bill, beaver-like tail, and webbed feet, native to Australia",
    "Pangolin": "a mammal covered in scales and known for its ability to roll into a ball for protection, found in Africa and Asia"}

    Birds1 = ["Eagle","Hummingbird","Ostrich","Penguin","Flamingo","Swan","Owl","Peacock","Kiwi","Parrot","Pelican","Seagull","Cardinal",
    "Toucan","Albatross","Pigeon","Hawk","Raven","Stork","Emu","Dove","Canary","Vulture","Kingfisher","Blue Jay"]
    Birds2 = {"Eagle": "a large bird of prey with a hooked beak, sharp talons, and impressive eyesight","Hummingbird": "a tiny bird known for its ability to hover in mid-air and its brightly-colored feathers",
    "Ostrich": "a flightless bird with a long neck, powerful legs, and the ability to run up to 43 miles per hour",
    "Penguin": "a bird that is adapted to life in cold environments and is known for its distinctive waddling gait",
    "Flamingo": "a tall, pink bird with a long, thin neck and distinctive curved beak",
    "Swan": "a large, graceful bird with a long, curved neck and distinctive white plumage",
    "Owl": "a nocturnal bird of prey with large, forward-facing eyes and the ability to rotate its head up to 270 degrees",
    "Peacock": "a large bird known for its colorful plumage and impressive courtship display",
    "Kiwi": "a flightless bird native to New Zealand with distinctive hair-like feathers and a long, curved beak",
    "Parrot": "a highly intelligent bird known for its ability to mimic human speech and for its brightly-colored plumage",
    "Pelican": "a large water bird with a distinctive pouch-like bill used for catching and carrying fish",
    "Seagull": "a common coastal bird with white and grey plumage and a distinctive squawking call",
    "Cardinal": "a small, brightly-colored bird with a distinctive crest and a sweet, musical song",
    "Toucan": "a brightly-colored bird with a large, curved bill that is native to the forests of Central and South America",
    "Albatross": "a large seabird with a long wingspan and the ability to fly for hours without landing",
    "Pigeon": "a common bird found in cities and other urban areas with a distinctive cooing call",
    "Hawk": "a bird of prey known for its sharp talons and keen eyesight",
    "Raven": "a large, black bird with a distinctive croaking call and a reputation for being intelligent and mysterious",
    "Stork": "a large bird with a long, thin beak and distinctive black and white plumage",
    "Emu": "a flightless bird native to Australia with distinctive shaggy feathers and powerful legs",
    "Dove": "a small, gentle bird known for its cooing call and symbolic association with peace",
    "Canary": "a small, brightly-colored bird known for its beautiful song and its popularity as a pet",
    "Vulture": "a large bird of prey that feeds on the carcasses of dead animals",
    "Kingfisher": "a small, brightly-colored bird with a distinctive long, pointed beak that is used for catching fish",
    "Blue Jay": "a small, noisy bird with blue and white plumage and a distinctive crest on its head"}
    
    Fishes1 = ["Clownfish","Angelfish","Betta fish","Pufferfish","Discus fish","Guppy","Rainbow fish","Swordtail","Goldfish","Tetra","Cichlid","Eel",
    "Lionfish","Mackerel","Salmon","Tuna","Seahorse","Barracuda","Clown triggerfish","Grouper","Wrasse","Flounder","Herring","Manta ray","Shark",]
    Fishes2 = {"Clownfish": "a small, brightly-colored fish with distinctive orange and white stripes,",
    "Angelfish": "a popular aquarium fish known for its unique shape and striking colors,",
    "Betta fish": "also known as Siamese fighting fish, a beautiful and territorial species with long, flowing fins,",
    "Pufferfish": "a spiky, round fish that can inflate its body to deter predators,",
    "Discus fish": "a colorful and graceful species that is highly prized by aquarium enthusiasts,",
    "Guppy": "a small, easy-to-care-for fish with a variety of colors and patterns,",
    "Rainbow fish": "a beautiful species known for its iridescent scales and peaceful nature,",
    "Swordtail": "a popular livebearer fish with a distinctive, sword-like tail fin,",
    "Goldfish": "a classic aquarium fish that comes in many different varieties, including fantails, orandas, and comets,",
    "Tetra": "a family of small, colorful fish that are well-suited for community aquariums,",
    "Cichlid": "a family of fish known for its many different shapes, sizes, and colors, as well as its aggressive behavior,",
    "Eel": "a long, snake-like fish that can be found in both fresh and saltwater environments,",
    "Lionfish": "a venomous species known for its striking appearance and impressive hunting skills,",
    "Mackerel": "a fast-swimming, predatory fish that is often used for food,",
    "Salmon": "a popular game fish that is known for its rich, flavorful flesh,",
    "Tuna": "a large, powerful fish that is prized for its meat, which is used in sushi and other dishes,",
    "Seahorse": "a small, slow-moving fish that is known for its unique appearance and fascinating breeding habits,",
    "Barracuda": "a predatory fish that is found in tropical and subtropical waters around the world,",
    "Clown triggerfish": "a brightly-colored species known for its distinctive, polka-dotted appearance,",
    "Grouper": "a large, slow-moving fish that can be found in warm waters around the world,",
    "Wrasse": "a family of fish that includes many different species known for their striking colors and patterns,",
    "Flounder": "a flat, bottom-dwelling fish that can change color to blend in with its surroundings,",
    "Herring": "a small, oily fish that is often used for food and forage,",
    "Manta ray": "a large, graceful fish that is found in tropical and subtropical waters around the world,",
    "Shark": "a powerful, predatory fish that is feared and respected by humans and other marine creatures alike,"}

print("╔═════════════════════════╗")
print("║ Welcome to BSIT2A's Zoo ║")
print("║ 🦅 🦜 🐤 🐔 🐢 🐊 🐍 🦦 ║")
print("║ Where we treat animals  ║")
print("║ with love and respect!  ║")
print("║ 🐲 🐢 🦎 🐠 🐡 🦈 🌊 🦉 ║")
print("║ Please Enjoy your tour! ║")
print("╚═════════════════════════╝")
name = input("Hi! What is your name?:  ")
print("Hi!", name, "please enjoy your tour here in our zoo!")
zkeeper = input("Are you a zookeeper? (yes or no): ")
if zkeeper.lower() == "yes":
    password = input("Please enter the password: ")
    if password == "mypassword":
        print("Access granted. Welcome, zookeeper!")
        print("1: If you want to add an animal   2: If you want to remove and animal  3:If you want to the see the animal's list  4:If you want to exit .")
        choice = eval(input())
        go = True
        while go == True:
            if choice == 1:
                General.addanimal()
                General.displayanimals()
                test = input("Do you want to add another animal?: ")
                if test == "yes":
                    continue
                elif test == "no":
                    break
                else:
                    "Invalid Choice"
                    break

            elif choice == 2:
                General.deleteanimal()
                General.displayanimals()
                test = input("Do you want to add rehome animal?: ")
                if test == "yes":
                    continue
                elif test == "no":
                    break
                else:
                    "Invalid Choice"
                    break
                
            elif choice == 3:
                General.displayanimals()
                continue

            elif choice == 4:
                break
    else:
        print("Incorrect password. Access denied.")
        print("Continuing to visitor panel.")

elif zkeeper.lower() == "No":
    print("Welcome, visitor!")

while True:
            print(" ╔═════════════════════════╗")
            print(" ║ Welcome to BSIT2A's Zoo ║")
            print(" ║     Visitor's Menu!     ║")
            print(" ╚═════════════════════════╝")
            print("What kingdom would you like to visit? 1:Reptiles 2:Mammals   3:Birds  4:Fish  5.Search  6.Exit")
            choice = eval(input( ))
            if choice == 1:
                print(" ╔═════════════════════════╗")
                print(" ║ Welcome to BSIT2A's Zoo ║")
                print(" ║     Reptile Kingdom     ║")
                print(" ║🦎 🐢 🐊 🐍 🐉 🐲 🐢 🦎  ║")
                print(" ╚═════════════════════════╝ ")
                print(" ")
                print("►Reptiles are cold blooded, scale covered vertebrates. Many species of reptiles look a little prehistoric. In fact, most dinosaurs could be classified as reptiles, and reptilian fossils that date back to over 300 million years. ")
                print(" ")
                print("Reptiles here in our beloved zoo!")
                fav = []
                for rept in Reptiles1:
                    print('►►',rept)
                animal_choice = input ("What particular reptile would you like to see?:  ")
                if animal_choice in Reptiles2:
                    print("►►",Reptiles2[animal_choice])
                    favo = input("Would you like to add this animal in your favorites?:  ")
                    if favo.lower() == "yes":
                        fav.append(animal_choice)
                        print(fav)
                    else:
                        continue

            if choice == 2:
                print(" ╔═════════════════════════╗")
                print(" ║ Welcome to BSIT2A's Zoo ║")
                print(" ║      Mammal Kingdom     ║")
                print(" ║🦥 🦝 🦦 🦨 🦇 🐋 🐎 🐼  ║")
                print(" ╚═════════════════════════╝ ")
                print(" ")
                print("►Mammal is a warm-blooded vertebrate animal of a class that is distinguished by the possession of hair or fur, the secretion of milk by females for the nourishment of the young, and (typically) the birth of live young.")
                print(" ")
                print("Mammals here in our beloved zoo!")
                for mamm in Mammals1:
                    print('►►',mamm)
                animal_choice = input ("What particular mammals would you like to see?: ")
                if animal_choice in Mammals2:
                    print("►►",Mammals2[animal_choice]) 
                    favo = input("Would you like to add this animal in your favorites?:  ")
                    if favo.lower() == "yes":
                        fav.append(animal_choice)
                        print(fav)  
                    else:
                        continue     

            if choice == 3:
                print(" ╔═════════════════════════╗")
                print(" ║ Welcome to BSIT2A's Zoo ║")
                print(" ║      Bird Kingdom       ║")
                print(" ║🦅 🦜 🐤 🐔 🦚 🦉 🕊️  🦢  ║")
                print(" ╚═════════════════════════╝ ")
                print(" ")
                print("►Birds are vertebrate animals adapted for flight. Many can also run, jump, swim, and dive. Some, like penguins, have lost the ability to fly but retained their wings. Birds are found worldwide and in all habitats.")
                print(" ")
                print("Birds here in our beloved zoo!")
                for berd in Birds1:
                    print('►►',berd)
                animal_choice = input ("What particular bird would you like to see?: ")
                if animal_choice in Birds2:
                    print("►►",Birds2[animal_choice])
                    favo = input("Would you like to add this animal in your favorites?:  ")
                    if favo.lower() == "yes":
                        fav.append(animal_choice)
                        print(fav)
                    else:
                        continue       
            
            if choice == 4:
                print(" ╔═════════════════════════╗")
                print(" ║ Welcome to BSIT2A's Zoo ║")
                print(" ║      Fish Kingdom       ║")
                print(" ║🐟 🐠 🐡 🦈 🌊 🐙 🦑 🐟  ║")
                print(" ╚═════════════════════════╝ ")
                print(" ")
                print("►Fish are aquatic vertebrate animals that have gills but lack limbs with digits, like fingers or toes. Recall that vertebrates are animals with internal backbones. Most fish are streamlined in their general body form.")
                print(" ")
                print("Fishes here in our beloved zoo!")
                for fesh in Fishes1:
                    print('►►',fesh)
                animal_choice = input ("What particular bird would you like to see?: ")
                if animal_choice in Fishes2:
                    print("►►",Fishes2[animal_choice])
                    favo = input("Would you like to add this animal in your favorites?:  ")
                    if favo.lower() == "yes":
                        fav.append(animal_choice)
                        print(fav)
                    else:
                        continue 

            if choice == 5:
                for every_animals in Gen:
                    print("►►",every_animals)
                search_anima = input("What animal would you like to search?: ")
                if search_anima in Gen:
                    print("►►",Gen2[search_anima])
                         
            
            if choice == 6:
                print("Program terminated! Thank you for using my app!")
                print("You're favorite animals during the tour are:", fav)
                break