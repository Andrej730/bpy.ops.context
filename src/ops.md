### `clip.add_marker`
* POLL_INTERNAL: `ED_space_clip_tracking_poll`
* POLL:
- 📋 `area.type` == `CLIP_EDITOR`
- 📋 `area.spaces.active.clip` is not `None`
- 📋 `area.spaces.active.mode` == `TRACKING`
* TAG_CONTEXT_OVERRIDE_SUPPORT

### `mesh.primitive_cube_add`:
* TAG_CONTEXT_NOT_USED
* clear previous selection
* newly added object is set as active and selected

### `mesh.separate`:

* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects`
* TAG_ACTIVE_OBJECT_NOT_AFFECTED
* newly added objects are selected (original objects selection status is not affected)
* newly objects (and their data) retain props from original separated objects (and their data)

### `object.convert`:

* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects`
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

### `object.editmode_toggle`:

* POLL: `active_object` is required and it should be EDITable
* TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED
* check view layer active object explicitly
* check view layer selected objects explicitly (non-EDITable objects are ignored)

### `object.join`:

* POLL: `active_object` is required and it should be EDITable
* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects` and `active_object`
* objects that don't match `active_object` type are ignored from `selected_editable_objects`  
(e.g. Curves when Mesh is active)
* active object is the join target and it should also be selected

### `object.make_single_user`:

* TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED
* check view layer selected objects explicitly
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

### `object.mode_set`:

* POLL: `active_object` is required and it should be EDITable
* TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED
* check view layer active object explicitly
* check view layer selected objects explicitly (non-EDITable objects are ignored)

### `object.transform_apply`:

* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects`
* TAG_ACTIVE_OBJECT_NOT_AFFECTED
