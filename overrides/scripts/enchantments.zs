# villager rng is annoying. this is more fun
val mending = <item:minecraft:enchanted_book>.withTag({StoredEnchantments: [{lvl: 1, id: 70}]});

mods.jei.JEI.addDescription(mending,
    "Repair your items!",
    "Crafting ingredients include:",
    "-ambrosium (aether's coal)",
    "-biotite (kill the ender dragon)");

recipes.addShapedMirrored("j Mending", mending,
    [[null, <minecraft:book>, null],
     [<minecraft:quartz>, <minecraft:dye:4>, <quark:biotite>],
     [<aether_legacy:ambrosium_shard>, <aether_legacy:ambrosium_shard>, <aether_legacy:ambrosium_shard>]]);
