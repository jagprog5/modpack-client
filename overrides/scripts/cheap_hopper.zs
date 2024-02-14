recipes.remove(<minecraft:hopper>);
recipes.addShaped("j Hopper", <minecraft:hopper>*8,
    [[<minecraft:iron_nugget>, null, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, <minecraft:chest>, <minecraft:iron_nugget>],
     [null, <minecraft:iron_nugget>, null]]);

recipes.remove(<uppers:upper>);
recipes.addShaped("j Upper", <uppers:upper>*8,
    [[null, <minecraft:iron_nugget>, null],
     [<minecraft:iron_nugget>, <minecraft:chest>, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, null, <minecraft:iron_nugget>]]);
