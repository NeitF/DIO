export abstract class DioAccount {
    private name: string
    private readonly accountNumber: number
    private balance: number = 0
    private status: boolean = true

    constructor(name: string, accountNumber: number){
        this.name = name
        this.accountNumber = accountNumber
    }

    public setName = (name: string): void => {
        this.name = name
        console.log("Nome alterado com sucesso")
    }

    public getName = (): string => {
        return this.name
    }
    
    public setBalance = (val: number): void => {
        this.balance += val
    }

    public deposit = (valor: number): void => {
        if(this.validateStatus()){
            this.balance += valor
            console.log("Você depositou R$" + valor)
        }
    }

    public withdraw = (valor: number): void => {
        if(this.validateStatus()  && valor <= this.balance){
            this.balance -= valor
            console.log("Você sacou R$" + valor)
        }
    }

    public getBalance = (): void => {
        console.log(this.balance)
    }

    protected validateStatus = (): boolean => {
        if(this.status){
            return this.status
        }
        throw new Error("Erro ao validar status")
    }
}