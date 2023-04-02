$(document).ready(function() {
	const $lawyerList = $(".laywer-card-list");
	const $lawyerScroller = $(".lawyer-scroller");
	$lawyerScroller.scrollLeft(0);

	const $lawyersMobileNavigationPrevious = $(".laywer-card-list .mobile-navigation.previous");
	const $lawyerMobileNavigationNext = $(".laywer-card-list .mobile-navigation.next");

	$lawyersMobileNavigationPrevious.on("click", onLawyerPreviousClick);
	$lawyerMobileNavigationNext.on("click", onLawyerNextClick);

	checkLawyerMobileNavigation();

	if ( $(".member-body ul li").length >= 4 ) {
		$(".member-body ul").css("margin-top", "0px !important;");
	}

	function onLawyerPreviousClick() {
		console.log("A");
		const $currentActive = $lawyerList.find(".active");
		$currentActive.removeClass("active");

		const $previous = $currentActive.prev();
		$previous.addClass("active");

		const scrollLeft = $lawyerScroller.scrollLeft();
		const offsetLeft = $previous.offset().left;
		$lawyerScroller.animate({ scrollLeft: scrollLeft + offsetLeft });

		checkLawyerMobileNavigation();
	}

	function onLawyerNextClick() {
		const $currentActive = $lawyerList.find(".active");
		$currentActive.removeClass("active");

		const $next = $currentActive.next();
		$next.addClass("active");

		const scrollLeft = $lawyerScroller.scrollLeft();
		const offsetLeft = $next.offset().left;
		$lawyerScroller.animate({ scrollLeft: scrollLeft + offsetLeft });

		checkLawyerMobileNavigation();
	}

	function checkLawyerMobileNavigation() {
		if (!isPhone()) {
			$lawyersMobileNavigationPrevious.hide();
			$lawyerMobileNavigationNext.hide();
			return;
		}

		const $currentActive = $lawyerList.find(".active");
		$lawyersMobileNavigationPrevious.toggle($currentActive.prev().length > 0);
		$lawyerMobileNavigationNext.toggle($currentActive.next().length > 0);
	}
});

