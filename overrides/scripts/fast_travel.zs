import crafttweaker.item.IIngredient;

val anyDirt as IIngredient =
    <minecraft:dirt>
    | <aether_legacy:aether_dirt>
    | <midnight:midnight_dirt>
    | <minecraft:netherrack>;

recipes.addShaped("ez warp scroll", <waystones:warp_scroll> * 64,
    [[null, anyDirt, null],
     [null, anyDirt, null],
     [null, anyDirt, null]]);

recipes.addShaped("ez glowing potion",
    <minecraft:potion>.withTag({
        display: {Name: "Potion of Eternal Glow"},
        CustomPotionEffects: [{
            Id: 24 as byte,
            Amplifier: 0 as byte,
            Duration: 2147483647,
            ShowParticles: 0 as byte
        }]
    }),
    [[anyDirt, anyDirt, anyDirt]]);