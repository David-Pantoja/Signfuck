import sys
import os

def convert_emojis_to_bf(input_file):
    emoji_map = {
        '👉': '>',
        '👈': '<',
        '👆': '+',
        '👇': '-',
        '👌': '.',
        '🫵': ',',
        '🫸': '[',
        '🫷': ']'
    }
    
    # read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    # check for 👏 clap at start and end
    if not content.startswith('👏') or not content.endswith('👏'):
        raise ValueError("File must start and end with 👏 emoji")
    
    # check for 👏 in the middle of the script (this would mean it is the end of the script)
    middle_content = content[1:-1] # claps are guaranteed to be at the start and end
    if '👏' in middle_content:
        raise ValueError("👏 emoji is only allowed at the start and end of the file")
    
    # remove the 👏 emojis and convert the rest to bf
    content = content[1:-1]  # claps are guaranteed to be at the start and end
    bf_code = ''.join(emoji_map.get(char, '') for char in content)
    
    # create output filename
    output_file = os.path.splitext(input_file)[0] + '.bf'
    
    # write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(bf_code)
    
    return output_file

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python signfuck.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist")
        sys.exit(1)
    
    try:
        output_file = convert_emojis_to_bf(input_file)
        print(f"Converted file saved as: {output_file}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
