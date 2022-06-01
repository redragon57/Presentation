extends Camera2D

const acceleration = 60
const maxSpeed = 25
const friction = 150

var mousePos = Vector2.ZERO
var velocity = Vector2.ZERO

func _ready():
	set_process_input(true)
	set_physics_process(false)

func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	input_vector.y = Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	input_vector = input_vector.normalized()

	var zoom_coef = clamp(zoom.x - 0.5, 0.2, 0.5)
	
	if input_vector != Vector2.ZERO:
		velocity += input_vector * acceleration * delta * zoom_coef
		velocity = velocity.clamped(maxSpeed * zoom_coef)
	else:
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)
	
	if Input.is_action_pressed("move_lock"):
		velocity = Vector2.ZERO

		var new_pos = get_local_mouse_position()

		if mousePos != Vector2.ZERO:
			position += (mousePos - new_pos)
		mousePos = new_pos

	else:
		mousePos = Vector2.ZERO
		position += velocity


	if Input.is_action_just_released("zoom_in"):
		zoom *=1.2
	if Input.is_action_just_released("zoom_out"):
		zoom /=1.2

	zoom.x = min(max(zoom.x, 0.5), 1.4)
	zoom.y = min(max(zoom.y, 0.5), 1.4)


func _on_Fond_Demar_PlayGame() -> void:
	set_physics_process(true)
