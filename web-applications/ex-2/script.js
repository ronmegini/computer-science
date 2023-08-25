var player1Score = 0;
var player2Score = 0;
var currentPlayer = 'player1'; // Start with player1's turn

$(document).ready(function () {
    
    $('#playerNamesModal').modal('show'); // Show modal on page load

    $('#startGame').click(function() {
        var player1Name = $('#player1Name').val() || 'Player 1'; // If empty, default to 'Player 1'
        var player2Name = $('#player2Name').val() || 'Player 2'; // If empty, default to 'Player 2'

        $('#player1Display').text(player1Name);
        $('#player2Display').text(player2Name);
        
        $('#playerNamesModal').modal('hide'); // Hide modal after collecting names

    });

    var selectedPiece = null;
    var selectedCell = null;

    // Using event delegation for .piece
    $('#board').on('click', '.piece', function() {
        if ($(this).hasClass(currentPlayer)) {
            if (selectedPiece) {
                selectedPiece.removeClass('selected');
            }
            selectedPiece = $(this);
            selectedPiece.addClass('selected');
            selectedCell = $(this).parent(); // Store the cell containing the piece.
        } else {
            alert("It's not your turn!");
        }
    });

    // Using event delegation for .cell.black
    $('#board').on('click', '.cell.black', function() {
        if (selectedPiece && $(this).children().length === 0) {
            if (isValidMove(selectedCell, $(this))) {
                $(this).append(selectedPiece);
                selectedPiece.removeClass('selected');
                selectedPiece = null;

                togglePlayer(); // Toggle to the other player after a valid move
            } else {
                alert("Invalid move!"); // Notify user of illegal move.
            }
        }
    });
});

function togglePlayer() {
    currentPlayer = (currentPlayer === 'player1') ? 'player2' : 'player1';
}

function isValidMove(fromCell, toCell) {
    var fromRow = fromCell.index('#board .cell') / 8 | 0;
    var fromCol = fromCell.index('#board .cell') % 8;
    var toRow = toCell.index('#board .cell') / 8 | 0;
    var toCol = toCell.index('#board .cell') % 8;

    var piece = fromCell.children().first();
    var moveDistanceRow = Math.abs(fromRow - toRow);
    var moveDistanceCol = Math.abs(fromCol - toCol);

    if (moveDistanceRow !== 1 || moveDistanceCol !== 1) {
        if (moveDistanceRow !== 2 || moveDistanceCol !== 2) {
            return false;
        } else {
            var middleRow = (fromRow + toRow) / 2;
            var middleCol = (fromCol + toCol) / 2;
            var middleCell = $('#board .cell').eq(middleRow * 8 + middleCol);
            var middlePiece = middleCell.children().first();

            if (middlePiece.length && !middlePiece.hasClass(currentPlayer)) {
                middlePiece.remove(); // Capture the piece
                updateScore(); // Update the score
                return true;
            } else {
                return false;
            }
        }
    }

    // Check direction based on the player
    if (piece.hasClass('player1') && toRow <= fromRow) {
        return false; // player1 pieces can only move down
    } else if (piece.hasClass('player2') && toRow >= fromRow) {
        return false; // player2 pieces can only move up
    }

    return true;
}

function updateScore() {
    if (currentPlayer === 'player1') {
        player1Score++;
        console.log(player1Score)
        $('#player1Score').text(player1Score); // Assuming you've added this to your HTML
    } else {
        player2Score++;
        console.log(player2Score)
        $('#player2Score').text(player2Score); // Assuming you've added this to your HTML
    }
}