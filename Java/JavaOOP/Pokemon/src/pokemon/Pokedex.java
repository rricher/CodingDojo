package pokemon;

import java.util.ArrayList;

public class Pokedex extends AbstractPokemon {
	
	private static ArrayList<String> myPokemons = new ArrayList<String>();

	@Override
	public void listPokemon() {
		System.out.println(myPokemons);
	}
	
	public static void addPokemon(String pokemon) {
		myPokemons.add(pokemon);
	}
	
}
