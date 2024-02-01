# vanilla rails are very cheap
recipes.remove(<minecraft:rail>);
recipes.addShaped("Track", <minecraft:rail>*32,
    [[<minecraft:iron_nugget>, null, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, <minecraft:stick>, <minecraft:iron_nugget>],
     [<minecraft:iron_nugget>, null, <minecraft:iron_nugget>]]);

# special vanilla rails are replaced by track kits
mods.jei.JEI.removeAndHide(<minecraft:golden_rail>);
mods.jei.JEI.removeAndHide(<minecraft:detector_rail>);
mods.jei.JEI.removeAndHide(<minecraft:activator_rail>);

# the track kits are modified to be vanilla friendly and cheap
# scheme is to replace track part ingredient with iron, advanced rail with gold, and to double (some) of the outputs

recipes.remove(<railcraft:track_kit:1>.withTag({railcraft: {kit: "railcraft_activator"}}));
recipes.addShaped("Activator Track Kit", <railcraft:track_kit:1>.withTag({railcraft: {kit: "railcraft_activator"}})*16,
    [[<ore:plankWood>, <minecraft:iron_ingot>, null],
     [<minecraft:redstone>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:2>.withTag({railcraft: {kit: "railcraft_booster"}}));
recipes.addShaped("Booster Track Kit", <railcraft:track_kit:2>.withTag({railcraft: {kit: "railcraft_booster"}})*32,
    [[<ore:plankWood>, <minecraft:iron_ingot>, <minecraft:gold_ingot>],
     [<minecraft:gold_ingot>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:3>.withTag({railcraft: {kit: "railcraft_buffer"}}));
recipes.addShaped("Buffer Stop Track Kit", <railcraft:track_kit:3>.withTag({railcraft: {kit: "railcraft_buffer"}})*2,
    [[<ore:plankWood>, <minecraft:iron_ingot>, null],
     [<minecraft:iron_ingot>, <minecraft:iron_ingot>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:4>.withTag({railcraft: {kit: "railcraft_control"}}));
recipes.addShaped("Control Track Kit", <railcraft:track_kit:4>.withTag({railcraft: {kit: "railcraft_control"}})*32,
    [[<ore:plankWood>, <minecraft:iron_ingot>, null],
     [<minecraft:gold_ingot>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:5>.withTag({railcraft: {kit: "railcraft_detector"}}));
recipes.addShaped("Detector Track Kit", <railcraft:track_kit:5>.withTag({railcraft: {kit: "railcraft_detector"}})*8,
    [[<ore:plankWood>, <minecraft:iron_ingot>, null],
     [<minecraft:stone_pressure_plate>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:6>.withTag({railcraft: {kit: "railcraft_disembarking"}}));
recipes.addShaped("Disembarking Track Kit", <railcraft:track_kit:6>.withTag({railcraft: {kit: "railcraft_disembarking"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, <minecraft:stone_pressure_plate>],
     [<minecraft:lead>, <minecraft:redstone>, null],
     [null, null, null]]);

# no need for receipt removal since it was already disable by module
recipes.addShaped("Dumping Track Kit", <railcraft:track_kit:7>.withTag({railcraft: {kit: "railcraft_dumping"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, null],
     [<minecraft:iron_trapdoor>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:8>.withTag({railcraft: {kit: "railcraft_embarking"}}));
recipes.addShaped("Embarking Track Kit", <railcraft:track_kit:8>.withTag({railcraft: {kit: "railcraft_embarking"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, <minecraft:ender_pearl>],
     [<minecraft:lead>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:9>.withTag({railcraft: {kit: "railcraft_gated"}}));
recipes.addShaped("Gated Track Kit", <railcraft:track_kit:9>.withTag({railcraft: {kit: "railcraft_gated"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, <ore:fenceGateWood>],
     [<minecraft:gold_ingot>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:10>.withTag({railcraft: {kit: "railcraft_locking"}}));
recipes.addShaped("Locking Track Kit", <railcraft:track_kit:10>.withTag({railcraft: {kit: "railcraft_locking"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, <minecraft:stone_pressure_plate>],
     [<minecraft:sticky_piston>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:11>.withTag({railcraft: {kit: "railcraft_one_way"}}));
recipes.addShaped("One-Way Track Kit", <railcraft:track_kit:11>.withTag({railcraft: {kit: "railcraft_one_way"}})*8,
    [[<ore:plankWood>, <minecraft:iron_ingot>, <minecraft:stone_pressure_plate>],
     [<minecraft:piston>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:15>.withTag({railcraft: {kit: "railcraft_messenger"}}));
recipes.addShaped("Messenger Track Kit", <railcraft:track_kit:15>.withTag({railcraft: {kit: "railcraft_messenger"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, null],
     [<minecraft:sign>, <minecraft:redstone>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:16>.withTag({railcraft: {kit: "railcraft_delayed"}}));
recipes.addShaped("Delayed Locking Track Kit", <railcraft:track_kit:16>.withTag({railcraft: {kit: "railcraft_delayed"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, <minecraft:stone_pressure_plate>],
     [<minecraft:sticky_piston>, <minecraft:repeater>, null],
     [null, null, null]]);

recipes.remove(<railcraft:track_kit:17>.withTag({railcraft: {kit: "railcraft_coupler"}}));
recipes.addShaped("Coupler Track Kit", <railcraft:track_kit:17>.withTag({railcraft: {kit: "railcraft_coupler"}})*4,
    [[<ore:plankWood>, <minecraft:iron_ingot>, null],
     [<minecraft:lead>, <minecraft:redstone>, null],
     [null, null, null]]);

# remove complicated unnecessary things
mods.jei.JEI.removeAndHide(<railcraft:tool_crowbar_steel>);
mods.jei.JEI.removeAndHide(<railcraft:tool_axe_steel>);
mods.jei.JEI.removeAndHide(<railcraft:tool_hoe_steel>);
mods.jei.JEI.removeAndHide(<railcraft:tool_pickaxe_steel>);
mods.jei.JEI.removeAndHide(<railcraft:tool_shears_steel>);
mods.jei.JEI.removeAndHide(<railcraft:tool_shovel_steel>);
mods.jei.JEI.removeAndHide(<railcraft:tool_sword_steel>);
mods.jei.JEI.removeAndHide(<railcraft:armor_boots_steel>);
mods.jei.JEI.removeAndHide(<railcraft:armor_chestplate_steel>);
mods.jei.JEI.removeAndHide(<railcraft:armor_leggings_steel>);
mods.jei.JEI.removeAndHide(<railcraft:armor_helmet_steel>);
mods.jei.JEI.removeAndHide(<railcraft:rail:*>);
mods.jei.JEI.removeAndHide(<railcraft:tie:*>);
mods.jei.JEI.removeAndHide(<railcraft:rebar>);
mods.jei.JEI.removeAndHide(<railcraft:tool_spike_maul_steel>);
mods.jei.JEI.removeAndHide(<railcraft:railbed:*>);
mods.jei.JEI.removeAndHide(<railcraft:manipulator:2>);
mods.jei.JEI.removeAndHide(<railcraft:manipulator:3>);
mods.jei.JEI.removeAndHide(<railcraft:manipulator:4>);
mods.jei.JEI.removeAndHide(<railcraft:manipulator:5>);
mods.jei.JEI.removeAndHide(<railcraft:chest_void>);
mods.jei.JEI.removeAndHide(<railcraft:track_parts>);

# remove tracks
mods.jei.JEI.removeAndHide(<railcraft:track_flex_abandoned>);

val seven_rail_types = ["abandoned", "electric", "high_speed", "high_speed_electric", "iron", "reinforced", "strap_iron"] as string[];
val five_rail_types = ["abandoned", "electric", "iron", "reinforced", "strap_iron"] as string[];

val kits_for_seven = ["activator", "booster", "detector", "locking", "messenger", "delayed"] as string[];
val kits_for_five = ["buffer", "control", "disembarking", "dumping", "embarking", "gated", "one_way", "coupler"] as string[];

for railType in seven_rail_types {
    for kititem in kits_for_seven {
        mods.jei.JEI.removeAndHide(<railcraft:track_outfitted>.withTag({railcraft: {rail: "railcraft_" + railType, kit: "railcraft_" + kititem}}));
    }
}

for railType in five_rail_types {
    for kititem in kits_for_five {
        mods.jei.JEI.removeAndHide(<railcraft:track_outfitted>.withTag({railcraft: {rail: "railcraft_" + railType, kit: "railcraft_" + kititem}}));
    }
}
