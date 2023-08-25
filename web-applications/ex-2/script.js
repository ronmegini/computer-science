// Initial score setup for both players
var scores = { player1: 0, player2: 0 };
// Set the current player to player1 as a starting point
var currentPlayer = 'player1';

// Start the execution when the document is fully loaded
$(document).ready(function () {
    
    // Automatically show a modal to get player names as soon as the page loads
    $('#playerNamesModal').modal('show');

    // When the "start game" button is clicked
    $('#startGame').click(function() {
        // Retrieve names from input fields or set default names if inputs are empty
        var player1Name = $('#player1Name').val() || 'Player 1';
        var player2Name = $('#player2Name').val() || 'Player 2';

        // Display retrieved names on the UI
        $('#player1Display').text(player1Name);
        $('#player2Display').text(player2Name);
        
        // Close the modal after setting player names
        $('#playerNamesModal').modal('hide');
    });

    // Initialize selectedPiece and selectedCell to null
    var selectedPiece = null;
    var selectedCell = null;

    // Add a click event listener for pieces on the board
    $('#board').on('click', '.piece', function() {
        // If the clicked piece belongs to the current player
        if ($(this).hasClass(currentPlayer)) {
            // If there's an already selected piece, deselect it
            if (selectedPiece) {
                selectedPiece.removeClass('selected');
            }
            // Select the current piece and store its containing cell
            selectedPiece = $(this);
            selectedPiece.addClass('selected');
            selectedCell = $(this).parent();
        } else {
            // Notify user when they try to move the opponent's piece
            alert("It's not your turn!");
        }
    });

    // Add a click event listener for black cells on the board
    $('#board').on('click', '.cell.black', function() {
        // If there's a selected piece and the destination cell is empty
        if (selectedPiece && $(this).children().length === 0) {
            // If it's a valid move
            if (isValidMove(selectedCell, $(this))) {
                // Move the selected piece to the new cell
                $(this).append(selectedPiece);
                selectedPiece.removeClass('selected');
                selectedPiece = null;

                // Switch the turn to the other player
                togglePlayer();
            } else {
                // Notify user of an invalid move attempt
                alert("Invalid move!");
            }
        }
    });
});

// Function to switch the current player
function togglePlayer() {
    currentPlayer = (currentPlayer === 'player1') ? 'player2' : 'player1';
}

// Function to check if a move is valid
function isValidMove(fromCell, toCell) {
    // Get the indexes/positions of origin and destination cells
    var fromRow = fromCell.index('#board .cell') / 8 | 0;
    var fromCol = fromCell.index('#board .cell') % 8;
    var toRow = toCell.index('#board .cell') / 8 | 0;
    var toCol = toCell.index('#board .cell') % 8;

    // Find the piece in the origin cell
    var piece = fromCell.children().first();

    // Calculate the distance of the move
    var moveDistanceRow = Math.abs(fromRow - toRow);
    var moveDistanceCol = Math.abs(fromCol - toCol);

    // If it's neither a direct move or a capture move, it's invalid
    if (moveDistanceRow !== 1 || moveDistanceCol !== 1) {
        if (moveDistanceRow === 2 || moveDistanceCol === 2) {
            // For capturing an opponent's piece

            // Find the piece in the middle of the jump
            var middleRow = (fromRow + toRow) / 2;
            var middleCol = (fromCol + toCol) / 2;
            var middleCell = $('#board .cell').eq(middleRow * 8 + middleCol);
            var middlePiece = middleCell.children().first();

            // If there's a piece to capture and it's not the current player's piece
            if (middlePiece.length && !middlePiece.hasClass(currentPlayer)) {
                middlePiece.remove();  // Remove the captured piece from the board
                updateScore();  // Increase the score for the current player
                togglePlayer(); // Change the current player to allow the current player another turn
                return true;
            } else {
                return false;
            }
        } else {
            return false;
            
        }
    }

    // Check move direction based on the player
    // Player1's pieces can only move downwards, player2's can only move upwards
    if (piece.hasClass('player1') && toRow <= fromRow) {
        return false;
    } else if (piece.hasClass('player2') && toRow >= fromRow) {
        return false;
    }

    return true;
}

// Function to update the current player's score
function updateScore() {
    // Increase the score of the current player
    scores[currentPlayer]++;

    // Update the displayed score (assumes you have these elements in your HTML)
    if (currentPlayer === 'player1') {
        $('#player1Score').text(scores[currentPlayer]);
    } else {
        $('#player2Score').text(scores[currentPlayer]);
    }
}
