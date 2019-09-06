export class Game {
    constructor(
      public id: number,
      public brand: string = "",
      public category: string[] = [],
      public stroy: string = "",
      public subgenre: string[] = [],
      public title: string,
      public url: string = "",
      public writer: string[] = [],
    ) {}
  }
