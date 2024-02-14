recipes.addShapeless("j String", <minecraft:string>, [<ore:wool>]);

furnace.addRecipe(<minecraft:leather>, <minecraft:rotten_flesh>);
furnace.setFuel(<minecraft:reeds>, 200);

recipes.remove(<minecraft:arrow>);
# order matters since flint is in stone tool ore dictionary
recipes.addShaped("j arrow v2", <minecraft:arrow>*32,
    [[null, <minecraft:flint>, null],
     [null, <ore:stickWood>, null],
     [null, <ore:feather>, null]]);
recipes.addShaped("j arrow v1", <minecraft:arrow>*2,
    [[null, <ore:materialStoneTool>, null],
     [null, <ore:stickWood>, null],
     [null, <ore:feather>, null]]);
