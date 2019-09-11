const NO_IMAGE_URL = "/img/no-image.png";

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
      game.image || NO_IMAGE_URL,
      game.writer || []);
  }

  constructor(
    public id: number,
    public brand: string = "",
    public category: string[] = [],
    public story: string = "",
    public subgenre: string[] = [],
    public title: string,
    public url: string = "",
    public image: string = "",
    public writer: string[] = [],
    affiliate: boolean = true) {
      if (affiliate) {
        this.url = `http://www.getchu.com/api/geturl.phtml/af/2/aftype/1/sid/46/id/${id}/url/soft.phtml-/?id=${id}`;
      }
    }
}
