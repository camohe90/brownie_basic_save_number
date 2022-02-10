// SPDX-License-Identifier: MIT

pragma solidity ^0.8.1;

contract Basic_storage{

    uint256 number;

    function saveNumber(uint256 _number) public{
        number = _number;
    }

    function readNumber()public view returns(uint256){
        return number;
    }
    
}

