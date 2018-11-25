pragma solidity ^0.4.19;

contract MyContract{

    uint myVariable;

    address owner;

    function MyContract() payable{
        myVariable = 5;
        owner = msg.sender;
    }

    function setMyVariable(uint mynewVariable){
        if(msg.sender == owner){
            myVariable = mynewVariable;
        }
    }

    function getMyVariable() constant returns(uint) {
        return myVariable;
    }

    function getMyContractBalance() constant returns(uint){
        return this.balance;
    }

    function () payable {

    }
}