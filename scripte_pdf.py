from weasyprint import HTML

HTML('index.html').write_pdf('CV_Dinahet_Stéphane.pdf')
print("Conversion réussie avec WeasyPrint : fichier enregistré sous 'CV_Dinahet_Stéphane.pdf'")
