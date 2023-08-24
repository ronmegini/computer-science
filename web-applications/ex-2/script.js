$(document).ready(function () {
    createBoard();

    var selectedPiece = null;

    $('.piece').click(function() {
        if (selectedPiece) {
            selectedPiece.removeClass('selected');
        }
        selectedPiece = $(this);
        selectedPiece.addClass('selected');
    });

    $('.cell.black').click(function() {
        if (selectedPiece && $(this).children().length === 0) {
            $(this).append(selectedPiece);
            selectedPiece.removeClass('selected');
            selectedPiece = null;
        }
    });


});

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
