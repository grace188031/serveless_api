
|  -  |     |        update        |    commit     | checkout |
| --- | --- | :------------------- | :-----------: | -------: |
| git |     | pull / fetch > merge | commit / push |    clone |
| hg  |     | pull > update        | commit / push |    clone |


tabUsage
Enter command in the command palette (Ctrl-Shift-P or Cmd-Shift-P) with cursor position in table syntax. The current table will be formatted. Or, you can format all the table syntax in opend text. At that time, markup language is automatically determined.

Command title:

Table: Format Current
format one table syntax contain current cursor position only
command: extension.table.formatCurrent
Table: Format All
format all table syntaxes in opend text
command: extension.table.formatAll
Sample:

Plain Text Table *1

| English  | Hello      | |            |            |
| Chinese  | 你好       | | Vietnamese | 嗔嘲       |
| Japanese | こんにちは | | Korean     | 안녕하세요 |

//=>
| English  | Hello      | |            |            |
| Chinese  | 你好       | | Vietnamese | 嗔嘲       |
| Japanese | こんにちは | | Korean     | 안녕하세요 |

Markdown

|  -  |     |        update        |    commit     | checkout |
| --- | --- | :------------------- | :-----------: | -------: |
| git |     | pull / fetch > merge | commit / push |    clone |
| hg  |     | pull > update        | commit / push |    clone |

// =>
|  -  |     |        update        |    commit     | checkout |
| --- | --- | :------------------- | :-----------: | -------: |
| git |     | pull / fetch > merge | commit / push |    clone |
| hg  |     | pull > update        | commit / push |    clone |

Textile

|_.      name      |_. age |
|   John Doe       |>.  35 |
|   Jane Doe       |<. 19  |
|   Nanashi Gonbei |=.  6  |

// =>
|_.      name      |_. age |
|   John Doe       |>.  35 |
|   Jane Doe       |<. 19  |
|   Nanashi Gonbei |=.  6  |

Grid Table

+------+------+------+------+------+------+
|      | Mon  | Tue  | Wed  | Thu  | Fri  |
+======+======+======+======+======+======+
| 田中 | (^^) | (xx) | (xx) | ('') | (^^) |
+------+------+------+------+------+------+
| 鈴木 | (^^) | (^^) | ('') | (xx) | (^^) |
+------+------+------+------+------+------+

// =>
+------+------+------+------+------+------+
|      | Mon  | Tue  | Wed  | Thu  | Fri  |
+======+======+======+======+======+======+
| 田中 | (^^) | (xx) | (xx) | ('') | (^^) |
+------+------+------+------+------+------+
| 鈴木 | (^^) | (^^) | ('') | (xx) | (^^) |
+------+------+------+------+------+------+

Simple Table *2

=====  =====  ========  =======
Input    .     Output
-----  -----  --------  -------
  A      B    "A or B"  A_and_B
=====  =====  ========  =======
False  False  False     False
True   False  True      False
=====  =====  ========  =======

// =>
=====  =====  ========  =======
Input    .     Output
-----  -----  --------  -------
  A      B    "A or B"  A_and_B
=====  =====  ========  =======
False  False  False     False
True   False  True      False
=====  =====  ========  =======

Configration
Some of configrations and examples of it.

tableformatter.common.centerAlignedHeader

// true
| Elem |   Win    | Lose  |
| ---- | :------- | ----: |
| Rock | Scissors | Paper |

// false
| Elem |   Win    | Lose  |
| ---- | :------- | ----: |
| Rock | Scissors | Paper |

tableformatter.markdown.oneSpacePadding

// true
|   Elem   |  Win  | Lose |
| -------- | :---- | ---: |
| Scissors | Paper | Rock |

// false
|   Elem   |  Win  | Lose |
| -------- | :---- | ---: |
| Scissors | Paper | Rock |

tableformatter.markdown.tableEdgesType

'Normal': Formatted table has delimiters on both sides.
'Borderless': Formatted table has no delimiters on both sides.
'Auto': If original table has no pipe delimiter at all line heads, format as borderless.
// Normal
| Elem  | Win  |   Lose   |
| ----- | :--- | :------- |
| Paper | Rock | Scissors |

// Borderless
Elem  | Win  |   Lose
----- | :--- | :-------
Paper | Rock | Scissors

Installation
Search extension in marketplace and Install.

In the command palette (Ctrl-Shift-P or Cmd-Shift-P) select Install Extensions.
Search for table formatter and select.
Roadmap
reStructuredText support
Grid table
Simple table
CSV support
Formatting
Configuration
Switching Enable Text algin
Escaped pipe string
Escaped break string
Simple table editing
Insert blank col and blank row
Insert escaped pipe and break
Convert to plain text table from CSV
Fast and simple shortcut format in table syntax
e.g.) Press Tab key in table syntax, and format current table
Probably needs updating of VSCood features about key bindings "when" property.
Release Notes
Changelog

Licence
MIT License

Author
Shuzo.I

Enjoy!

*1 It is misaligned because this monospaced font not compatible with CJK.

*2 Need to specific syntax. One cell content have no space, or put between double quotation.