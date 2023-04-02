$(document).ready(function() {
	$(".office-vertical-list .office").on("click", onOfficeMapClick);
	$(".office-list").on("office-change", ofMobileOfficeChange);

	const $maps = $(".offices-maps");
	const $phoneMapsScroller = $(".maps-phone .maps-scroller");
	$maps.scrollTop(0);
	$phoneMapsScroller.scrollLeft(0);

	function onOfficeMapClick() {
		$(this).siblings(".active").removeClass("active");
		$(this).addClass("active");

		const officeId = this.dataset.officeId;

		// const $map = $maps.find(`.map-${officeId}`);
		const $map = $maps.find('.map-' + officeId);
		const offsetTop = $map.offset().top - $maps.offset().top;
		const scrollTop = $maps.scrollTop();
		$maps.animate({ scrollTop: scrollTop + offsetTop });
	}

	function ofMobileOfficeChange() {
		const officeId = $(this).find(".office.active").get(0).dataset.officeId;

		// const $phoneMap = $phoneMapsScroller.find(`.map-${officeId}`);
		const $phoneMap = $phoneMapsScroller.find('.map-' + officeId);
		const offsetLeft = $phoneMap.offset().left - $phoneMapsScroller.offset().left;
		const scrollLeft = $phoneMapsScroller.scrollLeft();
		$phoneMapsScroller.animate({ scrollLeft: scrollLeft + offsetLeft });
	}
});