$(document).ready(function() {
	/*
	 * Eventos
	 */
	const $eventList = $(".event-list");
	const $eventsScroller = $(".events-scroller");
	$eventsScroller.scrollLeft(0);

	const $eventsMobileNavigationPrevious = $(".event-list .mobile-navigation.previous");
	const $eventsMobileNavigationNext = $(".event-list .mobile-navigation.next");

	$(".event-list .navigation-circle.desktop > div").on("click", onEventDesktopNavigationCircleClick);
	$(".event-list .navigation-circle.phone > div").on("click", onEventPhoneNavigationCircleClick);
	$eventsMobileNavigationPrevious.on("click", onEventPreviousClick);
	$eventsMobileNavigationNext.on("click", onEventNextClick);

	checkEventMobileNavigation();

	function onEventDesktopNavigationCircleClick() {
		const $currentActive = $eventList.find(".active");
		$currentActive.removeClass("active");

		const $this = $(this);
		$this.addClass("active");

		const circles = [...$this.parent().children()];
		const index = circles.indexOf(this);

		const $newActive = $eventsScroller.children().eq(index * 2);

		const scrollLeft = $eventsScroller.scrollLeft();
		const paddingLeft = parseInt($eventList.offset().left);
		const offsetLeft = $newActive.offset().left;
		$eventsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkEventMobileNavigation();
	}

	function onEventPhoneNavigationCircleClick(event) {
		event.stopPropagation();

		const $currentActive = $eventList.find(".active");
		$currentActive.removeClass("active");

		const $this = $(this);
		$this.addClass("active");

		const circles = [...$this.parent().children()];
		const index = circles.indexOf(this);

		const $newActive = $eventsScroller.children().eq(index);
		$newActive.addClass("active");

		const scrollLeft = $eventsScroller.scrollLeft();
		const paddingLeft = parseInt($eventList.css("padding-left"));
		const offsetLeft = $newActive.offset().left;
		$eventsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkEventMobileNavigation();
	}

	function onEventPreviousClick() {
		const $currentActive = $eventList.find(".active");
		$currentActive.removeClass("active");

		const $previous = $currentActive.prev();
		$previous.addClass("active");

		const scrollLeft = $eventsScroller.scrollLeft();
		const paddingLeft = parseInt($eventList.css("padding-left"));
		const offsetLeft = $previous.offset().left;
		$eventsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkEventMobileNavigation();
	}

	function onEventNextClick() {
		const $currentActive = $eventList.find(".active");
		$currentActive.removeClass("active");

		const $next = $currentActive.next();
		$next.addClass("active");

		const scrollLeft = $eventsScroller.scrollLeft();
		const paddingLeft = parseInt($eventList.css("padding-left"));
		const offsetLeft = $next.offset().left;
		$eventsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkEventMobileNavigation();
	}

	function checkEventMobileNavigation() {
		if (!isPhone()) {
			$eventsMobileNavigationPrevious.hide();
			$eventsMobileNavigationNext.hide();
			return;
		}

		const $currentActive = $eventList.find(".active");
		$eventsMobileNavigationPrevious.toggle($currentActive.prev().length > 0);
		$eventsMobileNavigationNext.toggle($currentActive.next().length > 0);
	}

	/*
	 * Publicações
	 */
	const $publicationList = $(".publication-list");
	const $publicationsScroller = $(".publications-scroller");
	$publicationsScroller.scrollLeft(0);

	const $publicationMobileNavigationPrevious = $(".publication-list .mobile-navigation.previous");
	const $publicationMobileNavigationNext = $(".publication-list .mobile-navigation.next");

	$(".publication-list .navigation-circle.desktop > div").on("click", onPublicationDesktopNavigationCircleClick);
	$(".publication-list .navigation-circle.phone > div").on("click", onPublicationPhoneNavigationCircleClick);
	$publicationMobileNavigationPrevious.on("click", onPublicationPreviousClick);
	$publicationMobileNavigationNext.on("click", onPublicationNextClick);

	checkPublicationMobileNavigation();

	function onPublicationDesktopNavigationCircleClick() {
		const $currentActive = $publicationList.find(".active");
		$currentActive.removeClass("active");

		const $this = $(this);
		$this.addClass("active");

		const circles = [...$this.parent().children()];
		const index = circles.indexOf(this);

		const $newActive = $publicationsScroller.children().eq(index);

		const scrollLeft = $publicationsScroller.scrollLeft();
		const paddingLeft = parseInt($publicationList.offset().left);
		const offsetLeft = $newActive.offset().left - parseInt($(".publication-list-content").css("padding-left"));
		console.log(scrollLeft, paddingLeft, offsetLeft);
		$publicationsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkPublicationMobileNavigation();
	}

	function onPublicationPhoneNavigationCircleClick(event) {
		event.stopPropagation();

		const $currentActive = $publicationList.find(".active");
		$currentActive.removeClass("active");

		const $this = $(this);
		$this.addClass("active");

		const circles = [...$this.parent().children()];
		const index = circles.indexOf(this);

		const $newActive = $publicationsScroller.children().eq(index);
		$newActive.addClass("active");

		const scrollLeft = $publicationsScroller.scrollLeft();
		const paddingLeft = parseInt($publicationList.css("padding-left"));
		const offsetLeft = $newActive.offset().left;
		$publicationsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkPublicationMobileNavigation();
	}

	function onPublicationPreviousClick() {
		const $currentActive = $publicationList.find(".active");
		$currentActive.removeClass("active");

		const $previous = $currentActive.prev();
		$previous.addClass("active");

		const scrollLeft = $publicationsScroller.scrollLeft();
		const paddingLeft = parseInt($publicationList.css("padding-left"));
		const offsetLeft = $previous.offset().left;
		$publicationsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkPublicationMobileNavigation();
	}

	function onPublicationNextClick() {
		const $currentActive = $publicationList.find(".active");
		$currentActive.removeClass("active");

		const $next = $currentActive.next();
		$next.addClass("active");

		const scrollLeft = $publicationsScroller.scrollLeft();
		const paddingLeft = parseInt($publicationList.css("padding-left"));
		const offsetLeft = $next.offset().left;
		$publicationsScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });

		checkPublicationMobileNavigation();
	}

	function checkPublicationMobileNavigation() {
		if (!isPhone()) {
			$publicationMobileNavigationPrevious.hide();
			$publicationMobileNavigationNext.hide();
			return;
		}

		const $currentActive = $publicationList.find(".active");
		$publicationMobileNavigationPrevious.toggle($currentActive.prev().length > 0);
		$publicationMobileNavigationNext.toggle($currentActive.next().length > 0);
	}
});