# for sorting ligand/protein mpnn fasta files


cat mpnn_2.fa | sed 'N;s/\n/|/' | sort -t '=' -k 5 -nr | awk -v RS="|" '1'

"""
sed 'N;s/\n/|/' joins the header and sequence into 1 string separated by "|" 


N -> reads next line and append to memory

s/\n/|/ -> search for new line (\n) and substitute with "|", so s = substitute, anything enclosed between // is the search term e.g. /{search term}/ then replacement string then / again



sort -t '=' -k 5 -nr -> sorting the strings. 
-t '=' -> means the = is a field separator, so now strings between an = is regarded as its own column e.g.
test=04, score=34, id=5 is now 
col 1	col2		col3
test	04, score	34, id

-k 5 -> use the 5th field for sorting, which when split is "0.6227, ligand_confidence"
-n -> Restrict the sort key to an initial numeric string, so it will only read the numbers. Alternatively, can use -k 5.6 so it reads the first 6 characters of field 5
-r -> descending order


awk -v RS="|" '1' 

-v RS="|" -> This is an option passed to awk that sets a variable named RS (record separator) to the pipe character ("|"). This tells awk to consider anything separated by a pipe as the end of a record, effectively splitting lines at each pipe.

'1' -> This is the actual awk program itself enclosed in single quotes. It consists of only one statement: 1. In awk, any number used as a program statement refers to the line number in the current record.

When awk reads a line, it uses the defined record separator (RS) to split the line into records (fields). Here, with RS="|" anything separated by a pipe is considered a separate record. The program statement 1 simply prints the first record (line number 1) from the split line.


Final note: using || as separator won't work because awk interprets the double pipes within the single quotes as the escape sequence for a single pipe character. so need to modify it to "[|][|]" or '\\|\\|' to escape them. Note the double and single quotes when using [] or escape characters.

"""


# for renaming ligand mpnn outputs from ">spia7, id=1, temp= ...." to ">spia7_1, >spia7_2, ... "

awk 'BEGIN { i = 0 } /^>/ { split($0, id, ","); i++; print id[1] "_" i; next } { print }'

needs gemini explanations.


# for moving files in all subdirectories to one directory

mv -t /destination/directory */*.jpg
cp -t /destination/directory */*.jpg

# add text to all files in folder
for f in *.md; do mv "$f" "test - $f"; done

# prepend files with directory name

for name in */*; do
    [ ! -f "$name" ] && continue

    dir="$( basename "$( dirname "$name" )" )"
    newname="$dir/${dir}${name##*/}"

    if [ ! -e "$newname" ]; then
        # echo mv "$name" "$newname"
		mv "$name" "$newname"
    fi
done