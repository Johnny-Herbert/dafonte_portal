// class NumberUtils {
// 	static pad(value, paddingSize, paddingCharacter = "0") {
// 		// let paddedValue = String(value);
// 		var paddedValue = String(value);
// 		while (paddedValue.length < paddingSize) paddedValue = paddingCharacter + paddedValue;
// 		return paddedValue;
// 	}
// }

var NumberUtils = {};
NumberUtils.pad = function (value, paddingSize, paddingCharacter) {
	// let paddedValue = String(value);
	var paddedValue = String(value);
	while (paddedValue.length < paddingSize) paddedValue = paddingCharacter + paddedValue;
	return paddedValue;
}