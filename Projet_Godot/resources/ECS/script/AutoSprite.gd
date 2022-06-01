extends Sprite

onready var health: BuildingHealth = get_parent().get_node_or_null("BuildingHealth")
onready var size: BuildingSize = get_parent().get_node_or_null("BuildingSize")
onready var rota: BuildingRotation = get_parent().get_node_or_null("BuildingRotation")

func _ready() -> void:
	if health:
		_on_BuildingHealth_on_state_changed(health.building_state)

func _update_image_index():
	var h = BuildingHealth.BuildingState.OLD
	var r = BuildingRotation.Rotation.NORTH
	
	if health:
		h = health.building_state
	if r:
		r = rota.rotation
	
	region_rect.position.x = 71 * (h * 3)
	
func _update_image_size():
	var s = BuildingSize.Size.L1
	if size:
		s = size.size

	region_rect.position.x = 108 * s

func _on_BuildingHealth_on_state_changed(state) -> void:
	_update_image_index()

func _on_BuildingSize_size_changed(size: int) -> void:
	_update_image_size()

func _on_BuildingRotation_rotation_changed(rota) -> void:
	_update_image_index()
