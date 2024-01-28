recipes.remove(<minecraft:rail>);
recipes.addShaped("Rail", <minecraft:rail>*32,
    [[<minecraft:iron_nugget>, null, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, <minecraft:stick>, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, null, <minecraft:iron_nugget>]]);

recipes.remove(<minecraft:golden_rail>);
recipes.addShaped("Powered Rail", <minecraft:golden_rail>*16,
    [[<minecraft:gold_nugget>, null, <minecraft:gold_nugget>],
     [<minecraft:gold_nugget>, <minecraft:stick>, <minecraft:gold_nugget>],
     [<minecraft:gold_nugget>, <minecraft:redstone>, <minecraft:gold_nugget>]]);

recipes.remove(<minecraft:detector_rail>);
recipes.addShaped("Detector Rail", <minecraft:detector_rail>*16,
    [[<minecraft:iron_nugget>, null, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, <minecraft:stone_pressure_plate>, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, <minecraft:redstone>, <minecraft:iron_nugget>]]);

recipes.remove(<minecraft:activator_rail>);
recipes.addShaped("Activator Rail", <minecraft:activator_rail>*16,
    [[<minecraft:iron_nugget>, <minecraft:stick>, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, <minecraft:redstone_torch>, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, <minecraft:stick>, <minecraft:iron_nugget>]]);
