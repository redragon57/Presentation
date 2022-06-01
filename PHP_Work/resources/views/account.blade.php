@extends('layouts.app')

@section('title','Account Page')
@section('s1')
<p>
	Hello {{$user}} !<br>
	Welcome on your account.
</p>
<ul>
	<li><a href="formpassword">Change password.</a></li>
	<li><a href="deleteuser">Delete my account.</a></li>
</ul>
<p><a href={{ route("signout")}}>Sign out</a></p>
@endsection
