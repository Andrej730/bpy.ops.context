### `constraint.childof_set_inverse`
* TAG_CONTEXT_OVERRIDE_SUPPORT
* 📋 can be overridden using `object` (🛠️`context_active_object()`)
* 📋 `constraint` context member can be provided to automatically fill operator args `constraint` (constraint name) and `owner`
* `constraint` is `Constraint` works only if operator started with `.invoke()`
* `constraint` must be one of the `object` constraints

### `clip.add_marker`
* POLL_INTERNAL: `ED_space_clip_tracking_poll`
* POLL:
* 📋 `area.type` == `CLIP_EDITOR`
* 📋 `area.spaces.active.clip` is not `None`
* 📋 `area.spaces.active.mode` == `TRACKING`
* TAG_CONTEXT_OVERRIDE_SUPPORT

### `mesh.primitive_cube_add`:
* TAG_CONTEXT_NOT_USED
* clear previous selection
* newly added object is set as active and selected

### `mesh.separate`:

* In OBJECT mode:
* TAG_CONTEXT_OVERRIDE_SUPPORT
* 📋 can be overridden using `selected_editable_objects`
* 📋 TAG_ACTIVE_OBJECT_NOT_AFFECTED
* In EDIT_MESH mode:
* TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED
* 📋 basically it affects `context.objects_in_mode`, but doesn't use this actual context member
* 📋 therefore it ignores selected objects that are in OBJECT mode, doesn't require explicit selection and skips hidden objects
* 📋 'by selection' separates selection for each object separately (e.g. if 1 face selected in N objects results in N separated objects)
* In both modes:
* 📋 newly added objects are selected (original objects selection status is not affected)
* 📋 newly objects (and their data) retain props from original separated objects (and their data)


### `object.convert`:

* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects`
* object is not recreated, even if object type is changed
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

### `object.delete`:

* POLL_INTERNAL: `ED_operator_objectmode`
* POLL: `context.mode` == `OBJECT`
* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_objects`
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

### `object.editmode_toggle`:

* POLL: `active_object` is required and it should be EDITable
* TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED
* check view layer active object explicitly
* check view layer selected objects explicitly (non-EDITable objects are ignored)

### `object.hide_view_set`
* POLL_INTERNAL: `object_hide_poll`
* POLL:
* 📋 `area.type` == `VIEW_3D`
* 📋 or (`area.type` == `OUTLINER` and `area.spaces.active.display_mode` in `('SCENES', 'VIEW_LAYER', 'LIBRARIES')`)
* TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED
* hide selected/unselected objects in viewport (EYE icon)
* check view layer selected objects explicitly
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

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

### `object.modifier_apply`:

* POLL_INTERNAL: `modifier_apply_poll`
* POLL: *undocumented*
* TAG_CONTEXT_OVERRIDE_SUPPORT
* affects just one object - `context.object`
* active object is not affected, because operator needs to support being applied to pinned object

### `object.select_all`
* POLL_INTERNAL: `objects_selectable_poll`
* POLL:
* 📋 `context.edit_object` is `None`
* 📋 and (`context.active_object` is `None` or `context.active_object.mode` == `OBJECT`)
* TAG_CONTEXT_OVERRIDE_SUPPORT_PARTIAL
* context override only supported for passing poll check
* manipulate view layer objects selection explicitly
* return `FINISHED` if there were any changes in selection
* return `PASS_THROUGH` if there were no changes but no objects are visible, otherwise return `CANCELLED`

### `object.transform_apply`:

* TAG_CONTEXT_OVERRIDE_SUPPORT
* can be overridden using `selected_editable_objects`
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

### `outliner.delete`:

* POLL_INTERNAL: `ED_operator_outliner_active`
* POLL: `area.type` == `OUTLINER`
* TAG_CONTEXT_OVERRIDE_NOT_SUPPORTED
* check outliner tree for selected IDs explicitly (ignore `selected_ids`)
* TAG_ACTIVE_OBJECT_NOT_AFFECTED

### `view3d.camera_to_view_selected`:

* POLL_INTERNAL: 🛠️`ED_operator_scene_editable`
* POLL:
* 📋`context.scene` is set and is editable
* TAG_CONTEXT_OVERRIDE_SUPPORT_PARTIAL
* context override is only supported for passing `area` and `scene`
* check view layer selected objects explicitly (🛠️`base_flag & BASE_SELECTED`)
* if `area` with `type` == `VIEW3D` is provided, then `SpaceView3D.camera` is used,  
otherwise `scene.camera` is used

### `view3d.camera_to_view`:

* POLL_INTERNAL: `view3d_camera_to_view_poll`
* POLL:
* 📋`area.type` == `VIEW_3D`
* 📋`region` = region from `area.regions` with type `WINDOW`
* 📋 active scene `camera` should not be `None`
* 📋 viewport is not in camera view (`RegionView3D.view_perspective` != `CAMERA`)
* TAG_CONTEXT_OVERRIDE_SUPPORT
* updates camera view for the scene's active camera
