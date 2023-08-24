$(document).ready(function () {
    
    $('#playerNamesModal').modal('show'); // Show modal on page load

    $('#startGame').click(function() {
        var player1Name = $('#player1Name').val() || 'Player 1'; // If empty, default to 'Player 1'
        var player2Name = $('#player2Name').val() || 'Player 2'; // If empty, default to 'Player 2'

        $('#player1Display').text(player1Name);
        $('#player2Display').text(player2Name);
        
        $('#playerNamesModal').modal('hide'); // Hide modal after collecting names

        createBoard();
    });

    var selectedPiece = null;
    var selectedCell = null;
    var currentPlayer = 'player1'; // Start with player1's turn

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

                currentPlayer = togglePlayer(currentPlayer); // Toggle to the other player after a valid move
            } else {
                alert("Invalid move!"); // Notify user of illegal move.
            }
        }
    });
});

function togglePlayer(currentPlayer) {
    return (currentPlayer === 'player1') ? 'player2' : 'player1';
}

function createBoard() {
    var isBlack = false;
    for (var row = 0; row < 8; row++) {
        for (var col = 0; col < 8; col++) {
            var cell = $('<div>').addClass('cell');
            if (isBlack) {
                cell.addClass('black');
                if (row < 3) {
                    var piece = $('<div>').addClass('piece player1');
                    cell.append(piece);
                }
                if (row > 4) {
                    var piece = $('<div>').addClass('piece player2');
                    cell.append(piece);
                }
            } else {
                cell.addClass('white');
            }
            $('#board').append(cell);
            isBlack = !isBlack;
        }
        isBlack = !isBlack;
    }
}

function isValidMove(fromCell, toCell) {
    var fromRow = fromCell.index('#board .cell') / 8 | 0;
    var fromCol = fromCell.index('#board .cell') % 8;
    var toRow = toCell.index('#board .cell') / 8 | 0;
    var toCol = toCell.index('#board .cell') % 8;
    
    var piece = fromCell.children().first();
    
    // Check if the move is diagonal
    if (Math.abs(fromRow - toRow) !== 1 || Math.abs(fromCol - toCol) !== 1) {
        return false;
    }

    // Check direction based on the player
    if (piece.hasClass('player1') && toRow <= fromRow) {
        return false; // player1 pieces can only move down
    } else if (piece.hasClass('player2') && toRow >= fromRow) {
        return false; // player2 pieces can only move up
    }
    
    return true;
}