---
title: bpy.ops.context
layout: default
---

# bpy.ops Python API documentation

Repository - <https://github.com/Andrej730/bpy.ops.context>

<h3 id="mesh.primitive_cube_add"><code>mesh.primitive_cube_add</code></h3>

* ⬜ context is not used
* clear previous selection
* newly added object is set as active and selected

<h3 id="mesh.separate"><code>mesh.separate</code></h3>

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected
* newly added objects are selected (original objects selection status is not affected)
* newly objects (and their data) retain props from original separated objects (and their data)

<h3 id="object.convert"><code>object.convert</code></h3>

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected

<h3 id="object.make_single_user"><code>object.make_single_user</code></h3>

* ❌ context override
* check view layer selected objects explicitly
* active object is not affected

<h3 id="object.editmode_toggle"><code>object.editmode_toggle</code></h3>

* POLL: `active_object` is required and it should be EDITable
* `temp_override(active_object)` is causing a crash (4.4.1). See [issue 137998](https://projects.blender.org/blender/blender/issues/137998).
* The rest is undocumented because of the crash

<h3 id="object.mode_set"><code>object.mode_set</code></h3>

* POLL: `active_object` is required and it should be EDITable
* ❌ context override
* check view layer active object explicitly
* check view layer selected objects explicitly (non-EDITable objects are ignored)

<h3 id="object.transform_apply"><code>object.transform_apply</code></h3>

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected
