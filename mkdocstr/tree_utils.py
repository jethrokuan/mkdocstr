from mkdocstr.ttypes import Location


def move_cursor(cursor, direction):
  if direction != "up":
    if cursor.goto_first_child():
      return "down"
    elif cursor.goto_next_sibling():
      return "right"
    elif cursor.goto_parent():
      return "up"
  else:
    if cursor.goto_next_sibling():
      return "right"
    elif cursor.goto_parent():
      return "up"
    return "done"


def find_node_in_tree(cursor, matcher):
  direction = None
  while direction != "done":
    if direction != "up":
      if matcher(cursor.node):
        return cursor.node
    direction = move_cursor(cursor, direction)
  return None
