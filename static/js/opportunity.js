$(document).ready(function () {
	hiddeSupport($('#personal-role-info').attr('value'));

	$('.academic-conclusion').mask('0000');
	$("input[name='personal-phone']").mask('(00) 000000-0000');

	// configurações do datepicker
	const datepickerOptions = {
		format:'mm/yyyy',
		autoHide: true,
		font: 'arial',
		endDate: new Date(),
		language: 'pt-BR',
	}

	const datepickerYearOptions = {
		format:'yyyy',
		autoHide: true,
		font: 'arial',
		language: 'pt-BR',
	}

	$('input[id^=datepicker]').map(function(index, item){
		if ($(item).attr('id') == 'datepicker-year') {
			$(item).mask('0000');
			$(item).datepicker(datepickerYearOptions);
		} else {
			$(item).mask('00/0000');
			$(item).datepicker(datepickerOptions);
		}
	});

	let dateBeginEl = $("#datepicker-0-date_begin");
	let dateFinishEl = $("#datepicker-0-date_finish");
	checkDateFinish(dateBeginEl, dateFinishEl);

	$('#personal-role-info').on('change', function () {
		hiddeSupport(this.value);
	});
	$(".btn-add-academic-formation").on('click', function () {
		const $academicInfosListContainer = $(".academic-infos-list-container");
		const $AcademicInfos = $academicInfosListContainer.find('.academic-infos');
		let $oldAcademicInfo = $AcademicInfos.last();
		let $newAcademicInfo = $oldAcademicInfo.clone();
		$newAcademicInfo.find('.academic-course').removeClass('is-invalid').val('');
		$newAcademicInfo.find('.academic-institution').removeClass('is-invalid').val('');
		$newAcademicInfo.find('.academic-conclusion').removeClass('is-invalid').val('');
		$newAcademicInfo.find('.academic-incomplete_course').removeClass('is-invalid').prop('checked', false);
		$newAcademicInfo.find('.academic-in_progress').removeClass('is-invalid').prop('checked', false);
		$newAcademicInfo.find('.academic-period').removeClass('is-invalid').val('X');
		$newAcademicInfo.find('.academic-shift').removeClass('is-invalid').val('X');
		const nextId = (parseInt($newAcademicInfo.prop('id').split('-')[1]) + 1).toString();
		$newAcademicInfo.prop('id', `academic-${nextId}`);
		$newAcademicInfo.find('.show-progress').prop('id', `show-${nextId}`);
		$newAcademicInfo.find('.show-progress').prop('style', 'display: none');
		$newAcademicInfo.find('.academic-in_progress').prop('id', `check-${nextId}`);
		$newAcademicInfo.find('.academic-incomplete_course').prop('id', `check-${nextId}-incomplete_course`);
		$newAcademicInfo.find('.academic-in_progress').prop('name', `academic-${nextId}-in_progress`);
		$newAcademicInfo.find('.academic-incomplete_course').prop('name', `academic-${nextId}-incomplete_course`);
		$newAcademicInfo.find('.academic-period').prop('name', `academic-${nextId}-period`);
		$newAcademicInfo.find('.academic-shift').prop('name', `academic-${nextId}-shift`);
		$academicInfosListContainer.append($newAcademicInfo);
		recalculateAcademicFormIndexes();
	});

	$(".btn-add-professional-formation").on('click', function () {
		const $professionalInfosListContainer = $(".professional-infos-list-container");
		const $ProfessionalInfos = $professionalInfosListContainer.find('.professional-infos');
		let $oldProfessionalInfo = $ProfessionalInfos.last();
		let $newProfessionalInfo = $oldProfessionalInfo.clone();
		let nextId = (parseInt($newProfessionalInfo.prop('id').split('-')[1]) + 1).toString();
		$newProfessionalInfo.find('.professional-enterprise').removeClass('is-invalid').removeClass('is-invalid').val('');
		$newProfessionalInfo.find('.professional-function').removeClass('is-invalid').removeClass('is-invalid').val('');

		let actualFunctionField = $newProfessionalInfo.find('.professional-actual_function');
		actualFunctionField.removeClass('is-invalid').prop('checked', false);
		nextId = (parseInt(actualFunctionField.prop('id').split('-')[1]) + 1).toString();
		$newProfessionalInfo.find('.professional-actual_function').prop('id', `check-${nextId}-actual_function`);
		$newProfessionalInfo.find('.professional-area').removeClass('is-invalid').val('');

		let dateBegin = $newProfessionalInfo.find('.professional-date_begin');
		dateBegin.prop('id', `datepicker-${nextId}-date_begin`);
		let dateFinish = $newProfessionalInfo.find('.professional-date_finish');
		dateFinish.prop('id', `datepicker-${nextId}-date_finish`);
		dateBegin.removeClass('is-invalid').val('');
		dateFinish.removeClass('is-invalid').val('');
		$newProfessionalInfo.find('.professional-activities').removeClass('is-invalid').val('');
		dateBegin.datepicker(datepickerOptions);
		dateFinish.datepicker(datepickerOptions);
		checkDateFinish(dateBegin, dateFinish);
		$professionalInfosListContainer.append($newProfessionalInfo);
		recalculateProfessionalFormIndexes();
	});

	$(".btn-add-language").on('click', function () {
		const $languagesInfosListContainer = $(".language-infos-list-container");
		const $LanguagelInfos = $languagesInfosListContainer.find('.language-infos');
		let $oldLanguagelInfo = $LanguagelInfos.last();
		let $newLanguagelInfo = $oldLanguagelInfo.clone();
		$newLanguagelInfo.find('.language-language').removeClass('is-invalid').val('');
		$newLanguagelInfo.find('.language-level').removeClass('is-invalid').val('');
		$languagesInfosListContainer.append($newLanguagelInfo);
		recalculateLanguageFormIndexes();
	});

	function recalculateAcademicFormIndexes() {
		const $AcademicInfos = $('.academic-infos');
		$AcademicInfos.each(function (index) {
			$(this).find('.academic-course').attr("name", `academic-${index}-course`);
			$(this).find('.academic-institution').attr("name", `academic-${index}-institution`);
			$(this).find('.academic-conclusion').attr("name", `academic-${index}-conclusion`);
		});
		$("[name='academic-TOTAL_FORMS']").val($AcademicInfos.length);
		$('.academic-conclusion').each(function() {
			$(this).mask('0000');
		});
	}

	function recalculateProfessionalFormIndexes() {
		const $ProfessionalInfos = $('.professional-infos');
		$ProfessionalInfos.each(function (index) {
			$(this).find('.professional-enterprise').attr("name", `professional-${index}-enterprise`);
			$(this).find('.professional-function').attr("name", `professional-${index}-function`);
			$(this).find('.professional-actual_function').attr("name", `professional-${index}-actual_function`);
			$(this).find('.professional-area').attr("name", `professional-${index}-area`);
			$(this).find('.professional-date_begin').attr("name", `professional-${index}-date_begin`);
			$(this).find('.professional-date_finish').attr("name", `professional-${index}-date_finish`);
			$(this).find('.professional-activities').attr("name", `professional-${index}-activities`);
		});
		$("[name='professional-TOTAL_FORMS']").val($ProfessionalInfos.length);
	}

	function recalculateLanguageFormIndexes() {
		const $LanguageInfos = $('.language-infos');
		$LanguageInfos.each(function (index) {
			$(this).find('.language-language').attr("name", `language-${index}-language`);
			$(this).find('.language-level').attr("name", `language-${index}-level`);
		});
		$("[name='language-TOTAL_FORMS']").val($LanguageInfos.length);
	}

	function checkDateFinish(dateBeginEl, dateFinishEl) {
		dateFinishEl.on('pick.datepicker', function (e) {
			if (e.date < dateBeginEl.datepicker('getDate')) {
			  e.preventDefault(); // Prevent to pick the date
			  dateFinishEl.datepicker('reset');
			}
		});
	}
});

