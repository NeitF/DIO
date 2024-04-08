import { DioAccount } from "./DioAccount";

export class CompanyAccount extends DioAccount{

    constructor(name: string, accountNumber: number){
        super(name, accountNumber)
    }

    public getLoan = (valor: number): void => {
        if(this.validateStatus()){
            this.setBalance(valor)
            console.log("Você pegou um empréstimo")
        }
    }
}