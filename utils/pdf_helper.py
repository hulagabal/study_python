from pypdf import PdfReader
 
def validate_pdf(target_path, expected_keywords):
 
    with open(target_path, "rb") as pdf_file:
        
        first_five_bytes = pdf_file.read(5)
        assert first_five_bytes == b"%PDF-" , f'Downloaded file does not have a valid PDF signature'
        reader = PdfReader(target_path)

        extracted_text = ""            
        for pdfpage in reader.pages:
            text = pdfpage.extract_text()
            if text is not None:
                extracted_text += text
                        
        assert len(extracted_text.strip()) > 0, f'extracted file is empty'
        
        for keyword in expected_keywords:
            assert keyword in extracted_text, f" Could not find '{keyword}' in PDF!"
        
        return extracted_text