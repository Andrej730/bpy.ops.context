---
title: bpy.ops.context
layout: default
---

# bpy.ops Python API documentation

Repository - <https://github.com/Andrej730/bpy.ops.context>

<h3 id="clip.add_marker"><code>clip.add_marker</code></h3>

* POLL_INTERNAL: `ED_space_clip_tracking_poll`
* POLL:
* 📋 `area.type` == `CLIP_EDITOR`
* 📋 `area.spaces.active.clip` is not `None`
* 📋 `area.spaces.active.mode` == `TRACKING`
* ✅ context override

<h3 id="mesh.primitive_cube_add"><code>mesh.primitive_cube_add</code></h3>

* ⬜ context is not used
* clear previous selection
* newly added object is set as active and selected

<h3 id="mesh.separate"><code>mesh.separate</code></h3>

* In OBJECT mode:
* ✅ context override
* 📋 can be overridden using `selected_editable_objects`
* 📋 TAG_ACTIVE_OBJECT_NOT_AFFECTED
* In EDIT_MESH mode:
* ❌ context override
* 📋 basically it affects `context.objects_in_mode`, but doesn&#x27;t use this actual context member
* 📋 therefore it ignores selected objects that are in OBJECT mode, doesn&#x27;t require explicit selection and skips hidden objects
* 📋 &#x27;by selection&#x27; separates selection for each object separately (e.g. if 1 face selected in N objects results in N separated objects)
* In both modes:
* 📋 newly added objects are selected (original objects selection status is not affected)
* 📋 newly objects (and their data) retain props from original separated objects (and their data)

<h3 id="object.convert"><code>object.convert</code></h3>

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected

<h3 id="object.delete"><code>object.delete</code></h3>

* ✅ context override
* can be overridden using `selected_objects`
* active object is not affected

<h3 id="object.editmode_toggle"><code>object.editmode_toggle</code></h3>

* POLL: `active_object` is required and it should be EDITable
* ❌ context override
* check view layer active object explicitly
* check view layer selected objects explicitly (non-EDITable objects are ignored)

<h3 id="object.join"><code>object.join</code></h3>

* POLL: `active_object` is required and it should be EDITable
* ✅ context override
* can be overridden using `selected_editable_objects` and `active_object`
* objects that don&#x27;t match `active_object` type are ignored from `selected_editable_objects`  
(e.g. Curves when Mesh is active)
* active object is the join target and it should also be selected

<h3 id="object.make_single_user"><code>object.make_single_user</code></h3>

* ❌ context override
* check view layer selected objects explicitly
* active object is not affected

<h3 id="object.mode_set"><code>object.mode_set</code></h3>

* POLL: `active_object` is required and it should be EDITable
* ❌ context override
* check view layer active object explicitly
* check view layer selected objects explicitly (non-EDITable objects are ignored)

<h3 id="object.transform_apply"><code>object.transform_apply</code></h3>

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected

<h3 id="outliner.delete"><code>outliner.delete</code></h3>

* POLL: `area.type` == `OUTLINER`
* ❌ context override
* check outliner tree for selected IDs explicitly (ignore `selected_ids`)
* active object is not affected
