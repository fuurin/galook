export default class Game {
  public static create(game: any) {
    return new Game(
      game.id,
      game.brand || "",
      game.category || "",
      game.story || "",
      game.subgenre || [],
      game.title,
      game.url || "",
      game.image || "",
      game.writer || []);
  }

  constructor(
    public id: number,
    public brand: string = "",
    public category: string[] = [],
    public stroy: string = "",
    public subgenre: string[] = [],
    public title: string,
    public url: string = "",
    public image: string = "",
    public writer: string[] = []) {}
}
