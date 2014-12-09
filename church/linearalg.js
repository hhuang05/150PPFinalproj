// Author: Moses Huang
// Purpose: Making interfaces to common Linear Algebra functions
// from the javascript library. Including additional implementation
// of necessary decompositions for sampling

var numlib = require('numbers');
var typeUtils = require('./type-utils.js');
var listToArray = typeUtils.listToArray;
var arrayToList = typeUtils.arrayToList;


// ***************************
// ******* Measures **********
// ***************************

var vec_twonorm = function(v) {
    var a = listToArray(v);
    var result = a.map(function(x) {return Math.pow(x,2)}).reduce(
	function(a,b) {
	    return a + b;
	});
    return Math.sqrt(result);
};

var matrix_infnorm = function(Mat) {
    var a = listToArray(Mat).map(listToArray);
    var b = a.map(
	function(lst) {
	    return lst.map(Math.abs).reduce(
		function(a,b) {
		    return a + b;
		});
	});
    return Math.max.apply(null, b);
};

var matrix_cond = function(Mat) {
    var m_norm = matrix_infnorm(Mat);
    var minv_norm = matrix_infnorm(matrix_invert(Mat));
    return m_norm * minv_norm;
};

// *************************
// ******* Vector **********
// *************************

var vec_dot = function(v1,v2) {
    var a = listToArray(v1);
    var b = listToArray(v2);

    return numlib.matrix.dotproduct(a,b);
};

var vec_plus = function(v1,v2) {
    var a = listToArray(v1);
    var b = listToArray(v2);
    var c = [];

    for (var i = 0; i < a.length; i++) {
	c.push(a[i] + b[i]);
    }
    
    return arrayToList(c);
};

var vec_minus = function(v1,v2) {
    var a = listToArray(v1);
    var b = listToArray(v2);
    var c = [];

    for (var i = 0; i < a.length; i++) {
	c.push(a[i] - b[i]);
    }
    
    return arrayToList(c);
};

// *************************
// ******* Matrix **********
// *************************

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
    var result = numlib.matrix.multiply(a, b).map(arrayToList);
    return arrayToList(result);
};


// *********************************
// ******* Decompositions **********
// *********************************

// Performs a Cholesky decomposition on Matrix Mat
var cholesky = function(Mat) {
    var a = listToArray(Mat).map(listToArray);

    var mat_size = a[0].length;
    
    var calcDiagEntry = function(A, j) {
	var L_sq = 0;
	for (var k = 0; k < j; k++) {
	    L_sq += Math.pow(A[j][k], 2);
	}
	return Math.sqrt(A[j][j] - L_sq);
    };
    
    var calcRow = function(A, i, j) {
	var L_mix = 0;
	for (var k = 0; k < j; k++) {
	    L_mix += A[i][k] * A[j][k];
	}
	return ((A[i][j] - L_mix) / A[j][j]);
    };
    
    var decomp = function(A, n) {
	for (var i = 0; i < n; i++) {

	    for (var j = 0; j < i; j++) {
		A[i][j] = calcRow(A, i, j);		
	    }

	    A[i][i] = calcDiagEntry(A, i);
	    
	    //Zero out the rest of the entries
	    for (var j = i+1; j < n; j++) {
		A[i][j] = 0;
	    }
	}
	return A;
    };
    
    return arrayToList(decomp(a, mat_size).map(arrayToList));
};

