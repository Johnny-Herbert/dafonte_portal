$.fn.extend({
	showFlex: function() {
		this.each(function() {
			this.style.display = "flex";
		});
	},

	toggleFlex: function(state) {
		if (typeof state === "boolean") {
			return state ? this.show() : this.hide();
		}

		return this.each(function() {
			const $this = $(this);
			if ($this.is(":visible")) {
				$this.hide();
			} else {
				console.log($this);
				$this.showFlex();
			}
		});
	},
});