$(document).ready(function() {
	const $pressList = $(".header-press-list");
	const $pressesScroller = $(".presses-scroller");
	$pressesScroller.scrollLeft(0);

	$("label[id=search-term-icon]").each(function() {
		$(this).on("click", onSearchTermClick);
	});

	$(".press-circle-navigation .navigation-circle > div").on("click", onPressNavigationCircleClick);
	onRepeatArticle();

	function onPressNavigationCircleClick() {
		const $currentActive = $(this).closest(".navigation-circle").find(".active");
		$currentActive.removeClass("active");

		const $this = $(this);
		$this.addClass("active");

		const circles = [...$this.parent().children()];
		const index = circles.indexOf(this);

		const $newActive = $pressesScroller.children().eq(index);

		const scrollLeft = $pressesScroller.scrollLeft();
		const paddingLeft = parseInt($pressList.offset().left);
		const offsetLeft = $newActive.offset().left;
		$pressesScroller.animate({ scrollLeft: scrollLeft + offsetLeft - paddingLeft });
		$(".navigation-page-number").text(NumberUtils.pad(index + 1, 2));
	}

	function onRepeatArticle() {
		// workaround para ignorar posts repetidos na tela de artigos publicados
		var array = [];
		var isMobile = $("div[id=header-desktop]").css('display') === 'none';
		if (!isMobile) {
			$("div[id^=article-]").each(function(){
				var id = $(this).attr('id');
				var display = $(this).css('display');
				if (array.includes(id)) {
					$(this).css('display', 'none');
				}
				else if (!array.includes(id) && display !== 'none'){
					array.push(id);
				}
			});

			$("div[id^=press-]").each(function(){
				var id = $(this).attr('id');
				var display = $(this).css('display');
				if (array.includes(id)) {
					$(this).css('display', 'none');
				}
				else if (!array.includes(id) && display !== 'none'){
					array.push(id);
				}
			});
		}
	}

	function onSearchTermClick(event) {
		event.preventDefault();
		const form = $(this).closest("form").get(0);
		form.submit();
	}
});