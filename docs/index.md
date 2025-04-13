---
title: bpy.ops.context
layout: default
---

# bpy.ops Python API documentation.

### `object.convert`:

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected

### `object.make_single_user` :

* ❌ context override
* check view layer selected objects explicitly
* active object is not affected

### `object.transform_apply`:

* ✅ context override
* can be overridden using `selected_editable_objects`
* active object is not affected
