### `mesh.primitive_cube_add`:
* TAG_CONTEXT_NOT_USED
* clear previous selection
* newly added object is set as active and selected

### `mesh.separate`:

* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects`
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

### `object.convert`:

* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects`
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

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
