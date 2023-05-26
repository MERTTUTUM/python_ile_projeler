from PyPDF2 import PdfMerger

birlestirici=PdfMerger()

birlestirici.append("D:\WebScrapıng\pdfbırlestır\mlyt.pdf")
birlestirici.append("D:\WebScrapıng\pdfbırlestır\mlyt-2.pdf")
birlestirici.append("D:\WebScrapıng\pdfbırlestır\mlyt-3.pdf")
birlestirici.append("D:\WebScrapıng\pdfbırlestır\mlyt-4.pdf")

birlestirici.write("D:\WebScrapıng\pdfbırlestır\sinav.pdf")