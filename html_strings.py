start_string ='''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title></title>
</head>
<body>'''

end_string = '''</body>
</html>'''

section_start = '<h2>{0}. '
section_end = '</h2>'

break_tag = '<br>'

subsection_start = '<h3>{0}.{1} '
subsection_end = '</h3>'

italics_start = '<i>'
italics_end = '</i>'

bold_start = '<b>'
bold_end = '</b>'

underline_start = '<u>'
underline_end = '</u>'

enumerate_start = '<ol>'
enumerate_end = '</ol>'

itemize_start = '<ul>'
itemize_end = '</ul>'

item_start = '<li>'
item_end ='</li>'

image_tag = '<img src=\"{0}\" height="72pt" width="72pt">'

sqrt_start = '&radic;<span style="text-decoration: overline">'
sqrt_end = '</span>'

fraction_start = '<span style="display: inline-block;vertical-align: middle;"><div style="text-align: center;border-bottom: 1px solid black;">'
fraction_between = '</div><div style="text-align: center;">'
fraction_end = '</div></span>'

integral_tag = '&#8747;<sub>{0}</sub><sup>{1}</sup>'

sum_tag = '&#8721;<sub>{0}</sub><sup>{1}</sup>'

caption_start = '<p style="text-align:center">'
caption_end = '</p>'
