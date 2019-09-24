export default class GameQuery {
  public static match = {
    perfect: "perfect",
    part: "part",
  };

  public qmatch: string = "";

  constructor(
    public name: string,
    public input: string,
    public match: string = GameQuery.match.perfect) {
      this.qmatch = name + '_match';
    }

  public query(ignoreEmpty: boolean = true): { [s: string]: string } {
    const q: { [s: string]: string } = {};
    if (ignoreEmpty && !this.input) return q;
    q[this.name] = this.input;
    q[this.qmatch] = this.match;
    return q;
  }
}
