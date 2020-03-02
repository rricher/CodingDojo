	package pokemon;

public class PokemonTester {

	public static void main(String[] args) {
		Pokemon charizard = new Pokemon("Charizard", 50, "Dragon, Fire");
		Pokemon charmander = new Pokemon("Charmander", 20, "Fire");
		charizard.attack(charmander);
		Pokedex pokedex = new Pokedex();
		pokedex.listPokemon();
		

	}

}
