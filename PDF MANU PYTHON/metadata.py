 def add_metadata(input_pdf, output_pdf, title, author):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    # Set the metadata directly using add_metadata
    metadata = {
        '/Title': title,
        '/Author': author,
        '/Producer': ''
    }
    pdf_writer.add_metadata(metadata)
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)
    print(f"PDF with added metadata saved as {output_pdf}")
 # Usage
 add_metadata('Portrait.pdf', 'metadata_added.pdf', 'Sample File for Python Coding', 'Dr. Raj
 # Reading PDF Metadata
 import PyPDF2
 def read_metadata(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    metadata = pdf_reader.metadata
    print("Metadata of the PDF:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
 # Usage
 read_metadata('metadata_added.pdf')
