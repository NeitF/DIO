import { DioAccount } from "./DioAccount";

export class OtherAccount extends DioAccount{

    constructor(name: string, accountNumber: number){
        super(name, accountNumber)
    }

    public override deposit = (val: number): void => {
        if(this.validateStatus()){
            this.setBalance(val + 10)
        }
    }
}