# transfer the VIAF info mation from the CSV file to TEI/XML file

Some part-time students will manually input all the VIAF info to the CSV file.

The scripts will take the VIAF from the CSV file and add them to the TEI file.

The person `id` in TEI corresponds to `NodeID 人物编号` in CSV file.

The data flow process is like this:

1. `人物数据1.0_VIAF.xlsx` is exported as a CSV file `Copy of 人物数据1.0_VIAF.csv`.
2. VIAF info is extracted from the CSV file.
3. VIAF info is integrated into the TEI file `sbdbTEI.xml`, with reference to the person's id.
4. The resulting TEI is saved as `output.xml`.
