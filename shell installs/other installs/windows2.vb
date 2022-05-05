Dim remoteUri As String = "http://belajar123.com/materi.zip"
Dim fileName As String = "materi.zip"
Dim password As String = "..."
Dim username As String = "..."

Using client as New WebClient()

    client.Credentials = New NetworkCredential(username, password)
    client.DownloadFile(remoteUri, fileName)
End Using
