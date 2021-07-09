from story import Story
from scene import Scene
from plot import RagsToRiches, DefeatingMonster
from narrator import FirstPerson
from character import Character, Dialogue

sabir = Character("sabir",15)
iko = Character("iko",13)
iko.arc = DefeatingMonster()

scene = Scene(goal_set="eat bagels",goal_achieved=0)
scene.location="circus"
scene.tension=0.47
scene.characters.lead = sabir
scene.characters.obstacle = iko

plot = RagsToRiches()
plot.add(scene)

story = Story(plot)
story.genre = "comedy"

narrator = FirstPerson(iko)

narrator.write(story)