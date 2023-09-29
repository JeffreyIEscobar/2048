$(document).ready(function() {
    // Initialize the game board and score
    var board = JSON.parse('[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]');
    var score = 0;
    var game_over = false;
    

    // Function to update the game board with animations
    function updateBoard() {
        for (var i = 0; i < 4; i++) {
            for (var j = 0; j < 4; j++) {
                var cellValue = board[i][j];
                var cellElement = $(".cell.row-" + i + ".col-" + j);

                // Add or update the cell's animation class
                var animationClass = "slide-in-" + cellValue;
                cellElement.text(cellValue > 0 ? cellValue : "");
                cellElement.attr("class", "cell cell-" + cellValue + " " + animationClass);

                // Remove the animation class after a short delay
                setTimeout(function() {
                    cellElement.removeClass(animationClass);
                }, 200); // Adjust the duration as needed
            }
        }

        // Update the score
        $("#score").text(score);

        // Check for game over
        if (game_over) {
            $("#game-over-message").removeClass("hidden").text("Game Over!");
        } else {
            $("#game-over-message").addClass("hidden");
        }
    }

    // Update the initial game board
    updateBoard();

    // Function to make a move
    function makeMove(direction) {
        $.ajax({
            type: "POST",
            url: "/move",
            data: { direction: direction },
            success: function(response) {
                board = response.board;
                score = response.score;
                game_over = response.game_over;
                updateBoard();
            }
        });
    }

    // Handle arrow key presses to make moves
    $(document).keydown(function(event) {
        switch (event.keyCode) {
            case 37: // Left arrow key
                makeMove("left");
                break;
            case 38: // Up arrow key
                makeMove("up");
                break;
            case 39: // Right arrow key
                makeMove("right");
                break;
            case 40: // Down arrow key
                makeMove("down");
                break;
        }
    });
});