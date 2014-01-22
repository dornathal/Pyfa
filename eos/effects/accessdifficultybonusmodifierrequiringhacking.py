# Used by:
# Modules named like: Algorithm (8 of 8)
# Implant: Poteque 'Prospector' Hacking HC-905
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda c: c.item.requiresSkill("Hacking"),
                                  "accessDifficultyBonus",
                                  container.getModifiedItemAttr("accessDifficultyBonusModifier"), position="post")
