#write an code which take 3or more pdf and merge them together into single pdf
from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["pdf/data1.pdf","pdf/balise ppt data.pdf","pdf/getting-started-with-pico.pdf"]:#pdf names enter here

    merger.append(pdf)

merger.write("merged-pdf.pdf")#merged pdf is of name merged-pdf.pdf
merger.close()