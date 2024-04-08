import { CompanyAccount } from "./class/CompanyAccount";
import { PeopleAccount } from "./class/PeopleAccount";
import { OtherAccount } from "./class/otherAccount";

const peopleAccount: PeopleAccount = new PeopleAccount("Nathan", 1, 2)
peopleAccount.deposit(20)
peopleAccount.withdraw(10)
console.log(peopleAccount)


const companyAccount: CompanyAccount = new CompanyAccount("DIO", 20)
companyAccount.deposit(10)
companyAccount.getLoan(1000)
console.log(companyAccount)

const otherAccount: OtherAccount = new OtherAccount("Lucas", 10)
otherAccount.deposit(100)
console.log(otherAccount)