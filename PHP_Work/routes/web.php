<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;
use App\Http\Controllers\UserController;
Route::get('/token', function (Request $request) {
    $token = $request->session()->token();
    $token = csrf_token();
});
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::group( [], function() {

	session_start();

	/* ------------------------------------------------------------------------
	| Public routing */
    Route::get('/', [UserController::class,'signin']);
	Route::get('signin', [UserController::class,'signin'])->name('signin');
	Route::post('adduser', [UserController::class,'adduser'])->name('adduser');
	Route::post('authenticate', [UserController::class,'authenticate'])->name('authenticate');
	Route::get('signup', [UserController::class,'signup'])->name('signup');
	// ------------------------------------------------------------------------

	/* ------------------------------------------------------------------------
	| Admin routing */
	Route::prefix('admin')->middleware('auth.myuser')->group( function() {
		Route::post('changepassword', [UserController::class,'changepassword'])->name('changepassword');
		Route::get('deleteuser',[UserController::class,'deleteuser'])->name('deleteuser');
		Route::get('formpassword',[UserController::class,'formpassword'] )->name('formpassword');
		Route::get('account', [UserController::class,'account'] )->name('account');
		Route::get('signout', [UserController::class,'signout'] )->name('signout');
	});
	// ------------------------------------------------------------------------
});
