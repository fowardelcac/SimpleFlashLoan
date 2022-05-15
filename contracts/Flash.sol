// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

import {FlashLoanSimpleReceiverBase} from "contracts/FlashLoanSimpleReceiverBase.sol";
import "interfaces/IERC2O.sol";
import "interfaces/IPool.sol";
import "interfaces/IPoolAddressesProvider.sol";

contract Flash is FlashLoanSimpleReceiverBase {
    address public immutable owner;

    constructor(IPoolAddressesProvider _provider)
        FlashLoanSimpleReceiverBase(_provider)
    {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    function executeOperation(
        address asset,
        uint256 amount,
        uint256 premium,
        address initiator,
        bytes calldata params
    ) external returns (bool) {
        //Logic///////
        uint256 _fee = premium + amount;
        IERC20(asset).approve(address(POOL), _fee);

        return true;
    }

    function withdraw(address _asset) external onlyOwner {
        uint256 balance = IERC20(_asset).balanceOf(address(this));
        require(balance > 0, "It doesn't money");
        IERC20(_asset).transfer(owner, balance);
    }

    function initFlashLoan(address _asset, uint256 _amount) external onlyOwner {
        //address receiverAddress = address(this);
        bytes memory params = "";
        //uint16 referralCode = 0;
        POOL.flashLoanSimple(address(this), _asset, _amount, params, 0);
    }
}
