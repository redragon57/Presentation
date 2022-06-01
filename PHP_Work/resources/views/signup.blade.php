@extends('layouts.app')

@section('title','Signup Page')
@section('s1')
<form action={{ route("adduser")}} method="post">
    @csrf
	<label for="login">Login</label>             <input type="text"     id="login"    name="login"    required autofocus>
	<label for="password">Password</label>       <input type="password" id="password" name="password" required>
	<label for="confirm">Confirm password</label><input type="password" id="confirm"  name="confirm"  required>
	<input type="submit" value="Signup">
</form>
<p>
	If you already have an account, <a href={{ route("signin")}}>signin</a>.
</p>
@endsection
