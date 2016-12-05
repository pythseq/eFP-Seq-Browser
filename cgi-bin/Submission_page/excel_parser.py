import openpyxl

f = open('submission_parse.html','w')
wb = openpyxl.load_workbook('bulk_template.xlsx')
sheet = wb.get_sheet_by_name('Data sheet')
all_rows = tuple(sheet.rows)

# Store string to be written into html file after all content is read.
total_XML = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script src="XMLgenerator-v2.js"></script>
<div class="SubmissionArea">
"""

# Iterate through each entry and corresponding cells.
for row in range(1, len(all_rows)):
    crow = all_rows[row] # Current entry
    total_XML += """
<div class="Entries" name="Entries">
<legend class="leftmargin"> Entry </legend>
    <form class="form">
        <fieldset>"""

    for x in range(1, 11):
        ccell = crow[x].value

# Prints alert to user if cell is empty. 
# Note: As of now, it's just printed, but this could be incorporated into the UI in the future (perhaps a popup?)
        if ccell is None:
            print("Input missing from Entry " + str(row) + ", column " + str(x))

# Stores content of each cell in a HTML wrapper
# form field is set to column index number (would need to be manually changed if template is changed)
        else:
            if x == 1 and ccell.isalpha():
                total_XML += """
                <div class='forminput'>
                    <p class='channelspecies' name='channelspecies' data-help-text='species'>""" + ccell + """</p>
                </div>"""

            elif x == 2:
                total_XML += """
                <div class='forminput'>
                    <p class='channeltitle' name='channeltitle' data-help-text='title'>""" + ccell + """</p>
                </div>"""

            elif x == 3: #how to validate BAM link?
                total_XML += """
                <div class='forminput'>
                    <p class='channelbamlink' name='channelbamlink' data-help-text='bam_link'>""" + ccell + """</p>
                </div>"""

            elif x == 4:
                total_XML += """
                <div class='forminput'>
                    <p name='channelpublicationlink' name='channelpublicationlink' data-help-text='publication_link'>""" + ccell + """</p>
                </div>"""

            elif x == 5 and ("ncbi" or "NCBI" in ccell):
                total_XML += """
                <div class='forminput'>
                    <p name='channelpublicationurl' name='channelpublicationurl' data-help-text='publication_url'>""" + ccell + """</p>
                </div>"""

            elif x == 6:
                total_XML += """
                <div class='forminput'>
                    <p name='channeltotalreadsmapped' name='channeltotalreadsmapped' data-help-text='svgname'>""" + str(ccell) + """</p>
                </div>"""

            elif x == 7 and ".svg" in ccell:
                total_XML += """
                <div class='forminput'>
                    <p name='channelsvgname' name='channelsvgname' data-help-text='total_reads_mapped'>""" + ccell + """</p>
                </div>"""

            elif x == 8:
                total_XML += """
                <div class='forminput'>
                    <p name='channeltissue' name='channeltissue' data-help-text='tissue'>""" + ccell + """</p>
                </div>"""

            elif x == 9:
                total_XML += """
                <div class='forminput'>
                    <p name='channelcontrols' name='channelcontrols' data-help-text='total_controls'>""" + ccell + """</p>
                </div>"""

            elif x == 10:
                replicates = ccell.split(", ")

                for i in replicates:
                    total_XML += """
                <div class='forminput'>
                    <p name='channelgroupwith' name='channelgroupwith' data-help-text='groupwith'>""" + i + """</p>
                </div>"""

    total_XML += """
        </fieldset>
    </form>
</div>
"""


total_XML += """
</div>
<div id="Cloning" class="button_fixed">
    <p>
        <button id="SubmitButton">Generate XML</button>
    </p>
</div>
<div id="generated" style="display:none">
  <h2>bamdata.xml</h2>
  <a href="#" id="DownloadLink">Download XML</a>
  <textarea id="ResultXml" style="width: 100%; height: 30em" readonly="readonly"></textarea>
</div>
</html>"""

print (total_XML) # Testing purposes

f.write(total_XML)
f.close()


