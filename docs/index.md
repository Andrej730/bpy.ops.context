---
title: bpy.ops.context
layout: default
---

# bpy.ops Python API documentation

Repository - <https://github.com/Andrej730/bpy.ops.context>

<h3 id="mesh.separate"><code>mesh.separate</code></h3>

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected

<h3 id="object.convert"><code>object.convert</code></h3>

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected

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
