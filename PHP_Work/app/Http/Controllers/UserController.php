<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use \App\Models\MyUser;

class UserController extends Controller
{
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function signin( Request $request ){
        return response()->view('signin',['message'=>(session('message')??'')]);
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function signup(Request $request ){
        return response()->view('signup',['message'=>(session('message')??'')]);
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function formpassword(Request $request ){
        return response()->view('formpassword');
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function signout(Request $request ){
        session_destroy();
        return redirect('signin');
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function account(Request $request ){
        return response()->view('account',['message'=>(session('message')??''),'user'=>session('user')]);
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function authenticate(Request $request ){
        unset(session('message'));
        if (!$request->filled('login','password')){
            session(['message' => "Some POST data are missing."]);
            return redirect()->route('signin');
        }
        $user = new MyUser($request->login,$request->password);
        try {
            if ( !$user->exists() )	{
                session(['message' => 'Wrong login/password.']);
                return redirect()->route('signin');
            }
        }
        catch (\PDOException $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('signin');
        }
        catch (\Exception $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('signin');
        }
        session(['user' => $request->login]);
        return redirect()->route('account');
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function adduser(Request $request ){
        unset(session('message'));
        if (!$request->filled('login','password','confirm')){
            session(['message' => "Some POST data are missing."]);
            return redirect()->route('signup');
        }
        if ( $request->password !== $request->confirm ) {
            session(['message' => "The two passwords differ."]);
            return redirect()->route('signup');
        }
        $user = new MyUser($request->login,$request->password);
        try {
            $user->create();
        }
        catch (\PDOException $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('signup');
        }
        catch (\Exception $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('signup');
        }
        session(['user' => $request->login]);
        return redirect()->route('signin');
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function changepassword(Request $request ){
        unset(session('message'));
        if (!$request->filled('newpassword','confirmpassword') ) {
            session(['message' => "Some POST data are missing."]);
            return redirect()->route('formpassword');
        }
        if ( $request->newpassword != $request->confirmpassword ) {
            session(['message' => "Error: passwords are different."]);
            return redirect()->route('formpassword');
        }
        $user = new MyUser($request->login,$request->password);
        try {
            $user->changePassword($request->newpassword);
        }
        catch (\PDOException $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('formpassword');
        }
        catch (\Exception $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('formpassword');
        }
        session(['message' => "Password successfully updated."]);
        return redirect()->route('account');
    }
    /**
     * Show the signin page
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function deleteuser(Request $request ){
        unset(session('message'));
        $login = session('user');
        $user = new MyUser($login);
        try {
            $user->delete();
        }
        catch (\PDOException $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('account');
        }
        catch (\Exception $e) {
            session(['message' => $e->getMessage()]);
            return redirect()->route('account');
        }
        session_destroy();
        session_start();
        session(['message' => "Account successfully deleted."]);
        return redirect()->route('signin');
    }
}
