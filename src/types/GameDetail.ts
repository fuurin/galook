import GameQuery from '@/types/GameQuery';

export default class GameDetail {
    public name: string = "";
    public input: string = "";
    public match: string = "";

    constructor(
        public label: string,
        query: GameQuery,
    ) {
        this.name = query.name;
        this.input = query.input;
        this.match = query.match;
    }

    public query(): GameQuery {
        return new GameQuery(this.name, this.input, this.match);
    }
}
