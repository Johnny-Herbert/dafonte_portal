const breakpointPhone = "";
const breakpointTablet = "";

function isPhone() {
	return window.matchMedia("(max-width: 767px)").matches;
}

function isTablet() {
	return !isPhone() && window.matchMedia("(max-width: 1199px)").matches;
}

$(document).ready(function() {
	$(".language-list > li").on("click", onLanguageChange);
	$(".icon-menu-open").on("click", onMobileMenuOpen);
	$(".icon-menu-close").on("click", onMobileMenuClose);
	$(".nested-list-container").on("click", onMobileNestedListClick);
});

function onLanguageChange() {
	$("[name='language']").val(this.dataset.languageCode);
	// this.closest("form").submit();
	$(".language-menu").submit();
}

function mobileMenuToggle() {
	$(".header-menu").toggleClass("mobile-open");
	const $this = $(this);
	$this.slideToggle(250, function(){$this.siblings(".material-icons").slideToggle(250)} );
	const $nav = $this.closest(".nav-mobile");
	$nav.toggleClass("nav-open");
	$nav.find(".menu-icons span").toggle();
}

function onMobileMenuOpen() {
	mobileMenuToggle.call(this);
	$(".header .logo").toggle();
}

function onMobileMenuClose() {
	mobileMenuToggle.call(this);
	setTimeout(function(){
		$(".header .logo").slideToggle();
	}, 750);
}

function onMobileNestedListClick() {
	$(this).find(".nested-list").slideToggle();
}
