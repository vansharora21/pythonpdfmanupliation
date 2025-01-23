#MERGING PDF FILES

import PyPDF2

def merge_pdf(pdf_list,output_path):
    pdf_writer=PyPDF2.PdfWriter()
    for pdf in pdf_list:
        pdf_reader=PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_path,'wb') as out:
        pdf_writer.write(out)
        print("merged pdf saved as{output_path}")


#using the above created functions
merge_pdf(['Page+2.pdf','Page+3.pdf'],'merged.pdf')
#output file will be merged.pdf








        
