Dim remoteUri As String = "file"
Dim fileName As String = "file"
Dim password As String = "..."
Dim username As String = "..."

Using client as New WebClient()

    client.Credentials = New NetworkCredential(username, password)
    client.DownloadFile(remoteUri, fileName)
End Using
