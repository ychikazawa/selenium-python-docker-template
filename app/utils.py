from datetime import datetime

def get_current_datetime_str():
   return datetime.now().strftime('%Y-%m-%d_%H%M%S')

def half_to_full_width_num(num):
    # Create a table of correspondence between half-width and full-width numbers
    trans_table = str.maketrans('0123456789', '０１２３４５６７８９')
    # Convert half-width numbers to full-width numbers
    return num.translate(trans_table)

def write_file(filepath: str, content: str):
    with open(filepath, 'w', encoding='utf-8') as f:
      f.write(content)