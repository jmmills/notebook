# from http://win32com.goermezer.de/content/view/173/284/

import win32com.client
 
wordapp = win32com.client.Dispatch("Word.Application") # Create new Word Object
wordapp.Visible = 0 # Word Application should`t be visible
worddoc = wordapp.Documents.Add() # Create new Document Object
worddoc.PageSetup.Orientation = 1 # Make some Setup to the Document:
worddoc.PageSetup.LeftMargin = 20
worddoc.PageSetup.TopMargin = 20
worddoc.PageSetup.BottomMargin = 20
worddoc.PageSetup.RightMargin = 20
worddoc.Content.Font.Size = 16
worddoc.Content.Paragraphs.TabStops.Add (100)
worddoc.Content.Text = "Hello, I am text embedded in a Microsoft Word '03 doc!"
worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Application
