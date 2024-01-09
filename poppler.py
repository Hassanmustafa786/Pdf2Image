from pdf2image import convert_from_path



images = convert_from_path('2023_Curriculum Vitae_EN Version 1.pdf', 500,
						    poppler_path="C:/Program Files/poppler-21.11.0/Library/bin")

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
