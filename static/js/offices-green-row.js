$(document).ready(function() {
	const $officeList = $(".office-list");
	const $officesScroller = $(".offices-scroller");
	$officesScroller.scrollLeft(0);

	const $mobileOfficesNavigationPrevious = $(".office-list .mobile-navigation.previous");
	const $mobileOfficesNavigationNext = $(".office-list .mobile-navigation.next");
	$mobileOfficesNavigationPrevious.on("click", onOfficesPreviousClick);
	$mobileOfficesNavigationNext.on("click", onOfficesNextClick);

	checkOfficesMobileNavigation();
	$('.city').each(function(index, elem) {
		$(elem).css('min-width', '100px');
	});

	function onOfficesPreviousClick() {
		const $currentActive = $officeList.find(".active");
		$currentActive.removeClass("active");

		const $previous = $currentActive.prev();
		$previous.addClass("active");

		const scrollLeft = $officesScroller.scrollLeft();
		const paddingLeft = parseInt($officeList.css("padding-left"));
		const offsetLeft = $previous.offset().left;
		$officesScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkOfficesMobileNavigation();
		$officeList.trigger("office-change");
	}

	function onOfficesNextClick() {
		const $currentActive = $officeList.find(".active");
		$currentActive.removeClass("active");

		const $next = $currentActive.next();
		$next.addClass("active");

		const scrollLeft = $officesScroller.scrollLeft();
		const paddingLeft = parseInt($officeList.css("padding-left"));
		const offsetLeft = $next.offset().left;
		$officesScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkOfficesMobileNavigation();
		$officeList.trigger("office-change");
	}

	function checkOfficesMobileNavigation() {
		const $currentActive = $officeList.find(".active");
		$mobileOfficesNavigationPrevious.toggle($currentActive.prev().length > 0);
		$mobileOfficesNavigationNext.toggle($currentActive.next().length > 0);
	}
});