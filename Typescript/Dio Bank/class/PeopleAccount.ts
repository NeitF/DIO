import { DioAccount } from "./DioAccount";

export class PeopleAccount extends DioAccount{
    doc_id: number

    constructor(name: string, accountNumber: number, doc_id: number){
        super(name, accountNumber)
        this.doc_id = doc_id
    }
}