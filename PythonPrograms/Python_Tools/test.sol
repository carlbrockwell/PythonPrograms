pragma solidity ^0.4.0;
contract SomeContract {
    uint public myVar;

    function SomeContract(uint _myVar) public {
        myVar = _myVar;
    }

    function getMyVar() public view returns(uint) {
        return 5*myVar;
    }
}