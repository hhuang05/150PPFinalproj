var numlib = require('numbers');
var typeUtils = require('./type-utils.js');
var listToArray = typeUtils.listToArray;
var arrayToList = typeUtils.arrayToList;

var matrix_invert = function(Mat) {
    var a = listToArray(Mat).map(listToArray);
    return arrayToList(numlib.matrix.inverse(a).map(arrayToList));
};

var matrix_identity = function(n) {
    return arrayToList(numlib.matrix.identity(n).map(arrayToList));
};

var matrix_mult = function(A, B) {
    var a = listToArray(A).map(listToArray);
    var b = listToArray(B).map(listToArray);
    var result = numlib.matrix.multiply(a, b).map(arrayToList)
    return arrayToList(result)
};
