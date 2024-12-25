import os

def merge_markdown_files(input_folder, output_file):
	with open(output_file, 'w') as outfile:
		for filename in os.listdir(input_folder):
			if filename.endswith('.md'):
				with open(os.path.join(input_folder, filename), 'r') as infile:
					outfile.write(infile.read())
					outfile.write('\n\n')  # Add a newline between files

input_folder = 'md'
output_file = 'merged.md'
merge_markdown_files(input_folder, output_file)