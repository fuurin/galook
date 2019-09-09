import axios from 'axios';

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
    public writer: string[] = []) {
    this.checkImage(image);
  }

  private checkImage(url: string, noImgUrl: string = NO_IMAGE_URL) {
    this.image = noImgUrl;
    // try {
    //   axios.get(url)
    //   .then(() => { this.image = url; })
    //   .catch(() => { this.image = noImgUrl; });
    // } catch {
    //   this.image = noImgUrl;
    // }
  }
}
