import xml.sax

class BookHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.title = ""
      self.author = ""
      self.year = ""
      self.price = ""
    
   
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "bookstore":
         print ("*****BOOK STORE*****")
         shelf = attributes["shelf"]
         print ("Shelf:", shelf)
      if tag == "book":
         print ("*****BOOK*****")
         category = attributes["category"]
         print ("Category:", category)
      if tag == "title":
         language = attributes["lang"]
         print ("Language:", language)

   
   def endElement(self, tag):
      if self.CurrentData == "title":
         print ("Title:", self.title)
      elif self.CurrentData == "author":
         print ("Author:", self.author)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "price":
         print ("Price:", self.price)
      self.CurrentData=""

   
   def characters(self, content):
      if self.CurrentData == "title":
         self.title = content
      elif self.CurrentData == "author":
         self.author = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "price":
         self.price = content
      
  
parser = xml.sax.make_parser()
Handler = BookHandler()
parser.setContentHandler( Handler )
parser.parse("input.xml")