function checkCourseProgress(checkbox) {
	if (!checkbox.id.includes('incomplete_course')) {
		const incompleteCourse = $(`#${checkbox.id}-incomplete_course`);
		if (incompleteCourse.prop('checked')) {
			incompleteCourse.prop('checked', false);
			incompleteCourse.val(false);
		}
	} else {
		const objectId = `${checkbox.id}`.replace('-incomplete_course', '');
		const inProgessCourse = $(`#${objectId}`);
		if (inProgessCourse.prop('checked')) {
			inProgessCourse.prop('checked', false);
			inProgessCourse.val(false);
			$("#show-" + objectId.split('-')[1]).css('display', 'none');
		}
	}
	$(checkbox).val(checkbox.checked);
}

function checkActualFunction(checkbox) {
	$(checkbox).val(checkbox.checked);
	const id = checkbox.id;
	if (!checkbox.checked) {
		return;
	}

	$('input[id^=check-][id$=-actual_function]').each( function() {
		if ($(this).prop('id') !== id) {
			$(this).val(false);
			$(this).prop('checked', false);
		}
	});
}

function showInProgress(checkbox) {
	checkCourseProgress(checkbox);
	const id = checkbox.id.split('-')[1];
	if (checkbox.checked) {
		$("#show-" + id).css('display', 'block')
	} else {
		$("#show-" + id).css('display', 'none')
	}
}

function hiddeSupport(value) {
	if (value == "SUPPORT") {
		$('#practice-area-hidden').hide();
		$('#specialization-sector-hidden').hide();
		$('#intend_area-hidden').show();
	} else {
		$('#practice-area-hidden').show()
		$('#specialization-sector-hidden').show();
		$('#intend_area-hidden').hide();
	}
}
