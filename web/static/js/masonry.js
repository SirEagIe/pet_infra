var $container = $('.container');
		$container.imagesLoaded(function(){
		    $container.masonry({
		        itemSelector: '.article',
		    });
		    $('.article img').addClass('not-loaded');
		    $('.article img.not-loaded').lazyload({
		        effect: 'fadeIn',
		        load: function() {
		            // Disable trigger on this image
		            $(this).removeClass("not-loaded");
		            $container.masonry('reload');
		        }
		    });
		    $('.article img.not-loaded').trigger('scroll');
		});
