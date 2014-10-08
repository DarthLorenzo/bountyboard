$(function() {

    // FUNCTIONS
    function renderStars() {
        var $this = $(this);
        var maxRating = ( $this.attr("data-bestRating") ) ? $this.attr("data-bestRating") : 5;
        var minRating = ( $this.attr("data-worstRating") ) ? $this.attr("data-worstRating") : 1;
        var thisRating = ( $this.attr("data-ratingValue") ) ? $this.attr("data-ratingValue") : 0;
        var thisOriginalText = $this.text();
        var starMarkup = '<span class="icon-star"></span>';

        $this.addClass("ratings-stars-visual");
        $this.attr("data-originalValue", thisOriginalText);
        if ( !$this.attr("title") ) {
            $this.attr("title", thisOriginalText);
        }
        for ( var i = 1; i < maxRating; i++) {
            starMarkup += '<span class="icon-star"></span>';
        }
        $this.html('<span class="ratings-stars-filled" style="width: ' + ( thisRating / maxRating * 100 ) + '%">' + starMarkup + '</span>');
        $this.append('<span class="ratings-stars-unfilled">' + starMarkup + '</span>');
        $this.append('<span class="visuallyhidden">' + thisOriginalText + '</span>');
    }

    $.fn.ratings = function () {
        return this.each(renderStars);
    };

});