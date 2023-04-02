$(document).ready(function() {
	$(".member-type-area-filter > li").on("click", onMemberTypeClick);
	$(".practice-area-filter > li").on("click", onAreaTypeClick);
	$(".specialization-sector-filter > li").on("click", onAreaTypeClick);
	$(".filters-initial > label > span").on("click", onLetterClick);
	$("#search-term-icon").on("click", onSearchTermClick);

	function onMemberTypeClick() {
		const $this = $(this);

		$this.find("> div input").prop("checked", true);

		const $oldActiveType = $this.parent().find("> .active");
		// $oldActiveType.removeClass("active");
		// $this.addClass("active");

		const $oldActiveArea = $this.find("ul li.active");

		if ($oldActiveType.get(0) !== this || $oldActiveArea.length > 0) {
			$this.closest("form").submit();
		}
	}

	function onAreaTypeClick(event) {
		event.stopPropagation();

		const $this = $(this);

		$this.find("input").prop("checked", true);

		const $oldActive = $this.parent().find(".active");
		// $oldActive.removeClass("active");
		// $this.addClass("active");

		if ($oldActive.get(0) !== this) {
			$this.closest("form").submit();
		}
	}

	function onLetterClick(event) {
		event.preventDefault();

		$(this).parent().children("input").prop("checked", true);
		$("#filter-by-initial").val("true");

		const form = $(this).closest("form").get(0);
		// const formData = new FormData(form);
		// console.table(Array.from(formData));
		form.submit();
	}

	function onSearchTermClick(event) {
		event.preventDefault();
		$("#filter-by-initial").val("false");
		const form = $(this).closest("form").get(0);
		form.submit();
	}
});
