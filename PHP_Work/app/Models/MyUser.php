<?php

namespace App\Models;

use Illuminate\Support\Facades\DB;
use PDO;

class MyUser
{
	private string $_login;
	private ?string $_password;

	private const USER_TABLE = "Users";

	public function __construct( string $login, string $password = null )
	{
		$this->setLogin($login);
		$this->setPassword($password);
	}

	public function login() : string
	{
		return $this->_login;
	}

	public function setLogin( string $login ) : void
	{
		$this->_login = $login;
	}

	public function password() : string
	{
		return $this->_password;
	}

	public function setPassword( ?string $password ) : void
	{
		$this->_password = $password;
	}

	public function exists() : bool
	{
		// 1. On prépare la requête $request
		$request = DB::connection()->getPdo()->prepare('SELECT password FROM '.self::USER_TABLE.' WHERE login = :login');
		// 2. On assigne $login au paramêtre :login
		$ok = $request->bindValue( ":login", $this->_login, PDO::PARAM_STR );
		// 3. On exécute la requête $request
		$ok &= $request->execute();

		if (!$ok)
			throw new \Exception("Error: user access in DB failed.");

		// 4. On vérifie que l'utilisateur a été trouvé et que son mot de passe
		//    correspond à celui de l'attribut $this->_password
		$user = $request->fetch(PDO::FETCH_ASSOC);
		return $user && password_verify($this->_password,$user['password']);
	}

	public function create() : void
	{
		$request = DB::connection()->getPdo()->prepare('INSERT INTO '.self::USER_TABLE.'(login,password) VALUES (:login,:password)');
		$ok =  $request->bindValue( ":login", $this->_login, PDO::PARAM_STR );
		$ok &= $request->bindValue( ":password", password_hash($this->_password,PASSWORD_DEFAULT), PDO::PARAM_STR );
		$ok &= $request->execute();

		if ( !$ok )
			throw new \Exception("Error: user creation in DB failed.");
	}

	public function changePassword( string $newpassword ) : void
	{
		$request = DB::connection()->getPdo()->prepare('UPDATE '.self::USER_TABLE.' SET password = :password WHERE login = :login');
		$ok =  $request->bindValue(':login',    $this->_login, PDO::PARAM_STR);
		$ok &= $request->bindValue(':password', password_hash($newpassword,PASSWORD_DEFAULT), PDO::PARAM_STR);
		$ok &= $request->execute();

		if ( !$ok )
			throw new \Exception("Error: password updating failed.");

		$this->setPassword($newpassword);
	}

	public function delete() : void
	{
		$request = DB::connection()->getPdo()->prepare('DELETE FROM '.self::USER_TABLE.' WHERE login = :login');
		$ok =  $request->bindValue(':login', $this->_login, PDO::PARAM_STR);
		$ok &= $request->execute();

		if ( !$ok )
			throw new \Exception("Error while deleting your account.");
	}
}
