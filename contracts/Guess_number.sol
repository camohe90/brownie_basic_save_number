// SPDX-License-Identifier: MIT

pragma solidity ^0.8.1;

contract Guess_number{
    address payable player;
    enum State {OPEN, COMPLETE}
    State public currState;
    uint private secretNumber;
    uint public balance;

    constructor (uint _secretNumber) payable{
        require(msg.value == 10*10**18, 'contract needs to be fund with at leats 10 eth');
        secretNumber = _secretNumber;
        currState = State.OPEN;
        balance = balance + msg.value;
    }

    function getBalance() public view returns(uint){
        return balance;
    }

    function play(uint guesessNumber, address _player) external payable{
        require(msg.value == 10**18, 'you must pay to play');
        require(currState == State.OPEN);
        player = payable(_player);
        balance = balance + msg.value;
        if (guesessNumber == secretNumber){
            player.transfer(address(this).balance);
            currState = State.COMPLETE;
        }
    }

}

